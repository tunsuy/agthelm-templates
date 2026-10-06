# crm-customer-assistant（示例）

v1beta1 增量字段示意模板（glossary / eval_set.items / actions / sources[].label），用于跑通新 schema。**不是**已交付真实单脱敏回流。

| 维度 | 值 |
|------|-----|
| 场景 | 客户管理销售助理 |
| 行业 | 通用服务 |
| 系统栈 | 飞书 + CRM + 邮件 |
| 写动作 | 人在环确认（跟进记录 / 报价单） |

动作段为条目级自描述：`systemLabel` / `actionLabel` / `write` 随包走，安装方在自己的操作目录里对键；对不上的条目诚实降级（展示但不可勾选），不静默吞。

生产安装：仅官方签名 tar；本目录 YAML 不能直装客户机房。
