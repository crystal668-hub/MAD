# 快速开始指南

## 安装步骤

### 1. 环境准备

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置API密钥

复制环境变量示例文件并填入你的API密钥：

```bash
copy .env.example .env
```

编辑 `.env` 文件，填入实际的API密钥：

```
OPENAI_API_KEY=your-actual-openai-key
ANTHROPIC_API_KEY=your-actual-anthropic-key
GOOGLE_API_KEY=your-actual-google-key
```

### 3. 准备数据

将化学文献数据（Markdown格式）放入 `data/raw/` 目录（可按反应类型分子目录）。

### 4. 构建向量数据库

```bash
python build_vector_db.py
```

## 基本使用

### 方式一：命令行运行 - 多Agent辩论

```bash
# 运行辩论（指定金属催化剂元素）
python main.py --components "Pt,Pd,Ru,Ir,Rh"

# 选择辩论引擎（默认：langgraph；可选：autogen）
python main.py --components "Pt,Pd,Ru,Ir,Rh" --engine langgraph
python main.py --components "Pt,Pd,Ru,Ir,Rh" --engine autogen

# 跳过RAG系统初始化（快速测试）
python main.py --components "Pt,Pd,Ru,Ir,Rh" --skip-rag

# 查看系统状态
python main.py --status

# 使用自定义配置文件
python main.py --config ./config/custom_config.yaml --components "硫酸,氢氧化钠,氯化钠"
```

### 方式二：ReAct推理模式 🆕

使用新的ReAct推理能力，获得透明的推理过程：

```bash
# 运行ReAct示例
python example_react.py

# 测试ReAct功能
python test_react.py
```

**ReAct推理的优势：**
- 💭 **Thought**: 查看Agent的思考过程
- 🎯 **Action**: 了解Agent采取的动作
- 👁️ **Observation**: 观察检索和查询结果
- 📝 **Trajectory**: 完整的推理轨迹记录

详细文档：
- 快速入门: `REACT_QUICKSTART.md`
- 完整文档: `REACT_CAPABILITY.md`
- 示例代码: `example_react.py`

### 方式三：Python脚本调用

```python
from main import MADSystem

# 创建系统实例
system = MADSystem(config_path="./config/config.yaml")

# 初始化系统
system.initialize()

# 运行辩论
components = ["Pt", "Pd", "Ru", "Ir", "Rh"]
result = system.run_debate(components)

# 打印结果
print(f"最终反应类型: {result['final_reaction_type']}")  
print(f"过电势: {result['final_overpotential']}")
```

## 模块化使用示例

### 单独使用RAG系统

```python
from database import RAGSystem

# 初始化RAG系统（从raw目录读取并切分）
rag = RAGSystem(
    data_dir="./data/raw",
    persist_dir="./data/chroma_db",
    collection_name="chemical_reactions"
)

# 构建索引（首次运行）
rag.build_index()

# 查询
result = rag.query("什么是氧化还原反应的过电势？")
print(result['answer'])

# 查看索引统计
stats = rag.get_index_stats()
print(f"索引chunks数量: {stats['document_count']}")
```

### 单独使用Agent

```python
from agents import create_agent

# 创建Agent（自动具备ReAct能力）
agent = create_agent(
    agent_type="openai",
    agent_id="test_agent",
    name="Test Agent",
    model_config={
        "provider": "openai",
        "model": "gpt-4",
        "api_key": "your-api-key",
        "temperature": 0.7
    }
)

# 传统方式：生成响应
response = agent.generate_response("分析这个化学反应...")
print(response.content)

# 🆕 ReAct方式：使用推理轨迹
response, trajectory = agent.generate_response_with_react(
    query="分析催化剂性能",
    components=["Pt", "Pd", "Ru"]
)

# 查看推理过程
for step in trajectory.steps:
    print(f"步骤{step.step_number}: {step.thought}")
    print(f"  动作: {step.action.value}")
    print(f"  观察: {step.observation[:100]}...")

# 保存轨迹
agent.save_trajectory("outputs/trajectory.json")
```

### 单独使用经验库

```python
from experience import ExperienceStore

# 初始化经验库
store = ExperienceStore(
    storage_path="./data/experience_db.json",
    max_experiences=1000
)

# 添加经验
experience = {
    "components": ["硫酸", "氢氧化钠"],
    "reaction_type": "酸碱中和反应",
    "overpotential": 0.3,
    "reasoning": "详细推理...",
    "confidence": 0.9
}
store.add_experience(experience)

# 查询经验
results = store.query_experiences(
    components=["硫酸", "氢氧化钠"],
    top_k=3
)
```

