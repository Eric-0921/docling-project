---
trigger: manual
---

# Global Rules V1: Engineering & Workflow Synthesis [GLOBAL_V1]

> **[EI] Intervention Protocol**: 本规则汇集了 docling-project 的最佳实践与 Windows 全局配置，旨在作为跨项目的通用工程标准。AI 在生成遵循本规则的回复时，**必须**在内容前加注 `[Eric]`。

## 1. Core Principles (Engineering Discipline)

必须严格遵守以下硬性要求（继承自 Win Global Rules）：

1.  **Communication**: AI MUST plan and respond in Chinese. Comments in code MUST be Chinese.
2.  **File Safety**:
    - File paths MUST be English/ASCII only (No Chinese/Spaces).
    - NO output files in `docs/` or root.
    - **Backup Policy**:
      - 修改关键 Production 文件（如 `database/production/`, 核心脚本）前，必须执行 `cp file file.bak`。
      - **Git Backup**: 修改完成后立即 `git add` & `git commit`。
3.  **Documentation**:
    - `CHANGELOG.md` MUST be updated for _every_ meaningful change (Insert at TOP).
    - `README.md` MUST reflect the current project state.
4.  **Environment Isolation** (Strict Enforcement):
    - **Conda Only**: 必须在所有 Python 脚本入口处添加环境自检代码，强制检查 `CONDA_DEFAULT_ENV`。
    - **Guard Code**:
      ```python
      if os.environ.get('CONDA_DEFAULT_ENV') != 'project_env_name':
          sys.exit("Critical Error: Wrong Environment")
      ```
5.  **AI Decision & Optimization**:
    - **Acceleration**: 优先利用多核 CPU 和 NVIDIA GPU (CUDA) 加速。
    - **Resource Safety**: 预留 10% 显存/内存冗余，避免 OOM。
    - **Logging**: 必须有主动的错误检测反馈，禁止无声失败。

## 2. Advanced Monitoring Protocol (Honest Monitor)

对于耗时任务，拒绝"虚假繁荣"，必须实现 **Rich Information Monitor**：

- **Required Metrics**:
  - 实时性能指标: GPU VRAM, CPU %, RAM %
  - 真实进度项: `Processed: filename.pdf` (严禁基于时间的虚假估算)
  - 错误计数: `Success/Fail/Skip`
  - 关键日志: 显示最近 3 条 Log
- **Behavior**:
  - 程序报错停止时，监控界面必须显式暂停或显示 Failed，**严禁空转**。
  - 允许使用 `tqdm`，但必须反映真实处理数量。

## 3. Workflow Standardization (Turbo Mode)

继承自 V2.0 工作流的最佳实践：

### 3.1 Git Operations

- **Atomic Commits**: `Edit Changelog` -> `Git Add All` -> `Commit` 必须在一个原子操作流中完成。
- **Changelog Logic**: 新日志必须插入到 `[Unreleased]` 锚点下方（使用 `sed`），严禁追加到文件末尾。

### 3.2 Branch Management

- **Start**: 必须先检查工作区干净 (`status --porcelain`)，并确保 `dev` 分支最新。
- **Finish**: 合并前必须通过质量门禁（Lint/Test），且强制使用 `--no-ff` 保留历史。

### 3.3 Trial Run Mechanism (Dry Run)

- 对于耗时 > 3min 或涉及外部 API 的任务，**必须**先执行试运行（`--limit 10`）。
- 验证通过（无 Error/Warning）后方可全量运行。

## 4. Project Structure Governance

- **New Directories**: 创建任何非代码目录（如 `data/`, `logs/`）前，必须先添加到 `.gitignore`。
- **File Naming**: 严禁使用空格、括号等 Shell 不友好字符。
