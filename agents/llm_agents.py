"""
===================================
LLM Agent实现模块
功能：实现四个不同LLM的Agent（OpenAI、xAI Grok、Google、DeepSeek）
所有Agent统一通过OpenRouter使用OpenAI兼容API格式调用
===================================
"""

import os
import re
from typing import Dict, List, Optional
import openai

from agents.base_agent import BaseAgent, AgentResponse


class OpenAIAgent(BaseAgent):
    """
    基于OpenAI GPT的Agent
    使用GPT模型进行推理和分析
    """
    
    def _init_llm_client(self) -> None:
        """初始化OpenAI客户端"""
        api_key = self.model_config.get('api_key')
        if not api_key:
            raise ValueError("OpenAI API key未配置")
        
        # 替换环境变量占位符
        if api_key.startswith("${") and api_key.endswith("}"):
            env_var = api_key[2:-1]
            api_key = os.getenv(env_var)
            if not api_key:
                raise ValueError(f"环境变量 {env_var} 未设置")
        
        # 获取base_url配置，默认使用OpenRouter
        base_url = self.model_config.get('base_url', 'https://openrouter.ai/api/v1')
        
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = self.model_config.get('model', 'gpt-4')
        self.temperature = self.model_config.get('temperature', 0.9)
        self.max_tokens = self.model_config.get('max_tokens', 2000)
        
        print(f"{self.name} (OpenAI {self.model}) 初始化成功 [base_url: {base_url}]")
    
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """
        生成响应
        
        Args:
            prompt: 输入提示
            context: 上下文信息
        
        Returns:
            AgentResponse: Agent响应
        """
        # 构建消息列表
        messages = [
            {"role": "system", "content": self.get_system_prompt()}
        ]
        
        # 添加对话历史
        messages.extend(self.conversation_history)
        
        # 添加当前提示
        messages.append({"role": "user", "content": prompt})
        
        try:
            # 调用OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # 提取响应内容
            content = response.choices[0].message.content
            
            # 添加到历史记录
            self.add_to_history("user", prompt)
            self.add_to_history("assistant", content)
            
            # 解析响应（提取反应类型、过电势等信息）
            parsed_info = self._parse_response(content)
            
            return AgentResponse(
                content=content,
                reaction_type=parsed_info.get('reaction_type'),
                overpotential=parsed_info.get('overpotential'),
                reasoning=parsed_info.get('reasoning'),
                confidence=parsed_info.get('confidence')
            )
        
        except Exception as e:
            error_msg = f"OpenAI API调用失败: {str(e)}"
            print(error_msg)
            return AgentResponse(content=error_msg)
    
    def _parse_response(self, content: str) -> Dict:
        """
        解析响应内容，提取结构化信息
        
        Args:
            content: 响应文本
        
        Returns:
            Dict: 解析后的信息
        """
        return _parse_llm_response(content)


