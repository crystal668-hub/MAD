"""
使用示例脚本
演示MAD系统的基本使用方法
"""

# ============================================================
# 示例1: 完整运行辩论系统
# ============================================================

def example_full_system():
    """完整系统运行示例"""
    from main import MADSystem
    
    print("=" * 60)
    print("示例1: 完整运行辩论系统")
    print("=" * 60)
    
    # 创建系统实例
    system = MADSystem(config_path="./config/config.yaml")
    
    # 初始化（跳过RAG以加快演示）
    system.initialize(skip_rag=True)
    
    # 定义化学组分
    components = ["硫酸", "氢氧化钠", "氯化钠", "硝酸", "碳酸钙"]
    
    # 运行辩论
    print(f"\n分析组分: {', '.join(components)}\n")
    result = system.run_debate(components)
    
    # 打印结果
    print("\n辩论结果:")
    print(f"  共识达成: {result['consensus_reached']}")
    print(f"  反应类型: {result['final_reaction_type']}")
    print(f"  过电势: {result['final_overpotential']}")
    print(f"  辩论轮数: {result['debate_rounds']}")


# ============================================================
# 示例2: 单独使用RAG系统
# ============================================================

def example_rag_system():
    """RAG系统使用示例"""
    from database import RAGSystem
    
    print("\n" + "=" * 60)
    print("示例2: 单独使用RAG系统")
    print("=" * 60)
    
    # 初始化RAG系统
    rag = RAGSystem(
        data_dir="./data/raw",
        persist_dir="./data/chroma_db",
        collection_name="test_collection",
        chunk_size=256,
        top_k=3
    )
    
    # 如果索引不存在，构建它
    if not rag._index_exists():
        print("\n构建RAG索引...")
        rag.build_index()
    
    # 执行查询
    query = "氧化还原反应的过电势是多少？"
    print(f"\n查询: {query}")
    
    result = rag.query(query)
    print(f"\n答案: {result['answer']}")
    
    # 打印来源文档
    if result['source_nodes']:
        print("\n来源文档:")
        for i, node in enumerate(result['source_nodes'][:2], 1):
            print(f"\n{i}. (相关度: {node['score']:.3f})")
            print(f"   {node['text'][:150]}...")


# ============================================================
# 示例3: 单独使用Agent
# ============================================================

def example_agent():
    """Agent使用示例"""
    from agents import create_agent
    import os
    
    print("\n" + "=" * 60)
    print("示例3: 单独使用Agent")
    print("=" * 60)
    
    # 检查API密钥
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\n⚠ 未设置OPENAI_API_KEY环境变量")
        print("请先设置API密钥: export OPENAI_API_KEY=your-key")
        return
    
    # 创建OpenAI Agent
    agent = create_agent(
        agent_type="openai",
        agent_id="demo_agent",
        name="Demo Agent",
        model_config={
            "provider": "openai",
            "model": "gpt-3.5-turbo",  # 使用较便宜的模型演示
            "api_key": api_key,
            "temperature": 0.7,
            "max_tokens": 500
        }
    )
    
    # 生成响应
    prompt = "请简要解释什么是化学反应的过电势？（50字以内）"
    print(f"\n提示: {prompt}")
    
    response = agent.generate_response(prompt)
    print(f"\nAgent响应:\n{response.content}")


# ============================================================
# 示例4: 经验库操作
# ============================================================

def example_experience_store():
    """经验库使用示例"""
    from experience import ExperienceStore
    
    print("\n" + "=" * 60)
    print("示例4: 经验库操作")
    print("=" * 60)
    
    # 初始化经验库
    store = ExperienceStore(
        storage_path="./data/example_experience.json",
        max_experiences=100
    )
    
    # 添加示例经验
    experiences = [
        {
            "components": ["硫酸", "氢氧化钠", "氯化钠"],
            "reaction_type": "酸碱中和反应",
            "overpotential": 0.1,
            "reasoning": "硫酸和氢氧化钠发生中和反应，过电势较低",
            "confidence": 0.95
        },
        {
            "components": ["硫酸", "氯化钠", "硝酸"],
            "reaction_type": "氧化还原反应",
            "overpotential": 0.45,
            "reasoning": "涉及电子转移，过电势较高",
            "confidence": 0.85
        }
    ]
    
    for exp in experiences:
        store.add_experience(exp)
    
    # 查询相关经验
    query_components = ["硫酸", "氯化钠"]
    print(f"\n查询组分: {', '.join(query_components)}")
    
    results = store.query_experiences(
        components=query_components,
        top_k=2
    )
    
    print(f"\n找到 {len(results)} 条相关经验:")
    for i, exp in enumerate(results, 1):
        print(f"\n{i}. {exp['reaction_type']} (相似度: {exp['similarity']:.2f})")
        print(f"   组分: {', '.join(exp['components'])}")
        print(f"   过电势: {exp['overpotential']}V")
    
    # 统计信息
    stats = store.get_statistics()
    print(f"\n经验库统计:")
    print(f"  总经验数: {stats['total_experiences']}")
    print(f"  平均过电势: {stats['avg_overpotential']:.3f}V")


