# agthelm-templates

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![DCO](https://img.shields.io/badge/DCO-required-green.svg)](CONTRIBUTING.md#dco)
[![CI](https://github.com/tunsuy/agthelm-templates/actions/workflows/validate.yml/badge.svg)](https://github.com/tunsuy/agthelm-templates/actions/workflows/validate.yml)

**English** | [中文](#agthelm-templates-中文)

Industry × system-stack **scenario templates**: specs, examples, and co-building source.

> **Not an app store.** This repo holds template **sources** (YAML / glossary / eval skeletons) and validators. Production installs only **agthelm-signed** tarballs (online download or air-gapped import). Unsigned packages must not enter production. Merging here does **not** mean a customer can install a production package.

Companion product: [agthelm](https://github.com/tunsuy/agthelm) (private-deploy enterprise AI foundation). Product ruling: `docs/decisions/ADR-004-scenario-templates.md` in that repo.

## Docs

| Doc | What |
|-----|------|
| [docs/overview.md](docs/overview.md) | Lifecycle: source repo → signed package → install |
| [docs/manifest.md](docs/manifest.md) | Manifest field reference |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute, DCO, PR checklist |
| [GOVERNANCE.md](GOVERNANCE.md) | Maintainership and release authority |
| [SECURITY.md](SECURITY.md) | Vulnerability disclosure |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community standards |
| [SUPPORT.md](SUPPORT.md) | Where to get help |
| [CHANGELOG.md](CHANGELOG.md) | Changes |
| [MAINTAINERS.md](MAINTAINERS.md) | Maintainers |

## Layout

```text
schema/          Manifest JSON Schema
examples/        Example templates (baseline sketches, not real customer data)
tools/           Local validators
docs/            Design and field docs
.github/         Issue / PR templates and CI
```

## Quick start

```bash
git clone https://github.com/tunsuy/agthelm-templates.git
cd agthelm-templates
python3 -m venv .venv && source .venv/bin/activate   # optional
pip install -r tools/requirements.txt
python3 tools/validate.py examples/discrete-mfg-aftersales
```

To start a new template: copy `examples/discrete-mfg-aftersales/`, change `metadata.id` / system stack / prompts, then re-run validation.

## Design in one line

Reuse unit = **scenario × industry × system stack**. Templates are “baseline + configure to converge,” not turnkey finished goods. Write-class actions default to **human-in-the-loop**.

## Status

Repo scaffold is live. `examples/` currently pass schema checks as illustrations; desensitized customer baselines grow as pilots land.

## License

[Apache License 2.0](LICENSE).

---

# agthelm-templates（中文）

[English](#agthelm-templates) | **中文**

行业 × 系统栈**场景模板**的规格、示例与共建仓。

> **这不是应用商店。** 本仓放模板**源**（YAML / 术语 / 评测骨架）与校验工具。企业生产环境只安装经 **agthelm 官方签名**的 tar 包（可出网直下或断网离线导入）。未签名包不得进生产。合进本仓 ≠ 客户可装生产包。

配套产品：[agthelm](https://github.com/tunsuy/agthelm)（私有化企业 AI 转型底座）。产品侧裁定见该仓 `docs/decisions/ADR-004-scenario-templates.md`。

## 文档导航

| 文档 | 说明 |
|------|------|
| [docs/overview.md](docs/overview.md) | 模板生命周期：源仓 → 签名包 → 装机 |
| [docs/manifest.md](docs/manifest.md) | Manifest 字段说明 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 如何贡献、DCO、PR 清单 |
| [GOVERNANCE.md](GOVERNANCE.md) | 维护与发布权 |
| [SECURITY.md](SECURITY.md) | 安全披露 |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 社区行为准则 |
| [SUPPORT.md](SUPPORT.md) | 求助渠道 |
| [CHANGELOG.md](CHANGELOG.md) | 变更记录 |
| [MAINTAINERS.md](MAINTAINERS.md) | 维护者 |

## 仓库结构

```text
schema/          Manifest JSON Schema
examples/        示例模板（基线示意，非真实客户数据）
tools/           本地校验脚本
docs/            设计与字段说明
.github/         Issue / PR 模板与 CI
```

## 快速开始

```bash
git clone https://github.com/tunsuy/agthelm-templates.git
cd agthelm-templates
python3 -m venv .venv && source .venv/bin/activate   # 可选
pip install -r tools/requirements.txt
python3 tools/validate.py examples/discrete-mfg-aftersales
```

新建模板：复制 `examples/discrete-mfg-aftersales/`，改 `metadata.id` / 系统栈 / prompt，再跑校验。

## 设计要点（一句话）

复用单元 = **场景 × 行业 × 系统栈**；模板是「基线 + 改配置收敛」，不是交钥匙成品。写类动作默认**人在环**。

## 状态

脚手架已开仓。`examples/` 当前为 schema 可跑通示意；真实交付脱敏标杆随试点回流递增。

## License

[Apache License 2.0](LICENSE)。