class XAIAgent(BaseAgent):
    """
    基于xAI Grok的Agent
    使用Grok模型进行推理和分析
    """
    
    def _init_llm_client(self) -> None:
        """初始化xAI Grok客户端"""
        api_key = self.model_config.get('api_key')
        if not api_key:
            raise ValueError("xAI API key未配置")
        
        # 替换环境变量占位符
        if api_key.startswith("${") and api_key.endswith("}"):
            env_var = api_key[2:-1]
            api_key = os.getenv(env_var)
            if not api_key:
                raise ValueError(f"环境变量 {env_var} 未设置")
        
        # 获取base_url配置，默认使用OpenRouter
        base_url = self.model_config.get('base_url', 'https://openrouter.ai/api/v1')
        
        # OpenRouter使用OpenAI兼容接口
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = self.model_config.get('model', 'x-ai/grok-beta')
        self.temperature = self.model_config.get('temperature', 0.9)
        self.max_tokens = self.model_config.get('max_tokens', 2000)
        
        print(f"{self.name} (xAI {self.model}) 初始化成功 [base_url: {base_url}]")
    
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """生成响应"""
        try:
            # 构建消息列表（使用OpenAI兼容格式）
            messages = [
                {"role": "system", "content": self.get_system_prompt()}
            ]
            messages.extend(self.conversation_history)
            messages.append({"role": "user", "content": prompt})
            
            # 调用OpenRouter API（OpenAI兼容接口）
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # 提取响应内容
            content = response.choices[0].message.content
            
            # 添加到历史记录
            self.add_to_history("user", prompt)
            self.add_to_history("assistant", content)
            
            # 解析响应
            parsed_info = self._parse_response(content)
            
            return AgentResponse(
                content=content,
                reaction_type=parsed_info.get('reaction_type'),
                overpotential=parsed_info.get('overpotential'),
                reasoning=parsed_info.get('reasoning'),
                confidence=parsed_info.get('confidence')
            )
        
        except Exception as e:
            error_msg = f"xAI API调用失败: {str(e)}"
            print(error_msg)
            return AgentResponse(content=error_msg)
    
    def _parse_response(self, content: str) -> Dict:
        """解析响应（使用统一的解析函数）"""
        return _parse_llm_response(content)


class GoogleAgent(BaseAgent):
    """
    基于Google Gemini的Agent
    使用Gemini模型进行推理和分析
    """
    
    def _init_llm_client(self) -> None:
        """初始化Google Gemini客户端"""
        api_key = self.model_config.get('api_key')
        if not api_key:
            raise ValueError("Google API key未配置")
        
        # 替换环境变量占位符
        if api_key.startswith("${") and api_key.endswith("}"):
            env_var = api_key[2:-1]
            api_key = os.getenv(env_var)
            if not api_key:
                raise ValueError(f"环境变量 {env_var} 未设置")
        
        # 获取base_url配置，默认使用OpenRouter
        base_url = self.model_config.get('base_url', 'https://openrouter.ai/api/v1')
        
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        self.model = self.model_config.get('model', 'google/gemini-pro')
        self.temperature = self.model_config.get('temperature', 0.9)
        self.max_tokens = self.model_config.get('max_tokens', 2000)
        
        print(f"{self.name} (Google {self.model}) 初始化成功 [base_url: {base_url}]")
    
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """生成响应"""
        try:
            # 构建消息列表（使用OpenAI兼容格式）
            messages = [
                {"role": "system", "content": self.get_system_prompt()}
            ]
            messages.extend(self.conversation_history)
            messages.append({"role": "user", "content": prompt})
            
            # 调用OpenRouter API（OpenAI兼容接口）
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # 提取响应内容
            content = response.choices[0].message.content
            
            # 添加到历史记录
            self.add_to_history("user", prompt)
            self.add_to_history("assistant", content)
            
            # 解析响应
            parsed_info = self._parse_response(content)
            
            return AgentResponse(
                content=content,
                reaction_type=parsed_info.get('reaction_type'),
                overpotential=parsed_info.get('overpotential'),
                reasoning=parsed_info.get('reasoning'),
                confidence=parsed_info.get('confidence')
            )
        
        except Exception as e:
            error_msg = f"Google API调用失败: {str(e)}"
            print(error_msg)
            return AgentResponse(content=error_msg)
    
    def _parse_response(self, content: str) -> Dict:
        """解析响应（使用统一的解析函数）"""
        return _parse_llm_response(content)


