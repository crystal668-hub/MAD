"""
===================================
辩论管理器模块
功能：管理多Agent辩论流程，监控共识达成
===================================
"""

from typing import List, Dict, Optional, Tuple
import time
from dataclasses import dataclass
from agents.base_agent import BaseAgent
from debate.autogen_setup import AutoGenSetup, create_termination_function


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


class DebateManager:
    """
    辩论管理器
    负责组织和监控多Agent辩论过程
    """
    
    def __init__(
        self,
        agents: List[BaseAgent],
        config: Dict,
        use_autogen: bool = True
    ):
        """
        初始化辩论管理器
        
        Args:
            agents: Agent列表
            config: 辩论配置
            use_autogen: 是否使用AutoGen框架
        """
        self.agents = agents
        self.config = config
        self.use_autogen = use_autogen
        
        # 辩论参数
        self.max_rounds = config.get('max_rounds', 10)
        self.consensus_threshold = config.get('consensus_threshold', 3)
        self.timeout = config.get('timeout', 300)
        
        # 辩论状态
        self.debate_history = []
        self.current_round = 0
        self.start_time = None
        
        # AutoGen设置
        if use_autogen:
            self.autogen_setup = AutoGenSetup(agents, config)
            self.autogen_agents, self.group_chat, self.manager = \
                self.autogen_setup.get_group_chat_setup()
    
    def start_debate(
        self,
        components: List[str],
        initial_prompt: Optional[str] = None
    ) -> DebateResult:
        """
        开始辩论
        
        Args:
            components: 化学组分列表
            initial_prompt: 初始提示（可选）
        
        Returns:
            DebateResult: 辩论结果
        """
        print("=" * 60)
        print("开始多Agent辩论")
        print("=" * 60)
        
        self.start_time = time.time()
        
        # 构建初始提示
        if initial_prompt is None:
            initial_prompt = self._build_initial_prompt(components)
        
        print(f"\n初始问题:\n{initial_prompt}\n")
        
        # 根据配置选择辩论方式
        if self.use_autogen:
            result = self._debate_with_autogen(initial_prompt)
        else:
            result = self._debate_manual(components, initial_prompt)
        
        elapsed_time = time.time() - self.start_time
        result.time_elapsed = elapsed_time
        
        print("\n" + "=" * 60)
        print(f"辩论结束 (耗时: {elapsed_time:.2f}秒)")
        print("=" * 60)
        
        return result
    
    def _build_initial_prompt(self, components: List[str]) -> str:
        """
        构建初始辩论提示
        
        Args:
            components: 化学组分列表
        
        Returns:
            str: 初始提示
        """
        components_str = "、".join(components)
        
        prompt = f"""请分析以下化学废液组分的反应特性，确定产生最低过电势的反应类型：

**化学组分**: {components_str}

**可选反应类型**:
1. 氢氧化反应
2. 氧化还原反应
3. 酸碱中和反应
4. 电解反应
5. 腐蚀反应
6. 催化反应
7. 络合反应
8. 沉淀反应
9. 氧化电解反应

**要求**:
1. 基于化学原理和文献知识进行分析
2. 给出具体的反应类型推荐
3. 如可能，估算过电势值
4. 提供详细的推理过程
5. 引用支持你观点的证据

请各位专家发表意见，通过辩论达成共识。"""
        
        return prompt
    
    def _debate_with_autogen(self, initial_prompt: str) -> DebateResult:
        """
        使用AutoGen框架进行辩论
        
        Args:
            initial_prompt: 初始提示
        
        Returns:
            DebateResult: 辩论结果
        """
        # 创建终止函数
        is_termination = create_termination_function(self.consensus_threshold)
        
        try:
            # 使用第一个agent发起对话
            first_agent = self.autogen_agents[0]
            
            # 开始群组聊天
            first_agent.initiate_chat(
                self.manager,
                message=initial_prompt,
                max_turns=self.max_rounds
            )
            
            # 提取辩论历史
            self.debate_history = self.group_chat.messages
            
            # 分析结果
            result = self._analyze_debate_result()
            
            return result
        
        except Exception as e:
            print(f"AutoGen辩论过程出错: {str(e)}")
            # 返回失败结果
            return DebateResult(
                consensus_reached=False,
                final_reaction_type=None,
                final_overpotential=None,
                reasoning_trajectory="",
                debate_rounds=self.current_round,
                debate_history=self.debate_history,
                time_elapsed=0
            )
    
    def _debate_manual(
        self,
        components: List[str],
        initial_prompt: str
    ) -> DebateResult:
        """
        手动管理辩论流程（不使用AutoGen）
        
        Args:
            components: 化学组分列表
            initial_prompt: 初始提示
        
        Returns:
            DebateResult: 辩论结果
        """
        print("使用手动辩论模式\n")
        
        # 为每个Agent准备增强提示
        enhanced_prompts = []
        for agent in self.agents:
            enhanced_prompt = agent.format_prompt_with_rag(
                query=initial_prompt,
                components=components,
                use_experience=True
            )
            enhanced_prompts.append(enhanced_prompt)
        
        # 辩论循环
        consensus_count = 0
        last_reaction = None
        
        for round_num in range(1, self.max_rounds + 1):
            self.current_round = round_num
            print(f"\n{'=' * 60}")
            print(f"第 {round_num} 轮辩论")
            print(f"{'=' * 60}\n")
            
            round_reactions = []
            
            # 每个Agent依次发言
            for i, agent in enumerate(self.agents):
                print(f"\n[{agent.name}] 正在思考...")
                
                # 构建当前提示（包含之前的辩论内容）
                if round_num == 1:
                    current_prompt = enhanced_prompts[i]
                else:
                    current_prompt = self._build_followup_prompt(
                        components,
                        agent,
                        self.debate_history
                    )
                
                # 生成响应
                response = agent.generate_response(current_prompt)
                
                # 记录辩论历史
                self.debate_history.append({
                    "round": round_num,
                    "agent": agent.name,
                    "content": response.content,
                    "reaction_type": response.reaction_type,
                    "overpotential": response.overpotential
                })
                
                # 打印响应
                print(f"\n[{agent.name}]:")
                print(response.content[:500] + "..." if len(response.content) > 500 else response.content)
                
                if response.reaction_type:
                    print(f"\n推荐反应: {response.reaction_type}")
                    round_reactions.append(response.reaction_type)
            
            # 检查是否达成共识
            if len(set(round_reactions)) == 1:
                # 所有Agent给出相同答案
                current_reaction = round_reactions[0]
                if current_reaction == last_reaction:
                    consensus_count += 1
                else:
                    consensus_count = 1
                    last_reaction = current_reaction
                
                print(f"\n>>> 本轮共识: {current_reaction} (连续 {consensus_count} 轮)")
                
                if consensus_count >= self.consensus_threshold:
                    print("\n✓ 达成最终共识!")
                    break
            else:
                consensus_count = 0
                last_reaction = None
                print(f"\n>>> 本轮意见分歧: {set(round_reactions)}")
        
        # 分析结果
        result = self._analyze_debate_result()
        
        return result
    
    def _build_followup_prompt(
        self,
        components: List[str],
        agent: BaseAgent,
        history: List[Dict]
    ) -> str:
        """
        构建后续轮次的提示
        
        Args:
            components: 化学组分
            agent: 当前Agent
            history: 辩论历史
        
        Returns:
            str: 后续提示
        """
        # 总结之前的观点
        previous_opinions = []
        for record in history[-len(self.agents):]:  # 只看上一轮
            previous_opinions.append(
                f"**{record['agent']}** 认为: {record.get('reaction_type', '未明确')} "
                f"(过电势: {record.get('overpotential', '未估算')})"
            )
        
        opinions_summary = "\n".join(previous_opinions)
        
        prompt = f"""基于之前的讨论，请重新评估你的观点：

**上一轮各方观点**:
{opinions_summary}

**请考虑**:
1. 其他专家的论据是否合理？
2. 是否有新的证据支持或反驳某个观点？
3. 你是否需要修正自己的结论？

如果你同意某个观点，请明确表示并给出理由。
如果你仍持不同意见，请提供更充分的证据。

请给出你的最终判断。"""
        
        # 使用RAG增强
        enhanced_prompt = agent.format_prompt_with_rag(
            query=prompt,
            components=components,
            use_experience=True
        )
        
        return enhanced_prompt
    
    def _analyze_debate_result(self) -> DebateResult:
        """
        分析辩论结果，提取共识
        
        Returns:
            DebateResult: 辩论结果
        """
        if not self.debate_history:
            return DebateResult(
                consensus_reached=False,
                final_reaction_type=None,
                final_overpotential=None,
                reasoning_trajectory="",
                debate_rounds=0,
                debate_history=[],
                time_elapsed=0
            )
        
        # 统计最后一轮的反应类型
        last_round = max([h['round'] for h in self.debate_history])
        last_round_reactions = [
            h['reaction_type'] for h in self.debate_history
            if h['round'] == last_round and h.get('reaction_type')
        ]
        
        # 检查是否达成共识
        consensus_reached = len(set(last_round_reactions)) == 1
        
        final_reaction = last_round_reactions[0] if consensus_reached else None
        
        # 提取过电势（取平均值）
        last_round_potentials = [
            h['overpotential'] for h in self.debate_history
            if h['round'] == last_round and h.get('overpotential') is not None
        ]
        final_overpotential = (
            sum(last_round_potentials) / len(last_round_potentials)
            if last_round_potentials else None
        )
        
        # 构建推理轨迹
        reasoning_trajectory = self._build_reasoning_trajectory()
        
        return DebateResult(
            consensus_reached=consensus_reached,
            final_reaction_type=final_reaction,
            final_overpotential=final_overpotential,
            reasoning_trajectory=reasoning_trajectory,
            debate_rounds=last_round,
            debate_history=self.debate_history,
            time_elapsed=0  # 将在外部设置
        )
    
    def _build_reasoning_trajectory(self) -> str:
        """
        构建推理轨迹摘要
        
        Returns:
            str: 推理轨迹文本
        """
        trajectory_parts = ["## 辩论推理轨迹\n"]
        
        current_round = 0
        for record in self.debate_history:
            if record['round'] != current_round:
                current_round = record['round']
                trajectory_parts.append(f"\n### 第{current_round}轮")
            
            trajectory_parts.append(
                f"\n**{record['agent']}**: "
                f"{record.get('reaction_type', '未明确')} "
                f"(过电势: {record.get('overpotential', '未估算')})"
            )
            
            # 添加简短摘要（前200字符）
            content = record['content']
            summary = content[:200] + "..." if len(content) > 200 else content
            trajectory_parts.append(f"  理由: {summary}")
        
        return "\n".join(trajectory_parts)
    
    def get_debate_summary(self) -> Dict:
        """
        获取辩论摘要
        
        Returns:
            Dict: 辩论统计信息
        """
        if not self.debate_history:
            return {"status": "未开始辩论"}
        
        total_rounds = max([h['round'] for h in self.debate_history])
        total_messages = len(self.debate_history)
        
        return {
            "status": "已完成",
            "total_rounds": total_rounds,
            "total_messages": total_messages,
            "agents_count": len(self.agents),
            "max_rounds": self.max_rounds
        }


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    from agents.agent_config import AgentConfig
    
    # 加载配置
    config = AgentConfig("../config/config.yaml")
    agents = config.create_all_agents()
    debate_config = config.get_debate_config()
    
    # 创建辩论管理器
    manager = DebateManager(
        agents=agents,
        config=debate_config,
        use_autogen=False  # 使用手动模式进行演示
    )
    
    # 开始辩论
    components = ["硫酸", "氢氧化钠", "氯化钠", "硝酸", "碳酸钙"]
    result = manager.start_debate(components)
    
    # 打印结果
    print(f"\n最终结果:")
    print(f"  共识达成: {result.consensus_reached}")
    print(f"  反应类型: {result.final_reaction_type}")
    print(f"  过电势: {result.final_overpotential}")
    print(f"  辩论轮数: {result.debate_rounds}")
