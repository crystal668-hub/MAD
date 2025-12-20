# 项目结构详解

## 目录树

```
MAD/
├── config/                          # 配置文件目录
│   └── config.yaml                 # 主配置文件
│
├── data/                           # 数据目录
│   ├── raw/                        # 原始化学文献数据
│   │   └── sample_literature.txt  # 示例文献
│   ├── processed/                  # 处理后的数据
│   └── chroma_db/                  # Chroma向量数据库（运行时生成）
│
├── database/                       # 数据库模块
│   ├── __init__.py                # 模块初始化
│   ├── vector_store.py            # 向量数据库管理
│   └── rag_system.py              # RAG系统实现
│
├── agents/                         # Agent模块
│   ├── __init__.py                # 模块初始化
│   ├── base_agent.py              # Agent基类
│   ├── llm_agents.py              # 三个LLM Agent实现
│   └── agent_config.py            # Agent配置管理
│
├── debate/                         # 辩论模块
│   ├── __init__.py                # 模块初始化
│   ├── autogen_setup.py           # AutoGen框架配置
│   └── debate_manager.py          # 辩论管理器
│
├── experience/                     # 经验库模块
│   ├── __init__.py                # 模块初始化
│   ├── experience_store.py        # 经验存储管理
│   └── experience_extractor.py    # 经验提取器
│
├── utils/                          # 工具模块
│   ├── __init__.py                # 模块初始化
│   ├── logger.py                  # 日志工具
│   └── helpers.py                 # 辅助函数
│
├── logs/                           # 日志目录（运行时生成）
│   ├── system.log                 # 系统日志
│   └── debates/                   # 辩论日志
│
├── outputs/                        # 输出目录（运行时生成）
│   └── result_*.json              # 辩论结果文件
│
├── main.py                         # 主程序入口
├── requirements.txt                # Python依赖列表
├── README.md                       # 项目说明文档
├── QUICKSTART.md                   # 快速开始指南
├── .env.example                    # 环境变量示例
└── .gitignore                      # Git忽略文件
```

## 模块功能详解

### 1. config/ - 配置模块

**config.yaml**: 系统主配置文件
- LLM配置：三个Agent的模型、API密钥、参数
- 向量数据库配置：Chroma设置
- RAG配置：文本分块、检索参数
- 辩论配置：轮数、共识阈值
- 经验库配置：存储路径、相关性阈值
- 化学配置：反应类型列表

### 2. data/ - 数据模块

