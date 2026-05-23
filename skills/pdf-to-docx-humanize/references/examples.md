# Example Task Shapes

## Chinese Book PDF

User asks to process a book-like PDF bundle that includes:

- source PDF
- PDF-to-DOCX export
- MinerU extracted folder with screenshots and `tex`

Focus on:

- front matter reconstruction
- static TOC from translated headings
- readable body flow
- chapter-start decoration
- no CJK internal spacing
- no floating body text boxes

## English SCI Article

User asks to process a journal article bundle.

Focus on:

- title, abstract, keywords, references
- figure and table placement
- equation and code block fidelity
- English paragraph flow and section headings
- minimal decorative reconstruction

## Mixed-Format Technical PDF

User asks to process a technical PDF with code, tables, and images.

Focus on:

- preserving code blocks and captions
- detecting page classes from the extracted assets
- using the MinerU screenshots as placement hints
- documenting any unavoidable reconstruction choices
