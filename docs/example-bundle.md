# 输入文件夹示例

建议一个 PDF 任务对应一个文件夹。

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

文件名不需要完全一致。`audit_bundle.py` 会递归扫描文件夹，寻找可能的 PDF、DOCX、TeX 和图片文件。

## 推荐准备

- 一个原始 PDF
- 一个 PDF 转出来的 DOCX，如果有的话
- 一个已经解压的 MinerU 文件夹，而不是只有压缩包
- MinerU 生成的页面截图、图片截图、表格截图、公式截图等

## 尽量避免

- 一个文件夹里混放很多无关 PDF
- 删除 MinerU 生成的图表截图
- 直接覆盖原始 PDF 或原始 DOCX
- 把私人文档、未授权论文、未授权书籍上传到公开仓库

## 小提示

如果你最在意排版，可以在调用 skill 时直接告诉 Codex：

```text
$pdf-to-docx-humanize 重点检查正文是否两端对齐，中文内部不要有多余空格，图表不要和文字重叠。
```

如果你最在意论文结构，可以说：

```text
$pdf-to-docx-humanize 重点保留论文标题、摘要、关键词、章节标题、图表、公式和参考文献结构。
```

如果你最在意书籍结构，可以说：

```text
$pdf-to-docx-humanize 重点重建封面之后的前言、目录、章节起始页、正文、图表、代码块和参考文献。
```
