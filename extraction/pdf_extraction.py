import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path,'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text+=page.extract_text()

    return text

# print(extract_text_from_pdf(pdf_path="C:\\Users\\jatin\\OneDrive\\Desktop\\MLNOTES\\file handling python notes.pdf"))