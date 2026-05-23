# humanize 依赖说明

`pdf-to-docx-humanize` 是一个编排型 skill。它负责让 Codex 识别 PDF 文件包、写任务草稿、规划转换流程、推动执行和验证输出。

它不替代 `humanize`。如果你想使用完整自动审查循环，需要另外安装 `humanize` skill 家族。

## 完整模式需要哪些 skill

完整模式需要：

- `humanize`
- `humanize-gen-plan`
- `humanize-refine-plan`
- `humanize-rlcr`

RLCR 是 Ralph-Loop with Codex Review（带 Codex 审查的 Ralph 循环）的缩写。简单说，就是执行、总结、审查、修正的循环。

## 为什么不把 humanize 直接放进这个仓库

主要有三个原因：

1. `humanize` 是独立工作流系统，有自己的脚本、hook（钩子）、审查逻辑和版本节奏。
2. 很多用户可能已经安装了 `humanize`，不应该被这个仓库偷偷覆盖。
3. 本仓库应该专注 PDF 文件包到 DOCX 工作流，不把依赖维护混在一起。

## 如果你已经安装 humanize

直接安装本仓库的 skill，然后在 PDF 文件夹里运行：

```text
$pdf-to-docx-humanize
```

默认最多跑 2 轮 RLCR，除非你明确要求其他轮次。

## 如果你没有安装 humanize

你仍然可以运行：

```text
$pdf-to-docx-humanize
```

但这时只能走降级模式。降级模式可以做：

- 审计输入文件包
- 写 `draft.md`
- 写 `plan.md`
- 做手动复查
- 验证最终 DOCX/PDF

降级模式不能运行真正的 `humanize-rlcr` 门控循环。最终报告里应该明确说明没有跑完整 RLCR。

## 怎么检查本机是否有 humanize

Windows PowerShell：

```powershell
Get-ChildItem $HOME\.codex\skills | Where-Object { $_.Name -like 'humanize*' }
```

macOS 或 Linux：

```bash
ls ~/.codex/skills/humanize*
```

如果只看到其中一两个，而不是四个都存在，完整模式可能仍然不能正常运行。
