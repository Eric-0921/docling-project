# Instrument Control (仪器控制层)

本目录包含所有直接与硬件交互的代码。

## 模块组成

### `drivers/`

基础驱动层，封装底层通信协议（VISA/Socket）。

- 提供统一的 `connect`, `write`, `query` 接口。
- 处理超时、错误重试和连接保活。

### `experiments/`

具体实验逻辑的实现。

- **Frequency Sweep**: 频率扫描测试。
- **Time Trace**: 随时间变化的信号采集。

## 开发规范

1. **Safety First**: 所有写入命令（Write）前必须确认参数在安全范围内。
2. **Dry Run**: 在实际连接仪器前，使用 `--simulation` 模式测试逻辑。
3. **Logging**: 必须通过标准 Logger 记录所有发送的 SCPI 指令和接收的数据。
