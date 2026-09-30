# 贡献指南

感谢参与 agthelm 场景模板共建。

## 我们收什么

- 钉在 **场景 × 行业 × 系统栈** 上的模板（例如「离散制造售后问答 × 钉钉 + 共享盘 + 用友」）
- manifest、连接器配置基线、术语 / 拒答规则、评测**骨架**、兼容矩阵
- schema / 校验工具改进

## 我们不收

- 客户业务数据、评测**实例**、真实组织树
- 无系统栈钉死的泛「行业流程」包
- 要求绕过官方签名、直装生产的改动
- 双边商店 / 自助上架相关设计

## 流程

1. Fork → 分支 → 在 `examples/<id>/` 或 `schema/` 改
2. 本地：`python3 tools/validate.py examples/<id>`
3. PR 描述写清：场景、行业、系统栈、兼容版本、是否含脱敏回流
4. CI 绿 + maintainer review → 合入
5. **签名发布**由官方另做；合进本仓 ≠ 客户可装生产包

## DCO

本仓使用 [Developer Certificate of Origin](https://developercertificate.org/)。每个 commit 须：

```text
Signed-off-by: Your Name <you@example.com>
```

可用 `git commit -s`。提交即表示你按 DCO 证明有权以 Apache-2.0 贡献该内容。

## License

贡献以 **Apache-2.0** 许可。见 [LICENSE](LICENSE)。
