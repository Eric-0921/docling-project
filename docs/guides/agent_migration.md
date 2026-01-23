项目从 Antigravity AI IDE 迁移到 ChatGPT / Codex：对比与迁移指南

1. 概述

  本文档面向已经在 Antigravity（原项目中位于 `.agent/` 的 skills、workflows、knowledge_base）中建立过 agent 的开发者。目标是说明 Antigravity 的概念如何映射到以 ChatGPT/Codex 为基础的开发方式，给出可执行的迁移路线和示例。

2. 核心概念对比（高层）

  - Antigravity: 内建的 agent 框架，通常包含 `skills`（技能文档 + knowledge_base）、`rules`、`workflows`、以及 IDE 层的可视化调试与部署。许多东西以文件/目录组织并由平台运行时解析执行。
  - ChatGPT / Codex: 模型驱动的对话与代码生成平台。没有统一的“skill runtime”框架，更多通过将知识、规则和工具调用封装为 prompt、system message、或中间层运行时（adapter）来实现 agent 行为。

3. 具体映射建议

  - Skill（SKILL.md + knowledge_base） -> Prompt 模板 + 元数据 JSON
    - 把每个 skill 的说明、示例交互、必需的上下文（slots）抽成 prompt 模板（system + user + few-shot examples）。
  - Workflows -> Orchestration 脚本或状态机
    - Antigravity 的可视化流程建议用 Python 脚本、state machine 库（如 `transitions`）、或简单的 step runner 来实现。
  - Rules -> 验证器或消息过滤器
    - 将规则实现为运行时前/后处理器：输入验证、意图判定、输出校验。
  - Tools（外部 API / 执行）-> Tool 接口 + function-calling（若使用 OpenAI function-calling）

4. 自定义能力与差异（重点）

  - 可扩展性：Antigravity 偏向“平台内扩展”（依赖 IDE），而 ChatGPT/Codex 更偏“代码化扩展”——开发者自行定义適配层（adapter）和工具。
  - 调试体验：Antigravity 可能有可视化追踪、inspect；ChatGPT 需要靠日志、mock 输入/输出、或本地 replay 来调试。
  - 部署方式：Antigravity 一体化；ChatGPT 迁移后通常部署自有运行时（serverless、容器）并通过 OpenAI API 调用模型。
  - 自定义规则与治理：在 ChatGPT 方案中，你要显式实现规则/安全检查（在 Antigravity 中可能是平台功能）。

5. 推荐迁移步骤（实践）

  1. 清点现有资源：列出 `.agent/skills/*`、`.agent/workflows/*`、以及 knowledge_base 的索引文件。
  2. 为每个 skill 创建一个 prompt 模板文件（例如 `agents/skills/<skill>/prompt.md`）和一个元数据文件 `meta.json`（参数、示例输入/输出）。
  3. 实现一个运行时适配器（Python）：负责加载 prompt 模板、注入上下文、调用 OpenAI Chat API、并将输出交给后处理器/规则引擎。
  4. 将 workflows 翻译为 orchestration 脚本（或规则化 state machine），并在本地用单元测试覆盖主要分支。
  5. 逐步替换：先把少量非关键 skill 迁移并在测试环境中验证行为，再扩展到全部 skill。

6. 建议仓库结构（示例）

  - agents/
    - skills/
      - <skill_name>/
        - prompt.md        # system + user + few-shot
        - meta.json        # 参数说明、示例输入/输出
    - workflows/
      - <flow>.py         # orchestration 或 state machine
    - runtime/
      - adapter.py        # 提示加载、API 调用、工具路由
  - tools/
    - query_kb.py         # 查询现有知识库的工具（可复用 `.agent/knowledge_base`）

7. 示例：prompt 模板与最小运行时（简要）

  - prompt.md（示例）

    System: 你是一个专注于仪器控制的助手，遵守安全规则：不要执行危险操作。

    User: 以下是设备状态：{device_state}。请给出下一步建议。

    Example:
    User: 状态 A -> Response: ...

  - 最小 Python 调用示例（使用 OpenAI Python 客户端）

    ```python
    import os
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system = open('agents/skills/foo/prompt.md').read()
    user_input = "设备温度 45C, 模式 X"

    messages = [
      {"role": "system", "content": system},
      {"role": "user", "content": user_input},
    ]

    resp = client.chat.completions.create(model='gpt-4o-mini', messages=messages)
    print(resp.choices[0].message.content)
    ```

8. 常见注意事项

  - 把可执行逻辑放在运行时/工具层，prompt 保持声明式与示例驱动。
  - 为关键 skill 写单元测试（mock OpenAI 返回），以便回归检测。
  - 记录安全/合规规则，放入规则引擎作为前后处理步骤。

9. 下一步建议（我可以代工的事项）

  - 把 `.agent/skills` 的 SKILL.md 自动解析成 prompt 模板与 meta.json（脚本化）。
  - 提供一个 `agents/runtime/adapter.py` 的可运行实现（包含示例环境变量与依赖说明）。
  - 将 workflows 转成 Python 脚本或 state machine 实现，并附单元测试。

如果你同意，我可以先把 `agents/README.md` 和一个最小 `adapter.py` 草稿生成到仓库里，随后把部分 skill 自动转换为 prompt 模板。
