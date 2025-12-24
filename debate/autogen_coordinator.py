"""
===================================
AutoGen Debate Coordinator
功能：使用AutoGen GroupChat完全管理多Agent辩论流程
===================================
"""

import re
import time
from typing import List, Dict, Optional, Tuple
from collections import Counter
from dataclasses import dataclass
import autogen
from autogen import ConversableAgent, GroupChat, GroupChatManager

from agents.base_agent import BaseAgent


@dataclass
class DebateResult:
    """
    辩论结果数据类
    封装辩论的最终结果和过程信息
    """
    consensus_reached: bool  # 是否达成共识
    final_reaction_type: Optional[str]  # 最终确定的反应类型
    final_overpotential: Optional[float]  # 最终过电势
    reasoning_trajectory: str  # 推理轨迹
    debate_rounds: int  # 辩论轮数
    debate_history: List[Dict]  # 完整辩论历史
    time_elapsed: float  # 耗时(秒)
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            "consensus_reached": self.consensus_reached,
            "final_reaction_type": self.final_reaction_type,
            "final_overpotential": self.final_overpotential,
            "reasoning_trajectory": self.reasoning_trajectory,
            "debate_rounds": self.debate_rounds,
            "debate_history": self.debate_history,
            "time_elapsed": self.time_elapsed
        }


