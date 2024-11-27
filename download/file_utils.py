import gtts

def save_to_text_file(text,filename):
    with open(filename,"w") as file:
        file.write(text)

def save_to_pdf(text,filename):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', size=12)
    pdf.multi_cell(0,10,text)
    pdf.output(filename)

