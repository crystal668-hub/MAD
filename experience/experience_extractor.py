"""
===================================
经验提取模块
功能：从辩论结果中提取结构化经验
===================================
"""

from typing import Dict, List, Optional
from debate.autogen_coordinator import DebateResult


class ExperienceExtractor:
    """
    经验提取器
    负责从辩论结果中提取和结构化经验
    """
    
    def __init__(self):
        """初始化经验提取器"""
        pass
    
    def extract_from_debate(
        self,
        debate_result: DebateResult,
        components: List[str],
        additional_info: Optional[Dict] = None
    ) -> Dict:
        """
        从辩论结果提取经验
        
        Args:
            debate_result: 辩论结果
            components: 化学组分列表
            additional_info: 额外信息（可选）
        
        Returns:
            Dict: 结构化的经验字典
        """
        # 基本信息
        experience = {
            "components": components,
            "reaction_type": debate_result.final_reaction_type,
            "overpotential": debate_result.final_overpotential,
            "reasoning": debate_result.reasoning_trajectory,
            "debate_rounds": debate_result.debate_rounds,
            "consensus_reached": debate_result.consensus_reached,
            "time_elapsed": debate_result.time_elapsed
        }
        
        # 提取置信度（基于辩论轮数和是否达成共识）
        experience["confidence"] = self._calculate_confidence(debate_result)
        
        # 提取关键论据
        experience["key_arguments"] = self._extract_key_arguments(debate_result)
        
        # 提取参与agent信息
        experience["agents_involved"] = self._extract_agents_info(debate_result)
        
        # 添加额外信息
        if additional_info:
            experience.update(additional_info)
        
        return experience
    
    def _calculate_confidence(self, debate_result: DebateResult) -> float:
        """
        计算经验的置信度
        
        Args:
            debate_result: 辩论结果
        
        Returns:
            float: 置信度（0-1）
        """
        # 基础置信度
        base_confidence = 0.5
        
        # 如果达成共识，增加置信度
        if debate_result.consensus_reached:
            base_confidence += 0.3
        
        # 辩论轮数越少，置信度越高（说明共识容易达成）
        if debate_result.debate_rounds <= 3:
            base_confidence += 0.2
        elif debate_result.debate_rounds <= 5:
            base_confidence += 0.1
        
        # 确保在0-1范围内
        confidence = min(max(base_confidence, 0.0), 1.0)
        
        return round(confidence, 2)
    
    def _extract_key_arguments(self, debate_result: DebateResult) -> List[str]:
        """
        提取关键论据
        
        Args:
            debate_result: 辩论结果
        
        Returns:
            List[str]: 关键论据列表
        """
        key_arguments = []
        
        # 从辩论历史中提取（简化版：提取包含特定关键词的语句）
        keywords = ["因为", "由于", "根据", "证据", "表明", "说明", "支持", "反对"]
        
        for record in debate_result.debate_history:
            content = record.get('content', '')
            
            # 提取包含关键词的句子
            for keyword in keywords:
                if keyword in content:
                    # 简单提取：找到关键词前后的文本
                    idx = content.find(keyword)
                    if idx != -1:
                        # 提取该句子（简化：前后各50字符）
                        start = max(0, idx - 50)
                        end = min(len(content), idx + 150)
                        argument = content[start:end].strip()
                        
                        if argument and len(argument) > 20:
                            key_arguments.append(argument)
                            break  # 每条记录只提取一个论据
        
        # 去重并限制数量
        key_arguments = list(set(key_arguments))[:5]
        
        return key_arguments
    
    def _extract_agents_info(self, debate_result: DebateResult) -> List[Dict]:
        """
        提取参与Agent的信息
        
        Args:
            debate_result: 辩论结果
        
        Returns:
            List[Dict]: Agent信息列表
        """
        agents_info = {}
        
        for record in debate_result.debate_history:
            agent_name = record.get('agent', 'Unknown')
            
            if agent_name not in agents_info:
                agents_info[agent_name] = {
                    "name": agent_name,
                    "total_messages": 0,
                    "positions": []
                }
            
            agents_info[agent_name]["total_messages"] += 1
            
            # 记录该agent的立场
            reaction = record.get('reaction_type')
            if reaction:
                agents_info[agent_name]["positions"].append(reaction)
        
        # 统计每个agent的最终立场
        for agent in agents_info.values():
            if agent["positions"]:
                # 取最后一次的立场作为最终立场
                agent["final_position"] = agent["positions"][-1]
                # 统计立场变化次数
                agent["position_changes"] = len(set(agent["positions"])) - 1
            else:
                agent["final_position"] = "未明确"
                agent["position_changes"] = 0
        
        return list(agents_info.values())
    
    def format_experience_summary(self, experience: Dict) -> str:
        """
        Format experience summary (for display)
        
        Args:
            experience: Experience dictionary
        
        Returns:
            str: Formatted summary text
        """
        summary_parts = [
            "=" * 60,
            "Experience Summary",
            "=" * 60,
            "",
            f"**Metal Catalyst Elements**: {', '.join(experience.get('components', []))}",
            f"**Reaction Type**: {experience.get('reaction_type', 'Unknown')}",
            f"**Overpotential**: {experience.get('overpotential', 'Not Estimated')}",
            f"**Confidence**: {experience.get('confidence', 0):.2f}",
            f"**Debate Rounds**: {experience.get('debate_rounds', 0)}",
            f"**Consensus Reached**: {'Yes' if experience.get('consensus_reached') else 'No'}",
            "",
            "**Key Arguments**:"
        ]
        
        # Add key arguments
        for i, arg in enumerate(experience.get('key_arguments', []), 1):
            summary_parts.append(f"{i}. {arg}")
        
        # 添加Agent信息
        summary_parts.append("")
        summary_parts.append("**参与Agent**:")
        for agent in experience.get('agents_involved', []):
            summary_parts.append(
                f"  - {agent['name']}: {agent['final_position']} "
                f"(立场变化{agent['position_changes']}次)"
            )
        
        summary_parts.append("")
        summary_parts.append("=" * 60)
        
        return "\n".join(summary_parts)
    
    def validate_experience(self, experience: Dict) -> tuple[bool, str]:
        """
        验证经验的完整性和有效性
        
        Args:
            experience: 经验字典
        
        Returns:
            tuple: (是否有效, 错误信息)
        """
        # 必需字段
        required_fields = [
            "components",
            "reaction_type",
            "reasoning",
            "debate_rounds",
            "consensus_reached"
        ]
        
        # 检查必需字段
        for field in required_fields:
            if field not in experience:
                return False, f"缺少必需字段: {field}"
            
            # 检查字段值的有效性
            value = experience[field]
            
            if field == "components":
                if not isinstance(value, list) or len(value) == 0:
                    return False, "components必须是非空列表"
            
            elif field == "reaction_type":
                if not value or value == "未知":
                    return False, "reaction_type不能为空或未知"
            
            elif field == "debate_rounds":
                if not isinstance(value, int) or value <= 0:
                    return False, "debate_rounds必须是正整数"
        
        # 所有检查通过
        return True, "经验有效"
    
    def merge_similar_experiences(
        self,
        experiences: List[Dict],
        similarity_threshold: float = 0.9
    ) -> List[Dict]:
        """
        合并相似的经验
        
        Args:
            experiences: 经验列表
            similarity_threshold: 相似度阈值
        
        Returns:
            List[Dict]: 合并后的经验列表
        """
        # 简化实现：基于组分和反应类型进行合并
        merged = []
        used_indices = set()
        
        for i, exp1 in enumerate(experiences):
            if i in used_indices:
                continue
            
            similar_group = [exp1]
            
            for j, exp2 in enumerate(experiences[i+1:], start=i+1):
                if j in used_indices:
                    continue
                
                # 检查相似度
                if self._are_experiences_similar(exp1, exp2, similarity_threshold):
                    similar_group.append(exp2)
                    used_indices.add(j)
            
            # 合并相似经验
            if len(similar_group) > 1:
                merged_exp = self._merge_experience_group(similar_group)
                merged.append(merged_exp)
            else:
                merged.append(exp1)
        
        return merged
    
    def _are_experiences_similar(
        self,
        exp1: Dict,
        exp2: Dict,
        threshold: float
    ) -> bool:
        """
        判断两个经验是否相似
        
        Args:
            exp1: 经验1
            exp2: 经验2
            threshold: 相似度阈值
        
        Returns:
            bool: 是否相似
        """
        # 反应类型必须相同
        if exp1.get('reaction_type') != exp2.get('reaction_type'):
            return False
        
        # 计算组分的相似度（使用Jaccard相似度）
        components1 = set(exp1.get('components', []))
        components2 = set(exp2.get('components', []))
        
        intersection = len(components1 & components2)
        union = len(components1 | components2)
        
        similarity = intersection / union if union > 0 else 0
        
        return similarity >= threshold
    
    def _merge_experience_group(self, group: List[Dict]) -> Dict:
        """
        合并一组相似经验
        
        Args:
            group: 相似经验组
        
        Returns:
            Dict: 合并后的经验
        """
        # 使用第一个经验作为基础
        merged = group[0].copy()
        
        # 合并组分（取并集）
        all_components = set()
        for exp in group:
            all_components.update(exp.get('components', []))
        merged['components'] = list(all_components)
        
        # 平均过电势
        potentials = [
            exp.get('overpotential') for exp in group
            if exp.get('overpotential') is not None
        ]
        if potentials:
            merged['overpotential'] = sum(potentials) / len(potentials)
        
        # 平均置信度
        confidences = [exp.get('confidence', 0.5) for exp in group]
        merged['confidence'] = sum(confidences) / len(confidences)
        
        # 标记为合并经验
        merged['merged_count'] = len(group)
        
        return merged


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    from debate.autogen_coordinator import DebateResult
    
    # 创建模拟辩论结果
    mock_result = DebateResult(
        consensus_reached=True,
        final_reaction_type="氧化还原反应",
        final_overpotential=0.45,
        reasoning_trajectory="详细的推理过程...",
        debate_rounds=3,
        debate_history=[
            {
                "round": 1,
                "agent": "GPT-4 Agent",
                "content": "根据文献证据，氧化还原反应最合适",
                "reaction_type": "氧化还原反应"
            }
        ],
        time_elapsed=120.5
    )
    
    # 提取经验
    extractor = ExperienceExtractor()
    experience = extractor.extract_from_debate(
        mock_result,
        components=["硫酸", "氢氧化钠", "氯化钠", "硝酸", "碳酸钙"]
    )
    
    # 打印摘要
    summary = extractor.format_experience_summary(experience)
    print(summary)
    
    # 验证经验
    is_valid, message = extractor.validate_experience(experience)
    print(f"\n经验验证: {message}")
