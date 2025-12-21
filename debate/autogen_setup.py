"""
===================================
AutoGen配置模块
功能：配置AutoGen框架用于多Agent辩论
===================================
"""

from typing import List, Dict, Optional
import autogen
from agents.base_agent import BaseAgent


class AutoGenSetup:
    """
    AutoGen框架配置类
    负责将自定义Agent包装为AutoGen可用的Agent
    """
    
    def __init__(self, agents: List[BaseAgent], config: Dict):
        """
        初始化AutoGen配置
        
        Args:
            agents: Agent列表
            config: 辩论配置
        """
        self.agents = agents
        self.config = config
        self.autogen_agents = []
        self.group_chat = None
        self.manager = None
        
    def create_autogen_agents(self) -> List:
        """
        将自定义Agent转换为AutoGen Agent
        
        Returns:
            List: AutoGen Agent列表
        """
        self.autogen_agents = []
        
        for agent in self.agents:
            # 创建AutoGen的AssistantAgent
            autogen_agent = autogen.AssistantAgent(
                name=agent.name.replace(" ", "_"),
                system_message=agent.get_system_prompt(),
                llm_config=self._get_llm_config_for_autogen(agent)
            )
            
            # 保存原始agent的引用，方便后续调用其方法
            autogen_agent._original_agent = agent
            
            self.autogen_agents.append(autogen_agent)
        
        print(f"成功创建 {len(self.autogen_agents)} 个AutoGen Agent")
        return self.autogen_agents
    
    def _get_llm_config_for_autogen(self, agent: BaseAgent) -> Dict:
        """
        为AutoGen生成LLM配置
        
        Args:
            agent: 自定义Agent
        
        Returns:
            Dict: AutoGen格式的LLM配置
        """
        model_config = agent.model_config
        
        # 根据provider构建配置
        provider = model_config.get('provider', 'openai')
        
        if provider == 'openai':
            return {
                "model": model_config.get('model', 'gpt-4'),
                "api_key": model_config.get('api_key'),
                "base_url": model_config.get('base_url', 'https://openrouter.ai/api/v1'),
                "temperature": model_config.get('temperature', 0.7),
                "max_tokens": model_config.get('max_tokens', 2000)
            }
        elif provider == 'xai':
            return {
                "model": model_config.get('model', 'x-ai/grok-beta'),
                "api_key": model_config.get('api_key'),
                "base_url": model_config.get('base_url', 'https://openrouter.ai/api/v1'),
                "temperature": model_config.get('temperature', 0.7),
                "max_tokens": model_config.get('max_tokens', 2000)
            }
        elif provider == 'google':
            return {
                "model": model_config.get('model', 'gemini-pro'),
                "api_key": model_config.get('api_key'),
                "base_url": model_config.get('base_url', 'https://openrouter.ai/api/v1'),
                "temperature": model_config.get('temperature', 0.7),
                "max_tokens": model_config.get('max_tokens', 2000),
                "api_type": "google"
            }
        else:
            raise ValueError(f"不支持的provider: {provider}")
    
    def create_group_chat(self) -> autogen.GroupChat:
        """
        创建群组聊天
        
        Returns:
            autogen.GroupChat: 群组聊天对象
        """
        if not self.autogen_agents:
            self.create_autogen_agents()
        
        # 创建群组聊天
        self.group_chat = autogen.GroupChat(
            agents=self.autogen_agents,
            messages=[],
            max_round=self.config.get('max_rounds', 10),
            speaker_selection_method=self.config.get('speaker_selection_method', 'round_robin')
        )
        
        print("成功创建AutoGen群组聊天")
        return self.group_chat
    
    def create_manager(self) -> autogen.GroupChatManager:
        """
        创建群组聊天管理器
        
        Returns:
            autogen.GroupChatManager: 管理器对象
        """
        if self.group_chat is None:
            self.create_group_chat()
        
        # 使用第一个agent的配置作为manager的配置
        manager_llm_config = self._get_llm_config_for_autogen(self.agents[0])
        
        self.manager = autogen.GroupChatManager(
            groupchat=self.group_chat,
            llm_config=manager_llm_config
        )
        
        print("成功创建AutoGen群组管理器")
        return self.manager
    
    def get_group_chat_setup(self) -> tuple:
        """
        获取完整的群组聊天设置
        
        Returns:
            tuple: (autogen_agents, group_chat, manager)
        """
        if self.manager is None:
            self.create_manager()
        
        return self.autogen_agents, self.group_chat, self.manager


# ===================================
# 自定义终止条件
# ===================================

def create_termination_function(num_agents: int = 3, required_consensus: int = 3):
    """
    创建自定义终止函数
    当所有agent达成共识时终止辩论（必须三方答案完全一致）
    
    Args:
        num_agents: Agent总数（默认3个）
        required_consensus: 达成共识所需的agent数量（默认3个，即全部一致）
    
    Returns:
        function: 终止判断函数
    """
    # 记录每个agent的最新答案
    agent_answers = {}
    
    def is_termination_msg(msg: Dict) -> bool:
        """
        判断是否应该终止辩论
        检查是否有足够数量的agent给出了相同答案（反应类型+过电势）
        
        Args:
            msg: 消息字典
        
        Returns:
            bool: 是否终止
        """
        content = msg.get('content', '').upper()
        content_lower = msg.get('content', '').lower()
        sender = msg.get('name', 'unknown')
        
        # 提取反应类型
        reaction_types = [
            "AOR", "CO2RR", "EOR", "HER", "HOR", 
            "HZOR", "O5H", "OER", "ORR", "SAC", "UOR"
        ]
        
        current_reaction = None
        for reaction in reaction_types:
            if reaction in content:
                current_reaction = reaction
                break
        
        # 提取过电势值
        import re
        current_overpotential = None
        potential_pattern = r'(\d+\.?\d*)\s*(v|伏|volt)'
        matches = re.findall(potential_pattern, content_lower)
        if matches:
            try:
                current_overpotential = round(float(matches[0][0]), 2)  # 保留2位小数
            except (ValueError, IndexError):
                pass
        
        # 如果提取到反应类型和过电势，记录该agent的答案（元组：反应类型+过电势）
        if current_reaction is not None and current_overpotential is not None:
            agent_answers[sender] = (current_reaction, current_overpotential)
        
        # 如果还没有足够的agent给出答案，继续辩论
        if len(agent_answers) < num_agents:
            return False
        
        # 统计每种答案（反应类型+过电势组合）的支持者数量
        from collections import Counter
        answer_counts = Counter(agent_answers.values())
        
        # 检查是否有任何答案达到了共识阈值
        for answer, count in answer_counts.items():
            if count >= required_consensus:
                reaction, overpotential = answer
                print(f"\n✓ 达成共识: {reaction}, 过电势: {overpotential}V ({count}/{num_agents}个agent支持)")
                # 重置计数器以便下次使用
                agent_answers.clear()
                return True
        
        return False
    
    return is_termination_msg


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    from agents.agent_config import AgentConfig
    
    # 加载配置并创建Agent
    config = AgentConfig("../config/config.yaml")
    agents = config.create_all_agents()
    
    # 获取辩论配置
    debate_config = config.get_debate_config()
    
    # 设置AutoGen
    autogen_setup = AutoGenSetup(agents, debate_config)
    autogen_agents, group_chat, manager = autogen_setup.get_group_chat_setup()
    
    print("\nAutoGen设置完成，准备开始辩论")
