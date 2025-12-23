"""
===================================
RAG系统实现模块
功能：实现基于LlamaIndex的检索增强生成系统
===================================
"""

import os
from typing import List, Dict, Optional, Any
from pathlib import Path

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Document,
    StorageContext,
    load_index_from_storage,
    Settings
)
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from database.vector_store import VectorStore


class RAGSystem:
    """
    检索增强生成（RAG）系统
    集成LlamaIndex和Chroma向量数据库，提供文档索引和检索功能
    """
    
    def __init__(
        self,
        data_dir: str,
        persist_dir: str,
        collection_name: str,
        embedding_model: Optional[Any] = None,
        top_k: int = 5
    ):
        """
        初始化RAG系统
        
        Args:
            data_dir: 已切分的chunk数据目录（data/processed）
            persist_dir: 索引持久化目录
            collection_name: 向量数据库集合名称
            embedding_model: 嵌入模型（可选）
            top_k: 检索返回的top-k结果
        """
        self.data_dir = data_dir
        self.persist_dir = persist_dir
        self.collection_name = collection_name
        self.top_k = top_k
        
        # 创建必要的目录
        os.makedirs(data_dir, exist_ok=True)
        os.makedirs(persist_dir, exist_ok=True)
        
        # 设置嵌入模型
        if embedding_model is None:
            # 默认使用OpenAI的嵌入模型
            embedding_model = OpenAIEmbedding(model="text-embedding-ada-002")
        
        Settings.embed_model = embedding_model
        
        # 初始化向量数据库
        self.vector_store = VectorStore(
            persist_directory=persist_dir,
            collection_name=collection_name
        )
        
        # 初始化索引（如果存在则加载，否则创建）
        self.index = None
        self.query_engine = None
        
        # 尝试加载已存在的索引
        if self._index_exists():
            self._load_index()
        else:
            print("索引不存在，请先调用 build_index() 构建索引")
    
    def _index_exists(self) -> bool:
        """
        检查索引是否已存在
        
        Returns:
            bool: 索引是否存在
        """
        storage_path = Path(self.persist_dir) / "docstore.json"
        return storage_path.exists()
    
    def _load_index(self) -> None:
        """
        从磁盘加载已存在的索引
        """
        try:
            # 创建存储上下文
            storage_context = StorageContext.from_defaults(
                persist_dir=self.persist_dir
            )
            
            # 加载索引
            self.index = load_index_from_storage(storage_context)
            
            # 创建查询引擎
            self._create_query_engine()
            
            print(f"成功加载索引: {self.collection_name}")
        except Exception as e:
            print(f"加载索引失败: {str(e)}")
            self.index = None
    
    def build_index(
        self,
        documents: Optional[List[Document]] = None,
        force_rebuild: bool = False
    ) -> None:
        """
        构建或重建索引
        
        Args:
            documents: 文档列表（可选，不提供则从data_dir读取）
            force_rebuild: 是否强制重建索引
        """
        # 检查是否需要重建
        if self._index_exists() and not force_rebuild:
            print("索引已存在，使用 force_rebuild=True 强制重建")
            return
        
        # 加载文档
        if documents is None:
            documents = self._load_documents()
        
        if not documents:
            print("警告：没有找到文档，无法构建索引")
            return
        
        # 创建存储上下文（使用Chroma向量存储）
        chroma_collection = self.vector_store.collection
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        # 构建索引（文档已经是切分好的chunks，无需再分割）
        print(f"开始构建索引，共 {len(documents)} 个chunks...")
        self.index = VectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            show_progress=True
        )
        
        # 持久化索引
        self.index.storage_context.persist(persist_dir=self.persist_dir)
        
        # 创建查询引擎
        self._create_query_engine()
        
        print("索引构建完成")
    
    def _load_documents(self) -> List[Document]:
        """
        从数据目录加载文档（已切分的chunks）
        每个txt文件格式：索引\t内容
        
        Returns:
            List[Document]: 文档列表（每个chunk作为一个Document）
        """
        # 检查数据目录是否存在文件
        data_path = Path(self.data_dir)
        if not data_path.exists() or not any(data_path.iterdir()):
            print(f"警告：数据目录 {self.data_dir} 不存在或为空")
            return []
        
        documents = []
        
        # 遍历所有txt文件
        for txt_file in data_path.glob('*.txt'):
            try:
                with open(txt_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        
                        # 解析格式：索引\t内容
                        parts = line.split('\t', 1)
                        if len(parts) == 2:
                            chunk_id, content = parts
                            # 创建Document对象
                            doc = Document(
                                text=content,
                                metadata={
                                    'source_file': txt_file.name,
                                    'chunk_id': chunk_id
                                }
                            )
                            documents.append(doc)
            except Exception as e:
                print(f"警告：读取文件 {txt_file.name} 时出错: {e}")
                continue
        
        print(f"成功加载 {len(documents)} 个chunks")
        return documents
    
    def _create_query_engine(self) -> None:
        """
        创建查询引擎
        """
        if self.index is None:
            print("错误：索引未初始化，无法创建查询引擎")
            return
        
        # 创建检索器
        retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=self.top_k
        )
        
        # 创建查询引擎
        self.query_engine = RetrieverQueryEngine(retriever=retriever)
        
        print("查询引擎创建完成")
    
    def query(self, query_text: str) -> Dict[str, Any]:
        """
        执行检索增强查询
        
        Args:
            query_text: 查询文本
        
        Returns:
            Dict: 查询结果，包含答案和来源文档
        """
        if self.query_engine is None:
            raise ValueError("查询引擎未初始化，请先构建或加载索引")
        
        # 执行查询
        response = self.query_engine.query(query_text)
        
        # 整理结果
        result = {
            "answer": str(response),
            "source_nodes": []
        }
        
        # 添加来源文档信息
        if hasattr(response, 'source_nodes'):
            for node in response.source_nodes:
                result["source_nodes"].append({
                    "text": node.node.text,
                    "score": node.score,
                    "metadata": node.node.metadata
                })
        
        return result
    
    def retrieve(self, query_text: str) -> List[Dict]:
        """
        仅执行检索（不生成答案）
        
        Args:
            query_text: 查询文本
        
        Returns:
            List[Dict]: 检索到的相关文档
        """
        if self.index is None:
            raise ValueError("索引未初始化")
        
        # 创建检索器
        retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=self.top_k
        )
        
        # 执行检索
        nodes = retriever.retrieve(query_text)
        
        # 整理结果
        results = []
        for node in nodes:
            results.append({
                "text": node.node.text,
                "score": node.score,
                "metadata": node.node.metadata
            })
        
        return results
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        向已有索引添加新文档
        
        Args:
            documents: 新文档列表
        """
        if self.index is None:
            print("索引不存在，将创建新索引")
            self.build_index(documents=documents)
            return
        
        # 插入文档到索引
        for doc in documents:
            self.index.insert(doc)
        
        # 持久化
        self.index.storage_context.persist(persist_dir=self.persist_dir)
        
        print(f"成功添加 {len(documents)} 个文档到索引")
    
    def get_index_stats(self) -> Dict:
        """
        获取索引统计信息
        
        Returns:
            Dict: 索引统计信息
        """
        if self.index is None:
            return {"status": "索引未初始化"}
        
        doc_count = self.vector_store.get_collection_count()
        
        return {
            "status": "已初始化",
            "collection_name": self.collection_name,
            "document_count": doc_count,
            "top_k": self.top_k
        }


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    # 初始化RAG系统
    rag = RAGSystem(
        data_dir="./data/processed",
        persist_dir="./data/chroma_db",
        collection_name="chemical_reactions",
        top_k=5
    )
    
    # 构建索引（首次运行）
    rag.build_index()
    
    # 执行查询
    if rag.query_engine:
        result = rag.query("什么是氧化还原反应的过电势？")
        print(f"\n查询结果: {result['answer']}")
        
        # 打印来源文档
        print("\n来源文档:")
        for i, node in enumerate(result['source_nodes'], 1):
            print(f"{i}. (相关度: {node['score']:.4f})")
            print(f"   {node['text'][:100]}...")
