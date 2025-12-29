"""
===================================
ReAct推理模块
功能：实现ReAct (Reasoning + Acting) 推理范式
将Agent的推理过程分解为 Thought → Action → Observation 的循环
===================================
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Callable
from enum import Enum
import json
from datetime import datetime


class ActionType(Enum):
    """动作类型枚举"""
    SEARCH_RAG = "search_rag"  # 从RAG系统检索知识
    QUERY_EXPERIENCE = "query_experience"  # 查询经验库
    ANALYZE = "analyze"  # 分析当前信息
    CONCLUDE = "conclude"  # 得出最终结论


@dataclass
class ReActStep:
    """
    ReAct推理的单步
    包含：Thought（思考）→ Action（动作）→ Observation（观察）
    """
    step_number: int  # 步骤编号
    thought: str  # Agent对当前问题的思考和分析
    action: ActionType  # Agent决定采取的动作
    action_input: Dict[str, Any]  # 动作的输入参数
    observation: str  # 动作执行后的观察结果
    observation_data: Optional[Any] = None  # 观察到的原始数据
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            "step_number": self.step_number,
            "thought": self.thought,
            "action": self.action.value,
            "action_input": self.action_input,
            "observation": self.observation,
            "observation_data": self.observation_data,
            "timestamp": self.timestamp
        }


@dataclass
class ReActTrajectory:
    """
    ReAct推理轨迹
    记录完整的推理过程：从原始query到最终answer的所有步骤
    """
    query: str  # 原始查询
    steps: List[ReActStep] = field(default_factory=list)  # 推理步骤列表
    final_answer: Optional[str] = None  # 最终答案
    total_steps: int = 0  # 总步骤数
    start_time: str = field(default_factory=lambda: datetime.now().isoformat())
    end_time: Optional[str] = None
    
    def add_step(self, step: ReActStep) -> None:
        """添加一个推理步骤"""
        self.steps.append(step)
        self.total_steps = len(self.steps)
    
    def finalize(self, final_answer: str) -> None:
        """完成推理，设置最终答案"""
        self.final_answer = final_answer
        self.end_time = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            "query": self.query,
            "steps": [step.to_dict() for step in self.steps],
            "final_answer": self.final_answer,
            "total_steps": self.total_steps,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
    
    def to_json(self, indent: int = 2) -> str:
        """转换为JSON字符串"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)
    
    def get_trajectory_summary(self) -> str:
        """获取推理轨迹的简要总结"""
        summary_parts = [
            f"=== ReAct推理轨迹 ===",
            f"原始问题: {self.query}",
            f"推理步骤数: {self.total_steps}",
            f""
        ]
        
        for step in self.steps:
            summary_parts.append(f"步骤 {step.step_number}:")
            summary_parts.append(f"  思考: {step.thought[:100]}...")
            summary_parts.append(f"  动作: {step.action.value}")
            summary_parts.append(f"  观察: {step.observation[:100]}...")
            summary_parts.append("")
        
        if self.final_answer:
            summary_parts.append(f"最终答案: {self.final_answer[:200]}...")
        
        return "\n".join(summary_parts)


