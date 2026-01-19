"""
===================================
OpenAI向量化模块
功能：使用OpenAI兼容SDK调用OpenRouter/百炼API进行文本向量化
===================================
"""

import os
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from tqdm import tqdm
from openai import OpenAI
import voyageai
from utils.logger import Logger

db_log_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
db_log_file = Path("./logs/db_log") / f"embedder_{db_log_timestamp}.log"
logger = Logger.get_logger(
    name=f"MAD.DB.Embedder.{db_log_timestamp}",
    log_file=str(db_log_file),
    level="INFO"
)


class MultiModelEmbedder:
    """
    多模型文本向量化器
    支持根据agent配置动态切换嵌入模型
    支持使用OpenRouter API、Voyage Python Package
    支持OpenAI、Voyage AI、Google等多种嵌入模型
    """
    
    def __init__(self, model_config: Dict, agent_configs: Dict = None):
        """
        初始化多模型向量化器
        
        Args:
            model_config: 默认模型配置字典
            agent_configs: 所有agent的配置字典 
        """
        self.default_model = model_config.get('embedding_model', 'text-embedding-3-large')
        self.api_key = model_config.get('api_key')
        self.base_url = model_config.get('emb_url', 'https://openrouter.ai/api/v1/embeddings')
        
        # 存储agent配置，用于动态选择模型
        self.agent_configs = agent_configs or {}
        
        # 懒加载Voyage AI客户端和OpenAI客户端
        self.voyage_clients: Dict[str, 'voyageai.Client'] = {}
        self.openai_clients: Dict[str, OpenAI] = {}
        
        # 从环境变量获取API Key
        if self.api_key and self.api_key.startswith('${') and self.api_key.endswith('}'):
            env_var = self.api_key[2:-1]
            self.api_key = os.environ.get(env_var)

        # 预先读取并规范化所有agent嵌入配置
        self.agent_embedding_profiles = self._build_agent_embedding_profiles()
        
        logger.info("[OK] 初始化向量化器")
        
        if self.agent_embedding_profiles:
            agent_models = {
                name: profile.get('embedding_model')
                for name, profile in self.agent_embedding_profiles.items()
            }
            agent_providers = {
                name: profile.get('embedding_provider')
                for name, profile in self.agent_embedding_profiles.items()
            }
            logger.info(f"  Agent向量模型提供方: {agent_providers}")

    def _resolve_env_var(self, value: Optional[str]) -> Optional[str]:
        if value and value.startswith('${') and value.endswith('}'):
            env_var = value[2:-1]
            return os.environ.get(env_var)
        return value

    def _normalize_openai_base_url(self, emb_url: Optional[str]) -> Optional[str]:
        if not emb_url:
            return emb_url
        if emb_url.endswith('/embeddings'):
            return emb_url.rsplit('/embeddings', 1)[0]
        return emb_url

    def _infer_provider_by_agent(self, agent_name: str, agent_config: Dict) -> str:
        if agent_name in ['agent2']:
            return 'voyage'
        if agent_name in ['agent4']:
            return 'bailian'
        if agent_name in ['agent1', 'agent3']:
            return 'openrouter'

        embedding_provider = (agent_config or {}).get('embedding_provider', '')
        if embedding_provider:
            return embedding_provider.lower()
        return 'openrouter'

    def _build_agent_embedding_profiles(self) -> Dict[str, Dict]:
        profiles: Dict[str, Dict] = {}
        for agent_name, cfg in self.agent_configs.items():
            embedding_model = cfg.get('embedding_model', self.default_model)
            emb_url = cfg.get('emb_url', self.base_url)
            openai_base_url = self._normalize_openai_base_url(emb_url)
            api_key = self._resolve_env_var(cfg.get('api_key', self.api_key))
            voyage_api_key = self._resolve_env_var(cfg.get('voyage_api_key'))
            embedding_provider = self._infer_provider_by_agent(agent_name, cfg)

            profiles[agent_name] = {
                'embedding_model': embedding_model,
                'emb_url': emb_url,
                'openai_base_url': openai_base_url,
                'api_key': api_key,
                'voyage_api_key': voyage_api_key,
                'embedding_provider': embedding_provider
            }
        return profiles
    
    def get_model_for_agent(self, agent_name: str = None) -> str:
        """
        获取指定agent使用的向量模型
        
        Args:
            agent_name: agent名称 (如 'agent1', 'agent2', 'agent3', 'agent4')
        
        Returns:
            str: 嵌入模型名称
        """
        if agent_name and agent_name in self.agent_configs:
            model = self.agent_configs[agent_name].get('embedding_model', self.default_model)
            return model
        return self.default_model
    
    def _get_voyage_client(self, agent_name: str) -> Optional['voyageai.Client']:
        """
        获取或创建Voyage AI客户端
        
        Args:
            agent_name: agent名称
            
        Returns:
            voyageai.Client或None
        """
        if agent_name not in self.voyage_clients:
            profile = self.agent_embedding_profiles.get(agent_name, {})
            voyage_api_key = profile.get('voyage_api_key')
            if voyage_api_key:
                self.voyage_clients[agent_name] = voyageai.Client(api_key=voyage_api_key)
                logger.info(f"[INFO] 为 {agent_name} 创建Voyage AI客户端")
            else:
                return None
                
        return self.voyage_clients.get(agent_name)

    def _get_openai_client(self, agent_name: str, api_key: str, base_url: str) -> OpenAI:
        if agent_name not in self.openai_clients:
            self.openai_clients[agent_name] = OpenAI(api_key=api_key, base_url=base_url)
        return self.openai_clients[agent_name]
        
    def _is_voyage_model(self, agent_name: str = None) -> bool:
        """
        判断指定agent是否使用Voyage向量模型
        
        Args:
            agent_name: agent名称
            
        Returns:
            bool: 是否使用Voyage AI
        """
        if not agent_name or agent_name not in self.agent_embedding_profiles:
            return False

        embedding_provider = self.agent_embedding_profiles[agent_name].get('embedding_provider', '')
        return embedding_provider == 'voyage'

    def _is_bailian_model(self, agent_name: str = None) -> bool:
        """
        判断指定agent是否使用百炼向量模型
        
        Args:
            agent_name: agent名称
            
        Returns:
            bool: 是否使用阿里云百炼
        """
        if not agent_name or agent_name not in self.agent_embedding_profiles:
            return False
        provider = self.agent_embedding_profiles[agent_name].get('embedding_provider', '')
        return provider in ['bailian', 'aliyun', 'qwen']

    def _get_bailian_base_url(self, agent_name: str) -> str:
        profile = self.agent_embedding_profiles.get(agent_name, {})
        return profile.get('emb_url', 'https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings')

    def _get_agent_profile(self, agent_name: Optional[str]) -> Dict:
        if agent_name and agent_name in self.agent_embedding_profiles:
            return self.agent_embedding_profiles[agent_name]
        return {
            'embedding_model': self.default_model,
            'emb_url': self.base_url,
            'openai_base_url': self._normalize_openai_base_url(self.base_url),
            'api_key': self.api_key,
            'embedding_provider': 'openrouter'
        }

    def embed_text(self, text: str, retry: int = 3, agent_name: str = None) -> List[float]:
        """
        将单个文本转换为向量
        
        Args:
            text: 输入文本
            retry: 重试次数
            agent_name: agent名称，用于选择对应的嵌入模型 (如 'agent1', 'agent2', 'agent3', 'agent4')
        
        Returns:
            List[float]: 向量
        """
        # 确定使用的agent
        use_agent = agent_name
        
        # 检查是否使用百炼或Voyage AI
        if use_agent and self._is_bailian_model(use_agent):
            return self._embed_text_bailian(text, retry, use_agent)
        if use_agent and self._is_voyage_model(use_agent):
            return self._embed_text_voyage(text, retry, use_agent)
        return self._embed_text_openrouter(text, retry, use_agent)
    
    def _embed_text_voyage(self, text: str, retry: int, agent_name: str) -> List[float]:
        """
        使用Voyage AI SDK进行文本向量化
        
        Args:
            text: 输入文本
            retry: 重试次数
            agent_name: agent名称
            
        Returns:
            List[float]: 向量
        """
        voyage_client = self._get_voyage_client(agent_name)
        if not voyage_client:
            raise ValueError(f"无法为 {agent_name} 创建Voyage AI客户端，请检查API密钥配置")
        
        model = self.get_model_for_agent(agent_name)
        
        for attempt in range(retry):
            try:
                # 使用Voyage AI SDK
                result = voyage_client.embed(
                    texts=[text],
                    model=model,
                    input_type="document"  # 可以是 "document" 或 "query"
                )
                
                if result and result.embeddings:
                    return result.embeddings[0]
                else:
                    raise Exception("Voyage AI返回空结果")
                    
            except Exception as e:
                logger.error(f"[ERROR] 向量化失败 (尝试 {attempt + 1}/{retry}): {str(e)}")
                if attempt < retry - 1:
                    time.sleep(2 ** attempt)
        
        raise Exception(f"向量化失败，已重试{retry}次")

    def _embed_text_bailian(self, text: str, retry: int, agent_name: str) -> List[float]:
        """
        使用阿里云百炼 OpenAI兼容SDK进行文本向量化
        
        Args:
            text: 输入文本
            retry: 重试次数
            agent_name: agent名称
            
        Returns:
            List[float]: 向量
        """
        profile = self._get_agent_profile(agent_name)
        api_key = profile.get('api_key')
        if not api_key:
            raise ValueError("百炼 API Key 未配置")

        base_url = self._normalize_openai_base_url(self._get_bailian_base_url(agent_name))
        model = profile.get('embedding_model', self.default_model)
        client = self._get_openai_client(agent_name, api_key, base_url)

        for attempt in range(retry):
            try:
                result = client.embeddings.create(model=model, input=text)
                if result and result.data:
                    return result.data[0].embedding
                raise Exception("百炼返回空结果")
            except Exception as e:
                logger.error(f"[ERROR] 向量化失败 (尝试 {attempt + 1}/{retry}): {str(e)}")
                if attempt < retry - 1:
                    time.sleep(2 ** attempt)

        raise Exception(f"向量化失败，已重试{retry}次")
    
    def _embed_text_openrouter(self, text: str, retry: int, agent_name: str = None) -> List[float]:
        """
        使用OpenRouter OpenAI兼容SDK进行文本向量化
        
        Args:
            text: 输入文本
            retry: 重试次数
            agent_name: agent名称
            
        Returns:
            List[float]: 向量
        """
        profile = self._get_agent_profile(agent_name)
        model = profile.get('embedding_model', self.default_model)
        base_url = profile.get('openai_base_url') or self._normalize_openai_base_url(profile.get('emb_url', self.base_url))
        api_key = profile.get('api_key')
        if not api_key:
            raise ValueError("OpenRouter API Key未配置")

        for attempt in range(retry):
            try:
                client = self._get_openai_client(agent_name or 'default', api_key, base_url)
                result = client.embeddings.create(model=model, input=text)
                if result and result.data:
                    return result.data[0].embedding
                raise Exception("OpenRouter返回空结果")
            except Exception as e:
                logger.error(f"[ERROR] 向量化失败 (尝试 {attempt + 1}/{retry}): {str(e)}")
                if attempt < retry - 1:
                    time.sleep(2 ** attempt)
        
        raise Exception(f"向量化失败,已重试{retry}次")
    
    def embed_batch(self, texts: List[str], batch_size: int = 10, show_progress: bool = True, agent_name: str = None) -> List[List[float]]:
        """
        批量文本向量化
        
        Args:
            texts: 文本列表
            batch_size: 批处理大小
            show_progress: 是否显示进度条
            agent_name: agent名称，用于选择对应的嵌入模型 
        
        Returns:
            List[List[float]]: 向量列表
        """
        # 确定使用的模型用于显示和维度获取
        if agent_name:
            model = self.get_model_for_agent(agent_name)
        else:
            model = self.default_model
        
        embeddings = []
        total_texts = len(texts)
        
        iterator = range(0, total_texts, batch_size)
        if show_progress:
            desc = f"向量化进度 [{model}]"
            iterator = tqdm(iterator, desc=desc, total=(total_texts + batch_size - 1) // batch_size)
        
        for i in iterator:
            batch = texts[i:i + batch_size]
            
            for text in batch:
                try:
                    embedding = self.embed_text(text, agent_name=agent_name)
                    embeddings.append(embedding)
                except Exception as e:
                    logger.error(f"\n[ERROR] 跳过文本 (索引 {len(embeddings)}): {str(e)}")
                    # 添加零向量占位
                    embeddings.append([0.0] * self.get_embedding_dimension(model))
            
            # 避免API限流
            if i + batch_size < total_texts:
                time.sleep(0.5)
        
        return embeddings
    
    def get_embedding_dimension(self, model: str = None) -> int:
        """
        获取向量维度
        
        Args:
            model: 模型名称，如果为None则使用默认模型
        
        Returns:
            int: 向量维度
        """
        use_model = model if model else self.default_model
        
        if 'voyage-3' in use_model.lower():
            return 1024
        elif 'voyage-2' in use_model.lower():
            return 1024
        elif 'voyage-large' in use_model.lower() or 'voyage-law' in use_model.lower() or 'voyage-code' in use_model.lower():
            return 1536
        elif 'large' in use_model.lower() or '3-large' in use_model.lower():
            return 3072
        elif 'small' in use_model.lower() or '3-small' in use_model.lower():
            return 1536
        elif 'ada' in use_model.lower():
            return 1536
        elif 'gemini-embedding' in use_model.lower():
            return 768
        elif 'embedding-v4' in use_model.lower():
            return 1536
        else:
            return 1536  # 默认维度