class AutoGenDebateCoordinator:
    """
    AutoGen辩论协调器
    完全依赖AutoGen GroupChat管理辩论流程，无需传统的Debate Manager
    """
    
    def __init__(
        self,
        agents: List[BaseAgent],
        config: Dict
    ):
        """
        初始化AutoGen辩论协调器
        
        Args:
            agents: Agent列表
            config: 辩论配置
        """
        self.agents = agents
        self.config = config
        
        # 辩论参数
        self.max_rounds = config.get('max_rounds', 10)
        self.consensus_threshold = config.get('consensus_threshold', 3)
        
        # AutoGen组件
        self.autogen_agents = []
        self.group_chat = None
        self.manager = None
    
    def start_debate(
        self,
        components: List[str],
        initial_prompt: Optional[str] = None
    ) -> DebateResult:
        """
        开始辩论
        
        Args:
            components: 金属催化剂元素列表
            initial_prompt: 初始提示（可选）
        
        Returns:
            DebateResult: 辩论结果
        """
        print("=" * 60)
        print("Starting Multi-Agent Debate (AutoGen Mode)")
        print("=" * 60)
        
        start_time = time.time()
        
        # 构建初始提示
        if initial_prompt is None:
            initial_prompt = self._build_initial_prompt(components)
        
        print(f"\nInitial Question:\n{initial_prompt}\n")
        
        # 为每个Agent准备RAG增强提示
        self._prepare_agents_with_rag(components, initial_prompt)
        
        # 创建AutoGen agents和GroupChat
        self._create_autogen_group_chat()
        
        # 启动对话
        try:
            # 使用第一个agent发起对话
            first_agent = self.autogen_agents[0]
            first_agent.initiate_chat(
                self.manager,
                message=initial_prompt,
                max_turns=self.max_rounds * len(self.agents)
            )
            
            # 提取辩论历史
            debate_history = self.group_chat.messages
            
            # 分析结果
            result = self._extract_consensus_from_history(debate_history, components)
            
            elapsed_time = time.time() - start_time
            result.time_elapsed = elapsed_time
            
            print("\n" + "=" * 60)
            print(f"Debate Ended (Time: {elapsed_time:.2f}s)")
            print("=" * 60)
            
            return result
            
        except Exception as e:
            print(f"Error during debate: {str(e)}")
            elapsed_time = time.time() - start_time
            
            return DebateResult(
                consensus_reached=False,
                final_reaction_type=None,
                final_overpotential=None,
                reasoning_trajectory=f"Debate failed: {str(e)}",
                debate_rounds=0,
                debate_history=[],
                time_elapsed=elapsed_time
            )
    
    def _build_initial_prompt(self, components: List[str]) -> str:
        """
        构建初始辩论提示
        
        Args:
            components: 金属催化剂元素列表
        
        Returns:
            str: 初始提示
        """
        components_str = ", ".join(components)
        
        prompt = f"""Please analyze the catalytic performance of the following five metal elements and determine which reaction type produces the lowest overpotential when these metals act as catalysts:

**Metal Catalyst Elements**: {components_str}

**Available Reaction Types**:
1. CO2RR (CO2 Reduction Reaction)
2. EOR (Ethanol Oxidation Reaction)
3. HER (Hydrogen Evolution Reaction)
4. HOR (Hydrogen Oxidation Reaction)
5. HZOR (Hydrazine Oxidation Reaction)
6. O5H (Oxidation of 5-hydroxymethylfurfural)
7. OER (Oxygen Evolution Reaction)
8. ORR (Oxygen Reduction Reaction)
9. UOR (Urea Oxidation Reaction)

**Requirements**:
1. Analyze based on catalytic principles, metal properties, and retrieved literature knowledge
2. Consider the catalytic activity, selectivity, and stability of these metal elements
3. Provide specific reaction type recommendations
4. Estimate the overpotential value for the catalytic reaction
5. Provide detailed reasoning process about catalytic mechanisms
6. Cite evidence supporting your viewpoint

Please provide your analysis in the format:
**Reaction Type**: [TYPE]
**Overpotential**: [VALUE]V
**Reasoning**: [Your detailed analysis]

Experts, please share your opinions and reach consensus through debate."""
        
        return prompt
    
    def _prepare_agents_with_rag(self, components: List[str], initial_prompt: str) -> None:
        """
        为每个Agent准备RAG增强的系统消息
        
        Args:
            components: 金属催化剂元素列表
            initial_prompt: 初始提示
        """
        self.enhanced_prompts = {}
        
        for agent in self.agents:
            # 使用Agent自己的RAG系统增强提示
            enhanced_prompt = agent.format_prompt_with_rag(
                query=initial_prompt,
                components=components,
                use_experience=True
            )
            
            self.enhanced_prompts[agent.agent_id] = enhanced_prompt
    
    def _create_autogen_group_chat(self) -> None:
        """
        创建AutoGen GroupChat和相关组件
        """
        # 转换为AutoGen agents
        self.autogen_agents = []
        
        for agent in self.agents:
            # 获取LLM配置
            llm_config = self._get_llm_config_for_autogen(agent)
            
            # 获取增强后的系统消息
            system_message = self.enhanced_prompts.get(
                agent.agent_id,
                agent.get_system_prompt()
            )
            
            # 创建AutoGen ConversableAgent
            autogen_agent = ConversableAgent(
                name=agent.name.replace(" ", "_"),
                system_message=system_message,
                llm_config=llm_config,
                human_input_mode="NEVER",  # 完全自动化
                max_consecutive_auto_reply=self.max_rounds
            )
            
            self.autogen_agents.append(autogen_agent)
        
        print(f"Created {len(self.autogen_agents)} AutoGen agents")
        
        # 创建GroupChat
        self.group_chat = GroupChat(
            agents=self.autogen_agents,
            messages=[],
            max_round=self.max_rounds * len(self.agents),
            speaker_selection_method="round_robin",  # 轮流发言
            allow_repeat_speaker=False
        )
        
        # 创建GroupChatManager
        # 注意: 使用 round_robin 模式时不需要 llm_config,发言顺序由规则决定
        self.manager = GroupChatManager(
            groupchat=self.group_chat,
            is_termination_msg=self._create_termination_function()
        )
    
    def _get_llm_config_for_autogen(self, agent: BaseAgent) -> Dict:
        """
        为每个 ConversableAgent 生成 AutoGen 格式的 LLM 配置
        
        Args:
            agent: 自定义Agent
        
        Returns:
            Dict: AutoGen格式的LLM配置
        """
        model_config = agent.model_config
        provider = model_config.get('provider', 'openai')
        
        config = {
            "model": model_config.get('model', 'gpt-4'),
            "api_key": model_config.get('api_key'),
            "base_url": model_config.get('base_url', 'https://openrouter.ai/api/v1'),
            "temperature": model_config.get('temperature', 0.9),
            "max_tokens": model_config.get('max_tokens', 2000)
        }
        
        return config
    
    def _create_termination_function(self):
        """
        创建AutoGen的终止检测函数
        
        Returns:
            Callable: 终止检测函数
        """
        num_agents = len(self.agents)
        required_consensus = max(2, int(num_agents * 0.75))  # 至少75%的agent同意
        agent_answers = {}  # 记录每个agent的答案
        
        def is_termination_msg(msg: Dict) -> bool:
            """
            检查是否应该终止对话
            """
            content = msg.get("content", "")
            sender = msg.get("name", "")
            
            if not content or not sender:
                return False
            
            # 提取反应类型
            reaction_types = [
                "CO2RR", "EOR", "HER", "HOR", 
                "HZOR", "O5H", "OER", "ORR", "UOR"
            ]
            
            current_reaction = None
            content_upper = content.upper()
            for reaction in reaction_types:
                if reaction in content_upper:
                    current_reaction = reaction
                    break
            
            # 提取过电势值
            potential_pattern = r'(\d+\.?\d*)\s*v'
            matches = re.findall(potential_pattern, content.lower())
            current_overpotential = None
            if matches:
                try:
                    current_overpotential = float(matches[0])
                except ValueError:
                    pass
            
            # 记录该agent的答案
            if current_reaction is not None and current_overpotential is not None:
                agent_answers[sender] = (current_reaction, current_overpotential)
            
            # 检查是否所有agent都给出了答案
            if len(agent_answers) < num_agents:
                return False
            
            # 统计每种答案的支持者数量
            answer_counts = Counter(agent_answers.values())
            
            # 检查是否有任何答案达到了共识阈值
            for answer, count in answer_counts.items():
                if count >= required_consensus:
                    reaction, overpotential = answer
                    print(f"\n✓ Consensus reached: {reaction}, Overpotential: {overpotential}V ({count}/{num_agents} agents support)")
                    return True
            
            return False
        
        return is_termination_msg
    
    def _extract_consensus_from_history(
        self,
        chat_history: List[Dict],
        components: List[str]
    ) -> DebateResult:
        """
        从对话历史中提取共识结果
        
        Args:
            chat_history: AutoGen的对话历史
            components: 金属催化剂元素列表
        
        Returns:
            DebateResult: 辩论结果
        """
        if not chat_history:
            return DebateResult(
                consensus_reached=False,
                final_reaction_type=None,
                final_overpotential=None,
                reasoning_trajectory="No debate history available",
                debate_rounds=0,
                debate_history=[],
                time_elapsed=0
            )
        
        # 统计最后一轮所有agent的意见
        num_agents = len(self.agents)
        recent_responses = chat_history[-num_agents:] if len(chat_history) >= num_agents else chat_history
        
        reaction_votes = {}
        overpotentials = {}
        
        # 解析每个响应
        for msg in recent_responses:
            content = msg.get('content', '')
            sender = msg.get('name', '')
            
            # 提取反应类型
            reaction_type = self._extract_reaction_type(content)
            overpotential = self._extract_overpotential(content)
            
            if reaction_type:
                if reaction_type not in reaction_votes:
                    reaction_votes[reaction_type] = []
                reaction_votes[reaction_type].append(sender)
                
                if overpotential is not None:
                    if reaction_type not in overpotentials:
                        overpotentials[reaction_type] = []
                    overpotentials[reaction_type].append(overpotential)
        
        # 确定共识
        consensus_reached = False
        final_reaction = None
        final_overpotential = None
        
        if reaction_votes:
            # 找出支持者最多的反应类型
            final_reaction = max(reaction_votes.items(), key=lambda x: len(x[1]))[0]
            num_supporters = len(reaction_votes[final_reaction])
            
            # 判断是否达成共识（至少75%支持）
            consensus_reached = num_supporters >= int(num_agents * 0.75)
            
            # 计算该反应类型的平均过电势
            if final_reaction in overpotentials and overpotentials[final_reaction]:
                final_overpotential = sum(overpotentials[final_reaction]) / len(overpotentials[final_reaction])
        
        # 构建推理轨迹
        reasoning_trajectory = self._build_reasoning_trajectory(chat_history)
        
        # 计算辩论轮数
        debate_rounds = len(chat_history) // num_agents
        
        # 转换历史格式
        formatted_history = []
        for msg in chat_history:
            formatted_history.append({
                'agent': msg.get('name', 'Unknown'),
                'content': msg.get('content', ''),
                'role': msg.get('role', 'assistant')
            })
        
        return DebateResult(
            consensus_reached=consensus_reached,
            final_reaction_type=final_reaction,
            final_overpotential=final_overpotential,
            reasoning_trajectory=reasoning_trajectory,
            debate_rounds=debate_rounds,
            debate_history=formatted_history,
            time_elapsed=0  # Will be set by caller
        )
    
    def _extract_reaction_type(self, content: str) -> Optional[str]:
        """提取反应类型"""
        reaction_types = [
            "CO2RR", "EOR", "HER", "HOR", 
            "HZOR", "O5H", "OER", "ORR", "UOR"
        ]
        
        content_upper = content.upper()
        for reaction in reaction_types:
            if reaction in content_upper:
                return reaction
        
        return None
    
    def _extract_overpotential(self, content: str) -> Optional[float]:
        """提取过电势值"""
        potential_pattern = r'(\d+\.?\d*)\s*v'
        matches = re.findall(potential_pattern, content.lower())
        
        if matches:
            try:
                return float(matches[0])
            except ValueError:
                pass
        
        return None
    
    def _build_reasoning_trajectory(self, chat_history: List[Dict]) -> str:
        """
        构建推理轨迹 - 提取完整的LLM推理链条
        
        Args:
            chat_history: 对话历史
        
        Returns:
            str: 完整推理轨迹文本（包含LLM的完整thinking过程）
        """
        trajectory_parts = ["=== Debate Reasoning Trajectory ===\n"]
        
        for i, msg in enumerate(chat_history, 1):
            agent_name = msg.get('name', 'Unknown')
            content = msg.get('content', '')
            
            # 提取关键信息
            reaction = self._extract_reaction_type(content)
            overpotential = self._extract_overpotential(content)
            
            # 保留完整的LLM推理内容（包括thinking模式的完整输出）
            trajectory_parts.append(f"\n[Round {(i-1)//len(self.agents) + 1}] {agent_name}:")
            if reaction:
                trajectory_parts.append(f"  Reaction: {reaction}")
            if overpotential:
                trajectory_parts.append(f"  Overpotential: {overpotential}V")
            trajectory_parts.append(f"  Complete Reasoning:\n{content}")
            trajectory_parts.append("-" * 80)  # 添加分隔线以便区分不同agent的推理
        
        return "\n".join(trajectory_parts)
