# Humanize Dependency

`pdf-to-docx-humanize` is an orchestration skill. It does not replace the `humanize` workflow system.

For the full workflow, install these four Codex skills:

- `humanize`
- `humanize-gen-plan`
- `humanize-refine-plan`
- `humanize-rlcr`

The dependency is kept separate for three reasons:

1. `humanize` has its own scripts, hooks, review behavior, and release cycle.
2. Users who already have `humanize` should not receive a hidden replacement.
3. This skill can stay focused on PDF bundle handling and DOCX validation.

## If You Have Humanize

Install this repository's skill and run `$pdf-to-docx-humanize` normally.

The default loop limit is 2 rounds unless you explicitly ask for another value.

## If You Do Not Have Humanize

Install `humanize` from its own source first. If you received this repository from another person, ask them for the matching `humanize` installation source.

Without `humanize`, the skill can still guide Codex through:

- bundle auditing
- writing `draft.md`
- writing `plan.md`
- manual review passes
- final DOCX/PDF validation

But it cannot run the real `humanize-rlcr` gate-controlled loop.

## Check Your Local Installation

Windows PowerShell:

```powershell
Get-ChildItem $HOME\.codex\skills | Where-Object { $_.Name -like 'humanize*' }
```

macOS or Linux:

```bash
ls ~/.codex/skills/humanize*
```
