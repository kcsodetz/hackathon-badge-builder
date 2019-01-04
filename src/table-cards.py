from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# Constant Values.
bottom_offset = 2 * inch
AC_width = 4.25 * inch
AC_height = 3 * inch
font_name = "Lato-Regular"
font_path = "../res/Lato/Lato-Regular.ttf"
jpg_path = "res/AccessCardsJpg/AC_Hacker.jpg"
pdf_path = "out/tables.pdf"
img_path = "../res/BM_Logo.jpg"

num_table_cards = 85

pdfmetrics.registerFont(TTFont(font_name, font_path))

# Define our canvas.
c = canvas.Canvas(pdf_path, pagesize=letter)
# from 1 to 86 (non inclusive, 85)
for i in range(1, num_table_cards + 1):
    c.setFont(font_name, 60)
    c.rotate(90)
    c.drawCentredString(6.5 * inch, 6.375 * -inch, "Table " + str(i))
    c.drawImage(img_path, 3 * inch, 6.9 * -inch, 1.5 * inch, 1.5 * inch)
    c.rotate(180)
    c.drawCentredString(6.5 * -inch, 2.375 * inch, "Table " + str(i))
    c.drawImage(img_path, 4.5 * -inch, 2 * inch, 1.5 * inch, 1.5 * inch)
    c.showPage()

print('Processed {} Table cards to {}'.format(num_table_cards, pdf_path))
c.save()
