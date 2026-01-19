# 项目结构详解

## 目录树

```
MAD/
├── config/                          # 配置文件目录
│   └── config.yaml                 # 主配置文件
│
├── data/                           # 数据目录
│   ├── raw/                        # 原始Markdown文献数据
│   │   └── *.md                   # Markdown格式的化学文献数据
│   └── chroma_db/                  # Chroma向量数据库（运行时生成）
│
├── database/                       # 数据库模块
│   ├── __init__.py                # 模块初始化
│   ├── openai_embedder.py         # OpenAI Embedding封装
│   ├── text_processor.py          # 文本预处理器
│   ├── vector_store.py            # 向量数据库管理
│   └── rag_system.py              # RAG系统实现
│
├── agents/                         # Agent模块
│   ├── __init__.py                # 模块初始化
│   ├── base_agent.py              # Agent基类
│   ├── llm_agents.py              # 四个LLM Agent实现（支持ReAct）
│   ├── agent_config.py            # Agent配置管理
│   ├── react_reasoning.py         # 🆕 ReAct推理引擎和数据结构
│   └── react_agent.py             # 🆕 ReAct Agent基类
│
├── debate/                         # 辩论模块
│   ├── __init__.py                # 模块初始化
│   └── autogen_coordinator.py     # AutoGen辩论协调器
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
│   ├── result_*.json              # 辩论结果文件
│   └── react_trajectory_*.json    # 🆕 ReAct推理轨迹文件
│
├── process_abstracts.py            # [已废弃] 旧版预处理脚本
├── main.py                         # 主程序入口
├── examples.py                     # 使用示例脚本
├── example_react.py                # 🆕 ReAct功能示例脚本
├── test_react.py                   # 🆕 ReAct功能测试脚本
├── requirements.txt                # Python依赖列表
├── README.md                       # 项目说明文档
├── QUICKSTART.md                   # 快速开始指南
├── REACT_QUICKSTART.md             # 🆕 ReAct快速入门指南
├── REACT_CAPABILITY.md             # 🆕 ReAct功能详细文档
├── REACT_SUMMARY.md                # 🆕 ReAct改造总结
├── PROJECT_STRUCTURE.md            # 项目结构详解（本文档）
├── .env.example                    # 环境变量示例
└── .gitignore                      # Git忽略文件
```

## 模块功能详解

### 1. config/ - 配置模块

**config.yaml**: 系统主配置文件
- LLM配置：四个Agent的模型、API密钥、参数
  - Agent1: OpenAI GPT-4o-mini
  - Agent2: xAI Grok-4.1-fast
  - Agent3: Google Gemini-3-pro
  - Agent4: DeepSeek V3.2
  - 每个Agent配置独立的embedding模型
- 向量数据库配置：Chroma设置
- RAG配置：检索与分块参数（top_k、相似度阈值、chunk_size、chunk_overlap）
- 辩论配置：轮数、共识阈值、超时设置
- 经验库配置：存储路径、容量、相关性阈值
- 化学配置：9种反应类型列表（CO2RR, EOR, HER, HOR, HZOR, O5H, OER, ORR, UOR）

### 2. data/ - 数据模块

