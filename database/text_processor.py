"""
===================================
文本预处理模块
功能：处理原始文本数据,准备向量化
包含TSV文件处理、文本加载、分块等功能
===================================
"""

import json
import csv
import re
from pathlib import Path
from typing import List, Dict, Optional


class TextProcessor:
    """
    文本预处理器
    负责加载和处理原始文本数据
    """
    
    def __init__(self, data_dir: str = "./data/raw"):
        """
        初始化文本处理器
        
        Args:
            data_dir: 原始数据目录
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def clean_text(self, text: str) -> str:
        """
        清洗文本内容，提升存储效率和可读性
        
        清洗操作包括：
        - 去除HTML标签
        - 去除控制字符和特殊Unicode字符
        - 统一换行符为空格
        - 去除多余空格
        - 去除无意义符号组合
        - 去除引用标记
        - 修复常见编码错误
        - 规范化标点符号
        
        Args:
            text: 原始文本
            
        Returns:
            str: 清洗后的文本
        """
        if not text:
            return ""
        
        # 1. 去除HTML标签
        text = re.sub(r'<[^>]+>', '', text)
        
        # 2. 去除特殊Unicode字符和控制字符
        text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
        
        # 3. 统一换行符为空格
        text = re.sub(r'[\r\n]+', ' ', text)
        
        # 4. 去除多余的空格（包括tab）
        text = re.sub(r'\s+', ' ', text)
        
        # 5. 去除常见的无意义符号组合
        text = re.sub(r'[_]{3,}', '', text)  # 连续下划线
        text = re.sub(r'[-]{3,}', '', text)  # 连续破折号
        text = re.sub(r'[=]{3,}', '', text)  # 连续等号
        text = re.sub(r'[*]{3,}', '', text)  # 连续星号
        
        # 6. 去除特殊的引用标记
        text = re.sub(r'\[\d+\]', '', text)  # [1], [2] 等引用标记
        text = re.sub(r'\(\d+\)', '', text)  # (1), (2) 等引用标记
        
        # 7. 处理常见的编码错误字符
        replacements = {
            'â€™': "'",  # 右单引号
            'â€œ': '"',  # 左双引号
            'â€': '"',   # 右双引号
            'â€"': '-',  # 长破折号
            'â€"': '-',  # 短破折号
            'Â°': '°',   # 度数符号
            'Î±': 'α',   # alpha
            'Î²': 'β',   # beta
            'Î³': 'γ',   # gamma
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        # 8. 规范化标点符号周围的空格
        text = re.sub(r'\s*([,.;:!?])\s*', r'\1 ', text)
        
        # 9. 去除首尾空格
        text = text.strip()
        
        return text
    
    def load_text_files(self, file_pattern: str = "*.txt") -> List[Dict]:
        """
        加载文本文件
        
        Args:
            file_pattern: 文件匹配模式
        
        Returns:
            List[Dict]: 文档列表,每个文档包含text和metadata
        """
        documents = []
        
        for file_path in self.data_dir.glob(file_pattern):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read().strip()
                
                if text:
                    documents.append({
                        'text': text,
                        'metadata': {
                            'source': str(file_path.name),
                            'file_path': str(file_path)
                        }
                    })
                    print(f"✓ 加载文件: {file_path.name}")
            except Exception as e:
                print(f"✗ 加载文件失败 ({file_path.name}): {str(e)}")
        
        return documents
    
    def load_processed_chunks(self, file_pattern: str = "*chunks.txt") -> List[Dict]:
        """
        加载已处理的数据块文件（如processed目录下的文件）
        
        Args:
            file_pattern: 文件匹配模式
        
        Returns:
            List[Dict]: 文档列表
        """
        documents = []
        processed_dir = Path("./data/processed")
        
        if not processed_dir.exists():
            print(f"✗ processed目录不存在: {processed_dir}")
            return documents
        
        for file_path in processed_dir.glob(file_pattern):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # 按行读取，每行作为一个chunk
                    lines = f.readlines()
                    
                for idx, line in enumerate(lines):
                    text = line.strip()
                    if text:
                        documents.append({
                            'text': text,
                            'metadata': {
                                'source': str(file_path.name),
                                'file_path': str(file_path),
                                'line_number': idx + 1
                            }
                        })
                
                print(f"✓ 从文件加载 {len(lines)} 个chunks: {file_path.name}")
            except Exception as e:
                print(f"✗ 加载文件失败 ({file_path.name}): {str(e)}")
        
        return documents
    
    def load_json_data(self, json_file: str, text_field: str = 'text') -> List[Dict]:
        """
        从JSON文件加载数据
        
        Args:
            json_file: JSON文件路径
            text_field: 文本字段名
        
        Returns:
            List[Dict]: 文档列表
        """
        documents = []
        json_path = self.data_dir / json_file
        
        if not json_path.exists():
            print(f"✗ JSON文件不存在: {json_path}")
            return documents
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 处理JSON数组
            if isinstance(data, list):
                for idx, item in enumerate(data):
                    if isinstance(item, dict) and text_field in item:
                        text = str(item[text_field]).strip()
                        if text:
                            metadata = {k: v for k, v in item.items() if k != text_field}
                            metadata['source'] = json_file
                            metadata['item_id'] = idx
                            
                            documents.append({
                                'text': text,
                                'metadata': metadata
                            })
            # 处理单个JSON对象
            elif isinstance(data, dict) and text_field in data:
                text = str(data[text_field]).strip()
                if text:
                    metadata = {k: v for k, v in data.items() if k != text_field}
                    metadata['source'] = json_file
                    
                    documents.append({
                        'text': text,
                        'metadata': metadata
                    })
            
            print(f"✓ 从JSON加载 {len(documents)} 条数据: {json_file}")
        except Exception as e:
            print(f"✗ 加载JSON失败 ({json_file}): {str(e)}")
        
        return documents
    
    def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """
        将长文本分块
        
        Args:
            text: 输入文本
            chunk_size: 分块大小(字符数)
            overlap: 重叠大小
        
        Returns:
            List[str]: 文本块列表
        """
        if len(text) <= chunk_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap
        
        return chunks
    
    def process_documents(self, documents: List[Dict], enable_chunking: bool = False, 
                         chunk_size: int = 512, overlap: int = 50) -> List[Dict]:
        """
        处理文档列表(可选分块)
        
        Args:
            documents: 文档列表
            enable_chunking: 是否启用分块
            chunk_size: 分块大小
            overlap: 重叠大小
        
        Returns:
            List[Dict]: 处理后的文档列表
        """
        processed_docs = []
        
        for doc in documents:
            text = doc['text']
            metadata = doc['metadata']
            
            if enable_chunking and len(text) > chunk_size: #如果允许进行chunk操作且文本长度超过chunk_size则分块
                chunks = self.chunk_text(text, chunk_size, overlap)
                for idx, chunk in enumerate(chunks):
                    chunk_metadata = metadata.copy()
                    chunk_metadata['chunk_id'] = idx
                    chunk_metadata['total_chunks'] = len(chunks)
                    
                    processed_docs.append({
                        'text': chunk,
                        'metadata': chunk_metadata
                    })
            else:
                processed_docs.append(doc)
        
        return processed_docs
    
    def process_tsv_to_chunks(self, input_file: str, output_file: str) -> int:
        """
        从TSV文件中提取abstract列，添加索引并保存为txt文件
        
        Args:
            input_file: 输入的TSV文件路径
            output_file: 输出的TXT文件路径
            
        Returns:
            int: 提取的chunks数量
        """
        chunks = []
        original_count = 0
        cleaned_count = 0
        
        try:
            # 读取TSV文件
            with open(input_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='\t')
                
                # 检查是否有abstract列
                if 'abstract' not in reader.fieldnames:
                    print(f"✗ 警告: {input_file} 中没有找到 'abstract' 列")
                    print(f"  可用的列: {reader.fieldnames}")
                    return 0
                
                # 提取abstract内容并清洗
                for row in reader:
                    abstract = (row.get('abstract') or '').strip()  # 处理None情况
                    if abstract:
                        original_count += 1
                        # 清洗文本
                        cleaned_abstract = self.clean_text(abstract)
                        if cleaned_abstract:  # 只保存非空的清洗后文本
                            chunks.append(cleaned_abstract)
                            cleaned_count += 1
            
            # 写入txt文件，每行一个chunk，带索引
            with open(output_file, 'w', encoding='utf-8') as f:
                for idx, chunk in enumerate(chunks):
                    # 格式：索引\t内容
                    f.write(f"{idx}\t{chunk}\n")
            
            print(f"✓ 成功处理: {Path(input_file).name}")
            print(f"  原始abstracts: {original_count} 个")
            print(f"  清洗后保存: {cleaned_count} 个chunks")
            if original_count > cleaned_count:
                print(f"  已过滤: {original_count - cleaned_count} 个空内容")
            print(f"  保存至: {output_file}")
            
            return len(chunks)
            
        except FileNotFoundError:
            print(f"✗ 错误: 找不到文件 {input_file}")
            return 0
        except Exception as e:
            print(f"✗ 处理文件时出错: {e}")
            return 0
    
    def process_all_tsv_files(self, raw_dir: Optional[str] = None, 
                             processed_dir: str = "./data/processed") -> Dict[str, int]:
        """
        处理指定目录下的所有TSV文件
        
        Args:
            raw_dir: 原始数据目录 (如果为None，使用self.data_dir)
            processed_dir: 处理后数据目录
            
        Returns:
            Dict[str, int]: 每个文件的处理结果统计
        """
        # 使用指定目录或默认目录
        raw_path = Path(raw_dir) if raw_dir else self.data_dir
        processed_path = Path(processed_dir)
        
        if not raw_path.exists():
            print(f"✗ 错误: {raw_path} 目录不存在")
            return {}
        
        # 创建processed目录（如果不存在）
        processed_path.mkdir(parents=True, exist_ok=True)
        
        # 查找所有TSV文件
        tsv_files = list(raw_path.glob('*.tsv'))
        
        if not tsv_files:
            print(f"✗ 在 {raw_path} 目录下没有找到TSV文件")
            return {}
        
        print(f"\n找到 {len(tsv_files)} 个TSV文件")
        print("-" * 60)
        
        results = {}
        
        # 处理每个TSV文件
        for tsv_file in tsv_files:
            # 生成输出文件名：将.tsv替换为_chunks.txt
            output_filename = tsv_file.stem + '_chunks.txt'
            output_file = processed_path / output_filename
            
            print(f"\n处理文件: {tsv_file.name}")
            chunk_count = self.process_tsv_to_chunks(tsv_file, output_file)
            results[tsv_file.name] = chunk_count
        
        print("\n" + "=" * 60)
        print(f"所有文件处理完成! 共处理 {len(results)} 个TSV文件")
        print(f"总计提取 {sum(results.values())} 个chunks")
        
        return results


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    processor = TextProcessor("./data/raw")
    
    print("=" * 60)
    print("文本处理器 - 使用示例")
    print("=" * 60)
    
    # 示例1: 处理TSV文件
    print("\n【示例1】处理TSV文件，提取abstract列")
    print("-" * 60)
    results = processor.process_all_tsv_files()
    
    # 示例2: 加载处理后的chunks
    print("\n【示例2】加载处理后的chunks文件")
    print("-" * 60)
    documents = processor.load_processed_chunks("*chunks.txt")
    print(f"\n共加载 {len(documents)} 个文档chunks")
    
    # 示例3: 加载原始文本文件并分块
    print("\n【示例3】加载并处理原始文本文件")
    print("-" * 60)
    raw_docs = processor.load_text_files("*.txt")
    print(f"加载了 {len(raw_docs)} 个文档")
    
    if raw_docs:
        processed = processor.process_documents(raw_docs, enable_chunking=True, chunk_size=512)
        print(f"处理后共 {len(processed)} 个文档块")
