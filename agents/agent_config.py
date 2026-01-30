"""
===================================
Agent配置模块
功能：从配置文件加载和管理Agent配置
===================================
"""

import yaml
from pathlib import Path
from typing import Dict, List, Union
from agents.llm_agents import create_agent
from agents.react_agent import ReActAgent


class AgentConfig:
    """
    Agent配置管理类
    负责从配置文件加载Agent设置并创建Agent实例
    """
    
    def __init__(self, config: Union[str, Dict]):
        """
        初始化Agent配置
        
        Args:
            config: 配置文件路径（str）或配置字典（Dict）
        """
        if isinstance(config, dict):
            self.config = config
            self.config_path = None
        else:
            self.config_path = Path(config)
            self.config = self._load_config()
        
    def _load_config(self) -> Dict:
        """
        加载配置文件
        
        Returns:
            Dict: 配置字典
        """
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        return config
    
    def get_llm_config(self, agent_name: str) -> Dict:
        """
        获取指定Agent的LLM配置
        
        Args:
            agent_name: Agent Name
        
        Returns:
            Dict: LLM Configuration
        """
        llm_config = self.config.get('llm', {})
        agent_config = llm_config.get(agent_name)
        
        if agent_config is None:
            raise ValueError(f"Agent configuration not found: {agent_name}")
        
        return agent_config
    
    def create_all_agents(
        self,
        rag_systems: Dict = None,
        experience_store = None
    ) -> List[ReActAgent]:
        """
        创建所有配置的Agent
        
        Args:
            rag_systems: RAG系统字典 {agent_id: rag_system}
            experience_store: 经验库实例
        
        Returns:
            List[ReActAgent]: Agent列表
        """
        agents = []
        
        if rag_systems is None:
            rag_systems = {}
        
        # Agent configuration mapping
        agent_configs = [
            ("agent1", "GPT Researcher", "agent1"),
            ("agent2", "DeepSeek Researcher", "agent2"),
            ("agent3", "Gemini Researcher", "agent3"),
            ("agent4", "Qwen Researcher", "agent4")
        ]
        
        for agent_key, agent_name, agent_id in agent_configs:
            try:
                model_config = self.get_llm_config(agent_key)
                provider = model_config.get('provider')
                
                # Get corresponding RAG system
                rag_system = rag_systems.get(agent_id)
                
                # Create Agent
                agent = create_agent(
                    agent_type=provider,
                    agent_id=agent_id,
                    name=agent_name,
                    model_config=model_config,
                    rag_system=rag_system,
                    experience_store=experience_store
                )
                
                agents.append(agent)
                print(f"✓ Successfully created Agent: {agent_name}")
                
            except Exception as e:
                print(f"✗ Failed to create Agent ({agent_name}): {str(e)}")
        
        return agents
    
    def get_debate_config(self) -> Dict:
        """
        Get debate configuration
        
        Returns:
            Dict: Debate configuration
        """
        return self.config.get('debate', {})
    
    def get_rag_config(self) -> Dict:
        """
        Get RAG configuration
        
        Returns:
            Dict: RAG configuration
        """
        return self.config.get('rag', {})
    
    def get_vector_store_config(self) -> Dict:
        """
        Get vector store configuration
        
        Returns:
            Dict: Vector store configuration
        """
        return self.config.get('vector_store', {})
    
    def get_experience_config(self) -> Dict:
        """
        Get experience configuration
        
        Returns:
            Dict: Experience configuration
        """
        return self.config.get('experience', {})
    
    def get_chemistry_config(self) -> Dict:
        """
        Get Reaction configuration
        
        Returns:
            Dict: Reaction configuration
        """
        return self.config.get('chemistry', {})


