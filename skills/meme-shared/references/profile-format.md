# 私有表达偏好格式

这是结构说明，不是预先启用的用户设置。只有用户要求初始化或持久化时才创建私有 `profile.md`，不可复制为公开安装文件。

建议使用 Markdown 加 YAML 元数据：

```yaml
schema_version: 1
account_alias: user-confirmed-alias
updated_at: YYYY-MM-DD
expression_source: explicit_user_preferences_or_authorized_samples
sample_count: 0
sample_window: none
```

正文分为：

- `Expression`：具体表达习惯及依据；不确定项标明，不存原文、完整标签树、记录 ID、凭据或敏感身份推断。
- `Preferences`：用户明确选择及适用范围。无设置时留空，不预填授权。可记录偏好 `on_request` 或 `session_light`，后者每个新会话仍需授权。

保留字段含义：`updated_at` 是偏好文件更新时间，`sample_count` 是本次实际读取的不同记录数；仅凭用户描述配置时为 0，不冒充采样。`sample_window` 记录实际覆盖日期或明确没有采样。

不存自动保存许可、上次提醒时间或本轮完成标志。持久文件描述偏好，不是跨会话执行凭证。更改表达部分不重写 Preferences；不兼容的新 schema 先保留文件，当前任务使用非个性化表达。
