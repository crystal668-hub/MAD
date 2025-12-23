"""
处理TSV文件，提取abstract列并添加索引保存为txt文件
"""
import os
import csv
from pathlib import Path


def process_tsv_to_chunks(input_file, output_file):
    """
    从TSV文件中提取abstract列，添加索引并保存为txt文件
    
    Args:
        input_file: 输入的TSV文件路径
        output_file: 输出的TXT文件路径
    """
    chunks = []
    
    try:
        # 读取TSV文件
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            
            # 检查是否有abstract列
            if 'abstract' not in reader.fieldnames:
                print(f"警告: {input_file} 中没有找到 'abstract' 列")
                print(f"可用的列: {reader.fieldnames}")
                return
            
            # 提取abstract内容
            for row in reader:
                abstract = (row.get('abstract') or '').strip()  # 处理None情况
                if abstract:  # 只保存非空的abstract
                    chunks.append(abstract)
        
        # 写入txt文件，每行一个chunk，带索引
        with open(output_file, 'w', encoding='utf-8') as f:
            for idx, chunk in enumerate(chunks):
                # 格式：索引\t内容
                f.write(f"{idx}\t{chunk}\n")
        
        print(f"成功处理: {input_file}")
        print(f"提取了 {len(chunks)} 个chunks")
        print(f"保存至: {output_file}")
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {input_file}")
    except Exception as e:
        print(f"处理文件时出错: {e}")


def process_all_tsv_files(raw_dir='data/raw', processed_dir='data/processed'):
    """
    处理raw目录下的所有TSV文件
    
    Args:
        raw_dir: 原始数据目录
        processed_dir: 处理后数据目录
    """
    # 确保目录存在
    raw_path = Path(raw_dir)
    processed_path = Path(processed_dir)
    
    if not raw_path.exists():
        print(f"错误: {raw_dir} 目录不存在")
        return
    
    # 创建processed目录（如果不存在）
    processed_path.mkdir(parents=True, exist_ok=True)
    
    # 查找所有TSV文件
    tsv_files = list(raw_path.glob('*.tsv'))
    
    if not tsv_files:
        print(f"在 {raw_dir} 目录下没有找到TSV文件")
        return
    
    print(f"找到 {len(tsv_files)} 个TSV文件")
    print("-" * 60)
    
    # 处理每个TSV文件
    for tsv_file in tsv_files:
        # 生成输出文件名：将.tsv替换为_chunks.txt
        output_filename = tsv_file.stem + '_chunks.txt'
        output_file = processed_path / output_filename
        
        print(f"\n处理文件: {tsv_file.name}")
        process_tsv_to_chunks(tsv_file, output_file)
    
    print("\n" + "=" * 60)
    print("所有文件处理完成!")


def main():
    """
    主函数
    可以选择处理单个文件或所有文件
    """
    print("=" * 60)
    print("TSV文件Abstract提取工具")
    print("=" * 60)
    
    # 处理所有TSV文件
    process_all_tsv_files()


if __name__ == '__main__':
    main()
