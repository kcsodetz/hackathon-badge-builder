"""
Python script to generate the Executive team badges for Boilermake VI

Author: Ken Sodetz
Since: 10/17/2018
"""
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Import font from .ttf file
pdfmetrics.registerFont(TTFont('Lato-Regular', '../res/Lato/Lato-Regular.ttf'))

# Constant Values
BOTTOM_OFFSET = 2 * inch
CARD_WIDTH = 4.25 * inch
CARD_HEIGHT = 3 * inch

# File paths
jpg_path = "../res/AccessCardsJpg/AC_Exec.jpg"
pdf_path = "out/execs.pdf"
csv_path = "data/execs.csv"

# Define our canvas
c = canvas.Canvas(pdf_path, pagesize=letter)


def draw(i, name, left_right_offset):
    """
    Draws the Access Cards on the page.
    :param i: Row offset to draw on, from 0 to 2
    :param name: Name of the exec
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: None
    """
    c.drawImage(jpg_path, left_right_offset, BOTTOM_OFFSET + i * CARD_HEIGHT, width=CARD_WIDTH,
                height=CARD_HEIGHT, mask=None)
    c.setFont("Lato-Regular", 16)
    c.drawCentredString(x=2.9 * inch + left_right_offset, y=BOTTOM_OFFSET + 2 * inch + i * CARD_HEIGHT,
                        text=name)
    c.setFont("Lato-Regular", 10)
    c.drawCentredString(x=0 + 2.9 * inch + left_right_offset, y=BOTTOM_OFFSET + 1.75 * inch + i * CARD_HEIGHT,
                        text="Purdue University")


# Open CSV file.
print("Reading from {}...".format(csv_path))
with open(csv_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    row_num = 0
    # For each row in the csv file.
    for row in csv_reader:
        # If line is even, draw left. Else draw right.
        if line_count % 2 == 0:
            draw(row_num, row[0], 0)
        else:
            draw(row_num, row[0], CARD_WIDTH)
            row_num += 1

        # If on the third row, go to a new page and reset the row.
        if row_num == 3:
            c.showPage()
            row_num = 0

        line_count += 1

print("Processed {} Badges to {}".format(line_count, pdf_path))
c.save()
