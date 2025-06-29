from PyPDF2 import PdfReader, PdfWriter
# load the file
input_pdf_path="C:/All__Docs_bhagyashree/SQL Notes Qsp.pdf"
reader=PdfReader(input_pdf_path)

# total number of pages and split
total_pages=len(reader.pages)
split_point=total_pages//2

# create 1st half pdf
writer_part1=PdfWriter()
for page in range(split_point):
    writer_part1.add_page(reader.pages[page])
part1_path = "C:/All__Docs_bhagyashree/SQL_Notes_Qsp_Part1.pdf"
with open(part1_path, "wb") as f:
    writer_part1.write(f)

writer_part2 = PdfWriter()
for page in range(split_point, total_pages):
    writer_part2.add_page(reader.pages[page])
part2_path = "C:/All__Docs_bhagyashree/SQL_Notes_Qsp_Part2.pdf"
with open(part2_path, "wb") as f:
    writer_part2.write(f)

part1_path, part2_path