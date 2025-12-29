"""
===================================
ReAct Agent实现模块
功能：集成ReAct推理能力的Agent
支持通过Thought→Action→Observation循环进行推理
===================================
"""

from typing import Dict, List, Optional, Any
from agents.base_agent import BaseAgent, AgentResponse
from agents.react_reasoning import (
    ReActEngine, 
    ReActTrajectory, 
    ReActStep,
    ActionType,
    create_react_prompt
)


class ReActAgent(BaseAgent):
    """
    具备ReAct推理能力的Agent
    将推理过程分解为明确的思考、行动和观察步骤
    """
    
    def __init__(
        self,
        agent_id: str,
        name: str,
        model_config: Dict,
        rag_system: Optional[Any] = None,
        experience_store: Optional[Any] = None,
        max_react_steps: int = 10,
        verbose: bool = True
    ):
        """
        初始化ReAct Agent
        
        Args:
            agent_id: Agent唯一标识符
            name: Agent名称
            model_config: 模型配置字典
            rag_system: RAG系统实例
            experience_store: 经验库实例
            max_react_steps: ReAct推理的最大步骤数
            verbose: 是否输出详细日志
        """
        super().__init__(agent_id, name, model_config, rag_system, experience_store)
        
        # 初始化ReAct引擎
        self.react_engine = ReActEngine(max_steps=max_react_steps, verbose=verbose)
        
        # 注册工具
        self._register_tools()
        
        # 当前推理轨迹
        self.current_trajectory: Optional[ReActTrajectory] = None
    
    def _register_tools(self) -> None:
        """注册ReAct可用的工具"""
        # 注册RAG检索工具
        self.react_engine.register_tool(
            ActionType.SEARCH_RAG,
            self._tool_search_rag
        )
        
        # 注册经验库查询工具
        self.react_engine.register_tool(
            ActionType.QUERY_EXPERIENCE,
            self._tool_query_experience
        )
        
        # 注册分析工具
        self.react_engine.register_tool(
            ActionType.ANALYZE,
            self._tool_analyze
        )
        
        # 注册结论工具
        self.react_engine.register_tool(
            ActionType.CONCLUDE,
            self._tool_conclude
        )
    
    def _tool_search_rag(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        RAG检索工具
        
        Args:
            query: 检索查询
            top_k: 返回结果数量
        
        Returns:
            List[Dict]: 检索结果
        """
        return self.retrieve_knowledge(query, top_k)
    
    def _tool_query_experience(self, components: List[str]) -> List[Dict]:
        """
        经验库查询工具
        
        Args:
            components: 化学组分列表
        
        Returns:
            List[Dict]: 相关经验列表
        """
        return self.retrieve_experience(components)
    
    def _tool_analyze(self, context: str) -> str:
        """
        分析工具
        
        Args:
            context: 需要分析的上下文
        
        Returns:
            str: 分析结果
        """
        return f"已记录待分析内容: {context[:100]}..."
    
    def _tool_conclude(self, conclusion: str) -> str:
        """
        结论工具
        
        Args:
            conclusion: 结论内容
        
        Returns:
            str: 确认信息
        """
        return conclusion
    
    def generate_response_with_react(
        self,
        query: str,
        components: Optional[List[str]] = None,
        context: Optional[Dict] = None
    ) -> tuple[AgentResponse, ReActTrajectory]:
        """
        使用ReAct推理生成响应
        
        Args:
            query: 输入查询
            components: 化学组分列表
            context: 额外上下文
        
        Returns:
            tuple: (AgentResponse, ReActTrajectory)
        """
        # 创建新的推理轨迹
        trajectory = ReActTrajectory(query=query)
        self.current_trajectory = trajectory
        
        # 构建初始上下文
        if components:
            query_with_context = f"{query}\n\n分析的金属催化剂元素: {', '.join(components)}"
        else:
            query_with_context = query
        
        # ReAct推理循环
        step_number = 0
        last_action = None
        final_answer = None
        
        while self.react_engine.should_continue(step_number, last_action):
            step_number += 1
            
            # 构建ReAct提示
            available_tools = [
                "search_rag: 从文献知识库检索相关信息",
                "query_experience: 查询历史经验库",
                "analyze: 分析当前收集的信息",
                "conclude: 得出最终结论"
            ]
            
            react_prompt = create_react_prompt(
                query_with_context,
                trajectory.steps,
                available_tools
            )
            
            # 调用LLM获取思考和行动
            llm_response = self._call_llm(react_prompt)
            
            # 解析LLM响应
            thought, action, action_input = self.react_engine.parse_llm_response(llm_response)
            
            # 如果没有解析到有效的动作，使用智能默认策略
            if not thought or not action_input:
                thought, action, action_input = self._smart_default_action(
                    step_number, 
                    trajectory.steps,
                    components
                )
            
            # 执行动作
            observation, observation_data = self.react_engine.execute_action(
                action,
                action_input
            )
            
            # 创建推理步骤
            step = ReActStep(
                step_number=step_number,
                thought=thought,
                action=action,
                action_input=action_input,
                observation=observation,
                observation_data=observation_data
            )
            
            # 添加到轨迹
            trajectory.add_step(step)
            
            # 记录步骤
            self.react_engine.log_step(step)
            
            # 如果是结论动作，提取最终答案
            if action == ActionType.CONCLUDE:
                final_answer = observation
                last_action = action
                break
            
            last_action = action
        
        # 如果循环结束但没有明确结论，生成最终答案
        if final_answer is None:
            final_answer = self._generate_final_answer(trajectory)
        
        # 完成轨迹
        trajectory.finalize(final_answer)
        
        # 构建AgentResponse
        response = AgentResponse(
            content=final_answer,
            reasoning=trajectory.get_trajectory_summary(),
            sources=self._extract_sources(trajectory)
        )
        
        return response, trajectory
    
    def _call_llm(self, prompt: str) -> str:
        """
        调用LLM（需要在子类中实现具体的调用逻辑）
        
        Args:
            prompt: 输入提示
        
        Returns:
            str: LLM响应
        """
        # 这是一个抽象方法，将在具体的Agent子类中实现
        # 例如在OpenAIReActAgent中调用OpenAI API
        raise NotImplementedError("子类必须实现_call_llm方法")
    
    def _smart_default_action(
        self,
        step_number: int,
        previous_steps: List[ReActStep],
        components: Optional[List[str]]
    ) -> tuple[str, ActionType, Dict[str, Any]]:
        """
        智能默认动作策略
        当LLM未返回有效动作时，根据当前状态选择合适的默认动作
        
        Args:
            step_number: 当前步骤编号
            previous_steps: 之前的步骤
            components: 化学组分
        
        Returns:
            tuple: (thought, action, action_input)
        """
        # 检查已执行的动作类型
        executed_actions = {step.action for step in previous_steps}
        
        # 步骤1-2: 优先检索RAG知识
        if ActionType.SEARCH_RAG not in executed_actions and step_number <= 2:
            thought = "需要从文献知识库中检索相关的催化剂性能数据"
            action = ActionType.SEARCH_RAG
            action_input = {
                "query": f"催化剂性能 过电势 {' '.join(components) if components else ''}",
                "top_k": 5
            }
        
        # 步骤3-4: 查询经验库
        elif ActionType.QUERY_EXPERIENCE not in executed_actions and components:
            thought = "需要查询历史经验库，寻找类似催化剂的应用案例"
            action = ActionType.QUERY_EXPERIENCE
            action_input = {"components": components}
        
        # 步骤5+: 分析或得出结论
        elif step_number >= 5:
            thought = "基于收集的信息，可以得出最终结论"
            action = ActionType.CONCLUDE
            action_input = {"conclusion": "需要综合分析所有信息得出结论"}
        
        # 默认: 分析
        else:
            thought = "需要分析当前收集到的信息"
            action = ActionType.ANALYZE
            action_input = {"context": "分析已收集的文献和经验数据"}
        
        return thought, action, action_input
    
    def _generate_final_answer(self, trajectory: ReActTrajectory) -> str:
        """
        根据推理轨迹生成最终答案
        
        Args:
            trajectory: 推理轨迹
        
        Returns:
            str: 最终答案
        """
        # 收集所有观察结果
        all_observations = "\n\n".join([
            f"步骤{step.step_number}观察: {step.observation}"
            for step in trajectory.steps
        ])
        
        # 构建总结提示
        summary_prompt = f"""
Based on the following reasoning process, please provide the final answer:

Original Question: {trajectory.query}

Reasoning Process:
{all_observations}

Please synthesize the above information and provide a final conclusion about catalyst performance and the optimal reaction type.
"""
        
        # 调用LLM生成最终答案
        try:
            final_answer = self._call_llm(summary_prompt)
            return final_answer
        except:
            return "基于推理过程，需要进一步分析才能得出结论。"
    
    def _extract_sources(self, trajectory: ReActTrajectory) -> List[Dict]:
        """
        从推理轨迹中提取信息源
        
        Args:
            trajectory: 推理轨迹
        
        Returns:
            List[Dict]: 信息源列表
        """
        sources = []
        
        for step in trajectory.steps:
            if step.action == ActionType.SEARCH_RAG and step.observation_data:
                sources.extend(step.observation_data[:3])  # 每步最多3个来源
            elif step.action == ActionType.QUERY_EXPERIENCE and step.observation_data:
                for exp in step.observation_data[:2]:  # 每步最多2个经验
                    sources.append({
                        "type": "experience",
                        "components": exp.get("components", []),
                        "reaction_type": exp.get("reaction_type", ""),
                    })
        
        return sources
    
    def get_trajectory(self) -> Optional[ReActTrajectory]:
        """获取当前的推理轨迹"""
        return self.current_trajectory
    
    def save_trajectory(self, output_path: str) -> None:
        """
        保存推理轨迹到文件
        
        Args:
            output_path: 输出文件路径
        """
        if self.current_trajectory is None:
            print("没有可保存的推理轨迹")
            return
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(self.current_trajectory.to_json())
            print(f"推理轨迹已保存到: {output_path}")
        except Exception as e:
            print(f"保存推理轨迹失败: {str(e)}")
