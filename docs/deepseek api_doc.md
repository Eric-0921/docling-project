https://api-docs.deepseek.com/zh-cn/guides/thinking_mode
DeepSeek 模型支持思考模式：在输出最终回答之前，模型会先输出一段思维链内容，以提升最终答案的准确性。

https://api-docs.deepseek.com/zh-cn/guides/multi_round_chat
DeepSeek /chat/completions API 是一个“无状态” API，即服务端不记录用户请求的上下文，用户在每次请求时，需将之前所有对话历史拼接好后，传递给对话 API

https://api-docs.deepseek.com/zh-cn/guides/chat_prefix_completion
对话前缀续写沿用 Chat Completion API，用户提供 assistant 开头的消息，来让模型补全其余的消息。

https://api-docs.deepseek.com/zh-cn/guides/json_mode
在很多场景下，用户需要让模型严格按照 JSON 格式来输出，以实现输出的结构化，便于后续逻辑进行解析。DeepSeek 提供了 JSON Output 功能，来确保模型输出合法的 JSON 字符串。

https://api-docs.deepseek.com/zh-cn/guides/tool_calls
Tool Calls 让模型能够调用外部工具，来增强自身能力。

https://api-docs.deepseek.com/zh-cn/guides/kv_cache
DeepSeek API 上下文硬盘缓存技术对所有用户默认开启，用户无需修改代码即可享用。用户的每一个请求都会触发硬盘缓存的构建。若后续请求与之前的请求在前缀上存在重复，则重复部分只需要从缓存中拉取，计入“缓存命中”。













