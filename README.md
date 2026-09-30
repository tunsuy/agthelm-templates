# agthelm-templates

行业 × 系统栈**场景模板**的规格、示例与共建仓（Apache-2.0）。

> **这不是应用商店。** 本仓放模板**源**（YAML / 术语 / 评测骨架）与校验工具。企业生产环境只安装经 **agthelm 官方签名**的 tar 包（可出网直下或断网离线导入）。未签名包不得进生产。

配套产品：[agthelm](https://github.com/tunsuy/agthelm)（私有化企业 AI 转型底座）。裁定见 agthelm 仓 `docs/decisions/ADR-004-scenario-templates.md`。

## 仓库结构

```
schema/          manifest 与兼容矩阵 JSON Schema
examples/        示例模板（基线示意，非真实客户数据）
tools/           本地校验脚本
.github/         PR 校验 CI
```

## 快速校验

```bash
# 需要 Python 3.10+ 与 pyyaml、jsonschema
pip install -r tools/requirements.txt
python3 tools/validate.py examples/discrete-mfg-aftersales
```

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。贡献须带 **DCO**（`Signed-off-by`）。合入后由官方策展；**发布签名包**的权利仅在 agthelm 官方。

## 状态

脚手架已开仓。标杆模板随真实交付脱敏回流递增；当前 `examples/` 仅为 schema 可跑通示意。
