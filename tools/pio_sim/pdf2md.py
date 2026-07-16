import pymupdf4llm
import pathlib

# PDF file path
pdf_path = "RP-008373-DS-2-rp2350-datasheet.pdf"

# Extract as Markdown text
md_text = pymupdf4llm.to_markdown(pdf_path)

# Save to file
pathlib.Path("RP-008373-DS-2-rp2350-datasheet.md").write_bytes(md_text.encode())