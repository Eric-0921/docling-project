---
trigger: model_decision
description: when writing code to control R&S SMB100A signal generator or OE1022D lock-in amplifier
---

# SCPI 设备控制规则 [TRIGGER]

> 本规则在 AI 编写 SMB100A 或 OE1022D 控制代码时自动触发。

## 核心原则

1. **Always use PyVISA** for instrument control
2. **Protect SCPI Commands**: Use exact syntax, do NOT translate
3. **Verify Connectivity**: Always include `*IDN?` connection check

## 知识库使用流程

**必须先查询知识库后再编写代码**：

1. **搜索命令**:
   ```bash
   python .agent/skills/scpi_expert/tools/query_kb.py "search term"
   ```
2. **阅读文档**: 使用 `view_file` 查看返回的 Markdown 内容
3. **编写代码**: 注释中标注命令来源

## 代码规范

- Python: `pyvisa` + `pyserial`
- **Error Protocol**: 必须实现以下错误检查函数，并在关键指令后调用：
  ```python
  def check_inst_errors(inst):
      # 必须循环读取直到错误队列为空
      errors = []
      while True:
          err = inst.query('SYST:ERR?')
          code = int(err.split(',')[0])
          if code == 0: break
          errors.append(err)
      if errors: raise RuntimeError(f"SCPI Errors: {errors}")
  ```
- 变量名/注释中标注单位 (Hz, dBm, V)

## 示例模式

```python
import pyvisa

rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP::192.168.1.10::INSTR')

# 检查连接
print(inst.query('*IDN?'))

# 设置频率 (命令来源: :SOURce:FREQuency:CW)
inst.write(':FREQ 100MHz')

# 检查错误
print(inst.query('SYST:ERR?'))
```
