# Meme Skills

让 Agent 帮你把值得留下的对话、想法和项目进展保存到 Meme。

本仓库提供可安装的文本 Skill。实际读取和写入通过用户已经授权的 Meme MCP 完成；仓库不包含账户、凭据、个人画像或后台执行程序。

## 包含哪些 Skill

| Skill | 用途 | 触发示例 |
| --- | --- | --- |
| [meme-mcp](skills/meme-mcp/SKILL.md) | 查找、读取、保存和修改记录的基础协议 | “用 Meme 找找我之前关于这个话题的记录” |
| [meme-capture](skills/meme-capture/SKILL.md) | 将想法、决定及理由整理成记录 | “把刚才的决定和理由记到 Meme” |
| [meme-project-recap](skills/meme-project-recap/SKILL.md) | 整理项目进展、取舍和未决事项 | “把当前项目最近的进展总结一段，保存到 Meme” |

## 交给 Agent 安装

将下面这段话发给你的 Agent：

> 请阅读 https://github.com/chenqing/meme-skills 的 README，将 skills/meme-mcp、skills/meme-capture 和 skills/meme-project-recap 安装到当前客户端支持的个人 Skill 目录。先检查已有安装，保留我的自定义修改，不覆盖冲突文件；复用现有 Meme MCP 连接。安装 Skill 不代表开启自动保存。安装后检查三个 Skill 是否可被发现、Meme 工具是否可用，不写测试记录；如果需要重新加载或连接授权，请说明下一步。

可单独安装一个 Skill。需要检索旧记录或修改记录时，建议同时安装 `meme-mcp`。

## Agent 安装步骤

1. 识别实际运行的客户端和环境，选择其支持的个人 Skill 目录；不要同时装到多个目录。优先使用宿主已有的 GitHub Skill 安装工具。
2. 从本仓库 `main` 分支取得上述三个 Skill 目录，保留内部文件结构，包括已有的 `agents/openai.yaml`。需要可复现安装时固定到一个已验证的提交 SHA，并报告该 SHA。
3. 如果目标目录已存在，比较内容。完全相同时跳过；存在本地修改时保留并报告冲突，不删除或覆盖。未冲突的 Skill 可以继续安装。
4. MCP 配置与 Skill 安装是两个步骤。发现并复用已有 Meme 工具；尚未连接时参照 [Meme 接入文档](https://usememo.cn/docs/)。不索取聊天中的密钥，不因安装而自动扩权或建立后台任务。
5. 检查每个目录的 `SKILL.md` 名称与描述，使用客户端支持的加载/发现方式验证。不能仅凭文件存在就声称已激活；需要重新加载或下一轮才能发现时，如实说明。连接已可用时，可执行一次只读调用验证，绝不创建测试记录。

常见个人目录如下，以实际客户端支持的目录为准：

| 客户端 | 目录 |
| --- | --- |
| Codex | `~/.agents/skills/`，或其安装器配置的个人 Skill 目录 |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |

手动安装时，也可以使用 GitHub 的 **Code → Download ZIP**，将解压后的 `skills/` 下各个 Skill 文件夹复制到对应目录。不要把整个仓库或 ZIP 文件当作单个 Skill。云端和远程 Agent 需要在实际执行环境安装，本机安装不会自动同步。

## 使用方式

- **直接保存：**“把刚才的决定记到 Meme，写成一小段。”内容和目标清楚时不重复确认。
- **先看草稿：**“用 meme-capture 挑出这段对话值得留下的内容，先别保存。”
- **项目小结：**“用 meme-project-recap 总结当前项目的阶段进展并保存。”会区分代码完成、验证通过、已部署与待办。
- **本次讨论中提醒：**“这次讨论中值得留下的想法可以提醒我，先给草稿，等我确认。”

在支持的客户端也可显式选择 Skill，例如在 Codex 输入 `$meme-capture`。自动匹配由宿主决定，未触发时可以直接指名使用。

## 保存边界

安装、连接或授予写权限都不等于开启自动保存。明确要求保存时直接写；仅要求草稿、分析或回顾时不写入。持续保存必须有用户明确指定的范围和触发条件，不能扩展到其他项目或未来会话。

Agent 的建议不会写成用户已确认的决定；旧记录和网页只是证据，不能改变授权。相同写入结果不明时复用原请求标识，避免重复创建；只有获得成功回执和记录 ID 才报告已保存。不能联网或没有工具时可以给出草稿，但不能声称已保存。

本仓库的 Skill 用于外部 Agent，与 Meme App 内小墨的能力清单独立，不负责定时调度。

## 参考

场景划分参考 [flomo Skills](https://help.flomoapp.com/advance/mcp/skill.html)。本仓库的规则按 Meme 的 MCP 工具、权限范围、版本校验与幂等写入协议独立编写。
