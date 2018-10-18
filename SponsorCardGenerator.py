"""
Python script to generate the Sponsor badges for Boilermake VI

Author: Ken Sodetz
Since: 10/17/2018
"""
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Import font from .ttf file
pdfmetrics.registerFont(TTFont('Lato-Regular', 'Resources/Lato/Lato-Regular.ttf'))

# Constant Values
edge_offset = .15 * inch
bottom_offset = 1 * inch
AC_width = 4 * inch
AC_height = 3.25 * inch
jpg_path = "Resources/AccessCardsJpg/AC_Sponsor.jpg"

# Define our canvas
c = canvas.Canvas('sponsors.pdf')


# Left row of cards
def draw_left(i, name, company):
    c.drawImage(jpg_path, edge_offset, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)
    c.setFont("Lato-Regular", 16)
    c.drawCentredString(x=edge_offset + 2.9 * inch, y=bottom_offset + 2.25 * inch + i * AC_height, text=name)
    c.setFont("Lato-Regular", 19)
    c.drawCentredString(x=edge_offset + 2.9 * inch, y=bottom_offset + 2 * inch + i * AC_height,
                        text=company)


# Right row of cards
def draw_right(i, name, company):
    c.drawImage(jpg_path, edge_offset + AC_width, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)
    c.setFont("Lato-Regular", 16)
    c.drawCentredString(x=edge_offset + 2.9 * inch + AC_width, y=bottom_offset + 2.25 * inch + i * AC_height,
                        text=name)
    c.setFont("Lato-Regular", 10)
    c.drawCentredString(x=edge_offset + 2.9 * inch + AC_width, y=bottom_offset + 2 * inch + i * AC_height,
                        text=company)


# Open CSV file.
with open('sponsors.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    row_num = 0
    # For each row in the csv file.
    for row in csv_reader:
        # If line is even, draw left. Else draw right.
        if line_count % 2 == 0:
            draw_left(row_num, row[0])
        else:
            draw_right(row_num, row[0])
            row_num += 1

        # If on the third row, go to a new page and reset the row.
        if row_num == 3:
            c.showPage()
            row_num = 0

        line_count += 1

print(f'Processed {line_count} Badges.')

c.save()