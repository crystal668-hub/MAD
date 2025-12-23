"""
===================================
向量数据库管理模块
功能：管理Chroma向量数据库的创建、查询和维护
===================================
"""

import os
from typing import List, Dict, Optional, Any, Callable
import chromadb
from chromadb.config import Settings
from pathlib import Path


class VectorStore:
    """
    向量数据库管理类
    负责Chroma向量数据库的初始化、文档添加、相似度检索等操作
    """
    
    def __init__(
        self,
        persist_directory: str,
        collection_name: str,
        embedding_function: Optional[Callable] = None,
        distance_metric: str = "cosine"
    ):
        """
        初始化向量数据库
        
        Args:
            persist_directory: 数据库持久化目录
            collection_name: 集合名称
            embedding_function: 嵌入函数（可选，如果为None则使用自定义向量）
            distance_metric: 距离度量方式，可选 "cosine", "l2", "ip"
        """
        self.persist_directory = Path(persist_directory)
        self.persist_directory.mkdir(parents=True, exist_ok=True)
        self.collection_name = collection_name
        self.distance_metric = distance_metric
        self.embedding_function = embedding_function
        
        # 初始化Chroma客户端
        self.client = chromadb.PersistentClient(
            path=str(self.persist_directory),
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        # 获取或创建集合
        self.collection = self._get_or_create_collection()
    
    def _get_or_create_collection(self):
        """
        获取已存在的集合或创建新集合
        
        Returns:
            chromadb.Collection: Chroma集合对象
        """
        try:
            # 如果没有embedding_function，不传递该参数
            if self.embedding_function is None:
                # 使用自定义向量，不需要embedding_function
                collection = self.client.get_or_create_collection(
                    name=self.collection_name,
                    metadata={"hnsw:space": self.distance_metric}
                )
                print(f"[OK] 初始化向量数据库 (使用自定义向量)")
            else:
                # 使用提供的embedding_function
                collection = self.client.get_or_create_collection(
                    name=self.collection_name,
                    embedding_function=self.embedding_function,
                    metadata={"hnsw:space": self.distance_metric}
                )
                print(f"[OK] 初始化向量数据库 (使用embedding_function)")
            
            print(f"  集合名称: {self.collection_name}")
            print(f"  存储路径: {self.persist_directory}")
            print(f"  当前文档数: {collection.count()}")
            
        except Exception as e:
            print(f"[ERROR] 初始化向量数据库失败: {str(e)}")
            raise
        
        return collection
    
    def add_documents(
        self,
        documents: List[str],
        metadatas: Optional[List[Dict]] = None,
        ids: Optional[List[str]] = None
    ) -> None:
        """
        向向量数据库添加文档
        
        Args:
            documents: 文档文本列表
            metadatas: 文档元数据列表（可选）
            ids: 文档ID列表（可选，不提供则自动生成）
        """
        # 自动生成ID（如果未提供）
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(documents))]
        
        # 添加文档到集合
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        
        print(f"成功添加 {len(documents)} 个文档到向量数据库")
    
    def query(
        self,
        query_texts: List[str],
        n_results: int = 5,
        where: Optional[Dict] = None,
        where_document: Optional[Dict] = None
    ) -> Dict:
        """
        查询向量数据库
        
        Args:
            query_texts: 查询文本列表
            n_results: 返回结果数量
            where: 元数据过滤条件（可选）
            where_document: 文档内容过滤条件（可选）
        
        Returns:
            Dict: 查询结果，包含文档、距离、元数据等
        """
        results = self.collection.query(
            query_texts=query_texts,
            n_results=n_results,
            where=where,
            where_document=where_document
        )
        
        return results
    
    def similarity_search(
        self,
        query_text: str,
        top_k: int = 5,
        threshold: Optional[float] = None
    ) -> List[Dict]:
        """
        相似度搜索
        
        Args:
            query_text: 查询文本
            top_k: 返回top-k个最相似结果
            threshold: 相似度阈值（可选）
        
        Returns:
            List[Dict]: 相似文档列表
        """
        results = self.query(
            query_texts=[query_text],
            n_results=top_k
        )
        
        # 解析结果
        similar_docs = []
        for i in range(len(results['ids'][0])):
            doc_dict = {
                'id': results['ids'][0][i],
                'document': results['documents'][0][i],
                'distance': results['distances'][0][i],
                'metadata': results['metadatas'][0][i] if results['metadatas'] else None
            }
            
            # 应用阈值过滤（如果指定）
            if threshold is None or doc_dict['distance'] <= threshold:
                similar_docs.append(doc_dict)
        
        return similar_docs
    
    def update_documents(
        self,
        ids: List[str],
        documents: Optional[List[str]] = None,
        metadatas: Optional[List[Dict]] = None
    ) -> None:
        """
        更新文档
        
        Args:
            ids: 要更新的文档ID列表
            documents: 新的文档文本列表（可选）
            metadatas: 新的元数据列表（可选）
        """
        self.collection.update(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        
        print(f"成功更新 {len(ids)} 个文档")
    
    def delete_documents(self, ids: List[str]) -> None:
        """
        删除文档
        
        Args:
            ids: 要删除的文档ID列表
        """
        self.collection.delete(ids=ids)
        print(f"成功删除 {len(ids)} 个文档")
    
    def add_documents_with_embeddings(
        self,
        texts: List[str],
        embeddings: List[List[float]],
        metadatas: Optional[List[Dict]] = None,
        ids: Optional[List[str]] = None
    ) -> None:
        """
        使用预生成的向量添加文档
        
        Args:
            texts: 文本列表
            embeddings: 向量列表
            metadatas: 元数据列表
            ids: 文档ID列表
        """
        if ids is None:
            ids = [f"doc_{i}_{hash(text[:50]) % 1000000}" for i, text in enumerate(texts)]
        
        if metadatas is None:
            metadatas = [{}] * len(texts)
        
        # 确保所有列表长度一致
        assert len(texts) == len(embeddings) == len(metadatas) == len(ids), \
            "texts, embeddings, metadatas, ids长度必须一致"
        
        # 批量添加
        batch_size = 100
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i + batch_size]
            batch_embeddings = embeddings[i:i + batch_size]
            batch_metadatas = metadatas[i:i + batch_size]
            batch_ids = ids[i:i + batch_size]
            
            self.collection.add(
                documents=batch_texts,
                embeddings=batch_embeddings,
                metadatas=batch_metadatas,
                ids=batch_ids
            )
        
        print(f"[OK] 添加 {len(texts)} 个文档到集合 '{self.collection_name}'")
    
    def similarity_search_with_embedding(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        where: Optional[Dict] = None
    ) -> List[Dict]:
        """
        使用预生成的查询向量进行相似度搜索
        
        Args:
            query_embedding: 查询向量
            top_k: 返回结果数量
            where: 元数据过滤条件
        
        Returns:
            List[Dict]: 搜索结果列表
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where
        )
        
        documents = []
        if results['documents'] and len(results['documents']) > 0:
            for i in range(len(results['documents'][0])):
                doc = {
                    'text': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {},
                    'distance': results['distances'][0][i] if results['distances'] else None,
                    'id': results['ids'][0][i] if results['ids'] else None
                }
                documents.append(doc)
        
        return documents
    
    def get_collection_count(self) -> int:
        """
        获取集合中的文档数量
        
        Returns:
            int: 文档数量
        """
        return self.collection.count()
    
    def reset_collection(self) -> None:
        """
        重置集合（删除所有文档）
        警告：此操作不可逆
        """
        self.client.delete_collection(name=self.collection_name)
        self.collection = self._get_or_create_collection()
        print(f"集合 {self.collection_name} 已重置")
    
    def get_all_documents(self) -> Dict:
        """
        获取集合中的所有文档
        
        Returns:
            Dict: 所有文档及其元数据
        """
        return self.collection.get()


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    # 初始化向量数据库
    vector_store = VectorStore(
        persist_directory="./data/chroma_db",
        collection_name="test_collection"
    )
    
    # 添加测试文档
    test_docs = [
        "氢氧化反应是一种常见的电化学反应",
        "氧化还原反应涉及电子转移",
        "酸碱中和反应会释放或吸收热量"
    ]
    
    test_metadata = [
        {"reaction_type": "氢氧化反应", "category": "电化学"},
        {"reaction_type": "氧化还原反应", "category": "电化学"},
        {"reaction_type": "酸碱中和", "category": "热化学"}
    ]
    
    vector_store.add_documents(
        documents=test_docs,
        metadatas=test_metadata
    )
    
    # 相似度搜索
    results = vector_store.similarity_search("电化学反应的特点", top_k=2)
    
    print("\n搜索结果:")
    for doc in results:
        print(f"- {doc['document']} (距离: {doc['distance']:.4f})")
