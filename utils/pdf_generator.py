from reportlab.lib.utils import simpleSplit
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os


PDF_FOLDER = "pdfs"
os.makedirs(PDF_FOLDER, exist_ok=True)

def save_as_pdf(text, filename):
    pdf_path = os.path.join(PDF_FOLDER, filename)
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, height - 40, "Meeting Minutes")
    y = height - 70
    c.setFont("Helvetica", 12)

    lines = text.strip().split(". ")
    for line in lines:
        bullet_line = f"- {line.strip()}"
        wrapped = simpleSplit(bullet_line, "Helvetica", 12, width - 80)
        for subline in wrapped:
            if y < 40:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40
            c.drawString(40, y, subline)
            y -= 18

    c.save()
    return pdf_path