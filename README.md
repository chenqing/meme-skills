# Meme Skills

让值得留下的对话成为记录，再让旧记录帮助你继续思考。通过已连接、已授权的 Meme MCP 工作。

## 分工

| Skill | 负责什么 | 依赖 |
| --- | --- | --- |
| [meme-capture · 随手沉淀](skills/meme-capture/SKILL.md) | 识别沉淀时机、保留用户表达、统一承接新记录保存 | 写入需要 meme-mcp；个性化可选 meme-shared |
| [meme-review · 记录回看](skills/meme-review/SKILL.md) | 对照真实新旧记录，找联系、判断变化或未决问题；默认只读 | 读取需要 meme-mcp；保存需要 meme-capture；个性化可选 meme-shared |
| [meme-shared · 表达偏好](skills/meme-shared/SKILL.md) | 管理可选的表达习惯和用户明确选择的偏好 | 从记录采样时需要 meme-mcp；仅保存用户明确设置不需 MCP |
| [meme-mcp · 操作协议](skills/meme-mcp/SKILL.md) | 检索、读取、编辑与标签操作，以及共用写入协议 | 已授权 Meme MCP |
| [meme-project-recap · 项目小结](skills/meme-project-recap/SKILL.md) | 可选工作场景，区分实现、测试、上线和待办 | 保存需要 meme-capture + meme-mcp；历史比较需要 meme-mcp |

capture 负责沉淀；review 负责回看；shared 负责个性化。项目小结只提炼事实，保存交给 capture。所有写入遵循 meme-mcp 的同一份协议，一个请求只有一个保存执行者。

## 让 Agent 安装

默认安装前四项，项目小结按需添加。把这段话发给 Agent：

> 请阅读 https://github.com/chenqing/meme-skills 的 README，将 skills/meme-mcp、skills/meme-capture、skills/meme-shared 和 skills/meme-review 安装到当前客户端支持的个人 Skill 目录，保留各目录的 references 和 agents 文件。先检查已有安装，保留自定义修改并报告冲突；复用现有 Meme MCP 连接。安装不开启自动保存、不初始化个人画像。完成后检查文件与依赖、说明实际加载状态，工具可用时只做读取验证，不写测试记录。

需要项目小结时追加：“同时安装 skills/meme-project-recap 及上述依赖。”只需要读写操作时可单独装 meme-mcp；只需要沉淀时装 meme-mcp + meme-capture。单独下载场景 Skill 不会自动安装依赖。

### Agent 安装步骤

1. 识别客户端及实际执行环境，优先使用宿主已有的 GitHub Skill 安装器，从本仓库 `main` 取得所需目录；可复现安装应固定提交 SHA 并报告版本。
2. 按上表补全实际需要的依赖。将各个 Skill 目录并列安装，保留整个目录里的 `SKILL.md`、`references/` 和 `agents/`；跨 Skill 引用依赖此结构。不能只下载单个 SKILL.md。
3. 目标文件相同就跳过；存在用户修改时保留并报告差异。更新时不要将新旧协议混用：一组依赖须更新到同一提交，任何必要文件冲突未解决前保留旧组，不宣称新版本可用。不要删除用户文件。
4. 安装与 MCP 授权分开。复用现有连接；尚未连接时参照 [Meme 接入文档](https://usememo.cn/docs/)。不要让用户把密钥发到聊天，也不要因为安装而扩权或建立任务。
5. 检查所需文件与相对引用，再用宿主支持的方式检查加载。仅文件存在不代表已激活；需要新会话或重新加载时如实说明。只读验证工具即可，不创建测试记录，不读取整库来试装。

| 客户端 | 常见个人目录，以宿主实际支持为准 |
| --- | --- |
| Codex | `~/.agents/skills/`，或安装器配置的个人目录 |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |

手动安装：GitHub **Code → Download ZIP**，复制 `skills/` 内需要的完整目录及依赖到同一个安装目录，不把整个仓库当作一个 Skill。云端与远程环境需分别安装。

### 从三 Skill 旧版升级

保留 meme-mcp、meme-capture、meme-project-recap 的名称；更新它们并补齐 references。需要回看和个性化再添加 meme-review、meme-shared。已修改的旧文件先比较合并，不强制覆盖。此次升级不修改现有 MCP 连接，也不读取或迁移用户记录。

## 怎么用

- **保存：**“把刚才确定的方案和取舍理由写到 Meme。”目标清楚直接保存，不重复确认。
- **草稿：**“看看这段讨论有什么值得留下的，先别存。”
- **本轮提醒：**“这次讨论中，有值得回看的判断可以提醒我，先给草稿。”用户忽略后不追问。
- **回看：**“看看昨天的 Meme，和以前有没有相连或不同的判断？”有真实证据才形成发现；没有就说明，不硬凑日报。
- **表达习惯：**“记住我的 Meme 草稿尽量保留原话、少打标签，不要读取历史记录。”仅更新明确指定的私有偏好。
- **可选采样：**“从我获授权的记录中学一下写法，先不要保存新记录。”有限采样并说明覆盖范围。
- **项目小结：**“把本项目最近的进展写一小段到 Meme。”只用可见证据，交给 capture 保存一次。

普通聊天不因出现“想法”或“记录”而启动保存。可以显式选择 `$meme-capture` 或 `$meme-review`；自动匹配由宿主决定。这里的规则不承诺跨客户端一致触发，也不自带后台执行器。

## 个性化是可选的

第一次保存可以直接完成，不必先建立画像。用户明确需要时才初始化共享表达设置，区分“写作习惯”和“允许做什么”。样本只能影响前者，不能推断自动保存授权。

个人 profile 放在宿主的账户隔离私有目录，或经用户确认的 `~/.config/meme-skills/accounts/<alias>/profile.md`，不写进仓库或 Skill 安装目录。账户对应不明确时不套用旧画像。公开仓库没有个人记录、画像、凭据或 MCP 返回内容。安装更新不触碰私有数据。

仅本轮有效的提醒许可不跨会话继承。持久文件不保存自动写入授权；需要跨会话执行时由宿主另行管理和授权。

## 开发与验证

```sh
python3 -m unittest discover -s tests -v
```

这个检查覆盖分发文件、相对引用和隔离边界，不能证明模型行为。行为验收场景与实测范围见 [评测说明](tests/behavior.md)。仅在模拟工具和合成记录上测试；不要用生产用户数据做发布测试。

场景设计参考 [flomo Skills](https://help.flomoapp.com/advance/mcp/skill.html)。Meme 的操作协议、偏好存储、失败处理与例子独立编写，使用 Meme 实际工具；不会调用 flomo 专属接口。
