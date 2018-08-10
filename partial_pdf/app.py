"""
    partial_pdf
    Extract a specific range of pages from a PDF file.
    By Nikolay Komolov
    https://github.com/nkspb
"""

import os, PyPDF2, easygui

# Select a pdf file
input_file_name = easygui.fileopenbox(title="Select a PDF file to open", default="*.pdf")
# Exit app if user pressed Cancel
if input_file_name is None:
    exit()

# Get page length of input file
input_file = PyPDF2.PdfFileReader(open(input_file_name, "rb"))
total_pages = input_file.getNumPages()

# Choose a beginning page
begin_page = easygui.enterbox("Enter the beginning page", "Beginning Page")
if begin_page is None:
    exit()
# Check input
while (not begin_page.isdigit() or begin_page == "0" or int(begin_page) > total_pages):
    easygui.msgbox("Please provide a valid number", "Whoops!")
    begin_page = easygui.enterbox("Enter the beginning page", "Beginning Page")
    if begin_page is None:
        exit()

# Choose an ending page
end_page = easygui.enterbox("Enter the ending page", "Ending Page")
if end_page is None:
    exit()
# Check input
while (not end_page.isdigit() or end_page == "0" or int(end_page) > total_pages or int(end_page) < int(begin_page)):
    easygui.msgbox("Please provide a valid number", "Whoops!")
    end_page = easygui.enterbox("Enter the ending page", "Ending Page")
    if end_page is None:
        exit()

# Choose output file
output_file_name = easygui.filesavebox(title="Save the PDF file as", default="*.pdf")
# Check that output file is not the same as input
while input_file_name == output_file_name:
    easygui.msgbox("Cannot overwrite the original file!", "Please choose another file...")
    output_file_name = easygui.filesavebox(title="Save the PDF file as", default="*.pdf")
if output_file_name is None:
    exit()
    
# Create a new pdf file
output_PDF = PyPDF2.PdfFileWriter()
for page_num in range(int(begin_page) - 1, int(end_page)):
    page = input_file.getPage(page_num)
    output_PDF.addPage(page)
# Save output file
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()