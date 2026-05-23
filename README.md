# PDF to DOCX Humanize Skill

Turn a prepared PDF bundle into a polished DOCX workflow in Codex.

This is a Codex skill for people who already have three local inputs for one document:

- the original PDF
- a PDF-to-DOCX export
- a MinerU extraction folder with the `.tex` file and figure/table/page screenshots

The skill asks Codex to inspect those files, write a concrete task draft, generate and refine an implementation plan, run a bounded review loop when `humanize` is available, and validate the final DOCX/PDF artifacts before reporting success.

## What You Get

- A reusable Codex skill named `$pdf-to-docx-humanize`
- A bundle audit script that finds PDFs, DOCX files, TeX files, and extracted images
- A workflow for books, journal papers, theses, and other structured PDFs
- Default review-loop limit of 2 rounds
- Clear handling for the external `humanize` dependency

This repository does not include any sample PDF, book, article, or converted document. It only contains the skill and installation helpers.

## Quick Start

### 1. Install Codex

Install and sign in to the Codex CLI first. If you do not have Codex yet, follow the official Codex installation guide for your system.

After Codex works, restart your terminal once.

### 2. Choose Full Mode or Fallback Mode

This skill has two operating modes:

| Mode | What you need | What happens |
| --- | --- | --- |
| Full mode | This skill plus the `humanize` skill family | Codex audits, drafts, plans, refines, runs the RLCR loop, and validates outputs. |
| Fallback mode | Only this skill | Codex audits, drafts, plans, performs manual review passes, and validates outputs, but does not run the real RLCR loop. |

Use full mode when possible. Use fallback mode only when you cannot install `humanize` yet.

### 3. Check or Install the `humanize` Skill Family

For the full workflow, this skill expects these Codex skills to exist:

- `humanize`
- `humanize-gen-plan`
- `humanize-refine-plan`
- `humanize-rlcr`

Check on Windows PowerShell:

```powershell
Get-ChildItem $HOME\.codex\skills | Where-Object { $_.Name -like 'humanize*' }
```

Check on macOS or Linux:

```bash
ls ~/.codex/skills/humanize*
```

If all four folders exist, continue.

If you do not have it, install `humanize` from its own distribution or repository first. In Codex, the usual pattern is:

```text
$skill-installer install <humanize GitHub URL or repository path>
```

You need all four skill folders listed above. This repository intentionally does not vendor `humanize`, because `humanize` is a separate workflow system with its own scripts and release cycle.

If `humanize` is missing, `$pdf-to-docx-humanize` can still audit the bundle and ask Codex to run a manual draft/plan/review fallback, but the real RLCR review loop requires `humanize`.

RLCR means Ralph-Loop with Codex Review, an iterative loop where one pass implements the plan and another pass reviews the result.

### 4. Install This Skill

Recommended inside Codex:

```text
$skill-installer install https://github.com/Rioneee/pdf-to-docx-humanize-skill/tree/main/skills/pdf-to-docx-humanize
```

Then restart Codex so it picks up the new skill.

Manual install on Windows:

```powershell
git clone https://github.com/Rioneee/pdf-to-docx-humanize-skill.git
cd pdf-to-docx-humanize-skill
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

Manual install on macOS or Linux:

```bash
git clone https://github.com/Rioneee/pdf-to-docx-humanize-skill.git
cd pdf-to-docx-humanize-skill
bash scripts/install.sh
```

Restart Codex after manual installation.

### 5. Prepare Your Document Folder

Create one local folder for one source document:

```text
my-paper/
  original.pdf
  original-converted.docx
  MinerU_latex_.../
    *.tex
    images/
    tables/
    ...
```

The filenames do not have to match this example. The skill audits the folder and identifies likely roles.

Keep private PDFs local. You do not need to upload your document to this GitHub repository.

### 6. Run the Skill

Open Codex in the document folder and send:

```text
$pdf-to-docx-humanize
```

For a more explicit request:

```text
$pdf-to-docx-humanize Convert this prepared PDF bundle into a polished DOCX. Use the source PDF, converted DOCX, and MinerU extraction folder. Keep the RLCR maximum at 2 rounds.
```

Codex should then:

1. Audit the folder.
2. Create `draft.md`.
3. Generate `plan.md`.
4. Add any needed `CMT: ... ENDCMT` comments.
5. Refine the plan.
6. Run `humanize-rlcr` with at most 2 rounds when available.
7. Validate the final DOCX/PDF.
8. Report final files and remaining limitations.

## Beginner Checklist

Before running the skill, check these items:

- Codex opens successfully.
- `$pdf-to-docx-humanize` appears as an available skill after restart.
- The document folder contains one original PDF.
- The document folder contains one converted DOCX, if available.
- The document folder contains the unpacked MinerU folder, not just the `.zip`.
- If you want the full loop, the four `humanize*` skills are installed.
- If RLCR is used, the document folder is a local git repository with at least one commit.

To make a local git repository without publishing anything:

```bash
git init
git add .
git commit -m "Initial document bundle"
```

Do not push private or copyrighted PDFs to GitHub unless you have the right to publish them.

## 中文快速开始

这个仓库提供一个 Codex skill：`$pdf-to-docx-humanize`。它适合你已经准备好了一个 PDF 处理文件夹的情况：

- 原始 PDF
- PDF 转出来的 DOCX
- MinerU 解压后的文件夹，里面有 `.tex`、图片、表格截图等

最简单流程：

1. 先确保 Codex CLI 能正常打开。
2. 如果要完整自动审查循环，先安装 `humanize`、`humanize-gen-plan`、`humanize-refine-plan`、`humanize-rlcr`。
3. 在 Codex 里安装本 skill：

```text
$skill-installer install https://github.com/Rioneee/pdf-to-docx-humanize-skill/tree/main/skills/pdf-to-docx-humanize
```

4. 重启 Codex。
5. 进入你的 PDF 文件夹。
6. 在 Codex 里输入：

```text
$pdf-to-docx-humanize
```

如果没有 `humanize`，这个 skill 仍然会尽量做审计、起草、规划和手动复查，但完整的 RLCR 自动审查循环必须依赖 `humanize`。

不要把自己的 PDF 上传到这个公开仓库。这个仓库只是安装 skill 用的。

## What This Skill Does Not Do

- It does not download papers for you.
- It does not include `humanize`.
- It does not guarantee perfect OCR or translation.
- It does not publish your PDF files.
- It does not replace final human proofreading for important documents.

## Troubleshooting

`$pdf-to-docx-humanize` is not found:

- Restart Codex after installation.
- Check that the skill was copied to `~/.codex/skills/pdf-to-docx-humanize`.
- On Windows, that is usually `%USERPROFILE%\.codex\skills\pdf-to-docx-humanize`.

`humanize` is missing:

- Install the four `humanize*` skills from the `humanize` distribution.
- Restart Codex.
- Re-run `$pdf-to-docx-humanize`.

RLCR refuses to start:

- RLCR usually requires a clean local git repository with at least one commit.
- Commit the initial local bundle first.
- Keep `.humanize/` out of public commits unless the `humanize` documentation says otherwise.

The output DOCX layout is wrong:

- Make sure the MinerU extraction folder is unpacked and visible in the same project folder.
- Keep figure/table screenshots from MinerU.
- Tell Codex the most important layout constraint directly, for example: "do not insert internal spaces inside Chinese body text" or "avoid floating body text boxes".

## Repository Layout

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

## Development

Run validation locally:

```bash
python scripts/validate_repo.py
python -m py_compile skills/pdf-to-docx-humanize/scripts/audit_bundle.py
```

## License

MIT License. See `LICENSE`.
