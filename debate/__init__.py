"""
辩论模块初始化文件
"""

from debate.autogen_setup import AutoGenSetup, create_termination_function
from debate.debate_manager import DebateManager, DebateResult

__all__ = [
    'AutoGenSetup',
    'create_termination_function',
    'DebateManager',
    'DebateResult'
]
