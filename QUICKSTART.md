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

将化学文献数据（TSV格式）放入 `data/raw/` 目录。

**TSV文件要求：**
- 必须包含 `abstract` 列
- 使用Tab（\t）分隔

### 4. 处理数据

运行数据处理脚本，提取abstract并切分chunks：

```bash
python -m database.text_processor
```

此脚本会：
- 读取 `data/raw/` 下的所有TSV文件
- 提取每行的 `abstract` 列内容
- 为每个chunk添加索引序号
- 将结果保存到 `data/processed/` （格式：`索引\t内容`）

**输出示例：**
```
0	This is the first abstract content...
1	This is the second abstract content...
2	This is the third abstract content...
```

## 基本使用

### 方式一：命令行运行

```bash
# 运行辩论（指定金属催化剂元素）
python main.py --components "Pt,Pd,Ru,Ir,Rh"

# 跳过RAG系统初始化（快速测试）
python main.py --components "Pt,Pd,Ru,Ir,Rh" --skip-rag

# 查看系统状态
python main.py --status

# 使用自定义配置文件
python main.py --config ./config/custom_config.yaml --components "硫酸,氢氧化钠,氯化钠"
```

### 方式二：Python脚本调用

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

# 初始化RAG系统（使用处理后的chunks）
rag = RAGSystem(
    data_dir="./data/processed",  # 注意：使用processed目录
    persist_dir="./data/chroma_db",
    collection_name="chemical_reactions"
)

# 构建索引（首次运行）
# chunks已经切分好，直接加载，无需再分割
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

# 创建Agent
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

# 生成响应
response = agent.generate_response("分析这个化学反应...")
print(response.content)
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
  - agent2: xAI Grok-4.1-fast  
  - agent3: Google Gemini-3-pro
  - agent4: DeepSeek V3.2
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
  - 支持11种反应类型（AOR, CO2RR, HER, OER, ORR等）

## 常见问题

### 1. API密钥错误

确保在 `.env` 文件中正确配置了所有API密钥，且格式正确。

### 2. 数据处理失败

- 检查TSV文件是否包含 `abstract` 列
- 确保使用Tab（\t）分隔
- 查看 `database.text_processor` 输出的错误信息

### 3. RAG系统初始化失败

- 确保已运行 `python -m database.text_processor` 处理数据
- 检查 `data/processed/` 目录是否包含txt文件
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

## 进阶使用

### 自定义Agent

创建新的Agent类继承 `BaseAgent`：

```python
from agents.base_agent import BaseAgent, AgentResponse

class CustomAgent(BaseAgent):
    def _init_llm_client(self):
        # 初始化你的LLM客户端
        pass
    
    def generate_response(self, prompt, context=None):
        # 实现响应生成逻辑
        pass
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
