<<<<<<< HEAD
# Multi-Agent Metal Catalyst Overpotential Prediction System

## Project Overview

This project aims to predict the reaction type that produces the lowest overpotential through a multi-agent debate mechanism, where five metal elements act as catalysts. The system employs four different LLM Agents, combined with RAG (Retrieval-Augmented Generation) technology and the AutoGen multi-agent debate framework, to reach consensus through collaborative reasoning.

## 系统架构

```
MAD/
├── config/              # 配置文件目录
│   └── config.yaml     # 主配置文件
├── data/               # 数据目录
│   ├── raw/           # 原始TSV数据文件
│   ├── processed/     # 切分后的chunks（txt格式）
│   └── chroma_db/     # 向量数据库（运行时生成）
├── database/          # 数据库模块
│   ├── rag_system.py  # RAG系统实现
│   └── vector_store.py # 向量数据库管理
├── agents/            # Agent模块
│   ├── base_agent.py  # Agent基类
│   ├── llm_agents.py  # 四个LLM Agent实现
│   └── agent_config.py # Agent配置
├── debate/            # 辩论模块
│   └── autogen_coordinator.py  # AutoGen辩论协调器
├── experience/        # 经验库模块
│   ├── experience_store.py      # 经验库管理
│   └── experience_extractor.py  # 经验提取
├── utils/             # 工具模块
│   ├── logger.py      # 日志工具
│   └── helpers.py     # 辅助函数
├── main.py            # 主程序入口
├── examples.py        # 使用示例
├── requirements.txt   # 依赖列表
└── README.md         # 项目说明
```

## 核心功能

### 1. 数据预处理（database/text_processor.py）
- 从TSV文件提取abstract列内容（整合后的文本处理器）
- **自动文本清洗**：去除HTML标签、多余空格、编码错误、引用标记等
- 自动添加索引序号
- 每行abstract作为一个独立chunk
- 输出为txt格式供RAG系统使用

### 2. 数据库建立（database/）
- 使用LlamaIndex对处理后的chunks进行索引构建
- 采用Chroma向量数据库存储嵌入向量
- 支持四个不同的embedding模型
- 直接加载预切分的chunks，无需二次分割

### 3. Agent Definition (agents/)
- **Agent 1**: Based on OpenAI GPT-4o-mini
- **Agent 2**: Based on xAI Grok-4.1-fast
- **Agent 3**: Based on Google Gemini-3-pro
- **Agent 4**: Based on DeepSeek V3.2
- Each Agent is equipped with an independent RAG system for retrieval augmentation
- Specialized in analyzing metal catalyst performance and electrochemical reactions

### 4. 多Agent辩论（debate/）
- 基于Microsoft AutoGen框架实现
- 四个Agent自由辩论直至达成共识
- 确保最终结果和推理轨迹保持一致

### 5. 经验提取（experience/）
- 从辩论中提取完整的LLM推理链条（包括thinking模式）
- 提取统一答案和关键论据
- 构建经验库用于后续推理辅助
- 支持经验检索和上下文增强

## 安装指南

### 环境要求
- Python 3.9+
- 至少8GB RAM
- 推荐使用GPU（用于本地embedding模型）

### 安装步骤

1. 克隆项目并进入目录
```bash
cd MAD
```

2. 创建虚拟环境
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置环境变量
创建 `.env` 文件并填入API密钥：
```
OPENAI_API_KEY=your_openai_api_key
XAI_API_KEY=your_xai_api_key
GOOGLE_API_KEY=your_google_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
```

5. 准备数据
将TSV格式的化学文献数据放入 `data/raw/` 目录，确保包含`abstract`列

6. 处理数据
```bash
# 提取abstract并切分chunks（使用整合后的文本处理器）
python -m database.text_processor
```
这会在 `data/processed/` 目录生成处理后的txt文件。

## 使用方法

### 基本使用

### 完整流程

1. **数据预处理**
```bash
# 处理data/raw下的TSV文件，提取abstract列
python -m database.text_processor
```