class DeepSeekAgent(BaseAgent):
    """
    基于DeepSeek的Agent
    使用DeepSeek模型进行推理和分析
    """
    
    def _init_llm_client(self) -> None:
        """初始化DeepSeek客户端"""
        api_key = self.model_config.get('api_key')
        if not api_key:
            raise ValueError("DeepSeek API key未配置")
        
        # 替换环境变量占位符
        if api_key.startswith("${") and api_key.endswith("}"):
            env_var = api_key[2:-1]
            api_key = os.getenv(env_var)
            if not api_key:
                raise ValueError(f"环境变量 {env_var} 未设置")
        
        # 获取base_url配置，默认使用OpenRouter
        base_url = self.model_config.get('base_url', 'https://openrouter.ai/api/v1')
        
        # OpenRouter使用OpenAI兼容接口
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = self.model_config.get('model', 'deepseek/deepseek-chat')
        self.temperature = self.model_config.get('temperature', 0.9)
        self.max_tokens = self.model_config.get('max_tokens', 2000)
        
        print(f"{self.name} (DeepSeek {self.model}) 初始化成功 [base_url: {base_url}]")
    
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """生成响应"""
        try:
            # 构建消息列表（使用OpenAI兼容格式）
            messages = [
                {"role": "system", "content": self.get_system_prompt()}
            ]
            messages.extend(self.conversation_history)
            messages.append({"role": "user", "content": prompt})
            
            # 调用OpenRouter API（OpenAI兼容接口）
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # 提取响应内容
            content = response.choices[0].message.content
            
            # 添加到历史记录
            self.add_to_history("user", prompt)
            self.add_to_history("assistant", content)
            
            # 解析响应
            parsed_info = self._parse_response(content)
            
            return AgentResponse(
                content=content,
                reaction_type=parsed_info.get('reaction_type'),
                overpotential=parsed_info.get('overpotential'),
                reasoning=parsed_info.get('reasoning'),
                confidence=parsed_info.get('confidence')
            )
        
        except Exception as e:
            error_msg = f"DeepSeek API调用失败: {str(e)}"
            print(error_msg)
            return AgentResponse(content=error_msg)
    
    def _parse_response(self, content: str) -> Dict:
        """解析响应（使用统一的解析函数）"""
        return _parse_llm_response(content)


# ===================================
# 辅助函数
# ===================================

def _parse_llm_response(content: str) -> Dict:
    """
    统一的LLM响应解析函数
    提取结构化信息（反应类型、过电势等）
    
    Args:
        content: LLM响应文本
    
    Returns:
        Dict: 解析后的结构化信息
    """
    parsed = {}
    
    content_lower = content.lower()
    content_upper = content.upper()
    
    # 提取反应类型
    reaction_types = [
        "CO2RR", "EOR", "HER", "HOR", 
        "HZOR", "O5H", "OER", "ORR", "UOR"
    ]
    for reaction in reaction_types:
        if reaction in content_upper:
            parsed['reaction_type'] = reaction
            break
    
    # 尝试提取过电势值（寻找数字+单位模式）
    potential_pattern = r'(\d+\.?\d*)\s*(v|volt|伏)'
    matches = re.findall(potential_pattern, content_lower)
    if matches:
        try:
            parsed['overpotential'] = float(matches[0][0])
        except ValueError:
            pass
    
    # 尝试提取推理部分 
    if any(keyword in content_lower for keyword in ["reasoning", "analysis", "推理", "分析"]):
        parsed['reasoning'] = content
    
    return parsed


# ===================================
# Agent工厂函数
# ===================================

def create_agent(
    agent_type: str,
    agent_id: str,
    name: str,
    model_config: Dict,
    rag_system=None,
    experience_store=None
) -> BaseAgent:
    """
    Agent工厂函数，根据类型创建相应的Agent
    
    Args:
        agent_type: Agent类型 ("openai", "xai", "google", "deepseek")
        agent_id: Agent ID
        name: Agent名称
        model_config: 模型配置
        rag_system: RAG系统
        experience_store: 经验库
    
    Returns:
        BaseAgent: 创建的Agent实例
    """
    agent_classes = {
        "openai": OpenAIAgent,
        "xai": XAIAgent,
        "google": GoogleAgent,
        "deepseek": DeepSeekAgent
    }
    
    agent_class = agent_classes.get(agent_type.lower())
    if agent_class is None:
        raise ValueError(f"不支持的Agent类型: {agent_type}")
    
    return agent_class(
        agent_id=agent_id,
        name=name,
        model_config=model_config,
        rag_system=rag_system,
        experience_store=experience_store
    )
