# 多Agent化学反应过电势预测系统

## 项目简介

本项目旨在通过多Agent辩论机制，为化学反应废液中的五种主要组分找到产生最低过电势的反应类型。系统采用三个不同的LLM Agent，结合RAG（检索增强生成）技术和AutoGen多Agent辩论框架，通过协作推理达成共识。

## 系统架构

```
MAD/
├── config/              # 配置文件目录
│   └── config.yaml     # 主配置文件
├── data/               # 数据目录
│   ├── raw/           # 原始化学文献数据
│   └── processed/     # 处理后的数据
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
├── main.py            # 主程序入口
├── requirements.txt   # 依赖列表
└── README.md         # 项目说明
```

## 核心功能

### 1. 数据库建立（database/）
- 使用LlamaIndex对化学文献数据进行索引构建
- 采用Chroma向量数据库存储嵌入向量
- 支持三个不同的embedding模型

### 2. Agent定义（agents/）
- **Agent 1**: 基于OpenAI GPT-4
- **Agent 2**: 基于Anthropic Claude
- **Agent 3**: 基于Google Gemini
- 每个Agent配备独立的RAG系统用于检索增强

### 3. 多Agent辩论（debate/）
- 基于Microsoft AutoGen框架实现
- 三个Agent自由辩论直至达成共识
- 确保最终结果和推理轨迹保持一致

### 4. 经验提取（experience/）
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
将化学文献数据放入 `data/raw/` 目录

## 使用方法

### 基本使用

```bash
python main.py --components "组分1,组分2,组分3,组分4,组分5"
```

### 高级选项

```bash
# 指定配置文件
python main.py --config config/custom_config.yaml

# 启用详细日志
python main.py --verbose

# 使用已有经验库
python main.py --use-experience
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