2. **Run debate system**
```bash
# Specify five metal catalyst elements for debate
python main.py --components "Pt,Pd,Ru,Ir,Rh"
```

### 高级选项

```bash
# Specify configuration file
python main.py --config config/custom_config.yaml --components "Pt,Pd,Ru"

# Skip RAG initialization (quick test)
python main.py --components "Pt,Pd,Ru" --skip-rag

# 查看系统状态
python main.py --status

# 使用示例脚本
python examples.py
```

## 配置说明

所有配置项位于 `config/config.yaml`，主要包括：

- **LLM配置**: 四个Agent的模型选择和参数
- **向量数据库配置**: Chroma数据库设置
- **RAG配置**: 文本分块和检索参数
- **辩论配置**: 轮数、超时、共识阈值
- **经验库配置**: 存储路径和相关性阈值

## 工作流程

1. **初始化阶段**
   - 加载配置和初始化日志系统
   - 构建RAG索引和向量数据库
   - 初始化四个LLM Agent

2. **Debate Phase**
   - Input five metal catalyst elements
   - Four Agents analyze based on RAG and experience store
   - Evaluate catalytic performance, reaction mechanisms, and overpotential
   - Consider metal properties: d-band center, work function, surface energy, etc.
   - 通过AutoGen框架组织多轮辩论
   - 监控共识达成情况

3. **结果提取阶段**
   - 提取最终一致的反应类型和过电势
   - 提取推理轨迹和关键论据
   - 存储到经验库供后续使用

4. **输出阶段**
   - 生成详细报告
   - 可视化辩论过程
   - 保存结果到文件

## 项目特点

✅ **模块化设计**: 功能解耦，易于维护和扩展  
✅ **详细注释**: 代码注释完整，提升可读性  
✅ **鲁棒性强**: 异常处理和错误恢复机制  
✅ **可配置性**: 灵活的YAML配置系统  
✅ **可扩展性**: 易于添加新的LLM或Agent  

## 注意事项

1. 确保API密钥有效且有足够的配额
2. 首次运行需要下载embedding模型，可能需要较长时间
3. 辩论过程可能消耗大量token，注意成本控制
4. 建议定期备份经验库数据

## 许可证

MIT License

## 联系方式

如有问题或建议，请提交Issue或联系项目维护者。

---
**项目创建日期**: 2025年12月20日
=======
# 多Agent化学反应过电势预测系统

## 项目简介

本项目旨在通过多Agent辩论机制，为化学反应废液中的五种主要组分找到产生最低过电势的反应类型。系统采用三个不同的LLM Agent，结合RAG（检索增强生成）技术和AutoGen多Agent辩论框架，通过协作推理达成共识。

## 系统架构

```
MAD/
├── config/              # 配置文件目录
│   └── config.yaml     # 主配置文件
├── data/               # 数据目录
│   ├── raw/           # 原始TSV数据文件
│   ├── processed/     # 切分后的chunks（txt格式）
│   └── chroma_db/     # 向量数据库（运行时生成）
├── database/          # 数据库模块
│   ├── rag_system.py  # RAG系统实现
│   └── vector_store.py # 向量数据库管理
├── agents/            # Agent模块
│   ├── base_agent.py  # Agent基类
│   ├── llm_agents.py  # 三个LLM Agent实现
│   └── agent_config.py # Agent配置
├── debate/            # 辩论模块
│   ├── debate_manager.py    # 辩论管理器
│   └── autogen_setup.py     # AutoGen配置
├── experience/        # 经验库模块
│   ├── experience_store.py      # 经验库管理
│   └── experience_extractor.py  # 经验提取
├── utils/             # 工具模块
│   ├── logger.py      # 日志工具
│   └── helpers.py     # 辅助函数
├── process_abstracts.py  # TSV数据处理脚本
├── main.py            # 主程序入口
├── examples.py        # 使用示例
├── requirements.txt   # 依赖列表
└── README.md         # 项目说明
```

## 核心功能

### 1. 数据预处理（process_abstracts.py）
- 从TSV文件提取abstract列内容
- 自动添加索引序号
- 每行abstract作为一个独立chunk
- 输出为txt格式供RAG系统使用

