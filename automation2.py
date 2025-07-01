from PyPDF2 import PdfReader
reader = PdfReader('C:\\Users\\shubh\\Downloads\\Document.pdf')
print(reader.pages[0].extract_text())
