# ReAct推理能力说明文档

## 概述

本项目已成功集成ReAct (Reasoning + Acting) 推理范式，将Agent的推理过程分解为明确的 **Thought → Action → Observation** 循环，使推理过程更加透明和可控。

## ReAct核心概念

### 推理循环

每一步决策被分解为三个部分：

1. **Thought (思考)**: Agent对当前问题的子目标分析与检索需求判断
2. **Action (动作)**: 对RAG工具或经验库工具的调用，在动作空间内选择采用的动作
3. **Observation (观察)**: 检索的结果或收集到的可用经验

### 推理轨迹 (Trajectory)

完整的推理轨迹包括：
- **原始query**: 用户的初始问题
- **推理步骤**: 每一步的Thought、Action和Observation
- **最终答案**: 基于推理轨迹得到的结论

## 架构设计

### 核心模块

```
agents/
├── react_reasoning.py      # ReAct推理引擎和数据结构
├── react_agent.py          # ReAct Agent基类
├── llm_agents.py          # 具体LLM Agent实现（已集成ReAct）
└── base_agent.py          # Agent基类
```

### 关键类

#### 1. ActionType (枚举)

定义Agent可执行的动作类型：

```python
class ActionType(Enum):
    SEARCH_RAG = "search_rag"           # 从RAG系统检索知识
    QUERY_EXPERIENCE = "query_experience"  # 查询经验库
    ANALYZE = "analyze"                  # 分析当前信息
    CONCLUDE = "conclude"                # 得出最终结论
```

#### 2. ReActStep (数据类)

表示推理的单个步骤：

```python
@dataclass
class ReActStep:
    step_number: int              # 步骤编号
    thought: str                  # 思考内容
    action: ActionType            # 执行的动作
    action_input: Dict[str, Any]  # 动作参数
    observation: str              # 观察结果
    observation_data: Any         # 原始数据
    timestamp: str                # 时间戳
```

#### 3. ReActTrajectory (数据类)

完整的推理轨迹：

```python
@dataclass
class ReActTrajectory:
    query: str                    # 原始查询
    steps: List[ReActStep]        # 推理步骤列表
    final_answer: str             # 最终答案
    total_steps: int              # 总步骤数
    start_time: str               # 开始时间
    end_time: str                 # 结束时间
```

#### 4. ReActEngine

推理引擎，协调整个ReAct过程：

- 注册和管理工具函数
- 执行动作并获取观察结果
- 解析LLM响应提取Thought和Action
- 判断推理是否应该继续

#### 5. ReActAgent

具备ReAct能力的Agent基类：

- 继承自BaseAgent
- 集成ReActEngine
- 实现工具注册和调用
- 提供`generate_response_with_react()`方法

## 使用方法

### 基本使用

```python
from agents import create_agent
from database.rag_system import RAGSystem
from experience.experience_store import ExperienceStore

# 初始化RAG系统和经验库
rag_system = RAGSystem(...)
experience_store = ExperienceStore(...)

# 创建具备ReAct能力的Agent
agent = create_agent(
    agent_type="openai",
    agent_id="agent_1",
    name="OpenAI Agent",
    model_config={...},
    rag_system=rag_system,
    experience_store=experience_store
)

# 使用ReAct推理
query = "分析Pt、Pd、Ru作为催化剂的性能"
components = ["Pt", "Pd", "Ru"]

response, trajectory = agent.generate_response_with_react(
    query=query,
    components=components
)

# 查看结果
print(f"最终答案: {response.content}")
print(f"推理步骤数: {trajectory.total_steps}")

# 查看详细推理过程
for step in trajectory.steps:
    print(f"步骤 {step.step_number}:")
    print(f"  思考: {step.thought}")
    print(f"  动作: {step.action.value}")
    print(f"  观察: {step.observation}")
```

### 保存推理轨迹

```python
# 保存为JSON文件
agent.save_trajectory("outputs/trajectory.json")

# 或直接使用trajectory对象
trajectory_json = trajectory.to_json()
trajectory_dict = trajectory.to_dict()
```

### 获取推理轨迹摘要

```python
summary = trajectory.get_trajectory_summary()
print(summary)
```

输出示例：
```
=== ReAct推理轨迹 ===
原始问题: 分析Pt、Pd、Ru作为催化剂的性能
推理步骤数: 5

步骤 1:
  思考: 需要从文献知识库中检索相关的催化剂性能数据
  动作: search_rag
  观察: 检索到 5 条相关文献知识...

步骤 2:
  思考: 需要查询历史经验库，寻找类似催化剂的应用案例
  动作: query_experience
  观察: 找到 3 条相关历史经验...

...

最终答案: 基于文献和经验分析，Pt在HER反应中表现最佳...
```

## 推理流程

### 完整推理循环

```
1. 初始化推理轨迹
   ↓
2. 构建ReAct提示（包含可用工具和历史步骤）
   ↓
3. 调用LLM获取响应
   ↓
4. 解析响应提取Thought和Action
   ↓
5. 执行Action获取Observation
   ↓
6. 创建ReActStep并添加到轨迹
   ↓
7. 判断是否继续（检查步骤数和动作类型）
   ↓
8. 如果继续，返回步骤2；否则生成最终答案
```

