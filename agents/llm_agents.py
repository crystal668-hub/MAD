"""
===================================
LLM Agent实现模块
功能：实现三个不同LLM的Agent（OpenAI、Anthropic、Google）
===================================
"""

import os
from typing import Dict, List, Optional
import openai
import anthropic
import google.generativeai as genai

from agents.base_agent import BaseAgent, AgentResponse


class OpenAIAgent(BaseAgent):
    """
    基于OpenAI GPT的Agent
    使用GPT-4模型进行推理和分析
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
        
        self.client = openai.OpenAI(api_key=api_key)
        self.model = self.model_config.get('model', 'gpt-4')
        self.temperature = self.model_config.get('temperature', 0.7)
        self.max_tokens = self.model_config.get('max_tokens', 2000)
        
        print(f"{self.name} (OpenAI {self.model}) 初始化成功")
    
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
        # 简单的关键词匹配（实际应用中可使用更复杂的NLP技术）
        parsed = {}
        
        content_lower = content.lower()
        
        # 提取反应类型
        reaction_types = [
            "氢氧化反应", "氧化还原反应", "酸碱中和反应", "电解反应",
            "腐蚀反应", "催化反应", "络合反应", "沉淀反应", "氧化电解反应"
        ]
        for reaction in reaction_types:
            if reaction in content:
                parsed['reaction_type'] = reaction
                break
        
        # 尝试提取过电势值（寻找数字+单位模式）
        import re
        potential_pattern = r'(\d+\.?\d*)\s*(v|伏|volt)'
        matches = re.findall(potential_pattern, content_lower)
        if matches:
            try:
                parsed['overpotential'] = float(matches[0][0])
            except ValueError:
                pass
        
        # 提取推理部分（简化版）
        if "推理" in content or "分析" in content:
            parsed['reasoning'] = content
        
        return parsed


class AnthropicAgent(BaseAgent):
    """
    基于Anthropic Claude的Agent
    使用Claude模型进行推理和分析
    """
    
    def _init_llm_client(self) -> None:
        """初始化Anthropic客户端"""
        api_key = self.model_config.get('api_key')
        if not api_key:
            raise ValueError("Anthropic API key未配置")
        
        # 替换环境变量占位符
        if api_key.startswith("${") and api_key.endswith("}"):
            env_var = api_key[2:-1]
            api_key = os.getenv(env_var)
            if not api_key:
                raise ValueError(f"环境变量 {env_var} 未设置")
        
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = self.model_config.get('model', 'claude-3-opus-20240229')
        self.temperature = self.model_config.get('temperature', 0.7)
        self.max_tokens = self.model_config.get('max_tokens', 2000)
        
        print(f"{self.name} (Anthropic {self.model}) 初始化成功")
    
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """生成响应"""
        try:
            # 调用Claude API
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=self.get_system_prompt(),
                messages=[
                    *self.conversation_history,
                    {"role": "user", "content": prompt}
                ]
            )
            
            # 提取响应内容
            content = response.content[0].text
            
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
            error_msg = f"Anthropic API调用失败: {str(e)}"
            print(error_msg)
            return AgentResponse(content=error_msg)
    
    def _parse_response(self, content: str) -> Dict:
        """解析响应（同OpenAIAgent）"""
        parsed = {}
        reaction_types = [
            "氢氧化反应", "氧化还原反应", "酸碱中和反应", "电解反应",
            "腐蚀反应", "催化反应", "络合反应", "沉淀反应", "氧化电解反应"
        ]
        for reaction in reaction_types:
            if reaction in content:
                parsed['reaction_type'] = reaction
                break
        
        import re
        potential_pattern = r'(\d+\.?\d*)\s*(v|伏|volt)'
        matches = re.findall(potential_pattern, content.lower())
        if matches:
            try:
                parsed['overpotential'] = float(matches[0][0])
            except ValueError:
                pass
        
        return parsed


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
        
        genai.configure(api_key=api_key)
        
        self.model = self.model_config.get('model', 'gemini-pro')
        self.temperature = self.model_config.get('temperature', 0.7)
        self.max_tokens = self.model_config.get('max_tokens', 2000)
        
        # 配置生成参数
        generation_config = {
            "temperature": self.temperature,
            "max_output_tokens": self.max_tokens,
        }
        
        self.client = genai.GenerativeModel(
            model_name=self.model,
            generation_config=generation_config
        )
        
        # 初始化聊天会话
        self.chat = self.client.start_chat(history=[])
        
        print(f"{self.name} (Google {self.model}) 初始化成功")
    
    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> AgentResponse:
        """生成响应"""
        try:
            # 构建完整提示（包含系统提示）
            full_prompt = f"{self.get_system_prompt()}\n\n{prompt}"
            
            # 发送消息
            response = self.chat.send_message(full_prompt)
            
            # 提取响应内容
            content = response.text
            
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
        """解析响应（同OpenAIAgent）"""
        parsed = {}
        reaction_types = [
            "氢氧化反应", "氧化还原反应", "酸碱中和反应", "电解反应",
            "腐蚀反应", "催化反应", "络合反应", "沉淀反应", "氧化电解反应"
        ]
        for reaction in reaction_types:
            if reaction in content:
                parsed['reaction_type'] = reaction
                break
        
        import re
        potential_pattern = r'(\d+\.?\d*)\s*(v|伏|volt)'
        matches = re.findall(potential_pattern, content.lower())
        if matches:
            try:
                parsed['overpotential'] = float(matches[0][0])
            except ValueError:
                pass
        
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
        agent_type: Agent类型 ("openai", "anthropic", "google")
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
        "anthropic": AnthropicAgent,
        "google": GoogleAgent
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
