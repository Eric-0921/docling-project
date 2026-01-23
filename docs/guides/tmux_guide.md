# Tmux 使用指南 (Tmux Quick Reference)

## 1. 什么是 Tmux？
Tmux 是一个终端复用器，允许您在一个终端窗口中运行多个会话，并且可以 **断开连接后保持进程运行**。

---

## 2. 核心概念

| 概念 | 说明 |
|:---|:---|
| **Session** | 会话，包含一个或多个窗口。断开 SSH 后会话仍在运行。 |
| **Window** | 窗口，类似浏览器的标签页。 |
| **Pane** | 面板，一个窗口可以分割成多个面板。 |

---

## 3. 常用命令

### 3.1 会话管理
```bash
# 创建新会话 (带名称)
tmux new -s my_session

# 列出所有会话
tmux ls

# 重新连接到会话 (最重要!)
tmux attach -t my_session

# 断开但保持会话运行 (在 tmux 内部)
Ctrl+B, 然后按 D

# 杀死会话
tmux kill-session -t my_session
```

### 3.2 窗口操作 (在 tmux 内部)
所有快捷键以 `Ctrl+B` 开头，按完后松开再按下一个键：

| 快捷键 | 功能 |
|:---|:---|
| `Ctrl+B` `c` | 创建新窗口 |
| `Ctrl+B` `n` | 切换到下一个窗口 |
| `Ctrl+B` `p` | 切换到上一个窗口 |
| `Ctrl+B` `数字` | 切换到指定编号的窗口 |

### 3.3 面板操作
| 快捷键 | 功能 |
|:---|:---|
| `Ctrl+B` `%` | 垂直分割 |
| `Ctrl+B` `"` | 水平分割 |
| `Ctrl+B` `方向键` | 在面板间切换 |
| `Ctrl+B` `x` | 关闭当前面板 |

### 3.4 滚动查看历史
```
Ctrl+B, 然后按 [
```
进入滚动模式后：
- 使用 **方向键** 或 **PgUp/PgDown** 滚动
- 按 `q` 退出滚动模式

---

## 4. 典型工作流

### 场景：运行长任务
```bash
# 1. 创建会话
tmux new -s translation_job

# 2. 激活环境并运行
conda activate doclingprj1
cd /home/tseng/git/docling-project
PYTHONPATH=. python ai_adapter/translation_agent/main.py

# 3. 断开 (任务继续运行)
Ctrl+B, D

# 4. 稍后重新连接查看
tmux attach -t translation_job
```

### 场景：SSH 断开后恢复
```bash
# 重新 SSH 登录后
tmux ls                        # 查看有哪些会话
tmux attach -t translation_job # 重新连接
```

---

## 5. 注意事项
1. **不要用 `exit` 退出** - 这会终止会话和进程。用 `Ctrl+B D` 断开。
2. **会话名称要有意义** - 便于识别多个会话。
3. **服务器重启会清除所有会话** - Tmux 无法在服务器重启后恢复。

---

## 6. 速查卡
```
┌─────────────────────────────────────────────┐
│  Tmux 速查                                  │
├─────────────────────────────────────────────┤
│  tmux new -s NAME     创建会话              │
│  tmux attach -t NAME  重新连接              │
│  tmux ls              列出会话              │
│  Ctrl+B D             断开 (不终止)         │
│  Ctrl+B [             滚动模式              │
└─────────────────────────────────────────────┘
```
