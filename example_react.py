"""
===================================
ReAct Agent使用示例
功能：演示如何使用具备ReAct推理能力的Agent
===================================
"""

import os
import yaml
from pathlib import Path

from agents.llm_agents import create_agent
from database.rag_system import RAGSystem
from experience.experience_store import ExperienceStore
from database.openai_embedder import OpenAIEmbedder


def load_config():
    """加载配置文件"""
    config_path = Path(__file__).parent / "config" / "config.yaml"
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def initialize_rag_system(config):
    """初始化RAG系统"""
    rag_config = config['rag']
    
    # 创建嵌入模型
    embedder = OpenAIEmbedder(
        api_key=os.getenv(rag_config['embedding']['api_key'].replace('${', '').replace('}', '')),
        model=rag_config['embedding']['model']
    )
    
    # 初始化RAG系统
    rag_system = RAGSystem(
        data_dir=rag_config['data_dir'],
        persist_dir=rag_config['persist_dir'],
        collection_name=rag_config['collection_name'],
        embedding_model=embedder,
        top_k=rag_config.get('top_k', 5)
    )
    
    return rag_system


def initialize_experience_store(config):
    """初始化经验库"""
    exp_config = config['experience']
    
    experience_store = ExperienceStore(
        storage_path=exp_config['storage_path'],
        max_experiences=exp_config.get('max_experiences', 1000),
        relevance_threshold=exp_config.get('relevance_threshold', 0.8)
    )
    
    return experience_store


def example_react_reasoning():
    """示例：使用ReAct推理分析催化剂"""
    print("="*70)
    print("ReAct Agent推理示例")
    print("="*70)
    
    # 加载配置
    config = load_config()
    
    # 初始化RAG和经验库
    print("\n初始化系统组件...")
    rag_system = initialize_rag_system(config)
    experience_store = initialize_experience_store(config)
    
    # 创建具备ReAct能力的Agent
    print("\n创建ReAct Agent...")
    agent_config = config['agents']['agents_list'][0]  # 使用第一个Agent配置
    
    agent = create_agent(
        agent_type=agent_config['type'],
        agent_id=agent_config['id'],
        name=agent_config['name'],
        model_config=agent_config['model'],
        rag_system=rag_system,
        experience_store=experience_store
    )
    
    # 测试查询
    query = "请分析以下五种金属元素作为催化剂的性能，预测哪种反应类型会产生最低的过电势"
    components = ["Pt", "Pd", "Ru", "Ir", "Rh"]
    
    print(f"\n{'='*70}")
    print(f"查询: {query}")
    print(f"金属元素: {', '.join(components)}")
    print(f"{'='*70}\n")
    
    # 使用ReAct推理
    print("开始ReAct推理过程...\n")
    response, trajectory = agent.generate_response_with_react(
        query=query,
        components=components
    )
    
    # 显示结果
    print(f"\n{'='*70}")
    print("ReAct推理完成")
    print(f"{'='*70}")
    print(f"\n最终答案:\n{response.content}")
    print(f"\n推理轨迹摘要:\n{trajectory.get_trajectory_summary()}")
    
    # 保存推理轨迹
    output_dir = Path(__file__).parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    trajectory_file = output_dir / f"react_trajectory_{timestamp}.json"
    
    agent.save_trajectory(str(trajectory_file))
    
    print(f"\n推理轨迹已保存到: {trajectory_file}")
    
    return response, trajectory


