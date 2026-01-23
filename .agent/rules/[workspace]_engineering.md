# 工作间工程规范 [WORKSPACE]

> 本规则在 docling-project 工作间内自动加载，无需手动触发。

## 1. 环境隔离 (Code-Level Enforcement)

AI 在 Tmux 中工作时容易忘记环境，**必须**在所有 Python 脚本入口处添加以下自检代码：

```python
import os, sys
# [AUTO-GENERATED] Environment Guard
if os.environ.get('CONDA_DEFAULT_ENV') != 'doclingprj1':
    print(f"❌ Critical Error: Must run in conda env 'doclingprj1', current: {os.environ.get('CONDA_DEFAULT_ENV')}")
    print("👉 Try: conda activate doclingprj1")
    sys.exit(1)
```

## 2. 任务监控 (Rich Information Monitor)

用户不需要虚假的进度条，通过 `rich.live` 表格展示**实时状态快照**：

- **必须展示的信息**：
  - **当前项**: 正在处理的具体文件名/页码 (`Current: page_12.pdf`)
  - **性能指标**: VRAM Usage (GB), CPU %, RAM %
  - **错误计数**: 成功/失败/跳过 (`S:10 / F:2 / SK:0`)
  - **最近日志**: 显示最后 3 条关键日志

- **禁止的行为**：
  - 🚫 估算 "剩余时间" (除非是简单的线性循环)
  - 🚫 简单的 `tqdm` 滚动条 (信息量太低)

## 3. 长任务托管 (Hosted Execution)

- 耗时 > 5分钟的任务 **必须** 放入 Tmux
- 使用 `tmux new -s job_name` 启动
- 必须实现 `SIGINT` (Ctrl+C) 优雅退出，保存当前进度 Checkpoint

## 4. 资源红线 (Resource Limits)

- **VRAM**: 保留 10% 冗余，严禁 OOM。
- **Disk**: 写入前检查空间，少于 1GB 停止写入。
- **Cleanup**: 必须在 `finally` 块中清理临时文件 (`/tmp/docling_*`)。

## 5. 预检机制 (Pre-flight Checks)

启动前必须检查：

1. **环境**: `doclingprj1` (由代码强制)
2. **依赖**: 关键库 (`rich`, `pyvisa`) 是否可导入
3. **权限**: 输出目录是否有写权限
