# 工作间工程规范 [WORKSPACE]

> 本规则在 docling-project 工作间内自动加载，无需手动触发。

## 1. 环境隔离 (Environment Isolation)

- **Conda Only**: 必须使用 `doclingprj1` 环境，严禁使用系统 Python
- **Shebang**: 脚本头部必须指定解释器路径或使用 `/usr/bin/env python`

## 2. 长任务托管 (Hosted Execution)

- 耗时 > 5分钟的任务 **必须** 放入 Tmux/Screen
- 编写 `run_job.sh` 封装环境激活和参数设置
- 使用 `tmux new -s job_name` 启动，`Ctrl+B, D` 脱离

## 3. 健壮性设计 (Robustness by Design)

- **Checkpoint**: 可中断恢复，不依赖"一次性成功"
- **Logging**:
  - `stdout`: 给用户看进度 (Rich UI)
  - `file`: 给开发者看错误 (Traceback)
- **Signal Handling**: 优雅处理 `SIGINT`/`SIGTERM`，确保数据落盘

## 4. 网络鲁棒性 (Network Resilience)

- 所有 API 调用必须实现**指数退避重试**
- 可重试: `timeout`, `connection reset`, `502/503/504`
- 不可重试: 认证失败、参数错误

## 5. 预检机制 (Pre-flight Checks)

启动长耗时任务前必须检查：

- 关键库是否可导入 (`json`, `rich`, `openai`)
- 磁盘空间、GPU 状态 (`nvidia-smi`)
- 输出目录是否存在、是否有写权限