**raw/**: 原始数据
- 存放化学文献（txt, pdf, docx, md格式）
- 用于构建RAG索引

**processed/**: 处理后的数据
- 中间处理结果
- 可选的数据预处理输出

**chroma_db/**: 向量数据库
- 自动生成的Chroma数据库文件
- 包含文档嵌入向量和索引

### 3. database/ - 数据库模块

**vector_store.py** (580行)
- `VectorStore`类：管理Chroma向量数据库
- 功能：文档添加、查询、更新、删除
- 支持相似度搜索和元数据过滤

**rag_system.py** (400行)
- `RAGSystem`类：实现完整的RAG流程
- 集成LlamaIndex和Chroma
- 功能：索引构建、文档加载、检索增强查询

### 4. agents/ - Agent模块

**base_agent.py** (350行)
- `BaseAgent`抽象基类：定义Agent接口
- `AgentResponse`数据类：封装响应
- 提供RAG检索、经验查询、提示增强等通用功能

**llm_agents.py** (450行)
- `OpenAIAgent`: 基于GPT-4的Agent
- `AnthropicAgent`: 基于Claude的Agent
- `GoogleAgent`: 基于Gemini的Agent
- `create_agent()`: Agent工厂函数

**agent_config.py** (200行)
- `AgentConfig`类：配置管理
- 从YAML加载配置并创建Agent
- 提供配置访问接口

### 5. debate/ - 辩论模块

**autogen_setup.py** (300行)
- `AutoGenSetup`类：AutoGen框架配置
- 将自定义Agent包装为AutoGen Agent
- 创建群组聊天和管理器
- `create_termination_function()`: 自定义终止条件

**debate_manager.py** (550行)
- `DebateManager`类：辩论流程管理
- `DebateResult`数据类：封装辩论结果
- 支持AutoGen和手动两种辩论模式
- 监控共识达成、提取推理轨迹

### 6. experience/ - 经验库模块

**experience_store.py** (400行)
- `ExperienceStore`类：经验存储管理
- 功能：添加、查询、删除经验
- 基于Jaccard相似度的经验检索
- 支持导入/导出和统计分析

**experience_extractor.py** (350行)
- `ExperienceExtractor`类：经验提取
- 从辩论结果提取结构化经验
- 计算置信度、提取关键论据
- 验证和合并经验

### 7. utils/ - 工具模块

**logger.py** (250行)
- `Logger`类：日志管理（单例模式）
- `DebateLogger`类：辩论专用日志
- 支持文件轮转和多级别日志

**helpers.py** (400行)
- 配置加载和环境变量替换
- 文件操作（JSON、YAML）
- 组分解析和验证
- 格式化和转换工具

### 8. main.py - 主程序

**MADSystem类** (300行)
- 系统整合和初始化
- 组件管理（RAG、Agent、经验库、辩论）
- 辩论执行和结果保存
- 命令行接口

## 数据流程

```
1. 初始化阶段
   └─> 加载配置 (config.yaml)
   └─> 初始化日志系统
   └─> 构建RAG索引 (data/raw → chroma_db)
   └─> 创建三个LLM Agent
   └─> 加载经验库 (experience_db.json)

2. 辩论阶段
   └─> 输入化学组分
   └─> Agent检索知识 (RAG系统)
   └─> Agent检索经验 (经验库)
   └─> 多轮辩论 (DebateManager)
   └─> 监控共识达成

3. 结果处理阶段
   └─> 提取辩论结果
   └─> 提取经验 (ExperienceExtractor)
   └─> 保存到经验库 (ExperienceStore)
   └─> 生成报告 (outputs/)
   └─> 记录日志 (logs/)
```

## 核心类关系

```
MADSystem
├── RAGSystem (database/)
│   └── VectorStore
├── BaseAgent (agents/)
│   ├── OpenAIAgent
│   ├── AnthropicAgent
│   └── GoogleAgent
├── DebateManager (debate/)
│   └── AutoGenSetup
├── ExperienceStore (experience/)
└── ExperienceExtractor (experience/)
```

## 配置与扩展点

### 易于扩展的部分

1. **添加新的Agent**
   - 继承`BaseAgent`
   - 实现`_init_llm_client()`和`generate_response()`
   - 在`llm_agents.py`中注册

2. **自定义辩论策略**
   - 修改`debate_manager.py`中的辩论逻辑
   - 实现自定义终止条件

3. **扩展经验库**
   - 修改`experience_store.py`中的相似度计算
   - 添加新的经验属性

4. **自定义RAG**
   - 使用不同的嵌入模型
   - 调整检索策略

### 配置文件驱动

大部分行为可通过`config.yaml`调整：
- 模型选择和参数
- 辩论规则
- RAG参数
- 日志级别
- 文件路径

## 运行时生成的文件

```
logs/
├── system.log                    # 系统运行日志
└── debates/
    └── debate_20251220_143052.log  # 每次辩论的详细日志

data/
├── chroma_db/                    # 向量数据库文件
│   ├── chroma.sqlite3
│   └── ...
└── experience_db.json            # 经验库（JSON格式）

outputs/
└── result_20251220_143052.json   # 辩论结果
```

## 代码规范

- **模块化**: 功能明确分离，低耦合
- **注释完整**: 每个类和函数都有详细的文档字符串
- **类型提示**: 使用Python类型注解
- **异常处理**: 完善的错误处理和日志记录
- **可测试性**: 各模块可独立测试

## 性能考虑

- **向量数据库**: 使用Chroma的持久化和索引优化
- **LLM调用**: 缓存和批处理（可扩展）
- **日志轮转**: 防止日志文件过大
- **经验库限制**: 自动清理旧经验

## 安全性

- **API密钥**: 通过环境变量管理，不硬编码
- **.gitignore**: 排除敏感文件
- **输入验证**: 组分和参数验证

---

此结构设计确保了代码的**可维护性**、**可扩展性**和**鲁棒性**，符合软件工程最佳实践。