class ReActEngine:
    """
    ReAct推理引擎
    协调Agent的思考、行动和观察过程
    """
    
    def __init__(
        self,
        max_steps: int = 10,
        verbose: bool = True
    ):
        """
        初始化ReAct引擎
        
        Args:
            max_steps: 最大推理步骤数
            verbose: 是否输出详细日志
        """
        self.max_steps = max_steps
        self.verbose = verbose
        
        # 工具函数映射
        self.tools: Dict[ActionType, Callable] = {}
    
    def register_tool(self, action_type: ActionType, tool_func: Callable) -> None:
        """
        注册工具函数
        
        Args:
            action_type: 动作类型
            tool_func: 工具函数
        """
        self.tools[action_type] = tool_func
        if self.verbose:
            print(f"已注册工具: {action_type.value}")
    
    def execute_action(
        self,
        action: ActionType,
        action_input: Dict[str, Any]
    ) -> tuple[str, Any]:
        """
        执行动作
        
        Args:
            action: 动作类型
            action_input: 动作输入参数
        
        Returns:
            tuple: (观察描述, 原始数据)
        """
        if action not in self.tools:
            return f"错误: 未注册的工具 {action.value}", None
        
        try:
            tool_func = self.tools[action]
            result = tool_func(**action_input)
            
            # 根据动作类型格式化观察结果
            if action == ActionType.SEARCH_RAG:
                observation = self._format_rag_observation(result)
            elif action == ActionType.QUERY_EXPERIENCE:
                observation = self._format_experience_observation(result)
            elif action == ActionType.ANALYZE:
                observation = result  # 分析结果直接返回
            elif action == ActionType.CONCLUDE:
                observation = result  # 结论直接返回
            else:
                observation = str(result)
            
            return observation, result
        
        except Exception as e:
            error_msg = f"执行动作 {action.value} 时发生错误: {str(e)}"
            if self.verbose:
                print(error_msg)
            return error_msg, None
    
    def _format_rag_observation(self, results: List[Dict]) -> str:
        """格式化RAG检索结果"""
        if not results:
            return "未检索到相关文献知识。"
        
        formatted = [f"检索到 {len(results)} 条相关文献知识:\n"]
        for i, result in enumerate(results[:3], 1):  # 只显示前3条
            score = result.get('score', 0)
            text = result.get('text', '')[:200]  # 截取前200字符
            formatted.append(f"{i}. [相关度: {score:.3f}] {text}...")
        
        return "\n".join(formatted)
    
    def _format_experience_observation(self, experiences: List[Dict]) -> str:
        """格式化经验库查询结果"""
        if not experiences:
            return "未找到相关历史经验。"
        
        formatted = [f"找到 {len(experiences)} 条相关历史经验:\n"]
        for i, exp in enumerate(experiences, 1):
            components = exp.get('components', [])
            reaction = exp.get('reaction_type', '未知')
            overpotential = exp.get('overpotential', '未知')
            formatted.append(
                f"{i}. 组分: {', '.join(components)} | "
                f"反应: {reaction} | 过电势: {overpotential}"
            )
        
        return "\n".join(formatted)
    
    def parse_llm_response(self, response: str) -> tuple[str, ActionType, Dict[str, Any]]:
        """
        解析LLM的响应，提取思考、动作和参数
        
        Args:
            response: LLM的响应文本
        
        Returns:
            tuple: (thought, action, action_input)
        """
        # 默认值
        thought = ""
        action = ActionType.ANALYZE
        action_input = {}
        
        lines = response.strip().split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            # 识别段落标记
            if line.lower().startswith('thought:') or line.lower().startswith('思考:'):
                current_section = 'thought'
                thought = line.split(':', 1)[1].strip() if ':' in line else ""
            elif line.lower().startswith('action:') or line.lower().startswith('动作:'):
                current_section = 'action'
                action_str = line.split(':', 1)[1].strip() if ':' in line else ""
                # 解析动作类型
                action = self._parse_action_type(action_str)
            elif line.lower().startswith('action input:') or line.lower().startswith('动作参数:'):
                current_section = 'action_input'
            elif current_section == 'thought' and line:
                thought += " " + line
            elif current_section == 'action_input' and line:
                # 尝试解析JSON格式的参数
                try:
                    action_input = json.loads(line)
                except:
                    # 如果不是JSON，尝试简单的key=value解析
                    if '=' in line or ':' in line:
                        parts = line.replace(':', '=').split('=', 1)
                        if len(parts) == 2:
                            action_input[parts[0].strip()] = parts[1].strip()
        
        return thought.strip(), action, action_input
    
    def _parse_action_type(self, action_str: str) -> ActionType:
        """解析动作类型字符串"""
        action_str_lower = action_str.lower()
        
        if 'rag' in action_str_lower or '检索' in action_str_lower or 'search' in action_str_lower:
            return ActionType.SEARCH_RAG
        elif 'experience' in action_str_lower or '经验' in action_str_lower:
            return ActionType.QUERY_EXPERIENCE
        elif 'conclude' in action_str_lower or '结论' in action_str_lower or 'final' in action_str_lower:
            return ActionType.CONCLUDE
        else:
            return ActionType.ANALYZE
    
    def should_continue(
        self,
        step_number: int,
        last_action: Optional[ActionType]
    ) -> bool:
        """
        判断是否应该继续推理
        
        Args:
            step_number: 当前步骤编号
            last_action: 上一步的动作
        
        Returns:
            bool: 是否继续
        """
        # 如果达到最大步骤数，停止
        if step_number >= self.max_steps:
            return False
        
        # 如果上一步是得出结论，停止
        if last_action == ActionType.CONCLUDE:
            return False
        
        return True
    
    def log_step(self, step: ReActStep) -> None:
        """记录并打印步骤信息"""
        if not self.verbose:
            return
        
        print(f"\n{'='*60}")
        print(f"步骤 {step.step_number}")
        print(f"{'='*60}")
        print(f"💭 思考: {step.thought}")
        print(f"🎯 动作: {step.action.value}")
        print(f"📝 动作参数: {step.action_input}")
        print(f"👁️ 观察: {step.observation[:300]}{'...' if len(step.observation) > 300 else ''}")
        print(f"{'='*60}\n")


def create_react_prompt(
    query: str,
    previous_steps: List[ReActStep],
    available_tools: List[str]
) -> str:
    """
    创建ReAct风格的提示词
    
    Args:
        query: 原始查询
        previous_steps: 之前的推理步骤
        available_tools: 可用的工具列表
    
    Returns:
        str: 格式化的提示词
    """
    tools_desc = "\n".join([f"- {tool}" for tool in available_tools])
    
    prompt_parts = [
        "你是一个使用ReAct推理模式的AI助手。请按照以下格式进行推理：",
        "",
        "Thought: 对当前问题的分析和下一步行动的思考",
        "Action: 选择要执行的动作",
        "Action Input: 动作的具体参数（JSON格式）",
        "",
        "可用的工具:",
        tools_desc,
        "",
        f"原始问题: {query}",
        ""
    ]
    
    # 添加之前的步骤历史
    if previous_steps:
        prompt_parts.append("之前的推理步骤:")
        for step in previous_steps:
            prompt_parts.append(f"\n步骤 {step.step_number}:")
            prompt_parts.append(f"Thought: {step.thought}")
            prompt_parts.append(f"Action: {step.action.value}")
            prompt_parts.append(f"Observation: {step.observation[:200]}...")
        prompt_parts.append("")
    
    prompt_parts.append("请继续下一步推理（如果已经可以得出结论，请使用 Action: conclude）:")
    
    return "\n".join(prompt_parts)
