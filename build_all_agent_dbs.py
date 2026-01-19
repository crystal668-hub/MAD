"""
======================================================
批量构建所有Agent的向量数据库脚本
功能：为每个Agent创建独立的向量数据库
======================================================
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 添加项目根目录到路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from build_vector_db import build_vector_database


def build_all_agent_databases(
    config_path: str = "./config/config.yaml",
    agent_names: list = None
):
    """
    为所有Agent构建向量数据库
    
    Args:
        config_path: 配置文件路径
        agent_names: Agent名称列表（默认为所有agent）
    """
    if agent_names is None:
        agent_names = ['agent1', 'agent2', 'agent3', 'agent4']
    
    print("=" * 70)
    print("批量构建向量数据库")
    print("=" * 70)
    print(f"\n将为以下 {len(agent_names)} 个Agent创建独立的向量数据库：")
    for agent_name in agent_names:
        print(f"  - {agent_name}")
    print()
    
    successful = []
    failed = []
    
    for idx, agent_name in enumerate(agent_names, 1):
        print(f"\n{'=' * 70}")
        print(f"[{idx}/{len(agent_names)}] 处理 {agent_name}")
        print(f"{'=' * 70}")
        
        try:
            build_vector_database(
                config_path=config_path,
                agent_name=agent_name
            )
            successful.append(agent_name)
            print(f"\n✓ {agent_name} 的向量数据库构建成功")
        except Exception as e:
            failed.append((agent_name, str(e)))
            print(f"\n✗ {agent_name} 的向量数据库构建失败: {str(e)}")
    
    # 输出总结
    print("\n" + "=" * 70)
    print("构建总结")
    print("=" * 70)
    print(f"\n成功: {len(successful)}/{len(agent_names)}")
    for agent_name in successful:
        print(f"  ✓ {agent_name}")
    
    if failed:
        print(f"\n失败: {len(failed)}/{len(agent_names)}")
        for agent_name, error in failed:
            print(f"  ✗ {agent_name}: {error}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    # 批量构建所有Agent的向量数据库
    build_all_agent_databases(
        config_path="./config/config.yaml"
    )
