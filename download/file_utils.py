from fpdf import FPDF

def save_to_text_file(text,filename):
    with open(filename,"w") as file:
        file.write(text)

from fpdf import FPDF

def save_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    # Use built-in Helvetica font (no need to download any font files)
    pdf.set_font("Helvetica", size=12)
    # If needed, encode text to handle special characters
    encoded_text = text.encode('latin-1', 'replace').decode('latin-1')
    # Write the text to the PDF
    pdf.multi_cell(0, 10, encoded_text)
    pdf.output(filename)