### 2. 数据库建立（database/）
- 使用LlamaIndex对处理后的chunks进行索引构建
- 采用Chroma向量数据库存储嵌入向量
- 支持三个不同的embedding模型
- 直接加载预切分的chunks，无需二次分割

### 3. Agent定义（agents/）
- **Agent 1**: 基于OpenAI GPT-4o-mini
- **Agent 2**: 基于xAI Grok-4.1-fast
- **Agent 3**: 基于Google Gemini-3-pro
- 每个Agent配备独立的RAG系统用于检索增强

### 4. 多Agent辩论（debate/）
- 基于Microsoft AutoGen框架实现
- 三个Agent自由辩论直至达成共识
- 确保最终结果和推理轨迹保持一致

### 5. 经验提取（experience/）
- 提取辩论过程中的统一答案和推理轨迹
- 构建经验库用于后续推理辅助
- 支持经验检索和上下文增强

## 安装指南

### 环境要求
- Python 3.9+
- 至少8GB RAM
- 推荐使用GPU（用于本地embedding模型）

### 安装步骤

1. 克隆项目并进入目录
```bash
cd MAD
```

2. 创建虚拟环境
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置环境变量
创建 `.env` 文件并填入API密钥：
```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
```

5. 准备数据
将TSV格式的化学文献数据放入 `data/raw/` 目录，确保包含`abstract`列

6. 处理数据
```bash
# 提取abstract并切分chunks
python process_abstracts.py
```
这会在 `data/processed/` 目录生成处理后的txt文件。

## 使用方法

### 基本使用

### 完整流程

1. **数据预处理**
```bash
# 处理data/raw下的TSV文件，提取abstract列
python process_abstracts.py
```

2. **运行辩论系统**
```bash
# 指定五种化学组分进行辩论
python main.py --components "硫酸,氢氧化钠,氯化钠,硝酸,碳酸钙"
```

### 高级选项

```bash
# 指定配置文件
python main.py --config config/custom_config.yaml --components "组分1,组分2,组分3"

# 跳过RAG初始化（快速测试）
python main.py --components "硫酸,氢氧化钠,氯化钠" --skip-rag

# 查看系统状态
python main.py --status

# 使用示例脚本
python examples.py
```

## 配置说明

所有配置项位于 `config/config.yaml`，主要包括：

- **LLM配置**: 三个Agent的模型选择和参数
- **向量数据库配置**: Chroma数据库设置
- **RAG配置**: 文本分块和检索参数
- **辩论配置**: 轮数、超时、共识阈值
- **经验库配置**: 存储路径和相关性阈值

## 工作流程

1. **初始化阶段**
   - 加载配置和初始化日志系统
   - 构建RAG索引和向量数据库
   - 初始化三个LLM Agent

2. **辩论阶段**
   - 输入五种化学组分
   - 三个Agent基于RAG和经验库进行推理
   - 通过AutoGen框架组织多轮辩论
   - 监控共识达成情况

3. **结果提取阶段**
   - 提取最终一致的反应类型和过电势
   - 提取推理轨迹和关键论据
   - 存储到经验库供后续使用

4. **输出阶段**
   - 生成详细报告
   - 可视化辩论过程
   - 保存结果到文件

## 项目特点

✅ **模块化设计**: 功能解耦，易于维护和扩展  
✅ **详细注释**: 代码注释完整，提升可读性  
✅ **鲁棒性强**: 异常处理和错误恢复机制  
✅ **可配置性**: 灵活的YAML配置系统  
✅ **可扩展性**: 易于添加新的LLM或Agent  

## 注意事项

1. 确保API密钥有效且有足够的配额
2. 首次运行需要下载embedding模型，可能需要较长时间
3. 辩论过程可能消耗大量token，注意成本控制
4. 建议定期备份经验库数据

## 许可证

MIT License

## 联系方式

如有问题或建议，请提交Issue或联系项目维护者。

---
**项目创建日期**: 2025年12月20日
>>>>>>> 09731afda1a80e1c6c5cbaa00a68a4a3c0db3a72
