import json
from types import SimpleNamespace

import pytest

from agents.react_agent import ReActAgent
from agents.react_reasoning import ActionType, ReActStep, ReActTrajectory


class FakeToolCall(SimpleNamespace):
    pass


class FakeMessage(SimpleNamespace):
    pass


class FakeReActAgent(ReActAgent):
    def _init_llm_client(self) -> None:
        self.client = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._call_count = 0
        self._last_tool_messages = []

    def _tool_search_rag(self, query: str, top_k: int = 5):
        return [
            {"score": 0.9, "text": "dummy result"}
        ]

    def _call_llm(self, messages, tools=None, tool_choice=None):
        self._call_count += 1
        if self._call_count == 1:
            tool_call = FakeToolCall(
                id="call_1",
                type="function",
                function=SimpleNamespace(
                    name="search_rag",
                    arguments=json.dumps({"query": "test", "top_k": 1})
                )
            )
            return FakeMessage(content="需要检索文献", tool_calls=[tool_call])

        self._last_tool_messages = [m for m in messages if m.get("role") == "tool"]
        return FakeMessage(content="最终答案", tool_calls=[])

    def generate_response(self, prompt: str, context=None):
        raise NotImplementedError("测试中不使用 generate_response")


def test_function_calling_react_loop_executes_tool_and_appends_tool_message():
    agent = FakeReActAgent(
        agent_id="test",
        name="TestAgent",
        model_config={},
        rag_system=None,
        experience_store=None,
        max_react_steps=3,
        verbose=False
    )

    response, trajectory = agent.generate_response_with_react(
        query="测试问题",
        components=["Pt"]
    )

    assert response.content == "最终答案"
    assert trajectory.total_steps == 2
    assert trajectory.steps[0].action == ActionType.SEARCH_RAG
    assert trajectory.steps[1].action == ActionType.CONCLUDE
    assert agent._last_tool_messages
    assert agent._last_tool_messages[0]["tool_call_id"] == "call_1"
    assert agent._last_tool_messages[0]["name"] == "search_rag"


def test_to_context_messages_reconstructs_tool_calls():
    steps = [
        ReActStep(
            step_number=1,
            thought="先检索",
            action=ActionType.SEARCH_RAG,
            action_input={"query": "a"},
            observation="obs1",
            tool_call_id="call_a"
        ),
        ReActStep(
            step_number=2,
            thought="再计算",
            action="calculate",
            action_input={"x": 1},
            observation="obs2",
            tool_call_id=None
        )
    ]
    trajectory = ReActTrajectory(query="问题", steps=steps)
    messages = trajectory.to_context_messages(system_prompt="SYS")

    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert len(messages) == 2 + 2 * len(steps)

    assistant_msg = messages[2]
    tool_msg = messages[3]
    assert assistant_msg["role"] == "assistant"
    assert assistant_msg["tool_calls"][0]["function"]["name"] == "search_rag"
    args = json.loads(assistant_msg["tool_calls"][0]["function"]["arguments"])
    assert args == {"query": "a"}
    assert tool_msg["role"] == "tool"
    assert tool_msg["tool_call_id"] == "call_a"
    assert tool_msg["content"] == "obs1"

    assistant_msg_2 = messages[4]
    tool_msg_2 = messages[5]
    assert assistant_msg_2["tool_calls"][0]["function"]["name"] == "calculate"
    assert tool_msg_2["tool_call_id"] == "react_step_2"
