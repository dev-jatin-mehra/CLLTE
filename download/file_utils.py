from fpdf import FPDF

def save_to_text_file(text,filename):
    with open(filename,"w") as file:
        file.write(text)

from fpdf import FPDF

def save_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    encoded_text = text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 10, encoded_text)
    pdf.output(filename)
