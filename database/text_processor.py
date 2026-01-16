"""
===================================
文本预处理模块
功能：处理原始文本数据,准备向量化
包含TSV文件处理、文本加载、分块等功能
支持LlamaIndex解析Markdown和txt文件
===================================
"""

import csv
import re
from pathlib import Path
from typing import List, Dict, Optional

from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter, MarkdownNodeParser
from llama_index.core.ingestion import IngestionPipeline


class TextProcessor:
    """
    文档预处理器
    负责加载和处理原始文档数据
    """
    
    def __init__(self, data_dir: str = "./data/raw"):
        """
        初始化文档处理器
        
        Args:
            data_dir: 原始数据目录
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def clean_text(self, text: str) -> str:
        """
        清洗文本内容，删除Acknowledgement和Reference部分
        
        清洗操作：
        - 删除Acknowledgement部分及其后的所有内容
        - 删除Reference/References部分及其后的所有内容
        
        Args:
            text: 原始文本
            
        Returns:
            str: 清洗后的文本
        """
        if not text:
            return ""
        
        # 删除Acknowledgement部分及其后的内容
        # 匹配各种可能的写法：Acknowledgement, Acknowledgements, ACKNOWLEDGEMENT等
        text = re.sub(
            r'(?i)(##?\s*)?Acknowledgements?.*$',
            '',
            text,
            flags=re.DOTALL
        )
        
        # 删除Reference/References部分及其后的内容
        # 匹配各种可能的写法：Reference, References, REFERENCE, REFERENCES等
        text = re.sub(
            r'(?i)(##?\s*)?References?.*$',
            '',
            text,
            flags=re.DOTALL
        )
        
        return text
    
    def extract_doi_from_content(self, content: str, filename: str = "") -> str:
        """
        从文本内容或文件名中提取DOI号
        
        Args:
            content: 文本内容
            filename: 文件名
            
        Returns:
            str: DOI号，如果未找到则返回"unknown"
        """
        # DOI的正则表达式模式
        # 标准DOI格式: 10.xxxx/yyyy
        doi_patterns = [
            r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+',  # 标准DOI格式
            r'doi:?\s*10\.\d{4,9}/[-._;()/:A-Za-z0-9]+',  # 带doi:前缀
            r'DOI:?\s*10\.\d{4,9}/[-._;()/:A-Za-z0-9]+'   # 带DOI:前缀
        ]
        
        # 首先尝试从文件名中提取
        if filename:
            for pattern in doi_patterns:
                match = re.search(pattern, filename, re.IGNORECASE)
                if match:
                    doi = match.group(0)
                    # 清理前缀
                    doi = re.sub(r'^(doi:?|DOI:?)\s*', '', doi, flags=re.IGNORECASE)
                    return doi.strip()
        
        # 从内容中提取（通常在文章开头）
        # 只检查前5000个字符以提高效率
        content_head = content[:5000] if len(content) > 5000 else content
        
        for pattern in doi_patterns:
            match = re.search(pattern, content_head, re.IGNORECASE)
            if match:
                doi = match.group(0)
                # 清理前缀
                doi = re.sub(r'^(doi:?|DOI:?)\s*', '', doi, flags=re.IGNORECASE)
                return doi.strip()
        
        return "unknown"
    
    def load_documents(
        self,
        data_dir: str,
        reaction_type: Optional[str] = None
    ) -> List[Document]:
        """
        使用SimpleDirectoryReader加载Markdown文件，创建Document对象并添加metadata
        
        Args:
            data_dir: 数据目录路径
            reaction_type: 反应类型
        
        Returns:
            List[Document]: Document对象列表
            metadata包含：
                - reaction_type: 反应类型
                - doc_id: 文献DOI号
        """
        data_path = Path(data_dir)
        if not data_path.exists():
            print(f"✗ 目录不存在: {data_dir}")
            return []
        
        try:
            reader = SimpleDirectoryReader(
                input_dir=str(data_path),
                required_exts=[".md"],  
                recursive=False  # 不递归读取子目录
            )
            documents = reader.load_data()
            
            if not documents:
                print(f"✗ 未找到任何Markdown文件: {data_dir}")
                return []
            
            # 为每个文档添加自定义metadata
            processed_documents = []
            for doc in documents:
                # 获取文件名（从原始metadata中）
                file_name = doc.metadata.get('file_name', '')
                file_path_str = doc.metadata.get('file_path', '')
                
                # 从文件名推断反应类型（如果未指定）
                inferred_reaction = reaction_type
                if inferred_reaction is None and file_name:
                    # 尝试从文件名中提取反应类型
                    filename_upper = Path(file_name).stem.upper()
                    reaction_types = ["CO2RR", "EOR", "HER", "HOR", "HZOR", "O5H", "OER", "ORR", "UOR"]
                    for rt in reaction_types:
                        if rt in filename_upper:
                            inferred_reaction = rt
                            break
                
                # 提取DOI号
                doc_id = self.extract_doi_from_content(doc.text, file_name)
                
                # 重置metadata为只包含reaction_type和doc_id
                doc.metadata = {
                    "reaction_type": inferred_reaction or "unknown",
                    "doc_id": doc_id
                }
                
                processed_documents.append(doc)
                
                print(f"✓ 加载 {file_name}")
                print(f"  反应类型: {doc.metadata['reaction_type']}")
                print(f"  DOI: {doc.metadata['doc_id']}")
            
            print(f"\n共加载 {len(processed_documents)} 个Document对象")
            return processed_documents
            
        except Exception as e:
            print(f"✗ 加载文档失败: {str(e)}")
            return []
    
    def load_reaction_documents(
        self,
        base_dir: str,
        reaction_configs: Dict[str, Dict]
    ) -> List[Document]:
        """
        按反应类型加载所有文献数据
        
        Args:
            base_dir: 数据根目录
            reaction_configs: 反应类型配置字典
        
        Returns:
            List[Document]: 所有反应类型的Document列表
            每个Document的metadata包含：
                - reaction_type: 反应类型
                - doc_id: 文献DOI号
        """
        all_documents = []
        base_path = Path(base_dir)
        
        for reaction_type, config in reaction_configs.items():
            reaction_path = base_path / config.get("path", reaction_type)
            
            print(f"\n--- 加载 {reaction_type} ---")
            docs = self.load_documents(
                data_dir=str(reaction_path),
                reaction_type=reaction_type
            )
            all_documents.extend(docs)
        
        return all_documents
    
    def chunk_documents(
        self,
        documents: List[Document],
        chunk_size: int = 256,
        chunk_overlap: int = 50
    ) -> List[Document]:
        """
        使用两级切分策略对Document对象进行分块
        
        两级切分策略：
        1. 第一级：使用MarkdownNodeParser基于Markdown标题切分，确保chunk不跨越大章节
        2. 第二级：使用SentenceSplitter对第一级节点进行细分
        3. 使用IngestionPipeline将两级切分器串联
        
        Args:
            documents: Document对象列表
            chunk_size: 分块大小（默认256）
            chunk_overlap: 分块重叠大小（默认50）
        
        Returns:
            List[Document]: 分块后的Document列表
        """
        if not documents:
            return []
        
        # 第一级：基于Markdown标题的切分器
        markdown_parser = MarkdownNodeParser()
        
        # 第二级：基于句子的细分切分器
        sentence_splitter = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        # 使用IngestionPipeline串联两级切分器
        pipeline = IngestionPipeline(
            transformations=[
                markdown_parser,      # 第一级：按标题切分
                sentence_splitter     # 第二级：按句子细分
            ]
        )
        
        chunked_documents = []
        
        for doc in documents:
            # 通过pipeline处理文档，获取分块后的节点
            nodes = pipeline.run(documents=[doc])
            
            # 将节点转换为Document对象，保留原始metadata
            for idx, node in enumerate(nodes):
                chunk_metadata = doc.metadata.copy()
                chunk_metadata["chunk_id"] = idx
                chunk_metadata["total_chunks"] = len(nodes)
                
                chunk_doc = Document(
                    text=node.get_content(),
                    metadata=chunk_metadata
                )
                chunked_documents.append(chunk_doc)
        
        print(f"\n分块完成: {len(documents)} 个文档 -> {len(chunked_documents)} 个chunks")
        return chunked_documents
