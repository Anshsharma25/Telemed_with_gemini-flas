from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(filename, patient_data):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Patient Summary Report")
    y = 700
    for k, v in patient_data.items():
        c.drawString(100, y, f"{k}: {v}")
        y -= 20
    c.save()