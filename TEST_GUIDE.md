# 测试脚本使用说明

## 文件：test_with_chroma.py

### 功能说明
本测试脚本实现以下功能：
1. **绑定向量数据库**：将所有4个Agent（GPT-4、Grok、Gemini、DeepSeek）全部绑定到现有的chroma_db向量数据库
2. **RAG检索测试**：验证向量数据库的检索功能是否正常工作
3. **辩论流程测试**：保持原有的辩论流程，执行完整的多Agent辩论

### 前置条件

1. **环境变量配置**
   确保 `.env` 文件中配置了所有必要的API密钥：
   ```bash
   OPENAI_API_KEY=your_openai_key
   XAI_API_KEY=your_xai_key
   GOOGLE_API_KEY=your_google_key
   DEEPSEEK_API_KEY=your_deepseek_key
   ```

2. **向量数据库**
   确保已经运行过 `build_vector_db.py` 构建了chroma向量数据库：
   ```bash
   python build_vector_db.py
   ```
   
   数据库位置：`./data/chroma_db/chroma.sqlite3`

3. **Python环境**
   激活conda环境：
   ```bash
   conda activate mad4chem
   ```

### 使用方法

#### 基本运行
```bash
python test_with_chroma.py
```

### 测试流程

脚本将执行以下步骤：

1. **加载配置** - 从 `config/config.yaml` 加载系统配置
2. **创建共享RAG系统** - 连接到现有的chroma_db向量数据库
3. **测试RAG检索** - 执行测试查询验证检索功能
4. **初始化Agent** - 创建4个Agent并全部绑定到RAG系统
5. **初始化辩论协调器** - 设置AutoGen辩论协调器
6. **运行测试辩论** - 使用测试催化剂组分（Pt, Pd, Ru, Ir, Rh）执行辩论
7. **输出结果** - 显示辩论结果并保存到outputs目录

### 输出说明

#### 控制台输出
脚本会在控制台显示详细的执行过程：
- ✓ 表示成功
- ✗ 表示失败或警告
- 各步骤的详细信息

#### 结果文件
辩论结果保存在：`./outputs/test_result_YYYYMMDD_HHMMSS.json`

结果文件包含：
```json
{
  "test_info": {
    "test_name": "四个Agent绑定Chroma向量数据库测试",
    "timestamp": "20231223_150000",
    "components": ["Pt", "Pd", "Ru", "Ir", "Rh"]
  },
  "rag_config": {
    "persist_dir": "./data/chroma_db",
    "collection_name": "chemical_reactions",
    "top_k": 5
  },
  "agents": [
    {"name": "GPT-4 Agent", "rag_enabled": true},
    {"name": "Grok Agent", "rag_enabled": true},
    {"name": "Gemini Agent", "rag_enabled": true},
    {"name": "DeepSeek Agent", "rag_enabled": true}
  ],
  "debate_result": {
    "consensus_reached": true/false,
    "final_reaction_type": "AOR",
    "final_overpotential": 0.35,
    "reasoning_trajectory": "...",
    "debate_rounds": 5,
    "debate_history": [...],
    "time_elapsed": 45.2
  }
}
```

### 验证要点

运行测试后，确认以下几点：

1. **RAG绑定成功**
   ```
   ✓ 成功创建 4 个Agent，全部绑定到chroma_db
     [1] GPT-4 Agent - ✓ 已绑定RAG
     [2] Grok Agent - ✓ 已绑定RAG
     [3] Gemini Agent - ✓ 已绑定RAG
     [4] DeepSeek Agent - ✓ 已绑定RAG
   ```

2. **RAG检索功能正常**
   ```
   ✓ 检索成功，返回 5 条结果
   ```

3. **辩论流程完整**
   - 各Agent轮流发言
   - 使用检索到的文献知识
   - 达成共识或完成最大轮数

### 与原有系统的区别

| 特性 | 原系统（main.py） | 测试脚本（test_with_chroma.py） |
|------|------------------|---------------------------|
| RAG绑定 | 部分Agent绑定 | **所有4个Agent绑定** |
| 数据库 | 可能新建索引 | **直接使用现有chroma_db** |
| 辩论流程 | 完整流程 | **完整流程（保持不变）** |
| 经验库 | 启用 | 简化版本（可选） |
| 用途 | 生产环境 | **测试验证** |

### 自定义测试

如需修改测试参数，编辑 `test_with_chroma.py` 中的相关变量：

```python
# 修改测试用的催化剂组分
test_components = ["Pt", "Pd", "Ru", "Ir", "Rh"]  # 改为你想测试的元素

# 修改测试查询
test_rag_retrieval(shared_rag, "your custom query")  # 改为你的查询
```

### 故障排查

#### 问题1：找不到chroma数据库
```
警告：未找到现有的chroma数据库文件
```
**解决方案**：先运行 `build_vector_db.py` 构建向量数据库

#### 问题2：API密钥错误
```
✗ 创建Agent失败: 环境变量 XXX_API_KEY 未设置
```
**解决方案**：检查 `.env` 文件中的API密钥配置

#### 问题3：检索返回空结果
```
警告：未检索到任何结果
```
**解决方案**：
- 检查向量数据库是否有数据
- 检查 `data/processed` 目录中是否有文本数据
- 重新运行 `build_vector_db.py`

### 扩展功能

如需在测试中添加更多功能：

1. **启用经验库**
   ```python
   from experience import ExperienceStore
   experience_store = ExperienceStore(...)
   agents = agent_config.create_all_agents(
       rag_systems=rag_systems,
       experience_store=experience_store  # 传入经验库
   )
   ```

2. **修改检索参数**
   ```python
   rag_system = RAGSystem(
       data_dir=data_dir,
       persist_dir=persist_dir,
       collection_name=collection_name,
       top_k=10  # 增加检索结果数量
   )
   ```

3. **调整辩论参数**
   在 `config/config.yaml` 中修改：
   ```yaml
   debate:
     max_rounds: 15  # 增加最大轮数
     consensus_threshold: 4  # 提高共识阈值
   ```

### 注意事项

1. **成本控制**：测试会调用多个LLM API，注意API用量
2. **网络连接**：确保可以访问OpenRouter API
3. **数据隐私**：测试数据会发送到LLM服务提供商
4. **性能考虑**：完整辩论可能需要几分钟时间

### 技术细节

- **RAG系统**：使用LlamaIndex + ChromaDB
- **嵌入模型**：默认使用OpenAI text-embedding-ada-002
- **辩论框架**：基于AutoGen的GroupChat
- **向量检索**：余弦相似度，Top-K=5

### 相关文件

- `config/config.yaml` - 系统配置文件
- `build_vector_db.py` - 构建向量数据库
- `main.py` - 主程序（生产环境使用）
- `data/chroma_db/` - 向量数据库存储目录
- `data/processed/` - 处理后的文本数据
