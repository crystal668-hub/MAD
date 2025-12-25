"""
===================================
Multi-Agent Metal Catalyst Overpotential Prediction System - Main Program
===================================

Functionality:
1. Initialize system components (RAG, Agents, experience store, etc.)
2. Execute multi-agent debate
3. Extract and save experience
4. Generate result reports

Version: 1.0.0
===================================
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 导入项目模块
from utils import (
    load_config,
    setup_logging,
    DebateLogger,
    parse_component_string,
    validate_components,
    print_header,
    print_section,
    dict_to_table,
    format_duration,
    save_json,
    ensure_dir
)
from database import RAGSystem
from agents import AgentConfig
from debate.autogen_coordinator import AutoGenDebateCoordinator
from experience import ExperienceStore, ExperienceExtractor


class MADSystem:
    """
    Multi-Agent Debate System Main Class
    Integrates all components and provides a unified interface for running the system.
    Analyzes metal catalyst elements to predict reaction types with lowest overpotential.
    """
    
    def __init__(self, config_path: str = "./config/config.yaml"):
        """
        初始化系统
        
        Args:
            config_path: 配置文件路径
        """
        print_header("Multi-Agent Metal Catalyst Overpotential Prediction System")
        print("Initializing system...")
        
        # 加载配置
        self.config = load_config(config_path)
        
        # 初始化日志
        self.logger = setup_logging(self.config)
        self.logger.info("系统初始化开始")
        
        # 初始化各个组件
        self.rag_systems = {}
        self.agents = []
        self.experience_store = None
        self.debate_coordinator = None
        
        # 初始化标志
        self._initialized = False
    
    def initialize(self, skip_rag: bool = False) -> None:
        """
        初始化所有系统组件
        
        Args:
            skip_rag: 是否跳过RAG系统初始化（用于快速测试）
        """
        if self._initialized:
            self.logger.warning("系统已经初始化，跳过重复初始化")
            return
        
        try:
            # 1. 初始化经验库
            self._init_experience_store()
            
            # 2. 初始化RAG系统（可选）
            if not skip_rag:
                self._init_rag_systems()
            else:
                self.logger.info("跳过RAG系统初始化")
            
            # 3. 初始化Agents
            self._init_agents()
            
            # 4. 初始化AutoGen辩论协调器
            self._init_debate_coordinator()
            
            self._initialized = True
            self.logger.info("系统初始化完成")
            print("\n✓ 系统初始化成功\n")
            
        except Exception as e:
            self.logger.error(f"系统初始化失败: {str(e)}", exc_info=True)
            print(f"\n✗ 系统初始化失败: {str(e)}\n")
            raise
    
    def _init_experience_store(self) -> None:
        """初始化经验库"""
        print("正在初始化经验库...")
        exp_config = self.config.get('experience', {})
        
        self.experience_store = ExperienceStore(
            storage_path=exp_config.get('storage_path', './data/experience_db.json'),
            max_experiences=exp_config.get('max_experiences', 1000),
            relevance_threshold=exp_config.get('relevance_threshold', 0.8)
        )
        
        self.logger.info("经验库初始化完成")
    
    def _init_rag_systems(self) -> None:
        """初始化RAG系统 - 为每个Agent创建独立的RAG系统"""
        print("正在初始化RAG系统...")
        rag_config = self.config.get('rag', {})
        vector_config = self.config.get('vector_store', {})
        
        # 为每个Agent创建独立的RAG系统
        data_dir = self.config.get('paths', {}).get('raw_data', './data/raw')
        persist_dir = vector_config.get('persist_directory', './data/chroma_db')
        base_collection_name = vector_config.get('collection_name', 'chemical_reactions')
        
        # 检查数据目录是否有文件
        if not any(Path(data_dir).iterdir()):
            self.logger.warning(f"数据目录为空: {data_dir}，RAG系统可能无法正常工作")
            print(f"  警告：数据目录为空，请将化学文献数据放入 {data_dir}")
        
        # 为每个Agent创建独立的RAG系统，使用不同的collection_name
        self.rag_systems = {}
        agent_names = ['agent1', 'agent2', 'agent3', 'agent4']
        
        for agent_name in agent_names:
            collection_name = f"{base_collection_name}_{agent_name}"
            print(f"  为 {agent_name} 创建RAG系统，使用集合: {collection_name}")
            
            rag_system = RAGSystem(
                data_dir=data_dir,
                persist_dir=persist_dir,
                collection_name=collection_name,
                chunk_size=rag_config.get('chunk_size', 512),
                chunk_overlap=rag_config.get('chunk_overlap', 50),
                top_k=rag_config.get('top_k', 5)
            )
            self.rag_systems[agent_name] = rag_system
        
        self.logger.info("RAG系统初始化完成")
    
    def _init_agents(self) -> None:
        """初始化Agent"""
        print("正在初始化Agents...")
        
        agent_config = AgentConfig(self.config)
        
        # 创建所有Agent
        self.agents = agent_config.create_all_agents(
            rag_systems=self.rag_systems,
            experience_store=self.experience_store
        )
        
        if not self.agents:
            raise RuntimeError("没有成功创建任何Agent")
        
        self.logger.info(f"成功初始化 {len(self.agents)} 个Agent")
    
    def _init_debate_coordinator(self) -> None:
        """初始化AutoGen辩论协调器"""
        print("正在初始化AutoGen辩论协调器...")
        
        debate_config = self.config.get('debate', {})
        
        self.debate_coordinator = AutoGenDebateCoordinator(
            agents=self.agents,
            config=debate_config,
            use_autogen=False  # 默认使用手动模式，更容易调试
        )
        
        self.logger.info("AutoGen辩论协调器初始化完成")
    
    def run_debate(
        self,
        components: List[str],
        save_result: bool = True
    ) -> dict:
        """
        Run debate
        
        Args:
            components: List of metal catalyst elements
            save_result: Whether to save results
        
        Returns:
            dict: Debate results
        """
        if not self._initialized:
            raise RuntimeError("System not initialized, please call initialize() first")
        
        # Validate components
        is_valid, error_msg = validate_components(components)
        if not is_valid:
            raise ValueError(f"Component validation failed: {error_msg}")
        
        self.logger.info(f"Starting debate with metal catalysts: {components}")
        
        # 创建辩论日志器
        debate_logger = DebateLogger()
        debate_logger.log_debate_start(components, self.config.get('debate', {}))
        
        # 执行辩论（使用AutoGen协调器）
        result = self.debate_coordinator.start_debate(components)
        
        # 记录辩论结束
        debate_logger.log_debate_end(result.to_dict())
        
        # 提取经验
        if result.consensus_reached:
            self._extract_and_save_experience(result, components)
        
        # 保存结果
        if save_result:
            self._save_result(result, components)
        
        self.logger.info("辩论完成")
        
        return result.to_dict()
    
    def _extract_and_save_experience(self, debate_result, components: List[str]) -> None:
        """提取并保存经验"""
        print("\n正在提取经验...")
        
        extractor = ExperienceExtractor()
        experience = extractor.extract_from_debate(debate_result, components)
        
        # 验证经验
        is_valid, msg = extractor.validate_experience(experience)
        if not is_valid:
            self.logger.warning(f"经验验证失败: {msg}")
            return
        
        # 保存到经验库
        self.experience_store.add_experience(experience)
        
        # 打印经验摘要
        summary = extractor.format_experience_summary(experience)
        print(summary)
        
        self.logger.info("经验提取和保存完成")
    
    def _save_result(self, result, components: List[str]) -> None:
        """保存辩论结果到文件"""
        output_dir = ensure_dir(self.config.get('paths', {}).get('outputs', './outputs'))
        
        from utils.helpers import create_experiment_id, generate_timestamp
        exp_id = create_experiment_id(components)
        timestamp = generate_timestamp()
        
        filename = f"result_{timestamp}.json"
        filepath = output_dir / filename
        
        result_data = {
            "experiment_id": exp_id,
            "timestamp": timestamp,
            "components": components,
            "result": result.to_dict()
        }
        
        save_json(result_data, filepath)
        
        print(f"\n结果已保存到: {filepath}")
        self.logger.info(f"结果已保存: {filepath}")
    
    def print_system_status(self) -> None:
        """打印系统状态"""
        print_header("系统状态")
        
        status = {
            "初始化状态": "已初始化" if self._initialized else "未初始化",
            "Agent数量": len(self.agents) if self.agents else 0,
            "经验库大小": len(self.experience_store.experiences) if self.experience_store else 0,
            "RAG系统": "已加载" if self.rag_systems else "未加载"
        }
        
        print(dict_to_table(status, headers=("项目", "状态")))
        
        if self.experience_store:
            stats = self.experience_store.get_statistics()
            print_section("经验库统计", dict_to_table(stats, headers=("指标", "值")))


def main():
    """主程序入口"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(
        description="多Agent化学反应过电势预测系统"
    )
    parser.add_argument(
        '--components',
        type=str,
        help='化学组分，用逗号或顿号分隔（例如：硫酸,氢氧化钠,氯化钠,硝酸,碳酸钙）'
    )
    parser.add_argument(
        '--config',
        type=str,
        default='./config/config.yaml',
        help='配置文件路径'
    )
    parser.add_argument(
        '--skip-rag',
        action='store_true',
        help='跳过RAG系统初始化（快速测试模式）'
    )
    parser.add_argument(
        '--status',
        action='store_true',
        help='显示系统状态'
    )
    
    args = parser.parse_args()
    
    try:
        # 创建系统实例
        system = MADSystem(config_path=args.config)
        
        # 初始化系统
        system.initialize(skip_rag=args.skip_rag)
        
        # 显示状态
        if args.status:
            system.print_system_status()
            return
        
        # 运行辩论
        if args.components:
            components = parse_component_string(args.components)
            print(f"\nAnalyzing metal catalyst elements: {', '.join(components)}\n")
            
            result = system.run_debate(components)
            
            # Print result summary
            print_header("Debate Result Summary")
            
            summary = {
                "Consensus Reached": "Yes" if result['consensus_reached'] else "No",
                "Reaction Type": result['final_reaction_type'] or "Not Determined",
                "Overpotential": f"{result['final_overpotential']}V" if result['final_overpotential'] else "Not Estimated",
                "Debate Rounds": result['debate_rounds'],
                "Time Elapsed": format_duration(result['time_elapsed'])
            }
            
            print(dict_to_table(summary, headers=("Item", "Result")))
        else:
            print("\nNo metal catalyst elements specified.")
            print("Usage: python main.py --components 'Pt,Pd,Ru,Ir,Rh'")
            print("使用 --components 参数指定组分，例如：")
            print("  python main.py --components '硫酸,氢氧化钠,氯化钠,硝酸,碳酸钙'")
            print("\n或使用 --status 查看系统状态")
            
            system.print_system_status()
    
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