# ============================================================
# 示例5: 配置管理
# ============================================================

def example_config():
    """配置管理示例"""
    from utils import load_config
    from agents import AgentConfig
    
    print("\n" + "=" * 60)
    print("示例5: 配置管理")
    print("=" * 60)
    
    # 加载配置
    config = load_config("./config/config.yaml")
    
    print("\n系统配置:")
    print(f"  辩论最大轮数: {config['debate']['max_rounds']}")
    print(f"  共识阈值: {config['debate']['consensus_threshold']}")
    print(f"  RAG chunk大小: {config['rag']['chunk_size']}")
    print(f"  RAG top-k: {config['rag']['top_k']}")
    
    # 使用AgentConfig
    agent_config = AgentConfig(config)
    
    print("\nAgent配置:")
    for i in range(1, 4):
        llm_cfg = agent_config.get_llm_config(f"agent{i}")
        print(f"  Agent{i}: {llm_cfg['provider']} - {llm_cfg['model']}")
    
    print("\n化学反应类型:")
    chem_config = agent_config.get_chemistry_config()
    for i, reaction in enumerate(chem_config['reaction_types'], 1):
        print(f"  {i}. {reaction}")


# ============================================================
# 示例6: 辅助工具
# ============================================================

def example_helpers():
    """辅助工具示例"""
    from utils import (
        parse_component_string,
        validate_components,
        format_component_list,
        create_experiment_id,
        dict_to_table
    )
    
    print("\n" + "=" * 60)
    print("示例6: 辅助工具")
    print("=" * 60)
    
    # 解析组分字符串
    component_str = "硫酸、氢氧化钠、氯化钠、硝酸、碳酸钙"
    components = parse_component_string(component_str)
    print(f"\n原始字符串: {component_str}")
    print(f"解析结果: {components}")
    
    # 验证组分
    is_valid, msg = validate_components(components)
    print(f"\n验证结果: {msg}")
    
    # 格式化组分列表
    formatted = format_component_list(components)
    print(f"格式化输出: {formatted}")
    
    # 创建实验ID
    exp_id = create_experiment_id(components)
    print(f"\n实验ID: {exp_id}")
    
    # 字典转表格
    data = {
        "反应类型": "氧化还原反应",
        "过电势": "0.45V",
        "置信度": "0.92",
        "辩论轮数": "3"
    }
    print("\n结果表格:")
    print(dict_to_table(data))


# ============================================================
# 主程序
# ============================================================

def main():
    """运行所有示例"""
    import sys
    
    examples = {
        "1": ("完整系统", example_full_system),
        "2": ("RAG系统", example_rag_system),
        "3": ("Agent", example_agent),
        "4": ("经验库", example_experience_store),
        "5": ("配置管理", example_config),
        "6": ("辅助工具", example_helpers),
    }
    
    print("\n" + "=" * 60)
    print("MAD系统使用示例")
    print("=" * 60)
    print("\n可用示例:")
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")
    print("  0. 运行所有示例")
    print("  q. 退出")
    
    choice = input("\n请选择示例编号: ").strip()
    
    if choice == 'q':
        print("退出")
        return
    
    if choice == '0':
        # 运行所有示例（除了需要API密钥的）
        for key in ["2", "4", "5", "6"]:
            try:
                examples[key][1]()
            except Exception as e:
                print(f"\n示例 {key} 执行失败: {str(e)}")
    elif choice in examples:
        try:
            examples[choice][1]()
        except Exception as e:
            print(f"\n示例执行失败: {str(e)}")
            import traceback
            traceback.print_exc()
    else:
        print("无效的选择")


if __name__ == "__main__":
    main()
