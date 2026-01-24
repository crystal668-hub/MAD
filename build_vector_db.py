"""
======================================================
向量数据库构建脚本
功能：使用LlamaIndex解析Markdown文件，构建Chroma向量数据库
支持九种电化学反应类型的文献数据存储
======================================================
"""

import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from agents.agent_config import AgentConfig
from database.vector_store import VectorStore
from database.text_processor import TextProcessor
from database.embedder import MultiModelEmbedder
from utils.logger import Logger

REACTION_CONFIGS = {
    "CO2RR": {"path": "CO2RR", "type": "fulltext"},   # CO2 Reduction Reaction
    "EOR": {"path": "EOR", "type": "fulltext"},       # Ethanol Oxidation Reaction
    "HER": {"path": "HER", "type": "fulltext"},       # Hydrogen Evolution Reaction
    "HOR": {"path": "HOR", "type": "fulltext"},       # Hydrogen Oxidation Reaction
    "HZOR": {"path": "HZOR", "type": "fulltext"},     # Hydrazine Oxidation Reaction
    "O5H": {"path": "O5H", "type": "fulltext"},       # Oxidation of 5-hydroxymethylfurfural
    "OER": {"path": "OER", "type": "fulltext"},       # Oxygen Evolution Reaction
    "ORR": {"path": "ORR", "type": "fulltext"},       # Oxygen Reduction Reaction
    "UOR": {"path": "UOR", "type": "fulltext"},       # Urea Oxidation Reaction
}


