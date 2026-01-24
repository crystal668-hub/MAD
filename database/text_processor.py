"""
===================================
文本预处理模块
功能：处理原始文本数据,准备向量化
包含文本加载、分块等功能
支持LlamaIndex解析Markdown文件
===================================
"""

import csv
import re
from difflib import SequenceMatcher
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter, MarkdownNodeParser
from llama_index.core.ingestion import IngestionPipeline
from utils.logger import Logger

db_log_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
db_log_file = Path("./logs/db_log") / f"text_processor_{db_log_timestamp}.log"
logger = Logger.get_logger(
    name=f"MAD.DB.TextProcessor.{db_log_timestamp}",
    log_file=str(db_log_file),
    level="INFO"
)


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
        self._metadata_index = None
    
    def clean_text(self, text: str) -> str:
        """
        清洗文本内容，删除Acknowledgement和Reference部分
        
        清洗操作：
        - 删除Acknowledgement部分及其后的所有内容
        - 删除Reference/References部分及其后的所有内容
        - 若无Reference标题，尝试移除末尾参考文献列表（启发式）
        
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

        # 若无Reference标题，尝试识别并删除末尾参考文献列表
        # 典型格式：
        # [1] Author, ... 2021 ...
        # 1. Author, ... 2021 ...
        # 1) Author, ... 2021 ...
        def _is_reference_line(line: str) -> bool:
            stripped = line.strip()
            if not stripped:
                return False
            if re.search(r'^\[\d+\]\s+\S', stripped):
                return True
            if re.search(r'^\d{1,3}[\.)]\s+\S', stripped):
                return True
            if re.search(r'\bdoi\b', stripped, re.IGNORECASE):
                return True
            if re.search(r'\b(19|20)\d{2}[a-z]?\b', stripped):
                if stripped.count(',') >= 2 or stripped.count('.') >= 2:
                    return True
            return False

        lines = text.splitlines()
        end_index = len(lines) - 1
        while end_index >= 0 and not lines[end_index].strip():
            end_index -= 1

        if end_index > 0:
            ref_lines = 0
            block_start = None
            for i in range(end_index, -1, -1):
                line = lines[i]
                if not line.strip():
                    if ref_lines > 0:
                        block_start = i
                    continue
                if _is_reference_line(line):
                    ref_lines += 1
                    block_start = i
                else:
                    if ref_lines >= 3:
                        break
                    ref_lines = 0
                    block_start = None

            if ref_lines >= 3 and block_start is not None:
                text = "\n".join(lines[:block_start]).rstrip()
        
        return text
    
    def _normalize_title(self, text: str) -> str:
        normalized = text.strip().lower()
        # 移除HTML标签（如 <sub>2</sub>, <sup>+</sup> 等）
        normalized = re.sub(r"<[^>]+>", "", normalized)
        # 移除括号和方括号内容
        normalized = re.sub(r"\(.*?\)|\[.*?\]|\{.*?\}", " ", normalized)
        # 移除年份
        normalized = re.sub(r"\b(19|20)\d{2}\b", " ", normalized)
        normalized = re.sub(r"\s+", " ", normalized)
        normalized = re.sub(r"[^0-9a-z\u4e00-\u9fff ]+", " ", normalized)
        normalized = re.sub(r"\s+", " ", normalized).strip()
        return normalized

    def _normalize_author(self, text: str) -> str:
        if not text:
            return ""
        author = text.split(",")[0]
        author = re.sub(r"[^a-zA-Z\u4e00-\u9fff]+", "", author).lower()
        return author

    def _extract_year_from_text(self, text: str) -> Optional[str]:
        match = re.search(r"\b(19|20)\d{2}\b", text)
        return match.group(0) if match else None

    def _extract_author_from_filename(self, filename: str) -> str:
        stem = Path(filename).stem
        parts = re.split(r"\s*[-–—]\s*", stem, maxsplit=1)
        author_part = parts[0] if parts else ""
        author_part = author_part.split("等")[0]
        author_part = author_part.split("et al")[0]
        return self._normalize_author(author_part)

    def _build_title_variants(self, title: str) -> List[str]:
        variants = [title]
        if ":" in title:
            variants.append(title.split(":", 1)[0].strip())
        if " - " in title:
            variants.append(title.split(" - ", 1)[0].strip())
        if " – " in title:
            variants.append(title.split(" – ", 1)[0].strip())
        if " — " in title:
            variants.append(title.split(" — ", 1)[0].strip())
        return [v for v in variants if v]

    def _extract_title_candidates(self, content: str, filename: str = "") -> List[str]:
        candidates = []
        
        # Priority 1: Filename title (most reliable for this dataset)
        # Format: "Author - Year - Title.md" or "Author等 - Year - Title.md"
        if filename:
            stem = Path(filename).stem
            # Split by " - " and extract the part after year
            parts = re.split(r'\s*[-–—]\s*', stem)
            
            title_part = None
            if len(parts) >= 3:
                # Try to find year part (4-digit number)
                for i, part in enumerate(parts):
                    if re.match(r'^\d{4}$', part.strip()):
                        # Everything after year is title
                        if i + 1 < len(parts):
                            title_part = ' - '.join(parts[i+1:])
                        break
            
            # Fallback: if no year found, use the whole stem
            if not title_part:
                title_part = stem
                # Remove common author patterns
                title_part = re.sub(r'^.+?等\s*[-–—]\s*\d{4}\s*[-–—]\s*', '', title_part)
                title_part = re.sub(r'^.+?\s*[-–—]\s*\d{4}\s*[-–—]\s*', '', title_part)
            
            if title_part and title_part.strip():
                candidates.extend(self._build_title_variants(title_part.strip()))
        
        # Priority 2: Content-based extraction as additional candidates
        if content:
            lines = content.splitlines()
            
            # Pattern A: **Title:** marker (common in published papers)
            found_title_marker = False
            for i, line in enumerate(lines[:50]):
                if re.search(r'\*\*Title:\*\*', line, re.IGNORECASE):
                    title = re.sub(r'\*\*Title:\*\*\s*', '', line, flags=re.IGNORECASE).strip()
                    title = re.sub(r'^\*\*|\*\*$', '', title).strip()
                    if title and len(title) > 15:
                        candidates.extend(self._build_title_variants(title))
                        found_title_marker = True
                        break
            
            # Pattern B: # title (最重要的内容标题,skip metadata headers)
            if not found_title_marker:  # Only if no **Title:** found
                skip_patterns = [
                    r'^accepted\s+article',
                    r'^research\s+article',
                    r'^original\s+article',
                    r'^review\s+article',
                    r'^\d+\.?\s*introduction',
                    r'^chemnanomat',
                    r'^received:',
                    r'^www\.',
                    r'^\d+\.\s+introduction',
                    r'^protective\s+immune',
                    r'^dalton\s+transactions?',
                    r'^inorganic\s+chemistry',
                    r'^.*?\s+frontiers?$',
                    r'^ecs\s+transactions?',
                    r'^advanced\s+(materials?|energy)',
                    r'^journal\s+of',
                    r'^nature\s+(chemistry|materials?|communications?)',
                    r'^angewandte\s+chemie',
                ]
                for line in lines[:50]:
                    stripped = line.strip()
                    if stripped.startswith("#"):
                        title = stripped.lstrip("# ").strip()
                        # Remove markdown formatting (**, *, etc.)
                        title = re.sub(r'^\*+|\*+$', '', title).strip()
                        title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title)  # Remove **text**
                        if title and len(title) > 15:
                            is_metadata = any(re.match(pat, title, re.IGNORECASE) for pat in skip_patterns)
                            if not is_metadata:
                                candidates.extend(self._build_title_variants(title))
                                break
            
            # Pattern C: Bold/italic text with keywords (lowest priority, skip journal headers)
            if len(candidates) <= 1:  # Only if filename extraction failed or too short
                for i in range(min(7, len(lines)), min(35, len(lines))):
                    line = lines[i].strip()
                    if re.search(r'\*\*[^\n]+\*\*', line) and not line.startswith('#'):
                        title = re.sub(r'\*+', ' ', line).strip()
                        title = re.sub(r'\s+', ' ', title)
                        if len(title) > 15:
                            skip_bold = [r'^(Abstract|Received|DOI|Introduction|Correspondence|Funding|Keywords)$', 
                                        r'^www\.', r'^Nanocrystals$', r'^\d+\s*$', r'^ECS Transactions',
                                        r'^\w+\s+Chemistry', r'^\w+\s+Materials']
                            is_skip = any(re.match(pat, title, re.IGNORECASE) for pat in skip_bold)
                            has_keywords = any(kw in title.lower() for kw in 
                                             ['catalyst', 'electro', 'oxidation', 'fuel', 'nanop', 'metal', 
                                              'reaction', 'interface', 'synthesis', 'performance', 'activity'])
                            if not is_skip and (has_keywords or len(title) > 40):
                                candidates.extend(self._build_title_variants(title))
                                break
        
        seen = set()
        deduped = []
        for candidate in candidates:
            if candidate not in seen:
                seen.add(candidate)
                deduped.append(candidate)
        return deduped

    def _get_reaction_key_from_path(self, file_path: str) -> Optional[str]:
        if not file_path:
            return None
        parts = [p.upper() for p in Path(file_path).parts]
        reaction_types = {"CO2RR", "EOR", "HER", "HOR", "HZOR", "O5H", "OER", "ORR", "UOR"}
        for part in parts:
            if part in reaction_types:
                return part.lower()
        return None

    def _load_metadata_index(self) -> Dict[str, Dict[str, Dict[str, str]]]:
        if self._metadata_index is not None:
            return self._metadata_index

        index: Dict[str, Dict[str, Dict[str, str]]] = {}
        metadata_dir = Path("./metadata")
        if not metadata_dir.exists():
            self._metadata_index = index
            return index

        for csv_path in metadata_dir.glob("*.csv"):
            reaction_key = csv_path.stem.lower()
            index[reaction_key] = {}
            try:
                with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
                    reader = csv.DictReader(handle)
                    for row in reader:
                        title = (row.get("Title") or "").strip()
                        doi = (row.get("DOI") or "").strip()
                        year = (row.get("Publication Year") or "").strip()
                        author = (row.get("Author") or "").strip()
                        if not title or not doi:
                            continue
                        normalized_title = self._normalize_title(title)
                        if normalized_title:
                            index[reaction_key][normalized_title] = {
                                "doi": doi,
                                "year": year,
                                "author": self._normalize_author(author)
                            }
            except Exception as exc:
                logger.error(f"✗ 读取元数据失败: {csv_path} - {exc}")

        self._metadata_index = index
        return index

    def _find_best_similarity_match(
        self,
        candidate: str,
        reaction_map: Dict[str, Dict[str, str]],
        year: Optional[str],
        author: str
    ) -> Optional[str]:
        best_score = 0.0
        best_doi = None
        
        # Extract first 5-8 significant words for prefix matching
        candidate_words = [w for w in candidate.split() if len(w) > 2][:8]
        candidate_prefix = ' '.join(candidate_words[:5]) if len(candidate_words) >= 5 else candidate
        
        for title_key, meta in reaction_map.items():
            # Skip year/author mismatch if hints available
            if year and meta.get("year") and meta.get("year") != year:
                continue
            if author and meta.get("author") and author not in meta.get("author"):
                continue
            
            # Strategy 1: Full similarity match
            ratio = SequenceMatcher(None, candidate, title_key).ratio()
            
            # Strategy 2: Prefix match (for truncated filenames)
            if len(candidate_words) >= 4:
                title_words = [w for w in title_key.split() if len(w) > 2]
                title_prefix = ' '.join(title_words[:5]) if len(title_words) >= 5 else title_key
                prefix_ratio = SequenceMatcher(None, candidate_prefix, title_prefix).ratio()
                # Boost score if prefix matches well
                if prefix_ratio > 0.85:
                    ratio = max(ratio, prefix_ratio * 0.95)
            
            if ratio > best_score:
                best_score = ratio
                best_doi = meta.get("doi")
        
        # Lower threshold for better recall with prefix matching
        if best_score >= 0.75:
            return best_doi
        return None

    def extract_doi_from_content(self, content: str, filename: str = "", file_path: str = "") -> str:
        """
        从外部CSV元数据中查找并返回DOI
        
        Args:
            content: 文本内容
            filename: 文件名
            file_path: 文件路径
            
        Returns:
            str: DOI，如果未找到则返回"unknown"
        """
        index = self._load_metadata_index()
        if not index:
            return "unknown"

        reaction_key = self._get_reaction_key_from_path(file_path)
        candidates = self._extract_title_candidates(content, filename)
        normalized_candidates = [self._normalize_title(c) for c in candidates]
        year_hint = self._extract_year_from_text(filename)
        author_hint = self._extract_author_from_filename(filename) if filename else ""

        if reaction_key and reaction_key in index:
            for candidate in normalized_candidates:
                meta = index[reaction_key].get(candidate)
                if meta and meta.get("doi"):
                    return meta["doi"]
            for candidate in normalized_candidates:
                doi = self._find_best_similarity_match(candidate, index[reaction_key], year_hint, author_hint)
                if doi:
                    return doi

        for reaction_map in index.values():
            for candidate in normalized_candidates:
                meta = reaction_map.get(candidate)
                if meta and meta.get("doi"):
                    return meta["doi"]
            for candidate in normalized_candidates:
                doi = self._find_best_similarity_match(candidate, reaction_map, year_hint, author_hint)
                if doi:
                    return doi

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
                - reaction_type: 所属反应类型
                - doc_id: 文献DOI号
        """
        data_path = Path(data_dir)
        if not data_path.exists():
            logger.error(f"✗ 目录不存在: {data_dir}")
            return []
        
        try:
            reader = SimpleDirectoryReader(
                input_dir=str(data_path),
                required_exts=[".md"],  
                recursive=False  
            )
            documents = reader.load_data()
            
            if not documents:
                logger.error(f"✗ 未找到任何Markdown文件: {data_dir}")
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
                doc_id = self.extract_doi_from_content(doc.text, file_name, file_path_str)
                
                # 重置metadata，只包含reaction_type和doc_id
                doc.metadata = {
                    "reaction_type": inferred_reaction or "unknown",
                    "doc_id": doc_id
                }
                
                processed_documents.append(doc)
                
                logger.info(f"✓ 加载 {file_name}")
                logger.info(f"  反应类型: {doc.metadata['reaction_type']}")
                logger.info(f"  DOI: {doc.metadata['doc_id']}")
            
            logger.info(f"\n共加载 {len(processed_documents)} 个Document对象")
            return processed_documents
            
        except Exception as e:
            logger.error(f"✗ 加载文档失败: {str(e)}")
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
            
            logger.info(f"\n--- 加载 {reaction_type} ---")
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
        使用 “两级切分策略” 对Document对象进行分块
        
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
                markdown_parser,      
                sentence_splitter     
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
        
        logger.info(f"\n分块完成: {len(documents)} 个文档 -> {len(chunked_documents)} 个chunks")
        return chunked_documents
