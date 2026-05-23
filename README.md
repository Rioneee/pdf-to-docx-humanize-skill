# PDF to DOCX Humanize Skill

中文优先说明：这是一个给 Codex CLI 使用的 skill。它适合把“已经准备好的 PDF 文件包”交给 Codex 处理，让 Codex 根据原 PDF、PDF 转出的 DOCX、MinerU 解析结果，组织一套更稳的 DOCX 重建、翻译、排版、审查和验证流程。

English summary: this repository provides a Codex skill named `$pdf-to-docx-humanize` for prepared PDF bundles. It audits the bundle, drafts a task, plans the work, optionally runs the `humanize` review loop, and validates the final DOCX/PDF outputs.

## 这个仓库解决什么问题

很多 PDF 转 Word 的结果看起来能打开，但真正阅读时会有这些问题：

- 正文排版错乱
- 图表位置错位
- 文字和图片重叠
- 中文正文里出现大量不该有的空格
- 目录、标题、页眉页脚、公式、表格、代码块不稳定
- 只靠一次转换很难保证质量

这个 skill 的目标不是“神奇地一键完美转换所有 PDF”，而是给 Codex 一套稳定工作流：先识别输入文件，再写任务草稿，再规划，再执行，再审查，再验证。它尤其适合英文书籍、英文论文、SCI 论文、技术 PDF、学位论文、报告等结构化 PDF。

## 你需要准备什么

一个文件夹里最好放齐三类东西：

- 原始 PDF
- PDF 转出来的 DOCX
- MinerU 解压后的文件夹，里面通常有 `.tex` 文件、页面截图、图表截图、图片资源等

示例：

```text
my-document/
  source.pdf
  source-converted.docx
  MinerU_latex_source/
    source.tex
    images/
      page_001.png
      figure_001.png
    tables/
      table_001.png
```

文件名不需要和示例完全一样。skill 会先扫描文件夹，自动识别可能的 PDF、DOCX、TeX 和图片资源。

不要把自己的 PDF、DOCX、论文、书籍或私人资料上传到这个公开仓库。这个仓库只用来安装 skill。

## 最快安装

如果你已经会用 Codex CLI，并且你的 Codex 里有 `$skill-installer`，直接在 Codex 里运行：

```text
$skill-installer install https://github.com/Rioneee/pdf-to-docx-humanize-skill/tree/main/skills/pdf-to-docx-humanize
```

然后重启 Codex。

进入你的 PDF 文件夹后，输入：

```text
$pdf-to-docx-humanize
```

## 从零开始安装

### 1. 安装并登录 Codex CLI

先确保你能正常打开 Codex CLI。CLI 是 Command Line Interface（命令行界面）的缩写。

如果你还没有 Codex CLI，请先按官方方式安装并登录。安装完成后，重启一次终端。

### 2. 安装本 skill

推荐方式是在 Codex 里用 `$skill-installer`：

```text
$skill-installer install https://github.com/Rioneee/pdf-to-docx-humanize-skill/tree/main/skills/pdf-to-docx-humanize
```

安装后重启 Codex。

如果你想手动安装，也可以先克隆本仓库。

Windows PowerShell：

