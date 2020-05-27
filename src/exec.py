"""
Python script to generate the Executive team badges for BoilerMake VII

Author: Ken Sodetz
Since: 10/17/2018
"""
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# BACKGROUND AND CSV FILES (Change as needed)
# ------------------------------------------
background_file = "exec_bkgd.jpg"
csv_file = "execs.csv"
# ------------------------------------------

# Font values
font_name = "Lato-Regular"
font_path = "../res/Lato/Lato-Regular.ttf"

# Terminal Colors
OK = '\033[92m'

# Constant Values. DO NOT CHANGE
BOTTOM_OFFSET = 2 * inch
CARD_WIDTH = 4.25 * inch
CARD_HEIGHT = 3 * inch
PDF_PATH = "out/execs.pdf"
CSV_FILE_PATH = "data/" + csv_file
BACKGROUND_PATH = "../res/Background_JPGs/" + background_file

# Define our canvas
c = canvas.Canvas(PDF_PATH, pagesize=letter)

# Import font from .ttf file
pdfmetrics.registerFont(TTFont(font_name, font_path))


def draw(i, name, left_right_offset):
    """
    Draws the Access Cards on the page.
    :param i: Row offset to draw on, from 0 to 2
    :param name: Name of the exec
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: None
    """
    c.drawImage(BACKGROUND_PATH, left_right_offset, BOTTOM_OFFSET + i * CARD_HEIGHT, width=CARD_WIDTH,
                height=CARD_HEIGHT, mask=None)
    c.setFont(font_name, 16)
    c.drawCentredString(x=2.9 * inch + left_right_offset, y=BOTTOM_OFFSET + 2 * inch + i * CARD_HEIGHT,
                        text=name)
    c.setFont(font_name, 10)
    c.drawCentredString(x=0 + 2.9 * inch + left_right_offset, y=BOTTOM_OFFSET + 1.75 * inch + i * CARD_HEIGHT,
                        text="Purdue University")


# Open CSV file.
print("Reading from {}...".format(CSV_FILE_PATH))
with open(CSV_FILE_PATH, mode='r') as csv_file:
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

print(OK + "Processed {} Badges to {}".format(line_count, PDF_PATH))
c.save()
