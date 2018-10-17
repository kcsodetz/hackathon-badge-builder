"""
Python script to generate the Executive team badges for Boilermake VI

Author: Ken Sodetz
Since: 10/16/2018
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Import font from .ttf file
pdfmetrics.registerFont(TTFont('Lato-Regular', 'Lato/Lato-Regular.ttf'))

# Constant Values
edge_offset = .15 * inch
bottom_offset = 1 * inch
AC_width = 4*inch
AC_height = 3.25 * inch
jpg_path = "AccessCardsJpg/AC_Exec.jpg"

# Define our canvas
c = canvas.Canvas('exec.pdf')

# Left row of cards
for i in range(3):
    c.drawImage(jpg_path, edge_offset, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)

    c.setFont("Lato-Regular", 16)
    c.drawCentredString(x=edge_offset + 2.9*inch, y=bottom_offset + 2.25*inch + i * AC_height, text="Ken Sodetz")
    c.setFont("Lato-Regular", 10)
    c.drawCentredString(x=edge_offset + 2.9*inch, y=bottom_offset + 2*inch + i * AC_height, text="Purdue University")

# Right row of cards
for i in range(3):
    c.drawImage(jpg_path, edge_offset + AC_width, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)
    c.setFont("Lato-Regular", 16)
    c.drawCentredString(x=edge_offset + 2.9*inch + AC_width, y=bottom_offset + 2.25*inch + i * AC_height,
                        text="Ken Sodetz")
    c.setFont("Lato-Regular", 10)
    c.drawCentredString(x=edge_offset + 2.9*inch + AC_width, y=bottom_offset + 2*inch + i * AC_height,
                        text="Purdue University")


c.showPage()
c.save()
