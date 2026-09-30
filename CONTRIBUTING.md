# 贡献指南

感谢参与 agthelm 场景模板共建。参与前请阅读 [行为准则](CODE_OF_CONDUCT.md) 与 [总览](docs/overview.md)。

## 我们收什么

- 钉在 **场景 × 行业 × 系统栈** 上的模板（例如「离散制造售后问答 × 钉钉 + 共享盘 + 用友」）
- `manifest.yaml`、连接器配置基线、术语 / 拒答规则、评测**骨架**、兼容矩阵
- schema / 校验工具 / 文档改进

## 我们不收

- 客户业务数据、评测**实例**、真实组织树或通讯录
- 无系统栈钉死的泛「行业流程」包
- 要求绕过官方签名、直装生产的改动
- 双边商店 / 自助上架相关设计

大改动（新 schema 字段、破坏性变更）请先开 Issue 讨论。

## 开发环境

- Python 3.10+
- `pip install -r tools/requirements.txt`

```bash
python3 tools/validate.py examples/<template-id>
```

## 提交流程

1. Fork 本仓，从 `main` 开分支（建议 `feat/<短名>` 或 `fix/<短名>`）
2. 在 `examples/<id>/` 或 `schema/` / `docs/` 改动
3. 本地校验通过；示例目录须含 `manifest.yaml` 与简短 `README.md`
4. Commit 使用清晰说明，并带 **DCO**（见下）
5. 开 PR，按模板填写：场景、行业、系统栈、兼容版本、是否脱敏回流
6. CI 绿 + maintainer review → 合入
7. **签名发布**由官方另做；合进本仓 ≠ 客户可装生产包

### Commit 建议

- 英文或中文均可，一句话说明「为什么」
- 一个 PR 尽量只做一类事（一个模板 / 一处 schema / 文档）

## DCO

本仓使用 [Developer Certificate of Origin](https://developercertificate.org/)。每个 commit 须包含：

```text
Signed-off-by: Your Name <you@example.com>
```

可用：

```bash
git commit -s -m "Add example for …"
```

提交即表示你按 DCO 证明有权以 Apache-2.0 贡献该内容。

## PR 自检清单

- [ ] `python3 tools/validate.py examples/<id>` 通过（若改了模板）
- [ ] 无客户数据 / 评测实例 / 真实组织信息
- [ ] `metadata.id` 稳定、小写、与目录名一致
- [ ] 兼容矩阵写清系统与版本范围
- [ ] Commit 含 `Signed-off-by`
- [ ] 行为符合 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## License

贡献以 [Apache-2.0](LICENSE) 许可。