**raw/**: 原始Markdown文献数据
- 存放Markdown格式的化学文献数据
- 可按反应类型分子目录

**chroma_db/**: 向量数据库
- 自动生成的Chroma数据库文件
- 包含文档嵌入向量和索引

### 3. database/ - 数据库模块

**openai_embedder.py** (约400行)
- `MultiModelEmbedder`类：多模型嵌入API封装
- 支持OpenAI、Voyage AI、Google Gemini等多种嵌入模型
- 根据agent配置动态切换嵌入模型
- 支持批量文本嵌入
- 自动处理API限流和重试
- 支持OpenRouter API和Voyage AI官方SDK两种调用方式

**text_processor.py** (约200行)
- `TextProcessor`类：文本预处理工具
- 功能：
   - 加载Markdown文献并清洗文本
   - 分块处理并保留元数据
- 注意：已整合process_abstracts.py的功能

**vector_store.py** (约350行)
- `VectorStore`类：管理Chroma向量数据库
- 功能：文档添加、查询、更新、删除
- 支持相似度搜索和元数据过滤
- 多集合管理和持久化

**rag_system.py** (约350行)
- `RAGSystem`类：实现完整的RAG流程
- 集成LlamaIndex和Chroma
- 功能：
   - 从data/raw加载Markdown并切分为chunks
   - 构建向量索引（统一分块策略）
  - 检索增强查询
  - 索引持久化和加载
  - 支持4个Agent的独立RAG系统
- 注意：分块由RAG系统内部完成

### 4. agents/ - Agent模块

**base_agent.py** (350行)
- `BaseAgent`抽象基类：定义Agent接口
- `AgentResponse`数据类：封装响应
- 提供RAG检索、经验查询、提示增强等通用功能

**react_reasoning.py** 🆕 (约400行)
- `ActionType`枚举：定义4种动作类型
  - `SEARCH_RAG`: 从RAG系统检索知识
  - `QUERY_EXPERIENCE`: 查询经验库
  - `ANALYZE`: 分析当前信息
  - `CONCLUDE`: 得出最终结论
- `ReActStep`数据类：单步推理（Thought→Action→Observation）
- `ReActTrajectory`数据类：完整推理轨迹
- `ReActEngine`类：推理引擎
  - 工具注册与管理
  - 动作执行与观察
  - LLM响应解析
  - 推理流程控制
- `create_react_prompt()`: 生成ReAct风格提示

**react_agent.py** 🆕 (约350行)
- `ReActAgent`基类：具备ReAct推理能力的Agent
- 继承自`BaseAgent`，集成`ReActEngine`
- 实现4个工具函数：
  - `_tool_search_rag()`: RAG检索工具
  - `_tool_query_experience()`: 经验查询工具
  - `_tool_analyze()`: 分析工具
  - `_tool_conclude()`: 结论工具
- `generate_response_with_react()`: ReAct推理主方法
- `_smart_default_action()`: 智能默认策略
- `save_trajectory()`: 保存推理轨迹

**llm_agents.py** (约500行，已升级)
- `OpenAIAgent`: 基于OpenAI GPT的Agent（支持ReAct）
- `XAIAgent`: 基于xAI Grok的Agent（支持ReAct）
- `GoogleAgent`: 基于Google Gemini的Agent（支持ReAct）
- `DeepSeekAgent`: 基于DeepSeek的Agent（支持ReAct）
- 所有Agent继承自`ReActAgent`
- 每个Agent实现`_call_llm()`方法支持ReAct循环
- `create_agent()`: Agent工厂函数
- 所有Agent通过OpenRouter的OpenAI兼容API调用

**agent_config.py** (200行)
- `AgentConfig`类：配置管理
- 从YAML加载配置并创建Agent
- 提供配置访问接口

### 5. debate/ - 辩论模块

**autogen_coordinator.py** (约520行)
- `AutoGenDebateCoordinator`类：完全基于AutoGen的辩论协调器
- `DebateResult`数据类：封装辩论结果
- 功能：
  - 为每个Agent准备RAG增强提示
  - 创建AutoGen GroupChat和ConversableAgent
  - 使用round_robin发言模式（无需Manager LLM）
  - 自定义终止条件检测（基于共识）
  - 提取完整LLM推理链条（包括thinking过程）
  - 分析辩论结果并达成共识

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

**MADSystem类** (约400行)
- 系统整合和初始化
- 组件管理（RAG、Agent、经验库、辩论）
- 辩论执行和结果保存
- 命令行接口（支持多种参数）

## 数据流程

```
0. 数据准备阶段
   └─> 放置Markdown文献 (data/raw/**/*.md)

1. 初始化阶段
   └─> 加载配置 (config.yaml)
   └─> 初始化日志系统
   └─> 构建RAG索引 (data/raw → chroma_db)
   └─> 创建四个LLM Agent（各配独立embedding）
   └─> 加载经验库 (experience_db.json)

2. 辩论阶段
   └─> 输入金属催化剂元素
   └─> Agent检索知识 (RAG系统)
   └─> Agent检索经验 (经验库)
   └─> 多轮辩论 (AutoGenDebateCoordinator)
   └─> 轮流发言模式 (round_robin)
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
│   ├── XAIAgent
│   ├── GoogleAgent
│   └── DeepSeekAgent
├── AutoGenDebateCoordinator (debate/)
│   ├── ConversableAgent (AutoGen)
│   ├── GroupChat (AutoGen)
│   └── GroupChatManager (AutoGen, 无LLM配置)
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
data/
├── processed/                    # 预处理后的chunks
   │   └── *_chunks.txt             # 由database/text_processor.py生成
├── chroma_db/                    # 向量数据库文件
│   ├── chroma.sqlite3
│   ├── docstore.json            # 文档存储
│   └── ...
└── experience_db.json            # 经验库（JSON格式）

logs/
├── system.log                    # 系统运行日志
└── debates/
    └── debate_20251221_*.log     # 每次辩论的详细日志

outputs/
└── result_20251221_*.json        # 辩论结果文件
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