### 智能默认策略

当LLM未返回有效动作时，系统使用智能默认策略：

- **步骤1-2**: 优先检索RAG知识
- **步骤3-4**: 查询经验库（如果有组分信息）
- **步骤5+**: 分析或得出结论

## 工具系统

### 已注册的工具

1. **search_rag**: 从RAG系统检索文献知识
   - 参数: `query` (检索查询), `top_k` (结果数量)
   - 返回: 相关文献片段列表

2. **query_experience**: 查询经验库
   - 参数: `components` (化学组分列表)
   - 返回: 相关历史经验列表

3. **analyze**: 分析当前信息
   - 参数: `context` (待分析内容)
   - 返回: 分析确认信息

4. **conclude**: 得出结论
   - 参数: `conclusion` (结论内容)
   - 返回: 结论内容（触发推理结束）

### 工具注册

```python
# 在ReActAgent中注册自定义工具
agent.react_engine.register_tool(
    ActionType.CUSTOM_TOOL,
    custom_tool_function
)
```

## 与现有系统的集成

### Agent类继承关系

```
BaseAgent (基类)
    ↓
ReActAgent (ReAct能力)
    ↓
├── OpenAIAgent
├── XAIAgent
├── GoogleAgent
└── DeepSeekAgent
```

所有具体的LLM Agent都已集成ReAct能力。

### 兼容性

- **保留原有接口**: `generate_response()` 方法仍然可用
- **新增ReAct接口**: `generate_response_with_react()` 提供ReAct推理
- **无缝切换**: 可以在同一个Agent上使用两种方法

## 示例代码

完整示例请参见 `example_react.py`，包含：

1. **基本ReAct推理示例**
2. **传统方法vs ReAct方法对比**
3. **逐步推理过程展示**

运行示例：

```bash
python example_react.py
```

## 配置参数

### ReAct引擎参数

```python
ReActEngine(
    max_steps=10,      # 最大推理步骤数
    verbose=True       # 是否输出详细日志
)
```

### Agent初始化参数

```python
agent = create_agent(
    agent_type="openai",
    agent_id="agent_1",
    name="OpenAI Agent",
    model_config={
        'api_key': '...',
        'model': 'gpt-4',
        'temperature': 0.9,
        'max_tokens': 2000
    },
    rag_system=rag_system,
    experience_store=experience_store
)
```

## 输出格式

### ReActTrajectory JSON结构

```json
{
  "query": "原始查询",
  "steps": [
    {
      "step_number": 1,
      "thought": "思考内容",
      "action": "search_rag",
      "action_input": {"query": "...", "top_k": 5},
      "observation": "观察结果",
      "observation_data": [...],
      "timestamp": "2025-12-29T10:30:00"
    },
    ...
  ],
  "final_answer": "最终答案",
  "total_steps": 5,
  "start_time": "2025-12-29T10:30:00",
  "end_time": "2025-12-29T10:31:00"
}
```

## 优势

### 相比传统方法

1. **透明性**: 每一步推理都清晰可见
2. **可控性**: 可以干预和指导推理过程
3. **可追溯**: 完整记录推理轨迹，便于分析和调试
4. **灵活性**: 可以动态调整工具和策略
5. **可解释性**: 明确展示推理依据和过程

### 应用场景

1. **复杂决策**: 需要多步推理和信息收集
2. **知识密集**: 需要查询多个知识源
3. **可解释AI**: 需要展示推理过程
4. **调试优化**: 需要分析Agent行为

## 扩展性

### 添加新工具

```python
# 1. 定义新的动作类型
class ActionType(Enum):
    # ... 现有动作
    CUSTOM_ACTION = "custom_action"

# 2. 实现工具函数
def custom_tool_function(**kwargs):
    # 工具逻辑
    return result

# 3. 注册工具
agent.react_engine.register_tool(
    ActionType.CUSTOM_ACTION,
    custom_tool_function
)
```

### 自定义推理策略

继承`ReActAgent`并重写`_smart_default_action`方法：

```python
class CustomReActAgent(ReActAgent):
    def _smart_default_action(self, step_number, previous_steps, components):
        # 自定义策略逻辑
        return thought, action, action_input
```

## 注意事项

1. **LLM响应解析**: 确保LLM能够按照预期格式返回Thought和Action
2. **工具执行**: 所有工具函数都应该有适当的错误处理
3. **步骤限制**: 设置合理的`max_steps`以避免无限循环
4. **成本控制**: ReAct模式会调用LLM多次，注意API成本

## 未来改进

1. **动态工具选择**: 根据问题类型自动选择可用工具
2. **并行执行**: 支持同时执行多个独立的Action
3. **结果缓存**: 缓存重复查询的结果
4. **自适应策略**: 根据历史表现优化默认策略
5. **可视化界面**: 提供推理过程的可视化展示

## 总结

ReAct推理能力为Agent系统带来了：
- 更强的推理能力
- 更好的可解释性
- 更灵活的扩展性
- 更便于调试和优化

所有现有的Agent (OpenAI, xAI, Google, DeepSeek) 都已支持ReAct推理，可以通过`generate_response_with_react()`方法直接使用。
