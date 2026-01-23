# AI Adapter (智能接口层)

本层作为 Project 的"大脑"，负责处理自然语言与机器代码之间的转换。

## 功能描述

- **Prompt Engineering**: 包含针对 SCPI 翻译优化的 prompt 模板。
- **Translation Engine**: 这里的代码负责将用户的自然语言需求（例如："将频率设置为 1GHz"）调用 LLM 转换为 `SOURce:FREQuency 1GHz`。
- **Context Injection**: 负责从 `knowledge_base` 中检索相关的手册章节，作为上下文提供给模型。

## 依赖

- DeepSeek V3/R1 API
- OpenAI Compatible SDK
