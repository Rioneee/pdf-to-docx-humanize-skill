---
name: pdf-to-docx-humanize
description: Orchestrate PDF-bundle conversion into polished DOCX outputs from a prepared source PDF, PDF-to-DOCX export, and MinerU extraction folder. Use when Codex needs to audit the bundle, draft the task, route it through humanize-gen-plan, humanize-refine-plan, and humanize-rlcr, and validate the final DOCX/PDF for books, SCI papers, theses, or other structured PDFs.
---

# PDF to DOCX Humanize

## Overview

Turn a prepared PDF bundle into a polished DOCX through the `humanize` workflow. Treat the bundle as the source of truth, then draft, plan, refine, run RLCR, and validate before claiming completion.

## Required Inputs

- Source PDF
- PDF-to-DOCX export
- MinerU unpacked folder with `tex`, images, tables, and screenshots

## Dependencies

For the full workflow, prefer the `humanize` skill family:

- `humanize`
- `humanize-gen-plan`
- `humanize-refine-plan`
- `humanize-rlcr`

If those skills are missing, do not pretend the RLCR loop ran. Fall back to a manual draft, plan, review, and validation sequence, and clearly report that the gate-controlled `humanize` loop was not available.

## Workflow

1. Audit the bundle.
   - Run `scripts/audit_bundle.py <bundle_root>`.
   - Identify source roles before touching anything.
   - Refuse to overwrite source inputs.
2. Draft the task.
   - Write a concrete `draft.md`.
   - State document type, language, intended output files, hard layout constraints, and known risks.
   - Keep the draft artifact-driven.
3. Generate the plan.
   - Use `humanize-gen-plan` on the draft.
   - Produce a structured `plan.md`.
4. Refine the plan.
   - Add `CMT: ... ENDCMT` only for genuine corrections or questions.
   - Use `humanize-refine-plan` to produce the clean plan and QA ledger.
5. Run RLCR.
   - Use `humanize-rlcr`.
   - Default to `--max 2` unless the user explicitly requests otherwise.
   - Keep the local `humanize` review defaults unless the user explicitly asks for another model.
   - Use the loop-generated prompt, summary, and review files as source of truth.
6. Validate the outputs.
   - Check DOCX package integrity, sections, headers, footers, spacing, float anchors, and page-class coverage.
   - Validate the PDF when available.
   - For books, require front matter, TOC, chapter starts, figures, tables, code, and end matter.
   - For papers, require title, abstract, headings, figures, tables, equations, references.
   - For other PDFs, derive page classes from the bundle instead of forcing a book template.
7. Report the result.
   - List final output files, checks passed, and residual limits.
   - Do not claim completion without the validation evidence.

## Prompting Rules

- Adapt prompts to the document type.
- Keep prompts explicit about source roles and output shape.
- Do not assume direct OpenAI SDK or API compatibility when the local Codex CLI may be configured through another provider, proxy, or relay.
- Use the `humanize` skill family for draft, plan, refinement, and RLCR transitions.
- Use `CMT: ... ENDCMT` only in annotated plans that need revision.

## References

- `references/workflow.md` for the canonical sequence
- `references/examples.md` for book/article prompt shapes
- `references/lessons.md` for reusable guardrails

## Scripts

- `scripts/audit_bundle.py` to summarize the input bundle before drafting
