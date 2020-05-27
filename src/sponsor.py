"""
Python script to generate the Sponsor badges for BoilerMake VII

Author: Ken Sodetz
Since: 1/22/2020
"""
import csv
import pyqrcode
import string
from os import remove, removedirs, makedirs
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# BACKGROUND FILE (Change as needed)
# ----------------------------------
background_file = "Sponsor_m.jpg"
# ----------------------------------

# Terminal Colors
OK = '\033[92m'

# Font values
hacker_font_name = "Roboto-Black"
university_font_name = "Roboto-Medium"
info_font_name = "Roboto-Light"
hacker_font_path = "../res/Fonts/Roboto/Roboto-Black.ttf"
info_font_path = "../res/Fonts/Roboto/Roboto-Light.ttf"
university_font_path = "../res/Fonts/Roboto/Roboto-Medium.ttf"

# Constant Values. DO NOT CHANGE
BOTTOM_OFFSET = 1 * inch
CARD_WIDTH = 4 * inch
CARD_HEIGHT = 3 * inch
PDF_PATH = "out/sponsors.pdf"
BACKGROUND_PATH = "../res/Background_JPGs/" + background_file

# Define our canvas.
c = canvas.Canvas(PDF_PATH, pagesize=letter)

# Import font from .ttf file.
pdfmetrics.registerFont(TTFont(hacker_font_name, hacker_font_path))
pdfmetrics.registerFont(TTFont(info_font_name, info_font_path))
pdfmetrics.registerFont(TTFont(university_font_name, university_font_path))


def draw(row_offset, left_right_offset):
    """
    Draws the Access Cards on the page.
    :param row_offset: Row to draw on, from 0 to 2.
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: none
    """
    # Draws an empty badge on the canvas.
    c.drawImage(BACKGROUND_PATH, left_right_offset, BOTTOM_OFFSET + row_offset * CARD_HEIGHT, width=CARD_WIDTH,
                height=CARD_HEIGHT, mask=None)

    # Set fill color to white
    c.setFillColorRGB(1, 1, 1)

    # Draws Boilermake website
    c.setFont(info_font_name, 10.5)
    c.drawString(x=(.7 + 2.15) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.365 * inch + row_offset * CARD_HEIGHT,
                 text="Boilermake.org")

    # Draws Boilermake slack
    c.drawString(x=(.7 + 1.59) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                 text="boilermakevii.slack.com")

    # Draw Sponsor
    c.drawString(x=0.6 * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                 text="Sponsor")


def draw_margins():
    """
    Draws margins on canvas for debugging
    :return: none
    """
    c.setFillColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(0, 1 * inch, 8.5 * inch, 1 * inch)
    c.line(0, 10 * inch, 8.5 * inch, 10 * inch)
    c.line(0.25 * inch, 0, 0.25 * inch, 11.5 * inch)
    c.line(4.25 * inch, 0, 4.25 * inch, 11.5 * inch)
    c.line(8.25 * inch, 0, 8.25 * inch, 11.5 * inch)


if __name__ == '__main__':
    # Open CSV file.
    line_count = 0
    row_num = 0
    # For each row in the csv file.
    for row in range(0, 35):
        # Create instance of a person object to pass to either the left draw or right draw function.
        # If line is even, draw on the left. Else draw on the right.
        if line_count % 2 == 0:
            draw(row_num, 0.25 * inch)
        else:
            draw(row_num, CARD_WIDTH + 0.25 * inch)
            row_num += 1

        # If on the third row, go to a new page and reset the row.
        if row_num == 3:
            # draw_margins()
            c.showPage()
            row_num = 0

        line_count += 1

    print(OK + 'Processed {} Badges to {}'.format(line_count, PDF_PATH))
    c.save()
