"""
===================================
Agent配置模块
功能：从配置文件加载和管理Agent配置
===================================
"""

import yaml
from pathlib import Path
from typing import Dict, List
from agents.llm_agents import create_agent
from agents.base_agent import BaseAgent


class AgentConfig:
    """
    Agent配置管理类
    负责从配置文件加载Agent设置并创建Agent实例
    """
    
    def __init__(self, config_path: str):
        """
        初始化Agent配置
        
        Args:
            config_path: 配置文件路径
        """
        self.config_path = Path(config_path)
        self.config = self._load_config()
        
    def _load_config(self) -> Dict:
        """
        加载配置文件
        
        Returns:
            Dict: 配置字典
        """
        if not self.config_path.exists():
            raise FileNotFoundError(f"配置文件不存在: {self.config_path}")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        return config
    
    def get_llm_config(self, agent_name: str) -> Dict:
        """
        获取指定Agent的LLM配置
        
        Args:
            agent_name: Agent名称 ("agent1", "agent2", "agent3")
        
        Returns:
            Dict: LLM配置
        """
        llm_config = self.config.get('llm', {})
        agent_config = llm_config.get(agent_name)
        
        if agent_config is None:
            raise ValueError(f"找不到Agent配置: {agent_name}")
        
        return agent_config
    
    def create_all_agents(
        self,
        rag_systems: Dict = None,
        experience_store = None
    ) -> List[BaseAgent]:
        """
        创建所有配置的Agent
        
        Args:
            rag_systems: RAG系统字典 {agent_id: rag_system}
            experience_store: 经验库实例
        
        Returns:
            List[BaseAgent]: Agent列表
        """
        agents = []
        
        # 默认的RAG系统字典
        if rag_systems is None:
            rag_systems = {}
        
        # Agent配置映射
        agent_configs = [
            ("agent1", "GPT-4 Agent", "agent1"),
            ("agent2", "Grok Agent", "agent2"),
            ("agent3", "Gemini Agent", "agent3")
        ]
        
        for agent_key, agent_name, agent_id in agent_configs:
            try:
                # 获取配置
                model_config = self.get_llm_config(agent_key)
                provider = model_config.get('provider')
                
                # 获取对应的RAG系统
                rag_system = rag_systems.get(agent_id)
                
                # 创建Agent
                agent = create_agent(
                    agent_type=provider,
                    agent_id=agent_id,
                    name=agent_name,
                    model_config=model_config,
                    rag_system=rag_system,
                    experience_store=experience_store
                )
                
                agents.append(agent)
                print(f"✓ 成功创建Agent: {agent_name}")
                
            except Exception as e:
                print(f"✗ 创建Agent失败 ({agent_name}): {str(e)}")
        
        return agents
    
    def get_debate_config(self) -> Dict:
        """
        获取辩论配置
        
        Returns:
            Dict: 辩论配置
        """
        return self.config.get('debate', {})
    
    def get_rag_config(self) -> Dict:
        """
        获取RAG配置
        
        Returns:
            Dict: RAG配置
        """
        return self.config.get('rag', {})
    
    def get_vector_store_config(self) -> Dict:
        """
        获取向量数据库配置
        
        Returns:
            Dict: 向量数据库配置
        """
        return self.config.get('vector_store', {})
    
    def get_experience_config(self) -> Dict:
        """
        获取经验库配置
        
        Returns:
            Dict: 经验库配置
        """
        return self.config.get('experience', {})
    
    def get_chemistry_config(self) -> Dict:
        """
        获取化学反应配置
        
        Returns:
            Dict: 化学反应配置
        """
        return self.config.get('chemistry', {})


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    # 加载配置
    config = AgentConfig("../config/config.yaml")
    
    # 创建所有Agent
    agents = config.create_all_agents()
    
    print(f"\n共创建 {len(agents)} 个Agent:")
    for agent in agents:
        print(f"  - {agent}")