def example_comparison():
    """示例：对比传统方法和ReAct方法"""
    print("="*70)
    print("传统方法 vs ReAct方法对比示例")
    print("="*70)
    
    # 加载配置
    config = load_config()
    
    # 初始化系统
    print("\n初始化系统组件...")
    rag_system = initialize_rag_system(config)
    experience_store = initialize_experience_store(config)
    
    agent_config = config['agents']['agents_list'][0]
    
    agent = create_agent(
        agent_type=agent_config['type'],
        agent_id=agent_config['id'],
        name=agent_config['name'],
        model_config=agent_config['model'],
        rag_system=rag_system,
        experience_store=experience_store
    )
    
    query = "分析Au、Ag、Cu作为CO2RR催化剂的性能"
    components = ["Au", "Ag", "Cu"]
    
    # 方法1: 传统方法
    print(f"\n{'='*70}")
    print("方法1: 传统RAG增强提示")
    print(f"{'='*70}\n")
    
    traditional_prompt = agent.format_prompt_with_rag(
        query=query,
        components=components,
        use_experience=True
    )
    
    traditional_response = agent.generate_response(traditional_prompt)
    print(f"传统方法响应:\n{traditional_response.content[:300]}...\n")
    
    # 方法2: ReAct方法
    print(f"\n{'='*70}")
    print("方法2: ReAct推理")
    print(f"{'='*70}\n")
    
    react_response, trajectory = agent.generate_response_with_react(
        query=query,
        components=components
    )
    
    print(f"ReAct方法响应:\n{react_response.content[:300]}...\n")
    print(f"\nReAct推理步骤数: {trajectory.total_steps}")
    print(f"使用的工具: {set(step.action.value for step in trajectory.steps)}")
    
    return traditional_response, react_response, trajectory


def example_step_by_step_analysis():
    """示例：详细展示ReAct的每一步推理"""
    print("="*70)
    print("ReAct逐步推理分析")
    print("="*70)
    
    # 加载配置
    config = load_config()
    
    # 初始化系统
    print("\n初始化系统组件...")
    rag_system = initialize_rag_system(config)
    experience_store = initialize_experience_store(config)
    
    agent_config = config['agents']['agents_list'][0]
    
    agent = create_agent(
        agent_type=agent_config['type'],
        agent_id=agent_config['id'],
        name=agent_config['name'],
        model_config=agent_config['model'],
        rag_system=rag_system,
        experience_store=experience_store
    )
    
    query = "预测Ni、Co、Fe作为HER催化剂的过电势"
    components = ["Ni", "Co", "Fe"]
    
    print(f"\n查询: {query}")
    print(f"组分: {', '.join(components)}\n")
    
    # 执行ReAct推理
    response, trajectory = agent.generate_response_with_react(
        query=query,
        components=components
    )
    
    # 详细展示每一步
    print(f"\n{'='*70}")
    print("详细推理过程")
    print(f"{'='*70}\n")
    
    for step in trajectory.steps:
        print(f"{'='*70}")
        print(f"步骤 {step.step_number}")
        print(f"{'='*70}")
        print(f"\n💭 Thought (思考):")
        print(f"   {step.thought}\n")
        print(f"🎯 Action (动作):")
        print(f"   类型: {step.action.value}")
        print(f"   参数: {step.action_input}\n")
        print(f"👁️ Observation (观察):")
        print(f"   {step.observation}\n")
    
    print(f"{'='*70}")
    print("最终结论")
    print(f"{'='*70}")
    print(f"\n{trajectory.final_answer}\n")
    
    return response, trajectory


if __name__ == "__main__":
    # 运行示例
    
    # 示例1: 基本ReAct推理
    print("\n" + "="*70)
    print("示例1: 基本ReAct推理")
    print("="*70)
    try:
        response1, trajectory1 = example_react_reasoning()
    except Exception as e:
        print(f"示例1执行出错: {str(e)}")
    
    # 示例2: 对比传统方法和ReAct方法
    print("\n\n" + "="*70)
    print("示例2: 方法对比")
    print("="*70)
    try:
        trad_resp, react_resp, traj = example_comparison()
    except Exception as e:
        print(f"示例2执行出错: {str(e)}")
    
    # 示例3: 逐步分析
    print("\n\n" + "="*70)
    print("示例3: 逐步推理分析")
    print("="*70)
    try:
        response3, trajectory3 = example_step_by_step_analysis()
    except Exception as e:
        print(f"示例3执行出错: {str(e)}")
    
    print("\n所有示例执行完成!")
