"""
Combine pdf files.
By Nikolay Komolov
github.com/nkspb
"""

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"<path to folder with input files>"

# Open file 1
input_file_name1 = os.path.join(path, "file1.pdf")
input_file1 = PdfFileReader(open(input_file_name1, "rb"))

# Open file 2
input_file_name2 = os.path.join(path, "file2.pdf")
input_file2 = PdfFileReader(open(input_file_name2, "rb"))

# Create PDF Writer
output_PDF = PdfFileWriter()

# Combine pdfs
for page_num in range(0, input_file1.getNumPages()):
    page = input_file1.getPage(page_num)
    output_PDF.addPage(page)

for page_num in range(0, input_file2.getNumPages()):
    page = input_file2.getPage(page_num)
    output_PDF.addPage(page)

# Save the result
output_file_name = os.path.join(path, "Output/Result.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
