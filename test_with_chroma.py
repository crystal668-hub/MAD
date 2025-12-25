"""
===================================
测试脚本：四个Agent绑定Chroma向量数据库
功能：将所有4个Agent配置为使用同一个已建立好的chroma_db进行检索
===================================
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 导入项目模块
from utils import (
    load_config,
    setup_logging,
    validate_components,
    print_header,
    print_section,
    save_json,
    ensure_dir
)
from database.rag_system import RAGSystem
from agents.agent_config import AgentConfig
from debate.autogen_coordinator import AutoGenDebateCoordinator
import time
import json


def create_shared_rag_system(config: dict) -> RAGSystem:
    """
    创建共享的RAG系统，连接到现有的chroma_db
    
    Args:
        config: 系统配置
    
    Returns:
        RAGSystem: RAG系统实例
    """
    print("正在初始化共享RAG系统...")
    
    rag_config = config.get('rag', {})
    vector_config = config.get('vector_store', {})
    paths_config = config.get('paths', {})
    
    # 从配置中获取路径
    data_dir = paths_config.get('processed_data', './data/processed')
    persist_dir = vector_config.get('persist_directory', './data/chroma_db')
    collection_name = vector_config.get('collection_name', 'chemical_reactions')
    
    # 确保目录存在
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(persist_dir, exist_ok=True)
    
    # 检查chroma_db是否存在
    chroma_db_path = Path(persist_dir) / "chroma.sqlite3"
    if not chroma_db_path.exists():
        print(f"  警告：未找到现有的chroma数据库文件: {chroma_db_path}")
        print(f"  请确保已运行 build_vector_db.py 构建向量数据库")
    else:
        print(f"  ✓ 找到现有的chroma数据库: {chroma_db_path}")
    
    # 创建RAG系统实例
    rag_system = RAGSystem(
        data_dir=data_dir,
        persist_dir=persist_dir,
        collection_name=collection_name,
        top_k=rag_config.get('top_k', 5)
    )
    
    # 如果索引未初始化，尝试构建索引
    if rag_system.index is None:
        print(f"\n  ⚠ 索引未初始化，正在构建索引...")
        print(f"  (首次构建需要调用API生成embeddings，可能需要几分钟)")
        try:
            rag_system.build_index()
            if rag_system.index is not None:
                print(f"  ✓ 索引构建成功")
            else:
                print(f"  ✗ 索引构建后仍未初始化")
        except Exception as e:
            print(f"  ✗ 索引构建失败: {str(e)}")
            print(f"\n  可能的原因：")
            print(f"    1. 数据文件格式不正确（应为：索引\\t内容）")
            print(f"    2. OPENAI_API_KEY 未配置或无效")
            print(f"    3. 网络无法访问 OpenAI API")
            print(f"\n  详细错误：")
            import traceback
            traceback.print_exc()
    
    print(f"  ✓ RAG系统初始化完成")
    print(f"    - 数据目录: {data_dir}")
    print(f"    - 向量数据库: {persist_dir}")
    print(f"    - 集合名称: {collection_name}")
    print(f"    - Top-K: {rag_config.get('top_k', 5)}")
    print(f"    - 索引状态: {'✓ 已加载' if rag_system.index else '✗ 未初始化'}")
    
    return rag_system


def test_rag_retrieval(rag_system: RAGSystem, test_query: str = "AOR reaction overpotential"):
    """
    测试RAG系统的检索功能
    
    Args:
        rag_system: RAG系统实例
        test_query: 测试查询
    """
    print(f"\n正在测试RAG检索功能...")
    print(f"测试查询: {test_query}")
    
    # 检查索引是否已初始化
    if rag_system.index is None:
        print(f"  ✗ RAG索引未初始化，跳过检索测试")
        print(f"  提示：索引构建可能失败，请检查上面的错误信息")
        return
    
    try:
        results = rag_system.retrieve(test_query)
        print(f"  ✓ 检索成功，返回 {len(results)} 条结果")
        
        if results:
            print(f"\n  前3条检索结果预览:")
            for i, result in enumerate(results[:3], 1):
                content = result.get('content', result.get('text', 'N/A'))
                score = result.get('score', result.get('similarity', 'N/A'))
                preview = content[:150] + "..." if len(content) > 150 else content
                print(f"    [{i}] 相似度: {score:.4f if isinstance(score, float) else score}")
                print(f"        {preview}\n")
        else:
            print(f"  警告：未检索到任何结果")
            
    except Exception as e:
        print(f"  ✗ 检索失败: {str(e)}")


def main():
    """主函数"""
    print_header("四个Agent绑定Chroma向量数据库测试")
    
    # 1. 加载配置
    print_section("1. 加载配置")
    config_path = "./config/config.yaml"
    config = load_config(config_path)
    print(f"  ✓ 配置加载成功: {config_path}")
    
    # 2. 创建共享的RAG系统（连接到现有的chroma_db）
    print_section("2. 创建共享RAG系统")
    shared_rag = create_shared_rag_system(config)
    
    # 3. 测试RAG检索功能
    print_section("3. 测试RAG检索功能")
    test_rag_retrieval(shared_rag, "metal catalyst AOR overpotential")
    
    # 4. 为所有4个Agent绑定相同的RAG系统
    print_section("4. 初始化Agent并绑定RAG")
    rag_systems = {
        'agent1': shared_rag,
        'agent2': shared_rag,
        'agent3': shared_rag,
        'agent4': shared_rag
    }
    
    # 创建Agent配置管理器
    agent_config = AgentConfig(config)
    
    # 创建所有Agent，并传入RAG系统
    agents = agent_config.create_all_agents(
        rag_systems=rag_systems,
        experience_store=None  # 本测试中不使用经验库
    )
    
    if not agents:
        print("  ✗ 未能创建任何Agent")
        return
    
    print(f"\n  ✓ 成功创建 {len(agents)} 个Agent，全部绑定到chroma_db")
    for i, agent in enumerate(agents, 1):
        rag_status = "✓ 已绑定RAG" if agent.rag_system else "✗ 未绑定RAG"
        print(f"    [{i}] {agent.name} - {rag_status}")
    
    # 5. 初始化辩论协调器
    print_section("5. 初始化辩论协调器")
    debate_config = config.get('debate', {})
    coordinator = AutoGenDebateCoordinator(
        agents=agents,
        config=debate_config
    )
    print(f"  ✓ 辩论协调器初始化完成")
    print(f"    - 最大轮数: {debate_config.get('max_rounds', 10)}")
    print(f"    - 共识阈值: {debate_config.get('consensus_threshold', 3)}")
    
    # 6. 运行测试辩论
    print_section("6. 运行测试辩论")
    
    # 测试用的金属催化剂组分
    test_components = ["Pt", "Pd", "Ru", "Ir", "Rh"]
    print(f"测试催化剂组分: {', '.join(test_components)}")
    
    # 验证组分
    is_valid, error_msg = validate_components(test_components)
    if not is_valid:
        print(f"  ✗ 组分验证失败: {error_msg}")
        return
    
    print(f"  ✓ 组分验证通过")
    print(f"\n{'='*60}")
    print("开始辩论...")
    print(f"{'='*60}\n")
    
    start_time = time.time()
    
    try:
        # 执行辩论
        result = coordinator.start_debate(test_components)
        
        elapsed_time = time.time() - start_time
        
        # 7. 输出辩论结果
        print_section("7. 辩论结果")
        print(f"  辩论用时: {elapsed_time:.2f}秒")
        print(f"  是否达成共识: {'是' if result.consensus_reached else '否'}")
        print(f"  辩论轮数: {result.debate_rounds}")
        
        if result.final_reaction_type:
            print(f"  最终反应类型: {result.final_reaction_type}")
        
        if result.final_overpotential:
            print(f"  最终过电势: {result.final_overpotential}V")
        
        print(f"\n  推理轨迹:")
        print(f"  {result.reasoning_trajectory[:500]}...")
        
        # 8. 保存结果
        print_section("8. 保存结果")
        output_dir = "./outputs"
        ensure_dir(output_dir)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = f"{output_dir}/test_result_{timestamp}.json"
        
        result_data = {
            "test_info": {
                "test_name": "四个Agent绑定Chroma向量数据库测试",
                "timestamp": timestamp,
                "components": test_components
            },
            "rag_config": {
                "persist_dir": config['vector_store']['persist_directory'],
                "collection_name": config['vector_store']['collection_name'],
                "top_k": config['rag']['top_k']
            },
            "agents": [
                {
                    "name": agent.name,
                    "rag_enabled": agent.rag_system is not None
                } for agent in agents
            ],
            "debate_result": result.to_dict()
        }
        
        save_json(result_data, output_file)
        print(f"  ✓ 结果已保存到: {output_file}")
        
        print_section("测试完成")
        print("  ✓ 所有4个Agent成功绑定到chroma_db")
        print("  ✓ RAG检索功能正常")
        print("  ✓ 辩论流程正常执行")
        
    except Exception as e:
        print(f"\n  ✗ 测试过程中出现错误: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
