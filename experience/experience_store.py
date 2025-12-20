"""
===================================
经验存储模块
功能：管理辩论经验的存储、检索和更新
===================================
"""

import json
import os
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path


class ExperienceStore:
    """
    经验库管理类
    负责存储、检索和管理历史辩论经验
    """
    
    def __init__(
        self,
        storage_path: str,
        max_experiences: int = 1000,
        relevance_threshold: float = 0.8
    ):
        """
        初始化经验库
        
        Args:
            storage_path: 经验库存储路径
            max_experiences: 最大存储经验数量
            relevance_threshold: 经验相关性阈值
        """
        self.storage_path = Path(storage_path)
        self.max_experiences = max_experiences
        self.relevance_threshold = relevance_threshold
        
        # 确保存储目录存在
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 加载已有经验
        self.experiences = self._load_experiences()
        
        print(f"经验库初始化完成，当前包含 {len(self.experiences)} 条经验")
    
    def _load_experiences(self) -> List[Dict]:
        """
        从磁盘加载经验
        
        Returns:
            List[Dict]: 经验列表
        """
        if not self.storage_path.exists():
            print(f"经验库文件不存在，创建新的经验库: {self.storage_path}")
            return []
        
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                experiences = json.load(f)
            return experiences
        except json.JSONDecodeError:
            print("警告：经验库文件损坏，创建新的经验库")
            return []
        except Exception as e:
            print(f"加载经验库失败: {str(e)}")
            return []
    
    def _save_experiences(self) -> None:
        """保存经验到磁盘"""
        try:
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(self.experiences, f, ensure_ascii=False, indent=2)
            print(f"经验库已保存，共 {len(self.experiences)} 条经验")
        except Exception as e:
            print(f"保存经验库失败: {str(e)}")
    
    def add_experience(self, experience: Dict) -> None:
        """
        添加新经验
        
        Args:
            experience: 经验字典，应包含以下字段:
                - components: 化学组分列表
                - reaction_type: 反应类型
                - overpotential: 过电势
                - reasoning: 推理过程
                - debate_rounds: 辩论轮数
                - confidence: 置信度
        """
        # 添加时间戳和唯一ID
        experience['id'] = self._generate_experience_id()
        experience['timestamp'] = datetime.now().isoformat()
        
        # 添加到经验列表
        self.experiences.append(experience)
        
        # 如果超过最大容量，移除最旧的经验
        if len(self.experiences) > self.max_experiences:
            self.experiences = self.experiences[-self.max_experiences:]
            print(f"经验库已满，移除最旧的经验，当前保留 {len(self.experiences)} 条")
        
        # 保存到磁盘
        self._save_experiences()
        
        print(f"新经验已添加: {experience.get('reaction_type', '未知')} "
              f"(组分数: {len(experience.get('components', []))})")
    
    def _generate_experience_id(self) -> str:
        """
        生成经验的唯一ID
        
        Returns:
            str: 唯一ID
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        return f"exp_{timestamp}"
    
    def query_experiences(
        self,
        components: List[str],
        top_k: int = 3,
        min_similarity: Optional[float] = None
    ) -> List[Dict]:
        """
        查询相关经验
        
        Args:
            components: 化学组分列表
            top_k: 返回top-k个最相关的经验
            min_similarity: 最小相似度阈值（可选）
        
        Returns:
            List[Dict]: 相关经验列表
        """
        if not self.experiences:
            return []
        
        # 计算每个经验与查询的相似度
        scored_experiences = []
        for exp in self.experiences:
            similarity = self._calculate_similarity(
                components,
                exp.get('components', [])
            )
            
            # 应用相似度阈值
            threshold = min_similarity if min_similarity is not None else self.relevance_threshold
            if similarity >= threshold:
                exp_with_score = exp.copy()
                exp_with_score['similarity'] = similarity
                scored_experiences.append(exp_with_score)
        
        # 按相似度排序
        scored_experiences.sort(key=lambda x: x['similarity'], reverse=True)
        
        # 返回top-k结果
        return scored_experiences[:top_k]
    
    def _calculate_similarity(
        self,
        components1: List[str],
        components2: List[str]
    ) -> float:
        """
        计算两个组分列表的相似度
        使用Jaccard相似度（可以替换为更复杂的方法）
        
        Args:
            components1: 组分列表1
            components2: 组分列表2
        
        Returns:
            float: 相似度（0-1）
        """
        # 转换为集合
        set1 = set(c.lower() for c in components1)
        set2 = set(c.lower() for c in components2)
        
        # 计算Jaccard相似度
        if not set1 and not set2:
            return 1.0
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        return intersection / union if union > 0 else 0.0
    
    def get_statistics(self) -> Dict:
        """
        获取经验库统计信息
        
        Returns:
            Dict: 统计信息
        """
        if not self.experiences:
            return {
                "total_experiences": 0,
                "reaction_type_distribution": {},
                "avg_debate_rounds": 0,
                "avg_overpotential": 0
            }
        
        # 统计反应类型分布
        reaction_counts = {}
        for exp in self.experiences:
            reaction = exp.get('reaction_type', '未知')
            reaction_counts[reaction] = reaction_counts.get(reaction, 0) + 1
        
        # 计算平均辩论轮数
        rounds = [exp.get('debate_rounds', 0) for exp in self.experiences]
        avg_rounds = sum(rounds) / len(rounds) if rounds else 0
        
        # 计算平均过电势
        potentials = [
            exp.get('overpotential', 0) for exp in self.experiences
            if exp.get('overpotential') is not None
        ]
        avg_potential = sum(potentials) / len(potentials) if potentials else 0
        
        return {
            "total_experiences": len(self.experiences),
            "reaction_type_distribution": reaction_counts,
            "avg_debate_rounds": round(avg_rounds, 2),
            "avg_overpotential": round(avg_potential, 4)
        }
    
    def search_by_reaction_type(self, reaction_type: str) -> List[Dict]:
        """
        按反应类型搜索经验
        
        Args:
            reaction_type: 反应类型
        
        Returns:
            List[Dict]: 匹配的经验列表
        """
        return [
            exp for exp in self.experiences
            if exp.get('reaction_type') == reaction_type
        ]
    
    def delete_experience(self, experience_id: str) -> bool:
        """
        删除指定经验
        
        Args:
            experience_id: 经验ID
        
        Returns:
            bool: 是否删除成功
        """
        initial_count = len(self.experiences)
        self.experiences = [
            exp for exp in self.experiences
            if exp.get('id') != experience_id
        ]
        
        if len(self.experiences) < initial_count:
            self._save_experiences()
            print(f"经验 {experience_id} 已删除")
            return True
        else:
            print(f"未找到经验 {experience_id}")
            return False
    
    def clear_all(self) -> None:
        """
        清空所有经验
        警告：此操作不可逆
        """
        self.experiences = []
        self._save_experiences()
        print("所有经验已清空")
    
    def export_to_file(self, export_path: str) -> None:
        """
        导出经验库到文件
        
        Args:
            export_path: 导出文件路径
        """
        try:
            with open(export_path, 'w', encoding='utf-8') as f:
                json.dump(self.experiences, f, ensure_ascii=False, indent=2)
            print(f"经验库已导出到: {export_path}")
        except Exception as e:
            print(f"导出失败: {str(e)}")
    
    def import_from_file(self, import_path: str, merge: bool = True) -> None:
        """
        从文件导入经验
        
        Args:
            import_path: 导入文件路径
            merge: 是否合并到现有经验（True）还是替换（False）
        """
        try:
            with open(import_path, 'r', encoding='utf-8') as f:
                imported_experiences = json.load(f)
            
            if merge:
                self.experiences.extend(imported_experiences)
            else:
                self.experiences = imported_experiences
            
            # 限制最大数量
            if len(self.experiences) > self.max_experiences:
                self.experiences = self.experiences[-self.max_experiences:]
            
            self._save_experiences()
            print(f"成功导入 {len(imported_experiences)} 条经验")
            
        except Exception as e:
            print(f"导入失败: {str(e)}")


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    # 初始化经验库
    store = ExperienceStore(
        storage_path="./data/experience_db.json",
        max_experiences=1000
    )
    
    # 添加测试经验
    test_experience = {
        "components": ["硫酸", "氢氧化钠", "氯化钠", "硝酸", "碳酸钙"],
        "reaction_type": "氧化还原反应",
        "overpotential": 0.45,
        "reasoning": "基于组分的氧化还原特性...",
        "debate_rounds": 3,
        "confidence": 0.9
    }
    
    store.add_experience(test_experience)
    
    # 查询相关经验
    results = store.query_experiences(
        components=["硫酸", "氢氧化钠", "氯化钠"],
        top_k=3
    )
    
    print(f"\n查询结果: {len(results)} 条相关经验")
    for exp in results:
        print(f"  - {exp['reaction_type']} (相似度: {exp['similarity']:.2f})")
    
    # 打印统计信息
    stats = store.get_statistics()
    print(f"\n经验库统计:")
    print(f"  总经验数: {stats['total_experiences']}")
    print(f"  平均辩论轮数: {stats['avg_debate_rounds']}")
