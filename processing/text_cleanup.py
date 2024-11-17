import sys
import os

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

import re

# def reorder_text(text):
#     cleaned_text =  re.sub(r'[^A-Za-z0-9\s]','',text)
#     return cleaned_text

def reorder_text(text, keep_spaces=True):
    if keep_spaces:
        return re.sub(r"[^A-Za-z0-9\s]", "", text).strip()
    return re.sub(r"[^A-Za-z0-9]", "", text).strip()


# text = extract_text_from_pdf(pdf_path="C:\\Users\\jatin\\OneDrive\\Desktop\\MLNOTES\\file handling python notes.pdf")
# print(reorder_text(text=text))