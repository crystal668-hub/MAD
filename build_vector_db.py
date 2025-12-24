"""
===================================
向量数据库构建脚本
功能：使用OpenAI Agent构建Chroma向量数据库
===================================
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from agents.agent_config import AgentConfig
from database.vector_store import VectorStore
from database.text_processor import TextProcessor
from database.openai_embedder import MultiModelEmbedder


def build_vector_database(
    config_path: str = "./config/config.yaml",
    use_processed_data: bool = True,
    agent_name: str = "agent1"
):
    """
    构建向量数据库
    
    Args:
        config_path: 配置文件路径
        use_processed_data: 是否使用processed目录的数据
        agent_name: 使用的Agent配置名称(默认agent1——OpenAI)
    """
    print("=" * 60)
    print("开始构建Chroma向量数据库")
    print("=" * 60)
    
    # 1. 加载配置
    print("\n[步骤 1/5] 加载配置...")
    config = AgentConfig(config_path)
    
    # 获取对应Agent配置
    llm_config = config.get_llm_config(agent_name)
    vector_config = config.get_vector_store_config()
    
    # 获取所有agent的配置字典（用于MultiModelEmbedder动态切换模型）
    all_agent_configs = {
        'agent1': config.get_llm_config('agent1'),
        'agent2': config.get_llm_config('agent2'),
        'agent3': config.get_llm_config('agent3'),
        'agent4': config.get_llm_config('agent4')
    }
    
    print(f"✓ 使用Agent: {agent_name}")
    print(f"✓ LLM模型: {llm_config.get('model')}")
    print(f"✓ 向量模型: {llm_config.get('embedding_model')}")
    
    # 2. 初始化文本处理器
    print("\n[步骤 2/5] 加载文本数据...")
    processor = TextProcessor()
    
    # 加载数据
    documents = []
    
    if use_processed_data:
        # 优先加载processed目录的预处理好的chunks数据
        print("  从processed目录加载数据...")
        processed_docs = processor.load_processed_chunks("*chunks.txt")
        documents.extend(processed_docs)
    
    if len(documents) == 0:
        # 如果没有processed数据，尝试从raw目录加载并预处理TSV文件
        print("  processed目录无数据，尝试从raw目录加载TSV文件...")
        processor_raw = TextProcessor("./data/raw")
        
        # 查找TSV文件
        raw_path = Path("./data/raw")
        tsv_files = list(raw_path.glob('*.tsv')) if raw_path.exists() else []
        
        if tsv_files:
            print(f"  找到 {len(tsv_files)} 个TSV文件，开始预处理...")
            # 处理所有TSV文件，生成chunks.txt到processed目录
            results = processor_raw.process_all_tsv_files(
                raw_dir="./data/raw",
                processed_dir="./data/processed"
            )
            
            if sum(results.values()) > 0:
                # 预处理成功，重新加载processed目录的数据
                print("\n  预处理完成，加载生成的chunks文件...")
                processed_docs = processor.load_processed_chunks("*chunks.txt")
                documents.extend(processed_docs)
            else:
                print("\n✗ TSV文件预处理失败，未生成有效数据")
        else:
            # 如果也没有TSV文件，尝试加载txt文件
            print("  未找到TSV文件，尝试加载txt文件...")
            txt_docs = processor_raw.load_text_files("*.txt")
            documents.extend(txt_docs)
    
    print(f"✓ 共加载 {len(documents)} 个文档")
    
    if len(documents) == 0:
        print("\n✗ 未找到任何文档,请检查数据目录")
        print("  可尝试:")
        print("    1. 将TSV文件放入 ./data/raw 目录（自动预处理）")
        print("    2. 将文本文件放入 ./data/raw 目录")
        print("    3. 或确保 ./data/processed 目录有 *chunks.txt 文件")
        return
    
    # 3. 处理文档
    print("\n[步骤 3/5] 处理文档...")
    processed_docs = processor.process_documents(
        documents,
        enable_chunking=False,  # processed数据已经分块，无需额外chunk
        chunk_size=512,
        overlap=50
    )
    print(f"✓ 处理后文档数: {len(processed_docs)}")
    
    # 4. 初始化向量化器
    print("\n[步骤 4/5] 初始化向量化器并生成向量...")
    try:
        embedder = MultiModelEmbedder(llm_config, agent_configs=all_agent_configs)
    except ValueError as e:
        print(f"\n✗ 初始化失败: {str(e)}")
        print("  请设置环境变量: set OPENAI_API_KEY=your_api_key")
        return
    
    # 提取文本和元数据
    texts = [doc['text'] for doc in processed_docs]
    metadatas = [doc['metadata'] for doc in processed_docs]
    
    print(f"✓ 准备向量化 {len(texts)} 个文本")
    
    # 生成向量
    print("\n开始向量化...")
    try:
        embeddings = embedder.embed_batch(texts, batch_size=10, show_progress=True, agent_name=agent_name)
    except Exception as e:
        print(f"\n✗ 向量化失败: {str(e)}")
        print("  请检查:")
        print("    1. API Key是否正确")
        print("    2. 网络连接是否正常")
        print("    3. API额度是否充足")
        return
    
    print(f"\n✓ 成功生成 {len(embeddings)} 个向量")
    print(f"✓ 向量维度: {len(embeddings[0]) if embeddings else 0}")
    
    # 5. 存储到Chroma向量数据库
    print("\n[步骤 5/5] 存储到向量数据库...")
    
    vector_store = VectorStore(
        persist_directory=vector_config.get('persist_directory', './data/chroma_db'),
        collection_name=vector_config.get('collection_name', 'chemical_reactions'),
        embedding_function=None  # 使用自定义向量
    )
    
    # 清空已有数据（可选）
    current_count = vector_store.get_collection_count()
    if current_count > 0:
        user_input = input(f"\n集合中已有 {current_count} 个文档，是否清空？(y/n): ")
        if user_input.lower() == 'y':
            vector_store.reset_collection()
            print("✓ 已清空集合")
    
    # 批量添加文档和向量
    try:
        vector_store.add_documents_with_embeddings(
            texts=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )
    except Exception as e:
        print(f"\n✗ 存储失败: {str(e)}")
        return
    
    print(f"✓ 成功存储到Chroma数据库")
    print(f"✓ 集合名称: {vector_config.get('collection_name')}")
    print(f"✓ 存储路径: {vector_config.get('persist_directory')}")
    print(f"✓ 文档总数: {vector_store.get_collection_count()}")
    
    # 6. 验证
    print("\n[验证] 测试检索功能...")
    test_query = "catalyst overpotential"
    print(f"测试查询: {test_query}")
    
    try:
        # 向量化查询文本
        query_embedding = embedder.embed_text(test_query, agent_name=agent_name)
        results = vector_store.similarity_search_with_embedding(
            query_embedding=query_embedding,
            top_k=3
        )
        
        print(f"\n✓ 检索到 {len(results)} 个结果")
        for idx, result in enumerate(results[:3], 1):
            print(f"\n结果 {idx}:")
            print(f"  文本: {result['text'][:100]}...")
            print(f"  相似度距离: {result.get('distance', 'N/A'):.4f}")
            metadata = result.get('metadata', {})
            print(f"  来源: {metadata.get('source', 'N/A')}")
    except Exception as e:
        print(f"✗ 验证失败: {str(e)}")
    
    print("\n" + "=" * 60)
    print("向量数据库构建完成!")
    print("=" * 60)


if __name__ == "__main__":
    # 运行构建脚本
    build_vector_database(
        config_path="./config/config.yaml",
        use_processed_data=True,  # 优先使用processed目录的数据
        agent_name="agent1"  # 使用对应agent配置
    )
