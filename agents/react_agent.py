"""
LangChain-based ReAct Agent.

Goal:
- Keep explicit "Thought -> Action -> Observation" trajectories.
- Avoid manual OpenAI tool message formatting by using LangChain message classes.
- Keep the original 4 tools: search_rag, search_experience, analyze, conclude.

Design:
Each ReAct iteration runs TWO LLM calls:
1) THOUGHT call (no tools): force explicit reasoning text.
2) ACTION call (with tools): model emits tool calls; we execute them and record observations.

Notes:
- The project currently uses OpenAI-compatible chat APIs (OpenRouter/DashScope). This agent
  builds a ChatOpenAI instance from config.yaml fields: model/api_key/base_url/temperature/max_tokens.
- LangChain is imported lazily so the codebase stays importable in minimal environments.
"""

from __future__ import annotations

import inspect
import os
import re
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Tuple

from agents.react_reasoning import ReActTrajectory, ReActStep, ActionType, ToolCallRecord
from utils.source_id import build_chroma_source_id


@dataclass
class AgentResponse:
    """Agent response payload."""

    content: str
    reasoning: Optional[str] = None
    confidence: Optional[float] = None
    sources: Optional[List[Dict[str, Any]]] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ToolResult:
    """Return type for tools that keeps raw data while displaying a compact observation."""

    observation: str
    data: Any = None

    def __str__(self) -> str:  # ToolMessage content
        return self.observation


def _resolve_env_var(value: Optional[str]) -> Optional[str]:
    if value and value.startswith("${") and value.endswith("}"):
        return os.getenv(value[2:-1])
    return value


def _lazy_langchain_imports():
    try:
        from langchain_openai import ChatOpenAI  # type: ignore
        from langchain_core.messages import (  # type: ignore
            SystemMessage,
            HumanMessage,
            AIMessage,
            ToolMessage,
        )
        from langchain_core.tools import StructuredTool  # type: ignore
    except Exception as e:  
        raise ImportError(
            "LangChain dependencies not found. Install: langchain-core langchain-openai."
        ) from e

    return ChatOpenAI, SystemMessage, HumanMessage, AIMessage, ToolMessage, StructuredTool


