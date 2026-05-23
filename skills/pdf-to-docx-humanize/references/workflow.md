# PDF to DOCX Humanize Workflow

## Scope

Use this skill to turn a prepared PDF bundle into a polished DOCX through the `humanize` workflow:

- start from a source PDF
- inspect the paired DOCX export if present
- inspect the MinerU unpacked folder with `tex`, images, tables, and screenshots
- draft the task
- generate a plan with `humanize-gen-plan`
- refine the plan with `humanize-refine-plan`
- run `humanize-rlcr`
- validate the final document and reports

## Expected Input Bundle

Prefer a folder containing:

- original PDF
- PDF-to-DOCX export
- MinerU extracted folder
  - `tex` file
  - page or figure screenshots
  - table screenshots
  - code or figure assets

## Workflow Rules

1. Audit the bundle first.
2. Detect language and document type.
3. Write a draft that states the objective, source roles, constraints, and likely risks.
4. Generate a plan through `humanize-gen-plan`.
5. Add inline comment blocks only where the plan needs correction or clarification.
6. Refine the plan through `humanize-refine-plan`.
7. Run `humanize-rlcr` with a hard maximum of 2 rounds.
8. During RLCR, prefer concrete artifacts and keep summaries machine-verifiable.
9. Verify the outputs with package checks, spacing checks, page-class checks, and review results.

## Prompting Rules

Keep prompts specific and artifact-driven:

- name the detected files and folders
- state whether the document is a book, thesis, article, or other PDF
- list hard constraints such as layout preservation, no internal CJK spacing, or no floating body objects
- ask for the exact output format expected from the run

## Model Routing Notes

- Treat local Codex CLI runs as user-configured. They may use direct OpenAI endpoints, a compatible provider, a proxy, or a relay.
- If a script or prompt assumes OpenAI API shape, check it against the local Codex CLI first.
- Use the workflow's own `humanize` scripts for draft/plan/RLCR transitions instead of ad hoc replacements.

## Missing Humanize Fallback

If `humanize` is not installed:

1. Audit the bundle.
2. Write `draft.md` directly.
3. Write `plan.md` directly, preserving acceptance criteria and validation requirements.
4. Perform at least one manual implementation/review pass.
5. Report that the gate-controlled RLCR loop did not run.

Do not label this fallback as equivalent to `humanize-rlcr`.

## Validation Checklist

- source bundle exists and is complete
- generated draft exists
- generated plan exists
- refined plan exists
- RLCR summary files exist
- final DOCX exists
- final PDF or export validation exists when available
- report bundle records source roles, decisions, validation, and residual limits

## When to Extend

Add a new helper script only when the same audit or verification step is needed repeatedly across multiple documents.
