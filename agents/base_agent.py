<<<<<<< HEAD
"""
===================================
Agent基类模块
功能：定义所有Agent的基本接口和通用功能
===================================
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class AgentResponse:
    """
    Agent响应数据类
    封装Agent的响应内容和相关元信息
    """
    content: str  # 响应内容
    reaction_type: Optional[str] = None  # 推荐的反应类型
    overpotential: Optional[float] = None  # 预测的过电势值
    reasoning: Optional[str] = None  # 推理过程
    confidence: Optional[float] = None  # 置信度
    sources: Optional[List[Dict]] = None  # 信息来源
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            "content": self.content,
            "reaction_type": self.reaction_type,
            "overpotential": self.overpotential,
            "reasoning": self.reasoning,
            "confidence": self.confidence,
            "sources": self.sources
        }


class BaseAgent(ABC):
    """
    Agent基类
    定义所有Agent必须实现的基本接口
    """
    
    def __init__(
        self,
        agent_id: str,
        name: str,
        model_config: Dict,
        rag_system: Optional[Any] = None,
        experience_store: Optional[Any] = None
    ):
        """
        初始化Agent
        
        Args:
            agent_id: Agent唯一标识符
            name: Agent名称
            model_config: 模型配置字典
            rag_system: RAG系统实例（可选）
            experience_store: 经验库实例（可选）
        """
        self.agent_id = agent_id
        self.name = name
        self.model_config = model_config
        self.rag_system = rag_system
        self.experience_store = experience_store
        
        # Agent状态
        self.conversation_history: List[Dict] = []
        self.current_context: Dict = {}
        
        # 初始化LLM客户端
        self._init_llm_client()
    
    @abstractmethod
    def _init_llm_client(self) -> None:
        """
        初始化LLM客户端
        子类必须实现此方法来初始化特定的LLM客户端
        """
        pass
    
    @abstractmethod
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """
        生成响应
        
        Args:
            prompt: 输入提示
            context: 上下文信息（可选）
        
        Returns:
            AgentResponse: Agent响应
        """
        pass
    
    def retrieve_knowledge(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        从RAG系统检索知识
        
        Args:
            query: 查询文本
            top_k: 返回的结果数量
        
        Returns:
            List[Dict]: 检索到的知识片段
        """
        if self.rag_system is None:
            return []
        
        try:
            # 执行检索
            results = self.rag_system.retrieve(query)
            return results[:top_k]
        except Exception as e:
            print(f"知识检索失败: {str(e)}")
            return []
    
    def retrieve_experience(self, components: List[str]) -> List[Dict]:
        """
        从经验库检索相关经验
        
        Args:
            components: 化学组分列表
        
        Returns:
            List[Dict]: 相关经验列表
        """
        if self.experience_store is None:
            return []
        
        try:
            # 从经验库查询相关经验
            experiences = self.experience_store.query_experiences(
                components=components,
                top_k=3
            )
            return experiences
        except Exception as e:
            print(f"经验检索失败: {str(e)}")
            return []
    
    def update_context(self, context: Dict) -> None:
        """
        更新Agent的上下文
        
        Args:
            context: 新的上下文信息
        """
        self.current_context.update(context)
    
    def add_to_history(self, role: str, content: str) -> None:
        """
        添加对话到历史记录
        
        Args:
            role: 角色（user/assistant/system）
            content: 对话内容
        """
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def clear_history(self) -> None:
        """清空对话历史"""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict]:
        """获取对话历史"""
        return self.conversation_history
    
    def get_system_prompt(self) -> str:
        """
        获取系统提示
        定义Agent的角色和行为准则
        
        Returns:
            str: 系统提示文本
        """
        return f"""You are {self.name}, a professional catalytic chemistry and electrochemistry expert.
Your task is to analyze the given metal elements as catalysts and predict which reaction type produces the lowest overpotential when these metals act as catalysts.

Available reaction types:
1. AOR (Alcohol Oxidation Reaction)
2. CO2RR (CO2 Reduction Reaction)
3. EOR (Ethanol Oxidation Reaction)
4. HER (Hydrogen Evolution Reaction)
5. HOR (Hydrogen Oxidation Reaction)
6. HZOR (Hydrazine Oxidation Reaction)
7. O5H (Oxygen Reduction 5-electron)
8. OER (Oxygen Evolution Reaction)
9. ORR (Oxygen Reduction Reaction)
10. SAC (Single Atom Catalyst)
11. UOR (Urea Oxidation Reaction)

Please analyze based on the following information:
1. Relevant knowledge from catalysis and electrochemistry literature
2. Historical experience and cases with these metal catalysts
3. Catalytic properties of the metal elements: electronic structure, d-band center, work function, surface energy, etc.
4. Reaction mechanisms and kinetics on metal surfaces
5. Adsorption/desorption behavior of reactants and intermediates

Your response should include:
- Recommended reaction type with the lowest overpotential
- Expected overpotential value (if estimable)
- Detailed reasoning about catalytic mechanisms and metal-reactant interactions
- Discussion of catalytic activity, selectivity, and stability
- Evidence and sources supporting your conclusion

Please maintain scientific rigor. If information is insufficient, please state clearly."""
    
    def format_prompt_with_rag(
        self,
        query: str,
        components: List[str],
        use_experience: bool = True
    ) -> str:
        """
        使用RAG增强提示
        
        Args:
            query: 原始查询
            components: 化学组分列表
            use_experience: 是否使用经验库
        
        Returns:
            str: 增强后的prompt
        """
        # Build component description
        components_str = ", ".join(components)
        
        # Retrieve relevant knowledge
        knowledge_results = self.retrieve_knowledge(
            f"Catalytic performance and overpotential of metal catalyst elements {components_str}"
        )
        
        # Retrieve relevant experience
        experiences = []
        if use_experience:
            experiences = self.retrieve_experience(components)
        
        # Build enhanced prompt
        prompt_parts = [
            f"## Task",
            f"Analyze the catalytic performance of the following five metal elements and predict which reaction type produces the lowest overpotential when these metals act as catalysts:",
            f"**Metal Catalyst Elements**: {components_str}",
            f"",
            f"## Relevant Literature Knowledge"
        ]
        
        # Add retrieved knowledge
        if knowledge_results:
            for i, result in enumerate(knowledge_results, 1):
                prompt_parts.append(f"### Literature {i} (Relevance: {result.get('score', 0):.3f})")
                prompt_parts.append(result['text'])
                prompt_parts.append("")
        else:
            prompt_parts.append("(No relevant literature retrieved)")
            prompt_parts.append("")
        
        # Add historical experience
        if experiences:
            prompt_parts.append("## Historical Experience with Similar Metal Catalysts")
            for i, exp in enumerate(experiences, 1):
                prompt_parts.append(f"### Experience {i}")
                prompt_parts.append(f"Metal Elements: {', '.join(exp.get('components', []))}")
                prompt_parts.append(f"Reaction Type: {exp.get('reaction_type', 'Unknown')}")
                prompt_parts.append(f"Overpotential: {exp.get('overpotential', 'Unknown')}")
                prompt_parts.append(f"Catalytic Mechanism: {exp.get('reasoning', '')}")
                prompt_parts.append("")
        
        # Add query
        prompt_parts.append("## Please Answer")
        prompt_parts.append(query)
        
        return "\n".join(prompt_parts)
    
    def __str__(self) -> str:
        """返回Agent的字符串表示"""
        return f"{self.name} (ID: {self.agent_id})"
    
    def __repr__(self) -> str:
        """返回Agent的详细表示"""
        return f"<{self.__class__.__name__} id={self.agent_id} name={self.name}>"
