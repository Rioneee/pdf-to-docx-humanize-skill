# Reusable Lessons

## Keep One Canonical Heading Map

Derive TOC entries and body headings from the same normalized heading map.
Do not maintain separate heuristics for TOC and body insertion.

## Split Decoration by Page Class

Separate front matter, chapter-start pages, and ordinary body pages into different section regimes.
Apply headers, footers, borders, and page-number styling per section.

## Produce a Sample Before the Full Output

Generate a focused sample DOCX that covers:

- front matter
- TOC
- body start
- image page
- table page
- code page

Use the sample to detect overlap, flow breaks, and decoration mistakes before building the final file.

## Record Page-Class Evidence

Store inspection evidence for the required page classes in both machine-readable and human-readable formats.
Prefer Word page locations plus PDF screenshots when possible.

## Keep the Report Ledger Explicit

Record every candidate in the migration ledger, including:

- page-number styling
- end matter handling
- non-migrated old floating objects

Use a concrete reason for each decision.

## Preserve the Original Inputs

Keep the source PDF, DOCX export, and MinerU bundle untouched.
Write polished outputs to new filenames only.

## Be Careful with PowerShell Encoding

When generating temporary PowerShell scripts that contain Chinese literals, write them as UTF-8 with BOM.
This avoids parser and output decoding issues on Windows.

## Treat Humanize Defaults as the Baseline

Use the local `humanize` skill defaults for RLCR unless the user explicitly overrides them.
Do not hardcode assumptions about direct OpenAI API compatibility.
