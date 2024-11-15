import sys
import os

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

import re
from extraction.pdf_extraction import extract_text_from_pdf

# Your code

def reorder_text(text):
    cleaned_text =  re.sub(r'[^A-Za-z0-9\s]','',text)
    return cleaned_text

text = extract_text_from_pdf(pdf_path="C:\\Users\\jatin\\OneDrive\\Desktop\\MLNOTES\\Python String.pdf")
print(reorder_text(text=text))