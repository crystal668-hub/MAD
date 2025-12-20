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
                "temperature": model_config.get('temperature', 0.7),
                "max_tokens": model_config.get('max_tokens', 2000)
            }
        elif provider == 'anthropic':
            # AutoGen可能需要特殊配置来支持Anthropic
            # 这里提供一个基本框架
            return {
                "model": model_config.get('model', 'claude-3-opus-20240229'),
                "api_key": model_config.get('api_key'),
                "temperature": model_config.get('temperature', 0.7),
                "max_tokens": model_config.get('max_tokens', 2000),
                "api_type": "anthropic"
            }
        elif provider == 'google':
            return {
                "model": model_config.get('model', 'gemini-pro'),
                "api_key": model_config.get('api_key'),
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

def create_termination_function(consensus_threshold: int = 3):
    """
    创建自定义终止函数
    当连续达成共识指定次数时终止辩论
    
    Args:
        consensus_threshold: 连续相同答案次数阈值
    
    Returns:
        function: 终止判断函数
    """
    # 记录连续相同答案的计数器
    consensus_tracker = {
        'last_reaction': None,
        'count': 0
    }
    
    def is_termination_msg(msg: Dict) -> bool:
        """
        判断是否应该终止辩论
        
        Args:
            msg: 消息字典
        
        Returns:
            bool: 是否终止
        """
        content = msg.get('content', '').lower()
        
        # 提取反应类型
        reaction_types = [
            "氢氧化反应", "氧化还原反应", "酸碱中和反应", "电解反应",
            "腐蚀反应", "催化反应", "络合反应", "沉淀反应", "氧化电解反应"
        ]
        
        current_reaction = None
        for reaction in reaction_types:
            if reaction in content:
                current_reaction = reaction
                break
        
        if current_reaction is None:
            return False
        
        # 检查是否与上一次相同
        if current_reaction == consensus_tracker['last_reaction']:
            consensus_tracker['count'] += 1
        else:
            consensus_tracker['last_reaction'] = current_reaction
            consensus_tracker['count'] = 1
        
        # 达到阈值则终止
        if consensus_tracker['count'] >= consensus_threshold:
            print(f"\n✓ 达成共识: {current_reaction} (连续{consensus_tracker['count']}次)")
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
