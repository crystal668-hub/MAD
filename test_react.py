"""
===================================
ReAct功能快速测试
功能：验证ReAct推理能力是否正常工作
===================================
"""

def test_react_imports():
    """测试1: 验证所有ReAct模块可以正常导入"""
    print("测试1: 导入ReAct模块...")
    try:
        from agents.react_reasoning import (
            ReActEngine, 
            ReActTrajectory, 
            ReActStep,
            ActionType,
            create_react_prompt
        )
        from agents.react_agent import ReActAgent
        from agents.llm_agents import OpenAIAgent, XAIAgent, GoogleAgent, DeepSeekAgent
        
        print("✓ 所有模块导入成功")
        return True
    except Exception as e:
        print(f"✗ 导入失败: {str(e)}")
        return False


def test_react_data_structures():
    """测试2: 验证ReAct数据结构"""
    print("\n测试2: 验证ReAct数据结构...")
    try:
        from agents.react_reasoning import ReActStep, ReActTrajectory, ActionType
        
        # 创建推理步骤
        step = ReActStep(
            step_number=1,
            thought="测试思考",
            action=ActionType.SEARCH_RAG,
            action_input={"query": "test", "top_k": 5},
            observation="测试观察结果"
        )
        
        # 创建推理轨迹
        trajectory = ReActTrajectory(query="测试查询")
        trajectory.add_step(step)
        trajectory.finalize("测试答案")
        
        # 验证数据
        assert trajectory.total_steps == 1
        assert trajectory.final_answer == "测试答案"
        assert len(trajectory.steps) == 1
        
        # 测试转换为字典
        traj_dict = trajectory.to_dict()
        assert 'query' in traj_dict
        assert 'steps' in traj_dict
        assert 'final_answer' in traj_dict
        
        print("✓ ReAct数据结构正常")
        return True
    except Exception as e:
        print(f"✗ 数据结构测试失败: {str(e)}")
        return False


def test_react_engine():
    """测试3: 验证ReAct引擎"""
    print("\n测试3: 验证ReAct引擎...")
    try:
        from agents.react_reasoning import ReActEngine, ActionType
        
        # 创建引擎
        engine = ReActEngine(max_steps=5, verbose=False)
        
        # 注册测试工具
        def test_tool(query: str) -> str:
            return f"工具返回: {query}"
        
        engine.register_tool(ActionType.SEARCH_RAG, test_tool)
        
        # 执行动作
        observation, data = engine.execute_action(
            ActionType.SEARCH_RAG,
            {"query": "测试查询"}
        )
        
        assert "工具返回" in observation or observation is not None
        
        # 测试解析LLM响应
        test_response = """
        Thought: 需要检索相关信息
        Action: search_rag
        Action Input: {"query": "催化剂性能"}
        """
        
        thought, action, action_input = engine.parse_llm_response(test_response)
        assert thought != ""
        assert action is not None
        
        print("✓ ReAct引擎功能正常")
        return True
    except Exception as e:
        print(f"✗ 引擎测试失败: {str(e)}")
        return False


def test_agent_inheritance():
    """测试4: 验证Agent继承关系"""
    print("\n测试4: 验证Agent继承关系...")
    try:
        from agents.react_agent import ReActAgent
        from agents.llm_agents import OpenAIAgent, XAIAgent, GoogleAgent, DeepSeekAgent
        from agents.base_agent import BaseAgent
        
        # 验证继承关系
        assert issubclass(ReActAgent, BaseAgent)
        assert issubclass(OpenAIAgent, ReActAgent)
        assert issubclass(XAIAgent, ReActAgent)
        assert issubclass(GoogleAgent, ReActAgent)
        assert issubclass(DeepSeekAgent, ReActAgent)
        
        print("✓ Agent继承关系正确")
        return True
    except Exception as e:
        print(f"✗ 继承关系测试失败: {str(e)}")
        return False


def test_create_react_prompt():
    """测试5: 验证ReAct提示生成"""
    print("\n测试5: 验证ReAct提示生成...")
    try:
        from agents.react_reasoning import create_react_prompt, ReActStep, ActionType
        
        # 创建测试步骤
        steps = [
            ReActStep(
                step_number=1,
                thought="第一步思考",
                action=ActionType.SEARCH_RAG,
                action_input={"query": "test"},
                observation="第一步观察"
            )
        ]
        
        # 生成提示
        prompt = create_react_prompt(
            query="测试查询",
            previous_steps=steps,
            available_tools=["search_rag", "query_experience"]
        )
        
        assert "测试查询" in prompt
        assert "第一步思考" in prompt
        assert len(prompt) > 0
        
        print("✓ ReAct提示生成正常")
        return True
    except Exception as e:
        print(f"✗ 提示生成测试失败: {str(e)}")
        return False


def test_trajectory_serialization():
    """测试6: 验证轨迹序列化"""
    print("\n测试6: 验证轨迹序列化...")
    try:
        from agents.react_reasoning import ReActTrajectory, ReActStep, ActionType
        import json
        
        # 创建轨迹
        trajectory = ReActTrajectory(query="序列化测试")
        
        for i in range(3):
            step = ReActStep(
                step_number=i+1,
                thought=f"思考{i+1}",
                action=ActionType.SEARCH_RAG,
                action_input={"query": f"query{i+1}"},
                observation=f"观察{i+1}"
            )
            trajectory.add_step(step)
        
        trajectory.finalize("最终答案")
        
        # 测试JSON序列化
        json_str = trajectory.to_json()
        assert len(json_str) > 0
        
        # 验证可以解析回来
        data = json.loads(json_str)
        assert data['query'] == "序列化测试"
        assert data['total_steps'] == 3
        assert data['final_answer'] == "最终答案"
        
        # 测试字典转换
        traj_dict = trajectory.to_dict()
        assert len(traj_dict['steps']) == 3
        
        # 测试摘要
        summary = trajectory.get_trajectory_summary()
        assert "序列化测试" in summary
        assert "3" in summary
        
        print("✓ 轨迹序列化功能正常")
        return True
    except Exception as e:
        print(f"✗ 序列化测试失败: {str(e)}")
        return False


def test_action_types():
    """测试7: 验证动作类型"""
    print("\n测试7: 验证动作类型...")
    try:
        from agents.react_reasoning import ActionType
        
        # 验证所有动作类型
        assert ActionType.SEARCH_RAG.value == "search_rag"
        assert ActionType.QUERY_EXPERIENCE.value == "query_experience"
        assert ActionType.ANALYZE.value == "analyze"
        assert ActionType.CONCLUDE.value == "conclude"
        
        # 验证枚举成员数量
        action_types = list(ActionType)
        assert len(action_types) == 4
        
        print("✓ 动作类型定义正确")
        return True
    except Exception as e:
        print(f"✗ 动作类型测试失败: {str(e)}")
        return False


def run_all_tests():
    """运行所有测试"""
    print("="*70)
    print("ReAct功能测试套件")
    print("="*70)
    
    tests = [
        test_react_imports,
        test_react_data_structures,
        test_react_engine,
        test_agent_inheritance,
        test_create_react_prompt,
        test_trajectory_serialization,
        test_action_types
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"测试执行出错: {str(e)}")
            results.append(False)
    
    print("\n" + "="*70)
    print("测试结果汇总")
    print("="*70)
    print(f"总测试数: {len(results)}")
    print(f"通过: {sum(results)}")
    print(f"失败: {len(results) - sum(results)}")
    
    if all(results):
        print("\n✓ 所有测试通过！ReAct功能正常工作。")
    else:
        print("\n✗ 部分测试失败，请检查错误信息。")
    
    return all(results)


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
