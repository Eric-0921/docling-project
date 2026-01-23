# 工作间工程规范 [WORKSPACE]

> **[EI] Intervention Protocol**: 本规则在 docling-project 工作间内自动加载。AI 在生成遵循本规则的回复时，**必须**在内容前加注 `[EI]` (Engineering Intervention) 以表明合规性。

## 1. 环境隔离 (Code-Level Enforcement)

AI 在终端和 Tmux 中工作时容易忘记环境，**必须**在所有 Python 脚本入口处添加以下自检代码：

```python
import os, sys
# [AUTO-GENERATED] Environment Guard
if os.environ.get('CONDA_DEFAULT_ENV') != 'doclingprj1':
    print(f"❌ Critical Error: Must run in conda env 'doclingprj1', current: {os.environ.get('CONDA_DEFAULT_ENV')}")
    print("👉 Try: conda activate doclingprj1")
    sys.exit(1)
```

## 2. 任务监控 (Honest Information Monitor)

用户需要真实的进度反馈，严禁"虚假繁荣"。

- **推荐**: 使用 `rich.live` 展示 VRAM Usage, CPU %, Error Count。
- **允许**: 使用 `tqdm` 滚动条，但必须遵守 **Honest Progress** 原则：
  - ✅ **真实计数**: 进度条必须基于实际处理完的 Item。
  - ✅ **异常反馈**: 遇到报错停止时，进度条描述必须更新为 `[FAILED]` 或暂停，严禁在后台报错时前台继续空转。
  - 🚫 **禁止造假**: 严禁使用基于时间的虚假估算 (fake estimation)。

## 3. 长任务托管 (Hosted Execution)

- 耗时 > 5分钟的任务 **必须** 放入 Tmux (`tmux new -s job_name`)。
- 必须实现 `SIGINT` (Ctrl+C) 优雅退出，保存当前进度 Checkpoint。

## 4. 资源红线 (Resource Limits)

- **VRAM**: 保留 10% 冗余，严禁 OOM。
- **Disk**: 写入前检查空间，少于 1GB 停止写入。
- **Cleanup**: 必须在 `finally` 块中清理临时文件。

## 5. 预检机制 (Pre-flight Checks)

启动前必须检查：

1. **环境**: `doclingprj1`
2. **依赖**: 关键库 (`rich`, `pyvisa`)
3. **权限**: 输出目录写权限

## 6. 试运行机制 (Dry Run Protocol)

对于耗时 > 10min 或涉及外部 API 的任务，在全量运行前 **必须** 执行试运行：

1. **抽样**: 使用 `--limit 10` 或随机抽取 5-10 个样本。
2. **验证**: 确认输出文件格式正确，无逻辑错误。
3. **日志**: 检查是否有异常 Warning。

只有试运行通过后，方可启动全量任务。

## 7. 备份策略 (Backup Policy)

**定义**: 关键 Production 文件包括 `database/production/` 下的数据及核心脚本。

- **操作**: 修改前先建立副本 `cp file.ext file.ext.bak_$(date +%s)`。
- **Git**: 修改完成后，**立即** 提交 Git 备份 (`git add ... && git commit`).
