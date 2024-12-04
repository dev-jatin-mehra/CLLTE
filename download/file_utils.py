import tempfile
from fpdf import FPDF

def save_to_text_file(text):
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt',encoding='utf-8') as temp_file:
        temp_file.write(text)
        temp_file.seek(0)
        return temp_file.name

def save_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    encoded_text = text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 10, encoded_text)
    with tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix='.pdf') as temp_file:
        pdf.output(temp_file.name)
        temp_file.seek(0)
        return temp_file.name