=======
"""
===================================
Agent基类模块
功能：定义所有Agent的基本接口和通用功能
===================================
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class AgentResponse:
    """
    Agent响应数据类
    封装Agent的响应内容和相关元信息
    """
    content: str  # 响应内容
    reaction_type: Optional[str] = None  # 推荐的反应类型
    overpotential: Optional[float] = None  # 预测的过电势值
    reasoning: Optional[str] = None  # 推理过程
    confidence: Optional[float] = None  # 置信度
    sources: Optional[List[Dict]] = None  # 信息来源
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            "content": self.content,
            "reaction_type": self.reaction_type,
            "overpotential": self.overpotential,
            "reasoning": self.reasoning,
            "confidence": self.confidence,
            "sources": self.sources
        }


class BaseAgent(ABC):
    """
    Agent基类
    定义所有Agent必须实现的基本接口
    """
    
    def __init__(
        self,
        agent_id: str,
        name: str,
        model_config: Dict,
        rag_system: Optional[Any] = None,
        experience_store: Optional[Any] = None
    ):
        """
        初始化Agent
        
        Args:
            agent_id: Agent唯一标识符
            name: Agent名称
            model_config: 模型配置字典
            rag_system: RAG系统实例（可选）
            experience_store: 经验库实例（可选）
        """
        self.agent_id = agent_id
        self.name = name
        self.model_config = model_config
        self.rag_system = rag_system
        self.experience_store = experience_store
        
        # Agent状态
        self.conversation_history: List[Dict] = []
        self.current_context: Dict = {}
        
        # 初始化LLM客户端
        self._init_llm_client()
    
    @abstractmethod
    def _init_llm_client(self) -> None:
        """
        初始化LLM客户端
        子类必须实现此方法来初始化特定的LLM客户端
        """
        pass
    
    @abstractmethod
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """
        生成响应
        
        Args:
            prompt: 输入提示
            context: 上下文信息（可选）
        
        Returns:
            AgentResponse: Agent响应
        """
        pass
    
    def retrieve_knowledge(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        从RAG系统检索知识
        
        Args:
            query: 查询文本
            top_k: 返回的结果数量
        
        Returns:
            List[Dict]: 检索到的知识片段
        """
        if self.rag_system is None:
            return []
        
        try:
            # 执行检索
            results = self.rag_system.retrieve(query)
            return results[:top_k]
        except Exception as e:
            print(f"知识检索失败: {str(e)}")
            return []
    
    def retrieve_experience(self, components: List[str]) -> List[Dict]:
        """
        从经验库检索相关经验
        
        Args:
            components: 化学组分列表
        
        Returns:
            List[Dict]: 相关经验列表
        """
        if self.experience_store is None:
            return []
        
        try:
            # 从经验库查询相关经验
            experiences = self.experience_store.query_experiences(
                components=components,
                top_k=3
            )
            return experiences
        except Exception as e:
            print(f"经验检索失败: {str(e)}")
            return []
    
    def update_context(self, context: Dict) -> None:
        """
        更新Agent的上下文
        
        Args:
            context: 新的上下文信息
        """
        self.current_context.update(context)
    
    def add_to_history(self, role: str, content: str) -> None:
        """
        添加对话到历史记录
        
        Args:
            role: 角色（user/assistant/system）
            content: 对话内容
        """
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def clear_history(self) -> None:
        """清空对话历史"""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict]:
        """获取对话历史"""
        return self.conversation_history
    
    def get_system_prompt(self) -> str:
        """
        获取系统提示
        定义Agent的角色和行为准则
        
        Returns:
            str: 系统提示文本
        """
        return f"""你是 {self.name}，一个专业的化学反应分析专家。
你的任务是分析给定的化学组分，预测产生最低过电势的反应类型。

可选的反应类型有：
1. AOR (Alcohol Oxidation Reaction)
2. CO2RR (CO2 Reduction Reaction)
3. EOR (Ethanol Oxidation Reaction)
4. HER (Hydrogen Evolution Reaction)
5. HOR (Hydrogen Oxidation Reaction)
6. HZOR (Hydrazine Oxidation Reaction)
7. O5H (Oxygen Reduction 5-electron)
8. OER (Oxygen Evolution Reaction)
9. ORR (Oxygen Reduction Reaction)
10. SAC (Single Atom Catalyst)
11. UOR (Urea Oxidation Reaction)

请基于以下信息进行分析：
1. 化学文献中的相关知识
2. 历史经验和案例
3. 组分的化学性质和反应特性

你的回答应包含：
- 推荐的反应类型
- 预期的过电势值（如果可以估算）
- 详细的推理过程
- 支持你结论的证据和来源

请保持科学严谨，如果信息不足，请明确说明。"""
    
    def format_prompt_with_rag(
        self,
        query: str,
        components: List[str],
        use_experience: bool = True
    ) -> str:
        """
        使用RAG增强提示
        
        Args:
            query: 原始查询
            components: 化学组分列表
            use_experience: 是否使用经验库
        
        Returns:
            str: 增强后的提示
        """
        # 构建组分描述
        components_str = "、".join(components)
        
        # 检索相关知识
        knowledge_results = self.retrieve_knowledge(
            f"化学组分 {components_str} 的反应特性和过电势"
        )
        
        # 检索相关经验
        experiences = []
        if use_experience:
            experiences = self.retrieve_experience(components)
        
        # 构建增强提示
        prompt_parts = [
            f"## 任务",
            f"分析以下五种化学组分的反应特性，预测产生最低过电势的反应类型：",
            f"**组分**: {components_str}",
            f"",
            f"## 相关文献知识"
        ]
        
        # 添加检索到的知识
        if knowledge_results:
            for i, result in enumerate(knowledge_results, 1):
                prompt_parts.append(f"### 文献 {i} (相关度: {result.get('score', 0):.3f})")
                prompt_parts.append(result['text'])
                prompt_parts.append("")
        else:
            prompt_parts.append("（未检索到相关文献）")
            prompt_parts.append("")
        
        # 添加历史经验
        if experiences:
            prompt_parts.append("## 历史经验")
            for i, exp in enumerate(experiences, 1):
                prompt_parts.append(f"### 经验 {i}")
                prompt_parts.append(f"组分: {', '.join(exp.get('components', []))}")
                prompt_parts.append(f"反应类型: {exp.get('reaction_type', '未知')}")
                prompt_parts.append(f"过电势: {exp.get('overpotential', '未知')}")
                prompt_parts.append(f"推理: {exp.get('reasoning', '')}")
                prompt_parts.append("")
        
        # 添加查询
        prompt_parts.append("## 请回答")
        prompt_parts.append(query)
        
        return "\n".join(prompt_parts)
    
    def __str__(self) -> str:
        """返回Agent的字符串表示"""
        return f"{self.name} (ID: {self.agent_id})"
    
    def __repr__(self) -> str:
        """返回Agent的详细表示"""
        return f"<{self.__class__.__name__} id={self.agent_id} name={self.name}>"
>>>>>>> 09731afda1a80e1c6c5cbaa00a68a4a3c0db3a72
