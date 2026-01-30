"""
===================================
RAG系统实现模块
功能：实现基于LlamaIndex的检索增强生成系统
===================================
"""

import os
from datetime import datetime
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
from llama_index.core.node_parser import SentenceSplitter, MarkdownNodeParser
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from database.vector_store import VectorStore
from utils.logger import Logger

db_log_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
db_log_file = Path("./logs/db_log") / f"rag_system_{db_log_timestamp}.log"
logger = Logger.get_logger(
    name=f"MAD.DB.RAGSystem.{db_log_timestamp}",
    log_file=str(db_log_file),
    level="INFO"
)


class RAGSystem:
    """
    RAG System
    Integrates LlamaIndex and Chroma vector database to provide document indexing and retrieval capabilities
    """
    
    def __init__(
        self,
        data_dir: str,
        persist_dir: str,
        collection_name: str,
        embedding_model: Optional[Any] = None,
        top_k: int = 5,
        chunk_size: int = 256,
        chunk_overlap: int = 50
    ):
        """
        初始化RAG系统
        
        Args:
            data_dir: 原始文献数据目录（data/raw）
            persist_dir: 索引持久化目录
            collection_name: 向量数据库集合名称
            embedding_model: 嵌入模型（可选）
            top_k: 检索返回的top-k结果
            chunk_size: 文本分块大小
            chunk_overlap: 文本分块重叠
        """
        self.data_dir = data_dir
        self.persist_dir = persist_dir
        self.collection_name = collection_name
        self.top_k = top_k
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
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
        self.retriever = None
        
        # 尝试加载已存在的索引
        if self._index_exists():
            self._load_index()
        else:
            logger.info("索引不存在，请先调用 build_index() 构建索引")
    
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
            # 使用ChromaDB向量存储创建存储上下文
            chroma_collection = self.vector_store.collection
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            
            # 创建存储上下文
            storage_context = StorageContext.from_defaults(
                vector_store=vector_store,
                persist_dir=self.persist_dir
            )
            
            # 加载索引
            self.index = load_index_from_storage(storage_context)
            
            # 创建查询引擎
            self._create_query_engine()
            
            logger.info(f"成功加载索引: {self.collection_name}")
        except Exception as e:
            logger.error(f"加载索引失败: {str(e)}")
            logger.warning("将需要重新构建索引")
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
            logger.info("索引已存在，使用 force_rebuild=True 强制重建")
            return
        
        # 加载文档
        if documents is None:
            documents = self._load_documents()
        
        if not documents:
            logger.warning("警告：没有找到文档，无法构建索引")
            return
        
        # 创建存储上下文（使用Chroma向量存储）
        chroma_collection = self.vector_store.collection
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        logger.info(f"开始构建索引，共 {len(documents)} 个chunks...")
        self.index = VectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            show_progress=True
        )
        
        # 持久化索引
        self.index.storage_context.persist(persist_dir=self.persist_dir)
        
        # 创建查询引擎
        self._create_query_engine()
        
        logger.info("索引构建完成")
    
    def _load_documents(self) -> List[Document]:
        """
        从数据目录加载Markdown文档并切分为chunks
        
        Returns:
            List[Document]: 文档列表（每个chunk作为一个Document）
        """
        # 检查数据目录是否存在Markdown文件
        data_path = Path(self.data_dir)
        if not data_path.exists() or not any(data_path.rglob('*.md')):
            logger.warning(f"警告：数据目录 {self.data_dir} 不存在或为空")
            return []

        try:
            reader = SimpleDirectoryReader(
                input_dir=str(data_path),
                required_exts=[".md"],
                recursive=True
            )
            raw_documents = reader.load_data()
        except Exception as e:
            logger.warning(f"警告：加载Markdown失败: {e}")
            return []

        if not raw_documents:
            logger.warning(f"警告：未找到Markdown文件: {self.data_dir}")
            return []

        markdown_parser = MarkdownNodeParser()
        sentence_splitter = SentenceSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

        pipeline = IngestionPipeline(
            transformations=[
                markdown_parser,
                sentence_splitter
            ]
        )

        chunked_documents: List[Document] = []
        for doc in raw_documents:
            try:
                nodes = pipeline.run(documents=[doc])
                for idx, node in enumerate(nodes):
                    chunked_documents.append(
                        Document(
                            text=node.get_content(),
                            metadata={
                                **doc.metadata,
                                "chunk_id": idx,
                                "total_chunks": len(nodes)
                            }
                        )
                    )
            except Exception as e:
                file_name = doc.metadata.get('file_name', 'unknown')
                logger.warning(f"警告：切分文件 {file_name} 时出错: {e}")
                continue

        logger.info(f"成功加载 {len(raw_documents)} 个文档，生成 {len(chunked_documents)} 个chunks")
        return chunked_documents
    
    def _create_query_engine(self) -> None:
        """
        创建查询引擎
        """
        if self.index is None:
            logger.error("错误：索引未初始化，无法创建查询引擎")
            return
        
        # 创建检索器
        self.retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=self.top_k
        )
        
        # 创建查询引擎
        self.query_engine = RetrieverQueryEngine(retriever=self.retriever)
        
        logger.info("查询引擎创建完成")
    
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

        if self.retriever is None:
            self._create_query_engine()

        # 执行检索
        nodes = self.retriever.retrieve(query_text)
        
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
            logger.info("索引不存在，将创建新索引")
            self.build_index(documents=documents)
            return
        
        # 插入文档到索引
        for doc in documents:
            self.index.insert(doc)
        
        # 持久化
        self.index.storage_context.persist(persist_dir=self.persist_dir)
        
        logger.info(f"成功添加 {len(documents)} 个文档到索引")
    
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


