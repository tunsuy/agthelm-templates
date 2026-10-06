# Manifest 字段说明

Schema 文件：[`schema/manifest.schema.json`](../schema/manifest.schema.json)  
`apiVersion`: `templates.agthelm.io/v1alpha1` \| `templates.agthelm.io/v1beta1` · `kind`: `ScenarioTemplate`

`v1beta1` 为纯增量（v1alpha1 包仍可校验通过）；新增字段见下文标 **v1beta1** 的段落。

## metadata

| 字段 | 必填 | 说明 |
|------|------|------|
| `id` | 是 | 稳定 ID，小写 `[a-z][a-z0-9_-]{1,63}`，与目录名一致 |
| `name` | 是 | 展示名 |
| `version` | 是 | semver，如 `0.1.0` |
| `description` | 否 | 简述；勿写入客户隐私 |
| `industry` | 否 | 行业切片，如 `discrete-manufacturing` |
| `scenario` | 否 | 场景名，如 `aftersales-qa` |

## spec.entry

入口通道与 handler。

- `channel`: `dingtalk.bot` \| `feishu.bot` \| `wecom.bot` \| `web` \| `api`
- `handler`: 逻辑处理名（字符串）

## spec.sources

知识源**角色**列表（非客户实例路径）。

- `type`: `feishu.wiki` \| `dingtalk.wiki` \| `smb` \| `confluence` \| `local`
- `role`: 场景内角色，如 `manuals` / `faq`
- `notes`: 可选说明
- `label`:（**v1beta1**）集合建议可读名（如「产品手册」）——安装方按角色在本库找同名或同类集合

## spec.acl_scope

- `mode`: `source_sync`（跟源端权限）或 `pattern_remap`（规则模式，部门树逐客户重绑）
- `notes`: 可选

## spec.prompt

- `system`: 系统提示词基线
- `refuse_rules`: 拒答规则字符串列表

## spec.tools

允许的工具枚举子集：`retrieve` · `cite` · `refuse` · `hitl_write`

## spec.eval_set

- `skeleton_count`: 评测骨架题量（只描述结构规模）
- `notes`: 明确「实例留在客户域」
- `items`:（**v1beta1**）结构化考题行，每行 `question`（必填）+ `expected`（可选）；
  `expected` 空 = 该题期望拒答。有 `items` 时 `skeleton_count` 仅作兼容统计

## spec.glossary（可选，**v1beta1**）

场景术语表结构化行，渲染进系统提示的「场景术语表」段：

- `term` / `definition` 均必填非空

## spec.actions（可选，**v1beta1**）

动作段白名单（条目级自描述：标签与写分级随包走）：

- `system` / `action`: 键，`^[a-z][a-z0-9_-]{0,63}$`
- `systemLabel` / `actionLabel`: 展示名（必填非空）——其他客户拿到模板即可读
- `write`: `true` = 改数据，安装后须走写操作确认闸

安装方在自己的操作目录里对键；对不上的条目诚实降级（展示但不可勾选），不静默吞。

## spec.sla

- `sync_hours_max`: 知识同步时限（小时）
- `cite_precision_min`: 引用可核目标（0–1）

## spec.compatibility

导入时硬校验用。每项：

- `system`: 系统标识（如 `dingtalk`、`yonyou-u8`）
- `versions`: 支持范围字符串（如 `6.5-7.x`、`*`）

## spec.hitl（可选）

- `write_actions`: `none` \| `im_confirm` \| `webhook`
- `notes`: 写动作边界说明

## 校验

```bash
python3 tools/validate.py examples/<id>
```