## 配置说明

主要配置位于 `config/config.yaml`：

- **llm**: 四个Agent的LLM配置
    - agent1: OpenAI GPT-4o-mini
    - agent2: DeepSeek V3.2  
    - agent3: Google Gemini-3-pro
    - agent4: Qwen3-Max
  - 每个均配置独立的embedding模型

- **vector_store**: Chroma向量数据库配置
  - persist_directory: 持久化目录
  - collection_name: 集合名称
  - distance_metric: 距离度量（cosine/l2/ip）

- **rag**: RAG系统参数
  - 注意：chunk_size和chunk_overlap已不使用，因为chunks已预切分
  - top_k: 检索返回数量
  - similarity_threshold: 相似度阈值

- **debate**: 辩论配置
  - max_rounds: 最大辩论轮数
  - consensus_threshold: 共识阈值
  - timeout: 超时时间

- **experience**: 经验库配置
  - storage_path: 存储路径
  - max_experiences: 最大存储数量
  - relevance_threshold: 相关性阈值

- **chemistry**: 化学反应相关配置
  - 支持9种反应类型（CO2RR, EOR, HER, HOR, HZOR, O5H, OER, ORR, UOR）

## 常见问题

### 1. API密钥错误

确保在 `.env` 文件中正确配置了所有API密钥，且格式正确。

### 2. 数据处理失败

- 检查 `data/raw/` 是否包含Markdown文件
- 查看 `build_vector_db.py` 或 `database.text_processor` 的错误信息

### 3. RAG系统初始化失败

- 确保已运行 `python build_vector_db.py` 构建向量数据库
- 检查 `data/raw/` 是否包含Markdown文件
- 首次运行需要时间构建索引
- 使用 `--skip-rag` 跳过RAG初始化进行快速测试

### 4. 内存不足

- 减少 `max_tokens` 配置
- 减少 `top_k` 检索数量
- 分批处理数据

### 5. 辩论不收敛

- 增加 `max_rounds` 配置
- 降低 `consensus_threshold`
- 检查提示词是否清晰

## 输出文件

运行后会生成以下文件：

- `logs/system.log`: 系统日志
- `logs/debates/debate_*.log`: 辩论详细日志
- `data/experience_db.json`: 经验库
- `outputs/result_*.json`: 辩论结果
- `outputs/react_trajectory_*.json`: 🆕 ReAct推理轨迹

## 进阶使用

### 自定义Agent

创建新的Agent类继承 `ReActAgent`（自动具备ReAct能力）：

```python
from agents.react_agent import ReActAgent
from agents.base_agent import AgentResponse

class CustomAgent(ReActAgent):
    def _init_llm_client(self):
        # 初始化你的LLM客户端
        pass
    
    def _call_llm(self, prompt: str) -> str:
        # 实现LLM调用逻辑（用于ReAct推理）
        pass
    
    def generate_response(self, prompt, context=None):
        # 实现响应生成逻辑（传统方式）
        pass
```

### 扩展ReAct工具 🆕

添加自定义工具到ReAct推理：

```python
from agents.react_reasoning import ActionType

# 定义新的动作类型
class CustomActionType(ActionType):
    CUSTOM_TOOL = "custom_tool"

# 实现工具函数
def custom_tool_function(**kwargs):
    # 工具逻辑
    return result

# 注册到Agent
agent.react_engine.register_tool(
    CustomActionType.CUSTOM_TOOL,
    custom_tool_function
)
```

### 自定义辩论策略

修改 `debate/debate_manager.py` 中的辩论逻辑：

```python
def custom_debate_strategy(self, components):
    # 实现自定义辩论流程
    pass
```

### 导出经验库

```python
from experience import ExperienceStore

store = ExperienceStore("./data/experience_db.json")
store.export_to_file("./backup/experiences_backup.json")
```

## 性能优化建议

1. **并行处理**: 为每个Agent使用独立的向量数据库集合
2. **缓存**: 启用LLM响应缓存减少API调用
3. **批处理**: 批量处理多个组分组合
4. **异步**: 使用异步IO提升性能

## 下一步

- 阅读 [README.md](README.md) 了解项目整体架构
- 查看各模块源码中的详细注释
- 根据实际需求调整 `config/config.yaml` 配置
- 在 `data/raw/` 中添加更多化学文献数据

## 技术支持

如遇问题，请查看：
1. 系统日志 `logs/system.log`
2. 辩论日志 `logs/debates/`
3. 项目文档和代码注释

祝使用愉快！
