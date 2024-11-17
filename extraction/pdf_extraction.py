import sys
import os
import PyPDF2
from io import BytesIO
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(project_root)
# from processing.text_cleanup import reorder_text
# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path,'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ""
#         for page in reader.pages:
#             text+=page.extract_text()

#     return text

def extract_text_from_pdf(pdf_path):
    pdf_file = pdf_path.read()
    pdf = BytesIO(pdf_file)

    pdf_reader = PyPDF2.PdfReader(pdf)
    text=""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text+=page.extract_text()

    return text