"""Debate module exports.

AutoGen is treated as an optional dependency so the LangGraph-style engine can run
in minimal environments (e.g., offline unit tests) without requiring pyautogen.
"""

from debate.langgraph_coordinator import LangGraphDebateCoordinator, GraphDebateResult

try:
    from debate.autogen_coordinator import AutoGenDebateCoordinator, DebateResult
except Exception:  # optional dependency (pyautogen -> autogen)
    AutoGenDebateCoordinator = None  # type: ignore
    DebateResult = None  # type: ignore

__all__ = [
    'LangGraphDebateCoordinator',
    'GraphDebateResult',
    'AutoGenDebateCoordinator',
    'DebateResult',
]
