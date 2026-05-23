# Contributing

Contributions are welcome when they keep the skill practical for real PDF-to-DOCX work.

Please keep changes focused on one of these areas:

- clearer installation and beginner usage
- safer bundle auditing
- better document-type prompts
- stronger validation checklists
- bug fixes for cross-platform installation

Do not add copyrighted PDFs, private documents, generated DOCX outputs, or local `.humanize/` loop state to the repository.

Before opening a pull request, run:

```bash
python scripts/validate_repo.py
python -m py_compile skills/pdf-to-docx-humanize/scripts/audit_bundle.py
```
