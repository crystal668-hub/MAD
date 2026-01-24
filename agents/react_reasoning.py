"""
===================================
ReAct推理模块
功能：实现ReAct (Reasoning + Acting) 推理范式
适配：OpenAI Function Calling (Structured Output)
===================================
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Callable, Union
from enum import Enum
import json
from datetime import datetime


class ActionType(Enum):
    """动作类型枚举"""
    SEARCH_RAG = "search_rag"          # 从RAG系统检索知识
    QUERY_EXPERIENCE = "query_experience" # 查询经验库
    ANALYZE = "analyze"                # 分析当前信息
    CONCLUDE = "conclude"              # 得出最终结论


@dataclass
class ReActStep:
    """
    ReAct推理的单步
    包含：Thought→ Action→ Observation
    """
    step_number: int
    thought: str
    action: Union[ActionType, str]  # 兼容枚举或字符串
    action_input: Dict[str, Any]
    observation: str
    tool_call_id: Optional[str] = None  # 关键：存储OpenAI返回的call_id
    observation_data: Optional[Any] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    @property
    def action_name(self) -> str:
        """安全获取动作名称的辅助属性"""
        return self.action.value if isinstance(self.action, ActionType) else str(self.action)

    def to_dict(self) -> Dict:
        return {
            "step_number": self.step_number,
            "thought": self.thought,
            "action": self.action_name,
            "action_input": self.action_input,
            "observation": self.observation,
            "tool_call_id": self.tool_call_id,
            "observation_data": self.observation_data,
            "timestamp": self.timestamp
        }


@dataclass
class ReActTrajectory:
    """
    ReAct推理轨迹
    记录完整的推理过程
    """
    query: str  
    steps: List[ReActStep] = field(default_factory=list)
    final_answer: Optional[str] = None  
    total_steps: int = 0  
    start_time: str = field(default_factory=lambda: datetime.now().isoformat())
    end_time: Optional[str] = None
    
    def add_step(self, step: ReActStep) -> None:
        self.steps.append(step)
        self.total_steps = len(self.steps)
    
    def finalize(self, final_answer: str) -> None:
        self.final_answer = final_answer
        self.end_time = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            "query": self.query,
            "steps": [step.to_dict() for step in self.steps],
            "final_answer": self.final_answer,
            "total_steps": self.total_steps,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
    
    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)
    
    def get_trajectory_summary(self) -> str:
        summary_parts = [
            f"=== ReAct推理轨迹 ===",
            f"原始问题: {self.query}",
            f"推理步骤数: {self.total_steps}",
            f""
        ]
        
        for step in self.steps:
            summary_parts.append(f"步骤 {step.step_number}:")
            summary_parts.append(f"  思考: {step.thought[:100]}...")
            summary_parts.append(f"  动作: {step.action_name}")
            summary_parts.append(f"  观察: {step.observation[:100]}...")
            summary_parts.append("")
        
        if self.final_answer:
            summary_parts.append(f"最终答案: {self.final_answer[:200]}...")
        
        return "\n".join(summary_parts)

    def to_context_messages(self, system_prompt: str) -> List[Dict[str, Any]]:
        """
        将推理轨迹转换为OpenAI Chat API messages
        这是构建上下文的核心方法
        """
        messages: List[Dict[str, Any]] = [
            {
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user", 
                "content": self.query
            }
        ]

        for step in self.steps:
            # 1. 优先使用真实的 tool_call_id，如果没有则生成一个
            call_id = step.tool_call_id or f"react_step_{step.step_number}"
            
            # 2. Assistant Message (Thought + Action)
            messages.append({
                "role": "assistant",
                "content": step.thought,  # 包含思考过程
                "tool_calls": [
                    {
                        "id": call_id,
                        "type": "function",
                        "function": {
                            "name": step.action_name, # 使用安全属性
                            "arguments": json.dumps(step.action_input, ensure_ascii=False)
                        }
                    }
                ]
            })
            
            # 3. Tool Message (Observation)
            messages.append({
                "role": "tool",
                "tool_call_id": call_id, # 必须与上面的 id 一致
                "content": step.observation
            })

        return messages


class ReActEngine:
    """ReAct推理引擎"""
    
    def __init__(self, max_steps: int = 10, verbose: bool = True):
        self.max_steps = max_steps
        self.verbose = verbose
        self.tools: Dict[ActionType, Callable] = {}
    
    def register_tool(self, action_type: ActionType, tool_func: Callable) -> None:
        self.tools[action_type] = tool_func
        if self.verbose:
            print(f"已注册工具: {action_type.value}")
    
    def execute_action(self, action: Union[ActionType, str], action_input: Dict[str, Any]) -> tuple[str, Any]:
        """执行动作，支持枚举或字符串输入"""
        # 1. 解析动作类型
        try:
            if isinstance(action, ActionType):
                normalized_action = action
            else:
                normalized_action = self.resolve_action_type(action)
        except ValueError as e:
            return f"系统错误: {str(e)}", None

        # 2. 检查工具是否存在
        if normalized_action not in self.tools:
            return f"错误: 未注册的工具 {normalized_action.value}", None
        
        # 3. 执行工具
        try:
            tool_func = self.tools[normalized_action]
            result = tool_func(**action_input)
            
            # 4. 格式化观察结果
            if normalized_action == ActionType.SEARCH_RAG:
                observation = self._format_rag_observation(result)
            elif normalized_action == ActionType.QUERY_EXPERIENCE:
                observation = self._format_experience_observation(result)
            elif normalized_action == ActionType.ANALYZE:
                observation = result
            elif normalized_action == ActionType.CONCLUDE:
                observation = result
            else:
                observation = str(result)
            
            return observation, result
        
        except Exception as e:
            error_msg = f"执行工具 {normalized_action.value} 失败: {str(e)}"
            if self.verbose:
                print(error_msg)
            return error_msg, None

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        """获取OpenAI Function Calling工具定义"""
        # 注意：这里的定义需要与 register_tool 中的函数签名保持一致
        return [
            {
                "type": "function",
                "function": {
                    "name": ActionType.SEARCH_RAG.value,
                    "description": "从文献知识库检索相关信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "检索查询"},
                            "top_k": {"type": "integer", "description": "返回结果数量", "default": 5}
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": ActionType.QUERY_EXPERIENCE.value,
                    "description": "查询历史经验库",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "components": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "化学组分列表"
                            }
                        },
                        "required": ["components"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": ActionType.ANALYZE.value,
                    "description": "分析当前收集的信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "context": {"type": "string", "description": "需要分析的上下文"}
                        },
                        "required": ["context"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": ActionType.CONCLUDE.value,
                    "description": "给出最终结论",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "conclusion": {"type": "string", "description": "最终结论"}
                        },
                        "required": ["conclusion"]
                    }
                }
            }
        ]

    def resolve_action_type(self, function_name: str) -> ActionType:
        """根据function名称解析动作类型"""
        try:
            return ActionType(function_name)
        except ValueError:
            valid = ", ".join([action.value for action in ActionType])
            raise ValueError(f"未知的工具名称: '{function_name}'。当前可用工具: {valid}")

    def parse_tool_arguments(self, arguments: str) -> Dict[str, Any]:
        """解析工具调用参数（JSON字符串）"""
        if not arguments:
            return {}
        try:
            return json.loads(arguments)
        except json.JSONDecodeError:
            # 简单的容错，返回空字典或者特定错误
            print(f"警告: 无法解析工具参数 JSON: {arguments}")
            return {}
    
    def _format_rag_observation(self, results: List[Dict]) -> str:
        """格式化RAG检索结果"""
        if not results:
            return "未检索到相关文献知识。"
        
        formatted = [f"检索到 {len(results)} 条相关文献知识:\n"]
        for i, result in enumerate(results[:3], 1):
            score = result.get('score', 0)
            text = result.get('text', '')[:200]
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
            formatted.append(f"{i}. 组分: {', '.join(components)} | 反应: {reaction} | 过电势: {overpotential}")
        return "\n".join(formatted)
    
    def should_continue(self, step_number: int, last_action: Optional[ActionType]) -> bool:
        if step_number >= self.max_steps:
            return False
        if last_action == ActionType.CONCLUDE:
            return False
        return True
    
    def log_step(self, step: ReActStep) -> None:
        if not self.verbose:
            return
        
        print(f"\n{'='*60}")
        print(f"Step {step.step_number}")
        print(f"{'='*60}")
        print(f" Thought: {step.thought}")
        print(f" Action: {step.action_name}") # 使用安全属性
        print(f" Action Input: {step.action_input}")
        print(f" Observation: {step.observation[:300]}{'...' if len(step.observation) > 300 else ''}")
        print(f"{'='*60}\n")

# 注意：已删除独立的 create_react_prompt 函数
# 请直接使用 trajectory.to_context_messages(system_prompt)