```powershell
git clone https://github.com/Rioneee/pdf-to-docx-humanize-skill.git
cd pdf-to-docx-humanize-skill
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

macOS 或 Linux：

```bash
git clone https://github.com/Rioneee/pdf-to-docx-humanize-skill.git
cd pdf-to-docx-humanize-skill
bash scripts/install.sh
```

手动安装后也要重启 Codex。

## 关于 humanize 依赖

这个 skill 有两种运行模式。

| 模式 | 需要什么 | 会发生什么 |
| --- | --- | --- |
| 完整模式 | 本 skill + `humanize` skill 家族 | Codex 会审计文件、写草稿、生成计划、精修计划、运行 RLCR 审查循环、验证输出。 |
| 降级模式 | 只有本 skill | Codex 会审计文件、写草稿、写计划、做手动复查和输出验证，但不会运行真正的 RLCR 循环。 |

RLCR 是 Ralph-Loop with Codex Review（带 Codex 审查的 Ralph 循环）的缩写，可以理解为“执行一轮，再让另一个审查步骤检查，再继续修”的自动化迭代流程。

完整模式需要这四个 skill：

- `humanize`
- `humanize-gen-plan`
- `humanize-refine-plan`
- `humanize-rlcr`

检查 Windows PowerShell 里是否已经安装：

```powershell
Get-ChildItem $HOME\.codex\skills | Where-Object { $_.Name -like 'humanize*' }
```

检查 macOS 或 Linux：

```bash
ls ~/.codex/skills/humanize*
```

如果四个 skill 都存在，就可以使用完整模式。

如果没有 `humanize`，你仍然可以调用 `$pdf-to-docx-humanize`。它会走降级模式，但必须清楚：降级模式不等于真正跑过 `humanize-rlcr`。如果你追求更稳的质量闭环，建议先安装 `humanize`。

本仓库没有直接内置 `humanize`，原因是 `humanize` 是独立工作流系统，有自己的脚本、审查逻辑和发布节奏。把它混进这个仓库反而会让用户难以更新和排错。

## 使用前检查清单

运行 `$pdf-to-docx-humanize` 前，建议确认：

- Codex CLI 能正常启动。
- 重启 Codex 后能识别 `$pdf-to-docx-humanize`。
- 当前文件夹里有原始 PDF。
- 当前文件夹里有 PDF 转出的 DOCX，若没有也要在任务里说明。
- MinerU 文件夹已经解压，不只是一个 `.zip` 压缩包。
- MinerU 生成的图、表、页面截图没有被删除。
- 如果要跑完整 RLCR，当前文件夹最好是一个本地 git 仓库，并且至少有一次提交。

如果你的 PDF 文件夹还不是 git 仓库，可以在该文件夹里执行：

```bash
git init
git add .
git commit -m "Initial document bundle"
```

这只是创建本地版本记录，不等于上传到 GitHub。不要把没有公开授权的 PDF 推送到公开仓库。

## 怎么调用

进入你的 PDF 文件夹后，在 Codex 里输入：

```text
$pdf-to-docx-humanize
```

如果你想把要求说得更清楚，可以这样写：

```text
$pdf-to-docx-humanize 请把当前文件夹里的 PDF 文件包处理成排版稳定、可阅读的 DOCX。优先参考原 PDF、PDF 转出的 DOCX，以及 MinerU 解压文件夹里的 tex、图片和表格截图。完整模式下 RLCR 最多 2 轮。
```

对于中文译文排版，你也可以加约束：

```text
$pdf-to-docx-humanize 重点避免中文正文内部出现多余空格，避免文字和图片重叠，图表尽量参考 MinerU 截图位置，输出前必须检查 DOCX 和 PDF 的阅读效果。
```

Codex 通常会按下面流程工作：

1. 审计当前文件夹，识别 PDF、DOCX、MinerU、TeX、图片和截图。
2. 写 `draft.md`，说明任务目标、输入文件、输出文件、排版约束和风险。
3. 调用或仿照 `humanize-gen-plan` 生成 `plan.md`。
4. 必要时用 `CMT: ... ENDCMT` 形式给计划加修改意见。
5. 调用或仿照 `humanize-refine-plan` 精修计划。
6. 有 `humanize` 时运行 `humanize-rlcr`，默认最多 2 轮。
7. 验证 DOCX 包结构、页面结构、图表位置、段落空格、页眉页脚、目录、参考文献等。
8. 报告最终文件、通过的检查和残留限制。

## 常见问题

### Codex 里找不到 `$pdf-to-docx-humanize`

先重启 Codex。

然后检查 skill 是否安装到了这里：

```text
~/.codex/skills/pdf-to-docx-humanize
```

Windows 通常是：

```text
%USERPROFILE%\.codex\skills\pdf-to-docx-humanize
```

### 提示缺少 humanize

这说明完整模式需要的 `humanize` skill 家族不全。

你可以先继续使用降级模式，也可以先安装 `humanize`、`humanize-gen-plan`、`humanize-refine-plan`、`humanize-rlcr` 后再重启 Codex。

### RLCR 启动失败

常见原因是当前文件夹不是 git 仓库，或者还没有任何提交。

可以先执行：

```bash
git init
git add .
git commit -m "Initial document bundle"
```

如果文件夹里有私人 PDF，不要把这个仓库推送到公开 GitHub。

### DOCX 排版仍然不理想

请明确告诉 Codex 你最在意的问题，例如：

- 中文正文内部不能有多余空格
- 图表不能和正文重叠
- 不要使用浮动文本框承载正文
- 表格优先用截图还是可编辑表格
- 是否需要页眉页脚、目录、参考文献、公式编号

PDF 转 DOCX 的质量很依赖原始 PDF 结构。复杂扫描件、双栏论文、公式密集文档、跨页表格，通常需要更多人工复核。

## 这个 skill 不做什么

- 不会替你下载论文或书籍。
- 不会把你的 PDF 上传到本仓库。
- 不保证 OCR（Optical Character Recognition，光学字符识别）一定完美。
- 不保证所有翻译、公式、参考文献都无需人工校对。
- 不内置 `humanize`，只负责和它协作。

## 仓库结构

```text
skills/pdf-to-docx-humanize/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
scripts/
  install.ps1
  install.sh
  validate_repo.py
docs/
  humanize-dependency.md
  example-bundle.md
```

## 开发者校验

如果你修改了这个仓库，可以运行：

```bash
python scripts/validate_repo.py
python -m py_compile skills/pdf-to-docx-humanize/scripts/audit_bundle.py
```

## 许可证

MIT License。详见 `LICENSE`。