def build_vector_database(
    config_path: str = "./config/config.yaml",
    data_dir: str = "./data/raw",
    reaction_configs: dict = None,
    agent_name: str = "agent2",
    chunk_size: int = 256,
    chunk_overlap: int = 50
):
    """
    构建向量数据库
    使用LlamaIndex解析Markdown，创建Document对象并进行chunk和索引构建
    使用Chromadb进行持久化数据存储
    
    Args:
        config_path: 配置文件路径
        data_dir: 原始数据目录，包含各反应类型子目录
        reaction_configs: 反应类型配置字典，None则使用默认配置
        agent_name: 使用的Agent配置名称
        chunk_size: 分块大小
        chunk_overlap: 分块重叠大小
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = Path("./logs") / f"build_vector_db_{timestamp}.log"
    logger = Logger.get_logger(
        name=f"MAD.BuildVectorDB.{timestamp}",
        log_file=str(log_file),
        level="INFO"
    )

    logger.info("=" * 60)
    logger.info("开始构建Chroma向量数据库")
    logger.info("=" * 60)
    
    # 构建反应类型配置
    if reaction_configs is None:
        reaction_configs = REACTION_CONFIGS
    
    # 1. 加载配置
    logger.info("\n[步骤 1/5] 加载配置...")
    config = AgentConfig(config_path)
    
    # 获取对应Agent配置
    llm_config = config.get_llm_config(agent_name)
    vector_config = config.get_vector_store_config()
    rag_config = config.get_rag_config()
    
    # 使用配置文件中的chunk参数
    chunk_size = rag_config.get('chunk_size', chunk_size)
    chunk_overlap = rag_config.get('chunk_overlap', chunk_overlap)
    
    # 获取所有agent的配置字典（用于MultiModelEmbedder动态切换模型）
    all_agent_configs = {
        'agent1': config.get_llm_config('agent1'),
        'agent2': config.get_llm_config('agent2'),
        'agent3': config.get_llm_config('agent3'),
        'agent4': config.get_llm_config('agent4')
    }
    
    # 根据agent名称设置不同的collection_name
    base_collection_name = vector_config.get('collection_name', 'chemical_reactions_recommendation')
    collection_name = f"{base_collection_name}_{agent_name}"
    
    logger.info(f"✓ Agent_used: {agent_name}")
    logger.info(f"✓ base_model: {llm_config.get('model')}")
    logger.info(f"✓ embedding_model: {llm_config.get('embedding_model')}")
    logger.info(f"✓ collection_name: {collection_name}")
    logger.info(f"✓ chunk_size: {chunk_size}, chunk_overlap: {chunk_overlap}")
    
    # 2. 使用LlamaIndex加载文档
    logger.info("\n[步骤 2/5] 加载文献数据...")
    processor = TextProcessor(data_dir)
    
    # 检查数据目录结构
    data_path = Path(data_dir)
    if not data_path.exists():
        logger.error(f"\n✗ 数据目录不存在: {data_dir}")
        logger.error("  请确保数据目录结构如下:")
        for _, cfg in reaction_configs.items():
            file_type = "*.md"
            logger.error(f"    {data_dir}/{cfg['path']}/{file_type}")
        return
    
    # 加载所有反应类型的文档
    documents = processor.load_reaction_documents(
        base_dir=data_dir,
        reaction_configs=reaction_configs
    )  
    
    logger.info(f"\n✓ 共加载 {len(documents)} 个Document对象")
    
    if len(documents) == 0:
        logger.error("\n✗ 未找到任何文档，请检查数据目录")
        logger.error("  支持的文件格式: .md")
        logger.error(f" 数据目录: {data_dir}")
        return
    
    # 3. 对Document进行chunk分块
    logger.info("\n[步骤 3/5] 对Document进行chunk切分...")
    chunked_documents = processor.chunk_documents(
        documents=documents,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    logger.info(f"✓ 分块后文档数: {len(chunked_documents)}")
    
    # 4. 初始化向量化器
    logger.info("\n[步骤 4/5] 初始化向量化器并生成向量...")
    try:
        embedder = MultiModelEmbedder(llm_config, agent_configs=all_agent_configs)
    except ValueError as e:
        logger.error(f"\n✗ 初始化失败: {str(e)}")
        return
    
    # 利用doc属性获取文本和元数据
    texts = [doc.text for doc in chunked_documents]
    metadatas = [doc.metadata for doc in chunked_documents]
    
    logger.info(f"✓ 准备向量化 {len(texts)} 个文本")
    
    # 生成向量
    logger.info("\n开始向量化...")
    try:
        embeddings = embedder.embed_batch(texts, batch_size=10, show_progress=True, agent_name=agent_name)
    except Exception as e:
        logger.error(f"\n✗ 向量化失败: {str(e)}")
        return
    
    logger.info(f"\n✓ 成功生成 {len(embeddings)} 个向量")
    logger.info(f"✓ 向量维度: {len(embeddings[0]) if embeddings else 0}")
    
    # 5. 存储到Chroma向量数据库
    logger.info("\n[步骤 5/5] 存储到Chroma向量数据库...")
    
    vector_store = VectorStore(
        persist_directory=vector_config.get('persist_directory', './data/chroma_db'),
        collection_name=collection_name,  
        embedding_function=None  
    )
    
    # 清空已有数据（可选）
    current_count = vector_store.get_collection_count()
    if current_count > 0:
        prompt = f"\n集合中已有 {current_count} 个文档，是否清空？(y/n): "
        logger.info(prompt)
        user_input = input(prompt)
        if user_input.lower() == 'y':
            vector_store.reset_collection()
            logger.info("✓ 已清空集合")
    
    # 批量添加文档和向量
    try:
        vector_store.add_documents(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )
    except Exception as e:
        logger.error(f"\n✗ 存储失败: {str(e)}")
        return
    
    logger.info("✓ 成功存储到Chroma数据库")
    logger.info(f"✓ 集合名称: {collection_name}")
    logger.info(f"✓ 存储路径: {vector_config.get('persist_directory')}")
    logger.info(f"✓ 文档总数: {vector_store.get_collection_count()}")
    logger.info("\n" + "=" * 60)
    logger.info("向量数据库构建完成!")
    logger.info("=" * 60)


if __name__ == "__main__":
    build_vector_database(
        config_path="./config/config.yaml",
        data_dir="./data/raw",              
        reaction_configs=REACTION_CONFIGS,  
        agent_name="agent2",                
        chunk_size=256,                     
        chunk_overlap=50                    
    )
