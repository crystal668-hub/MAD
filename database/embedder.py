"""
===================================
OpenAI向量化模块
功能：使用OpenRouter或Voyage AI SDK调用api进行文本向量化
===================================
"""

import os
import time
from typing import List, Dict, Optional
import requests
from tqdm import tqdm

try:
    import voyageai
    VOYAGE_AVAILABLE = True
except ImportError:
    VOYAGE_AVAILABLE = False


class MultiModelEmbedder:
    """
    多模型文本向量化器
    支持根据agent配置动态切换嵌入模型
    支持使用OpenRouter API或Voyage AI官方SDK
    支持OpenAI、Voyage AI、Google Gemini等多种嵌入模型
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
        self.current_agent = None
        
        # Voyage AI客户端（懒加载）
        self.voyage_clients: Dict[str, 'voyageai.Client'] = {}
        
        # 从环境变量获取API Key
        if self.api_key and self.api_key.startswith('${') and self.api_key.endswith('}'):
            env_var = self.api_key[2:-1]
            self.api_key = os.environ.get(env_var)
        
        if not self.api_key:
            raise ValueError("API Key未设置，请设置环境变量 xxxx_API_KEY")
        
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        print(f"[OK] 初始化多模型向量化器")
        print(f"  默认模型: {self.default_model}")
        print(f"  API地址: {self.base_url}")
        if self.agent_configs:
            agent_models = {name: cfg.get('embedding_model') for name, cfg in self.agent_configs.items()}
            print(f"  可用Agent模型: {agent_models}")
    
    def get_model_for_agent(self, agent_name: str = None) -> str:
        """
        获取指定agent使用的嵌入模型
        
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
        if not VOYAGE_AVAILABLE:
            return None
            
        if agent_name not in self.voyage_clients:
            agent_config = self.agent_configs.get(agent_name, {})
            voyage_api_key = agent_config.get('voyage_api_key')
            
            # 从环境变量获取API Key
            if voyage_api_key and voyage_api_key.startswith('${') and voyage_api_key.endswith('}'):
                env_var = voyage_api_key[2:-1]
                voyage_api_key = os.environ.get(env_var)
            
            if voyage_api_key:
                self.voyage_clients[agent_name] = voyageai.Client(api_key=voyage_api_key)
                print(f"[INFO] 为 {agent_name} 创建Voyage AI客户端")
            else:
                return None
                
        return self.voyage_clients.get(agent_name)
    
    def _is_voyage_model(self, agent_name: str = None) -> bool:
        """
        判断指定agent是否使用Voyage AI模型
        
        Args:
            agent_name: agent名称
            
        Returns:
            bool: 是否使用Voyage AI
        """
        if not agent_name or agent_name not in self.agent_configs:
            return False
            
        agent_config = self.agent_configs[agent_name]
        embedding_provider = agent_config.get('embedding_provider', '')
        
        return embedding_provider.lower() == 'voyage'

    def _is_bailian_model(self, agent_name: str = None) -> bool:
        """判断是否使用百炼/通义千问向量接口"""
        if not agent_name or agent_name not in self.agent_configs:
            return False
        provider = self.agent_configs[agent_name].get('embedding_provider', '')
        return provider.lower() in ['bailian', 'aliyun', 'qwen']

    def _get_bailian_base_url(self, agent_name: str) -> str:
        agent_config = self.agent_configs.get(agent_name, {})
        return agent_config.get('emb_url', 'https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings')
    
    def set_agent(self, agent_name: str) -> None:
        """
        设置当前使用的agent，后续调用将使用该agent的嵌入模型
        
        Args:
            agent_name: agent名称 (如 'agent1', 'agent2', 'agent3', 'agent4')
        """
        if agent_name not in self.agent_configs:
            print(f"[WARNING] Agent '{agent_name}' 不存在，将使用默认模型")
            self.current_agent = None
        else:
            self.current_agent = agent_name
            model = self.get_model_for_agent(agent_name)
            print(f"[INFO] 切换到 {agent_name} 的嵌入模型: {model}")
    
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
        use_agent = agent_name if agent_name else self.current_agent
        
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
        if not VOYAGE_AVAILABLE:
            raise ImportError("Voyage AI SDK未安装，请运行: pip install voyageai")
        
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
                print(f"[ERROR] Voyage AI向量化失败 (尝试 {attempt + 1}/{retry}): {str(e)}")
                if attempt < retry - 1:
                    time.sleep(2 ** attempt)
        
        raise Exception(f"Voyage AI向量化失败，已重试{retry}次")

    def _embed_text_bailian(self, text: str, retry: int, agent_name: str) -> List[float]:
        """使用百炼OpenAI兼容HTTP接口进行文本向量化"""
        agent_config = self.agent_configs.get(agent_name, {})
        api_key = agent_config.get('bailian_api_key') or agent_config.get('api_key') or self.api_key
        if api_key and api_key.startswith('${') and api_key.endswith('}'):
            env_var = api_key[2:-1]
            api_key = os.environ.get(env_var)
        if not api_key:
            raise ValueError("百炼 API Key 未配置")
        
        base_url = self._get_bailian_base_url(agent_name)
        model = self.get_model_for_agent(agent_name)
        payload = {
            'model': model,
            'input': text
        }
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        for attempt in range(retry):
            try:
                response = requests.post(
                    base_url,
                    headers=headers,
                    json=payload,
                    timeout=30
                )
                if response.status_code == 200:
                    result = response.json()
                    embedding = result['data'][0]['embedding']
                    return embedding
                else:
                    error_msg = f"API请求失败 (状态码: {response.status_code})"
                    if response.text:
                        error_msg += f", 响应: {response.text[:200]}"
                    print(f"[ERROR] {error_msg}")
                    if attempt < retry - 1:
                        time.sleep(2 ** attempt)
            except Exception as e:
                print(f"[ERROR] 百炼向量化失败 (尝试 {attempt + 1}/{retry}): {str(e)}")
                if attempt < retry - 1:
                    time.sleep(2 ** attempt)
        
        raise Exception(f"百炼向量化失败，已重试{retry}次")
    
    def _embed_text_openrouter(self, text: str, retry: int, agent_name: str = None) -> List[float]:
        """
        使用OpenRouter API进行文本向量化
        
        Args:
            text: 输入文本
            retry: 重试次数
            agent_name: agent名称
            
        Returns:
            List[float]: 向量
        """
        # 确定使用的模型：优先使用agent_name指定的，其次使用set_agent设置的，最后使用默认模型
        if agent_name:
            model = self.get_model_for_agent(agent_name)
        else:
            model = self.default_model
        
        payload = {
            'model': model,
            'input': text
        }
        
        for attempt in range(retry):
            try:
                response = requests.post(
                    self.base_url,
                    headers=self.headers,
                    json=payload,
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    embedding = result['data'][0]['embedding']
                    return embedding
                else:
                    error_msg = f"API请求失败 (状态码: {response.status_code})"
                    if response.text:
                        error_msg += f", 响应: {response.text[:200]}"
                    print(f"[ERROR] {error_msg}")
                    if attempt < retry - 1:
                        time.sleep(2 ** attempt)
                    
            except Exception as e:
                print(f"[ERROR] 向量化失败 (尝试 {attempt + 1}/{retry}): {str(e)}")
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
            agent_name: agent名称，用于选择对应的嵌入模型 (如 'agent1', 'agent2', 'agent3', 'agent4')
        
        Returns:
            List[List[float]]: 向量列表
        """
        # 确定使用的模型用于显示和维度获取
        if agent_name:
            model = self.get_model_for_agent(agent_name)
        elif self.current_agent:
            model = self.get_model_for_agent(self.current_agent)
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
                    print(f"\n[ERROR] 跳过文本 (索引 {len(embeddings)}): {str(e)}")
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


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    # 测试配置 - 包含多个agent的配置
    test_config = {
        'embedding_model': 'openai/text-embedding-3-large',
        'api_key': '${OPENAI_API_KEY}',
        'emb_url': 'https://openrouter.ai/api/v1/embeddings'
    }
    
    # 模拟从config.yaml加载的agent配置
    agent_configs = {
        'agent1': {
            'embedding_model': 'openai/text-embedding-3-large',
            'emb_url': 'https://openrouter.ai/api/v1/embeddings'
        },
        'agent2': {
            'embedding_model': 'voyage-3-large',
            'embedding_provider': 'voyage',
            'voyage_api_key': '${VOYAGE_API_KEY}'
        },
        'agent3': {
            'embedding_model': 'google/gemini-embedding-001',
            'emb_url': 'https://openrouter.ai/api/v1/embeddings'
        },
        'agent4': {
            'embedding_model': 'text-embedding-v4',
            'embedding_provider': 'bailian',
            'bailian_api_key': '${QWEN_API_KEY}',
            'emb_url': 'https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings'
        }
    }
    
    try:
        embedder = MultiModelEmbedder(test_config, agent_configs)
        
        # 测试1: 使用默认模型
        print("\n=== 测试1: 默认模型 ===")
        test_text = "This is a test sentence for embedding."
        embedding = embedder.embed_text(test_text)
        print(f"向量维度: {len(embedding)}")
        print(f"向量前5个值: {embedding[:5]}")
        
        # 测试2: 使用agent1的模型
        print("\n=== 测试2: Agent1模型 ===")
        embedding_agent1 = embedder.embed_text(test_text, agent_name='agent1')
        print(f"向量维度: {len(embedding_agent1)}")
        
        # 测试3: 使用agent3的模型
        print("\n=== 测试3: Agent3模型 ===")
        embedding_agent3 = embedder.embed_text(test_text, agent_name='agent3')
        print(f"向量维度: {len(embedding_agent3)}")
        
        # 测试4: 使用set_agent切换后批量处理
        print("\n=== 测试4: 设置Agent2并批量处理 ===")
        embedder.set_agent('agent2')
        test_texts = [
            "Platinum catalysts for hydrogen evolution",
            "Gold nanoparticles for CO2 reduction",
            "Ruthenium for oxygen evolution reaction"
        ]
        embeddings = embedder.embed_batch(test_texts, batch_size=2)
        print(f"批量向量化完成，共 {len(embeddings)} 个向量")
        
        # 测试5: 直接指定agent进行批量处理
        print("\n=== 测试5: 直接指定Agent3批量处理 ===")
        embeddings_agent3 = embedder.embed_batch(test_texts, batch_size=2, agent_name='agent3')
        print(f"批量向量化完成，共 {len(embeddings_agent3)} 个向量")
        
    except Exception as e:
        print(f"✗ 测试失败: {str(e)}")