def _build_chat_model_from_config(model_config: Dict[str, Any]):
    ChatOpenAI, *_rest = _lazy_langchain_imports()

    api_key = _resolve_env_var(model_config.get("api_key"))
    if not api_key:
        raise ValueError("API key not provided (or env var not set) in model_config")

    base_url = model_config.get("base_url") or "https://openrouter.ai/api/v1"
    model = model_config.get("model") or "gpt-4"
    temperature = float(model_config.get("temperature", 0.9))
    max_tokens = int(model_config.get("max_tokens", 2000))

    sig = inspect.signature(ChatOpenAI)
    kwargs: Dict[str, Any] = {
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    # Support both old/new param names across langchain_openai versions.
    if "api_key" in sig.parameters:
        kwargs["api_key"] = api_key
    elif "openai_api_key" in sig.parameters:
        kwargs["openai_api_key"] = api_key

    if "base_url" in sig.parameters:
        kwargs["base_url"] = base_url
    elif "openai_api_base" in sig.parameters:
        kwargs["openai_api_base"] = base_url

    return ChatOpenAI(**kwargs)


class ReActAgent:
    """
    Memoryless-per-call agent that produces explicit ReAct trajectories.

    Compatibility:
    - Keeps generate_response_with_react(...) signature used by debate coordinators.
    - Keeps generate_response(...) for legacy callers.
    """

    def __init__(
        self,
        agent_id: str,
        name: str,
        model_config: Dict[str, Any],
        rag_system: Optional[Any] = None,
        experience_store: Optional[Any] = None,
        system_prompt: Optional[str] = None,
        max_react_steps: int = 10,
        verbose: bool = True,
    ) -> None:
        self.agent_id = agent_id
        self.name = name
        self.model_config = dict(model_config or {})
        self.rag_system = rag_system
        self.experience_store = experience_store
        self.system_prompt = system_prompt or ""
        self.max_react_steps = int(max_react_steps)
        self.verbose = bool(verbose)

        self.current_trajectory: Optional[ReActTrajectory] = None

        # Lazy init
        self._llm = None

    # -------------------------
    # Tools (raw retrieval)
    # -------------------------

    def retrieve_knowledge(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        if self.rag_system is None:
            raise RuntimeError("RAG System is not configured.")
        try:
            results = self.rag_system.retrieve(query)
            return (results or [])[: int(top_k)]
        except Exception as e:
            return [{"text": "", "score": 0.0, "metadata": {}, "error": str(e)}]

    def retrieve_experience(self, components: List[str], top_k: int = 5) -> List[Dict[str, Any]]:
        if self.experience_store is None:
            return []
        try:
            return self.experience_store.query_experiences(components=components, top_k=int(top_k)) or []
        except Exception as e:
            return [{"error": str(e), "components": components}]

    # -------------------------
    # LangChain tool wrappers
    # -------------------------

    def _tool_search_rag(self, query: str, top_k: int = 5) -> ToolResult:
        results = self.retrieve_knowledge(query=query, top_k=top_k)

        # Enrich with stable source_id for later verification.
        collection = getattr(self.rag_system, "collection_name", "unknown")
        for item in results or []:
            meta = item.get("metadata") or {}
            doc_id = meta.get("doc_id") or meta.get("doi") or meta.get("id")
            chunk_id = meta.get("chunk_id")
            if doc_id is None or chunk_id is None:
                continue
            try:
                item["source_id"] = build_chroma_source_id(str(collection), str(doc_id), int(chunk_id))
            except Exception:
                continue

        observation = _format_rag_observation(results)
        return ToolResult(observation=observation, data=results)

    def _tool_search_experience(self, components: List[str], top_k: int = 3) -> ToolResult:
        experiences = self.retrieve_experience(components=components, top_k=top_k)
        observation = _format_experience_observation(experiences)
        return ToolResult(observation=observation, data=experiences)

    def _tool_analyze(self, gap_analysis: str, next_step_plan: str) -> ToolResult:
        payload = {"gap_analysis": gap_analysis, "next_step_plan": next_step_plan}
        observation = (
            "Analysis Recorded:\n"
            f"- Gaps/Findings: {gap_analysis}\n"
            f"- Next Strategic Move: {next_step_plan}"
        )
        return ToolResult(observation=observation, data=payload)

    def _tool_conclude(self, conclusion: str) -> ToolResult:
        return ToolResult(observation=conclusion, data=conclusion)

    def _build_tools(self):
        _ChatOpenAI, _SystemMessage, _HumanMessage, _AIMessage, _ToolMessage, StructuredTool = _lazy_langchain_imports()

        tools = [
            StructuredTool.from_function(
                func=self._tool_search_rag,
                name=ActionType.SEARCH_RAG.value,
                description=(
                    "Search the local literature database (Chroma-backed RAG) and return relevant chunks. "
                    "Use AFTER `search_experience` when you need verifiable citations; cite source_id from results."
                ),
            ),
            StructuredTool.from_function(
                func=self._tool_search_experience,
                name=ActionType.SEARCH_EXPERIENCE.value,
                description="Search the experience database for similar past cases / guidelines (preferred before `search_rag`).",
            ),
            StructuredTool.from_function(
                func=self._tool_analyze,
                name=ActionType.ANALYZE.value,
                description="Stop searching and synthesize what is known/unknown; plan next step.",
            ),
            StructuredTool.from_function(
                func=self._tool_conclude,
                name=ActionType.CONCLUDE.value,
                description="Submit the final answer and stop.",
            ),
        ]
        tools_by_name = {t.name: t for t in tools}
        return tools, tools_by_name

    # -------------------------
    # LLM helpers
    # -------------------------

    def _get_llm(self):
        if self._llm is None:
            self._llm = _build_chat_model_from_config(self.model_config)
        return self._llm

    @staticmethod
    def _get_thought_phase_instruction() -> str:
        return (
            "CURRENT PHASE: THOUGHT\n"
            "Output ONLY your reasoning in plain text.\n"
            "- Do NOT call tools.\n"
            "- Do NOT include any tool-call markup/tags (e.g. <invoke ...>, <tool_call ...>, <|...|>, DSML blocks).\n"
            "- Do NOT output JSON or markdown.\n"
        )

    @staticmethod
    def _get_action_phase_instruction() -> str:
        return (
            "CURRENT PHASE: ACTION\n"
            "You MUST call one or more tools.\n"
            "Do NOT output normal text answers in this phase; use tool calls.\n"
            "Critical constraint:\n"
            "- In a single ACTION step, do NOT mix search tools (`search_rag`, `search_experience`) with "
            "analysis tools (`analyze`, `conclude`).\n"
            "  - If you need evidence: call one or more search tools first.\n"
            "  - After you receive observations, in the NEXT step you may call `analyze` or `conclude`.\n"
            "Rules:\n"
            "- Tool priority: prefer `search_experience` FIRST; then use `search_rag` for verifiable citations.\n"
            "- Prefer using tools over guessing.\n"
            "- If you have enough evidence, call `conclude`.\n"
        )

    # -------------------------
    # Public API
    # -------------------------

    def generate_response(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> AgentResponse:
        components = None
        if context:
            components = context.get("components")
        response, _trajectory = self.generate_response_with_react(query=prompt, components=components, context=context)
        return response

    def generate_response_with_react(
        self,
        query: str,
        components: Optional[List[str]] = None,
        context: Optional[Dict[str, Any]] = None,
        system_prompt_override: Optional[str] = None,
    ) -> Tuple[AgentResponse, ReActTrajectory]:
        ChatOpenAI, SystemMessage, HumanMessage, AIMessage, ToolMessage, _StructuredTool = _lazy_langchain_imports()

        full_query = query
        if components:
            full_query = f"{query}\n\nComponents: {', '.join(components)}"

        trajectory = ReActTrajectory(query=full_query)
        self.current_trajectory = trajectory

        llm = self._get_llm()
        tools, tools_by_name = self._build_tools()

        # Bind tools to enable tool-calling.
        if hasattr(llm, "bind_tools"):
            llm_with_tools = llm.bind_tools(tools)
        else:  # pragma: no cover
            llm_with_tools = llm.bind(tools=tools)

        system_prompt = system_prompt_override if system_prompt_override is not None else self.system_prompt
        messages: List[Any] = [SystemMessage(content=system_prompt), HumanMessage(content=full_query)]

        step_number = 0
        final_answer: Optional[str] = None

        while step_number < self.max_react_steps:
            # ----- THOUGHT -----
            thought_msg = llm.invoke(messages + [SystemMessage(content=self._get_thought_phase_instruction())])
            thought_content = getattr(thought_msg, "content", "") or ""
            thought_content = thought_content.strip()
            if not thought_content:
                thought_content = "I need to gather evidence and decide the next action."
            thought_content = _sanitize_thought(thought_content)

            # ----- ACTION (tool calls) -----
            tool_calls: List[Dict[str, Any]] = []
            action_msg = None
            raw_action_text = ""
            for attempt in range(2):
                retry_hint = ""
                if attempt > 0:
                    retry_hint = (
                        "\nERROR: You did not call any tools in the previous ACTION attempt.\n"
                        "You MUST call at least one tool now (no free-form answers).\n"
                    )

                action_msg = llm_with_tools.invoke(
                    messages
                    + [
                        SystemMessage(content=self._get_action_phase_instruction() + retry_hint),
                        SystemMessage(content=f"THOUGHT (plan; do not repeat):\n{thought_content}"),
                    ]
                )
                tool_calls = _extract_tool_calls(action_msg)
                raw_action_text = (getattr(action_msg, "content", "") or "").strip()
                if tool_calls:
                    break

            if not tool_calls:
                # Record an explicit failure step, but DO NOT accept this as the final answer.
                # Also do NOT append the raw assistant content to the chat history, as it can be off-topic/noisy.
                step_number += 1
                observation = (
                    "ACTION FAILED: model did not emit any tool calls. "
                    "Retry in next step.\n"
                    f"Raw content (truncated): {(raw_action_text[:500] + '...') if len(raw_action_text) > 500 else raw_action_text}"
                )
                trajectory.add_step(
                    ReActStep(
                        step_number=step_number,
                        thought=thought_content,
                        action="no_tool_call",
                        action_input={},
                        observation=observation,
                        tool_calls=[],
                    )
                )
                continue

            # Only keep the ACTION assistant message in history if it actually issued tool calls.
            messages.append(action_msg)

            normalized_calls: List[Tuple[str, Dict[str, Any], str]] = [
                _normalize_tool_call(call) for call in tool_calls
            ]
            search_tools = {ActionType.SEARCH_RAG.value, ActionType.SEARCH_EXPERIENCE.value}
            analysis_tools = {ActionType.ANALYZE.value, ActionType.CONCLUDE.value}
            has_search = any(name in search_tools for name, _args, _id in normalized_calls)
            has_analysis = any(name in analysis_tools for name, _args, _id in normalized_calls)
            mixed_search_and_analysis = has_search and has_analysis
            mixed_error = (
                "Policy violation: mixed search and analysis in one ACTION step. "
                "Call only search tools first; after receiving observations, call `analyze`/`conclude` in the next step."
            )

            tool_call_records: List[ToolCallRecord] = []
            observation_sections: List[str] = []

            for tool_name, tool_args, tool_call_id in normalized_calls:

                # If the model tried to both search and analyze/conclude in the same ACTION step,
                # refuse the analysis/conclude calls (they wouldn't be grounded in the fresh observations).
                blocked = mixed_search_and_analysis and tool_name in analysis_tools
                if blocked:
                    result = ToolResult(observation=mixed_error, data={"error": "mixed_search_and_analysis"})
                else:
                    tool = tools_by_name.get(tool_name)
                    if tool is None:
                        result = ToolResult(observation=f"Error: Unknown tool '{tool_name}'", data=None)
                    else:
                        try:
                            result = tool.invoke(tool_args)
                            if not isinstance(result, ToolResult):
                                result = ToolResult(observation=str(result), data=result)
                        except Exception as e:
                            result = ToolResult(observation=f"Tool error: {str(e)}", data=None)

                observation_text = str(result)
                messages.append(ToolMessage(content=observation_text, tool_call_id=tool_call_id))

                tool_call_records.append(
                    ToolCallRecord(
                        tool_name=tool_name,
                        tool_call_id=tool_call_id,
                        tool_args=tool_args,
                        observation=observation_text,
                        observation_data=result.data,
                    )
                )
                observation_sections.append(f"--- Observation ({tool_name}) ---\n{observation_text}")

                if tool_name == ActionType.CONCLUDE.value and not blocked:
                    final_answer = observation_text
                    break

            step_number += 1
            aggregated_observation = "\n\n".join(observation_sections).strip()
            if not aggregated_observation:
                aggregated_observation = "(no observation)"

            # Keep legacy single-action fields populated for compatibility/debugging,
            # but the authoritative per-call details live in `tool_calls`.
            if len(tool_call_records) == 1:
                action = tool_call_records[0].tool_name
                action_input = tool_call_records[0].tool_args
                tool_call_id = tool_call_records[0].tool_call_id
                observation_data = tool_call_records[0].observation_data
            else:
                action = "multi_tool"
                action_input = {"tool_calls": [{"tool_name": c.tool_name, "tool_args": c.tool_args} for c in tool_call_records]}
                tool_call_id = None
                observation_data = None

            trajectory.add_step(
                ReActStep(
                    step_number=step_number,
                    thought=thought_content,
                    action=action,
                    action_input=action_input,
                    observation=aggregated_observation,
                    tool_call_id=tool_call_id,
                    observation_data=observation_data,
                    tool_calls=tool_call_records,
                )
            )

            if final_answer is not None:
                break

        if final_answer is None:
            # Hard fallback: ask for a final answer text, then record it via the `conclude` tool
            # so downstream callers (tests / debate protocol) see a proper CONCLUDE action.
            retrieved = _collect_retrieved_source_ids_from_trajectory(trajectory)
            sid_hint = ""
            if retrieved:
                sid_hint = (
                    "\nYou MUST cite at least one of these source_id values verbatim in your final answer:\n"
                    + "\n".join(f"- {sid}" for sid in sorted(list(retrieved))[:10])
                )

            forced = llm.invoke(
                messages
                + [
                    SystemMessage(
                        content=(
                            "FINAL PHASE: Write the best possible final answer now.\n"
                            "- Include the reaction type explicitly.\n"
                            "- Summarize key performance metrics.\n"
                            "- If you used literature evidence, cite source_id exactly as provided.\n"
                            + sid_hint
                        )
                    )
                ]
            )
            draft = (getattr(forced, "content", "") or "").strip() or "No conclusion generated."

            # If the model forgot to include a verifiable source_id, attach a minimal evidence line.
            if retrieved and not any(sid in draft for sid in retrieved):
                draft = draft.rstrip() + "\n\nEvidence (retrieved source_id): " + ", ".join(sorted(list(retrieved))[:3])

            final_answer = draft

            # Record a final CONCLUDE step.
            step_number += 1
            tool_call = ToolCallRecord(
                tool_name=ActionType.CONCLUDE.value,
                tool_call_id="forced_conclude",
                tool_args={"conclusion": final_answer},
                observation=final_answer,
                observation_data=final_answer,
            )
            trajectory.add_step(
                ReActStep(
                    step_number=step_number,
                    thought="Forced conclusion (model failed to call conclude tool).",
                    action=ActionType.CONCLUDE.value,
                    action_input={"conclusion": final_answer},
                    observation=final_answer,
                    tool_call_id="forced_conclude",
                    observation_data=final_answer,
                    tool_calls=[tool_call],
                )
            )

        trajectory.finalize(final_answer)
        response = AgentResponse(
            content=final_answer,
            reasoning=trajectory.get_trajectory_summary(),
            sources=_extract_sources(trajectory),
        )
        return response, trajectory

    def save_trajectory(self, output_path: str) -> None:
        if not self.current_trajectory:
            return
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(self.current_trajectory.to_json())


def _extract_tool_calls(action_msg: Any) -> List[Dict[str, Any]]:
    # LangChain AIMessage typically exposes .tool_calls
    tool_calls = getattr(action_msg, "tool_calls", None)
    if isinstance(tool_calls, list):
        return tool_calls

    # Fallback: additional_kwargs
    add = getattr(action_msg, "additional_kwargs", {}) or {}
    tool_calls = add.get("tool_calls")
    if isinstance(tool_calls, list):
        return tool_calls

    return []


def _normalize_tool_call(call: Any) -> Tuple[str, Dict[str, Any], str]:
    """
    Normalize tool call formats across LangChain/openai variants.
    Returns (name, args, id).
    """
    if isinstance(call, dict):
        call_id = call.get("id") or call.get("tool_call_id") or f"tool_{id(call)}"

        # New style: {"name": "...", "args": {...}}
        name = call.get("name")
        args = call.get("args")
        if name and isinstance(args, dict):
            return str(name), args, str(call_id)

        # OpenAI style: {"function": {"name": "...", "arguments": "..."}}
        fn = call.get("function") or {}
        fn_name = fn.get("name")
        fn_args = fn.get("arguments")
        if fn_name:
            if isinstance(fn_args, dict):
                return str(fn_name), fn_args, str(call_id)
            if isinstance(fn_args, str):
                try:
                    import json

                    return str(fn_name), json.loads(fn_args), str(call_id)
                except Exception:
                    return str(fn_name), {}, str(call_id)

    # Unknown shape
    return "unknown_tool", {}, f"tool_{id(call)}"


def _sanitize_thought(text: str) -> str:
    """
    Some models emit tool-call markup in plain text (e.g. DSML/XML blocks) even when tools are disabled.
    That text pollutes later calls if we feed it back. Keep only a readable thought.
    """
    if not text:
        return ""

    # Remove common tool-call block patterns (best-effort).
    cleaned = re.sub(r"<[^>]*function_calls[^>]*>.*?</[^>]*function_calls[^>]*>", "", text, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r"<[^>]*(invoke|tool_call)[^>]*>.*?</[^>]*(invoke|tool_call)[^>]*>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)

    # Drop standalone markup-like lines that usually appear with DSML (<|...|> or <｜...｜>).
    kept: List[str] = []
    for line in cleaned.splitlines():
        stripped = line.strip()
        if not stripped:
            kept.append(line)
            continue
        if stripped.startswith("<") and ("DSML" in stripped or "function_calls" in stripped or "invoke" in stripped):
            continue
        kept.append(line)
    cleaned = "\n".join(kept).strip()
    return cleaned


def _collect_retrieved_source_ids_from_trajectory(trajectory: Optional[ReActTrajectory]) -> set[str]:
    if trajectory is None:
        return set()
    sids: set[str] = set()
    for step in getattr(trajectory, "steps", []) or []:
        for call in getattr(step, "tool_calls", []) or []:
            if getattr(call, "tool_name", "") != ActionType.SEARCH_RAG.value:
                continue
            data = getattr(call, "observation_data", None) or []
            for item in data:
                sid = item.get("source_id")
                if sid:
                    sids.add(sid)
    # Backward-compatible fallback (legacy single-tool steps).
    for step in getattr(trajectory, "steps", []) or []:
        if getattr(step, "action_name", "") != ActionType.SEARCH_RAG.value:
            continue
        data = getattr(step, "observation_data", None) or []
        for item in data:
            sid = item.get("source_id")
            if sid:
                sids.add(sid)
    return sids


def _format_rag_observation(results: List[Dict[str, Any]]) -> str:
    if not results:
        return "No relevant literature knowledge found."

    lines: List[str] = [f"Found {len(results)} relevant documents:"]
    for i, r in enumerate(results[:5], 1):
        score = r.get("score")
        source_id = r.get("source_id")
        meta = r.get("metadata") or {}
        if not source_id:
            doc_id = meta.get("doc_id")
            chunk_id = meta.get("chunk_id")
            if doc_id is not None and chunk_id is not None:
                source_id = f"doi:{doc_id}#chunk:{chunk_id}"
        text = (r.get("text") or "").strip()
        if len(text) > 800:
            text = text[:800] + "...(truncated)"
        head = f"{i}."
        if score is not None:
            try:
                head += f" [Relevance: {float(score):.3f}]"
            except Exception:
                pass
        if source_id:
            head += f" [Source: {source_id}]"
        lines.append(head)
        lines.append(text)
    return "\n".join(lines)


def _format_experience_observation(experiences: List[Dict[str, Any]]) -> str:
    if not experiences:
        return "No relevant historical experiences found."
    lines: List[str] = [f"Found {len(experiences)} relevant experiences:"]
    for i, exp in enumerate(experiences[:5], 1):
        kind = (exp.get("kind") or "experience").strip()
        gid = (exp.get("guideline_id") or "").strip()
        comps = exp.get("components") or []
        reaction = exp.get("reaction_type") or "unknown"
        pack = exp.get("source_pack") or ""
        sim = exp.get("similarity")

        header_parts = [f"{i}.", f"[{kind}]"]
        if gid:
            header_parts.append(f"[{gid}]")
        if sim is not None:
            try:
                header_parts.append(f"[Similarity: {float(sim):.3f}]")
            except Exception:
                pass
        if comps:
            header_parts.append(f"Components: {', '.join(comps)}")
        header_parts.append(f"Reaction: {reaction}")
        if pack:
            header_parts.append(f"Pack: {pack}")
        lines.append(" ".join(header_parts))

        title = (exp.get("title") or exp.get("products") or exp.get("id") or "").strip()
        if title:
            lines.append(f"Title: {title}")

        perf = exp.get("performance")
        if perf:
            lines.append(f"Performance: {str(perf).strip()}")

        notes = exp.get("content") or exp.get("reasoning") or exp.get("key_arguments")
        if notes and notes != perf:
            snippet = str(notes).strip()
            if len(snippet) > 600:
                snippet = snippet[:600] + "...(truncated)"
            lines.append(f"Notes: {snippet}")
    return "\n".join(lines)


def _extract_sources(trajectory: ReActTrajectory) -> List[Dict[str, Any]]:
    sources: List[Dict[str, Any]] = []
    for step in trajectory.steps:
        # New: multi-tool step support.
        for call in getattr(step, "tool_calls", []) or []:
            if call.tool_name == ActionType.SEARCH_RAG.value and isinstance(call.observation_data, list):
                sources.extend(call.observation_data[:3])
            if call.tool_name == ActionType.SEARCH_EXPERIENCE.value and isinstance(call.observation_data, list):
                sources.extend(call.observation_data[:2])

        # Backward-compatible fallback (legacy single-tool steps).
        action_name = getattr(step, "action_name", "")
        if action_name == ActionType.SEARCH_RAG.value and isinstance(getattr(step, "observation_data", None), list):
            sources.extend(getattr(step, "observation_data")[:3])
        if action_name == ActionType.SEARCH_EXPERIENCE.value and isinstance(getattr(step, "observation_data", None), list):
            sources.extend(getattr(step, "observation_data")[:2])
    return sources
