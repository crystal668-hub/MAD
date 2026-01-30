# 向量数据库多Agent独立化说明

## 修改概述

现在系统已经支持为每个Agent创建独立的向量数据库。不同的Agent将使用不同的embedding模型和独立的向量数据库集合。

## 修改内容

### 1. `build_vector_db.py` - 向量数据库构建脚本
- **修改位置**：第47-62行
- **修改内容**：
  - 根据`agent_name`动态生成`collection_name`
  - 格式：`{base_collection_name}_{agent_name}`
  - 例如：`chemical_reactions_agent1`, `chemical_reactions_agent2`
  
### 2. `main.py` - 主程序
- **修改位置**：`_init_rag_systems`方法
- **修改内容**：
  - 为每个Agent创建独立的RAG系统
  - 每个RAG系统使用不同的`collection_name`
  - 不再共享同一个RAG系统

### 3. 新增文件：`build_all_agent_dbs.py`
- **功能**：批量为所有Agent构建向量数据库
- **特点**：自动化处理，提供详细的进度和结果报告

## 使用方法

### 方法一：为单个Agent构建向量数据库

```bash
# 激活环境
conda activate mad4chem

# 为agent1构建向量数据库
python build_vector_db.py
```

修改`build_vector_db.py`的最后几行来指定不同的agent：
```python
if __name__ == "__main__":
    build_vector_database(
        config_path="./config/config.yaml",
        agent_name="agent2"  
    )
```

### 方法二：批量为所有Agent构建向量数据库（推荐）

```bash
# 一次性为所有agent构建向量数据库
python build_all_agent_dbs.py
```

这会自动为agent1、agent2、agent3、agent4创建独立的向量数据库。

## 数据库命名规则

| Agent | 使用的Embedding模型 | 向量数据库集合名称 |
|-------|-------------------|------------------|
| agent1 (GPT 5.2) | openai/text-embedding-3-large | chemical_reactions_agent1 |
| agent2 (DeepSeek V3.2) | voyage-3-large | chemical_reactions_agent2 |
| agent3 (Gemini 3 pro) | google/gemini-embedding-001 | chemical_reactions_agent3 |
| agent4 (Qwen3 Max) | text-embedding-v4 | chemical_reactions_agent4 |

## 数据库存储位置

所有向量数据库集合存储在同一个目录下：
```
./data/chroma_db/
├── chroma.sqlite3                    # ChromaDB元数据
├── {uuid1}/                          # chemical_reactions_agent1
├── {uuid2}/                          # chemical_reactions_agent2
├── {uuid3}/                          # chemical_reactions_agent3
└── {uuid4}/                          # chemical_reactions_agent4
```

## 验证修改

### 1. 检查build_vector_db.py的输出

构建向量数据库时应该看到类似输出：
```
============================================================
开始构建Chroma向量数据库
============================================================

[步骤 1/5] 加载配置...
✓ 使用Agent: agent2
✓ LLM模型: deepseek/deepseek-v3.2
✓ 向量模型: voyage-3-large
✓ 向量数据库集合: chemical_reactions_agent2    <-- 注意这里
...
✓ 集合名称: chemical_reactions_agent2           <-- 和这里
```

### 2. 检查main.py的输出

运行主程序时应该看到：
```
正在初始化RAG系统...
  为 agent1 创建RAG系统，使用集合: chemical_reactions_agent1
  为 agent2 创建RAG系统，使用集合: chemical_reactions_agent2
  为 agent3 创建RAG系统，使用集合: chemical_reactions_agent3
  为 agent4 创建RAG系统，使用集合: chemical_reactions_agent4
```

### 3. 使用Python检查数据库

```python
import chromadb

client = chromadb.PersistentClient(path="./data/chroma_db")

# 列出所有集合
collections = client.list_collections()
for col in collections:
    print(f"{col.name}: {col.count()} 文档")

# 输出示例：
# chemical_reactions_agent1: 1234 文档
# chemical_reactions_agent2: 1234 文档
# chemical_reactions_agent3: 1234 文档
# chemical_reactions_agent4: 1234 文档
```

## 注意事项

1. **数据一致性**：所有Agent使用相同的源数据，但embedding模型不同，因此向量表示会有差异
2. **存储空间**：每个Agent都有独立的向量数据库，会占用更多存储空间
3. **构建时间**：首次构建需要为每个Agent分别调用embedding API，时间会更长
4. **API配额**：确保各个API服务的配额充足（特别是Voyage AI和Google Gemini）

## 优势

1. **模型独立性**：每个Agent使用最适合自己的embedding模型
2. **性能优化**：不同embedding模型可能在不同类型的查询上表现更好
3. **易于扩展**：添加新Agent时只需构建对应的向量数据库
4. **调试方便**：可以单独测试每个Agent的检索效果

## 故障排查

### 问题1：某个Agent的向量数据库构建失败
**解决方案**：
- 检查对应的API Key是否正确配置
- 确认embedding模型名称是否正确
- 查看错误日志，确认是网络问题还是配额问题

### 问题2：主程序提示找不到向量数据库
**解决方案**：
- 确保已经为对应的Agent运行过`build_vector_db.py`
- 检查`collection_name`是否匹配

### 问题3：想重新构建某个Agent的向量数据库
**解决方案**：
- 直接运行构建脚本，程序会提示是否清空现有数据
- 或手动删除对应的collection后重新构建
