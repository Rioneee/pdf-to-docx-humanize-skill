# Example Input Bundle

Use one folder per document.

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

The exact folder names can differ. The audit script searches recursively for likely PDFs, DOCX files, TeX files, and images.

## Good Inputs

- One original source PDF
- One converted DOCX if available
- One unpacked MinerU folder, not only a compressed archive
- Figure, table, equation, or page screenshots preserved from MinerU

## Avoid

- Running on a folder full of unrelated PDFs
- Deleting the MinerU screenshots before conversion
- Overwriting the original PDF or DOCX export
- Publishing private documents to a public repository
