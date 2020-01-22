"""
Python script to generate the Hacker badges for BoilerMake VI

Author: Ken Sodetz
Since: 10/16/2018
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

# BACKGROUND AND CSV FILES (Change as needed)
# ----------------------------------
background_file = "Organizer_m.jpg"
csv_file = "execs.csv"
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
PDF_PATH = "out/organizers.pdf"
CSV_FILE_PATH = "data/" + csv_file
BACKGROUND_PATH = "../res/Background_JPGs/" + background_file
TMP_DIR = "tmp/"
QR_EXT = ".png"

# Define our canvas.
c = canvas.Canvas(PDF_PATH, pagesize=letter)

# Import font from .ttf file.
pdfmetrics.registerFont(TTFont(hacker_font_name, hacker_font_path))
pdfmetrics.registerFont(TTFont(info_font_name, info_font_path))
pdfmetrics.registerFont(TTFont(university_font_name, university_font_path))

# List of leads
leads = ["Jeonghu Park",
         "Zach Johnson",
         "C.J. Enright",
         "Peter Kfoury",
         "Ryan Sullivan"
         ]


def draw(row_offset, organizer_name, left_right_offset):
    """
    Draws the Access Cards on the page.
    :param organizer_name: Name of exec member
    :param row_offset: Row to draw on, from 0 to 2.
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: none
    """
    # Draws an empty badge on the canvas.
    c.drawImage(BACKGROUND_PATH, left_right_offset, BOTTOM_OFFSET + row_offset * CARD_HEIGHT, width=CARD_WIDTH,
                height=CARD_HEIGHT, mask=None)

    # Set fill color to white
    c.setFillColorRGB(1, 1, 1)

    # Set font size based on organizer's name length
    c.setFont(hacker_font_name, 18)
    if len(organizer_name) >= 18:
        c.setFont(hacker_font_name, 15.5)

    # Draw organizer's full name
    c.drawString(x=0.6 * inch + left_right_offset, y=BOTTOM_OFFSET + 0.4 * inch + row_offset * CARD_HEIGHT,
                 text=organizer_name)

    # Draws Boilermake website
    c.setFont(info_font_name, 10.5)
    c.drawString(x=(.7 + 2.15) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.365 * inch + row_offset * CARD_HEIGHT,
                 text="Boilermake.org")

    # Draws Boilermake slack
    c.drawString(x=(.7 + 1.59) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                 text="boilermakevii.slack.com")

    # Draw Organizer
    c.setFont(university_font_name, 10.5)
    if "Anita" in organizer_name:
        c.drawString(x=0.6 * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                     text="Director")
    elif organizer_name in leads:
        c.drawString(x=0.6 * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                     text="Lead Organizer")
    else:
        c.drawString(x=0.6 * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                     text="Organizer")


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
    print('Reading from {}'.format(CSV_FILE_PATH))
    with open(CSV_FILE_PATH, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_num = 0
        # For each row in the csv file.
        for row in csv_reader:
            # Create instance of a person object to pass to either the left draw or right draw function.
            organizer = row[0]
            # If line is even, draw on the left. Else draw on the right.
            if line_count % 2 == 0:
                draw(row_num, organizer, 0.25 * inch)
            else:
                draw(row_num, organizer, CARD_WIDTH + 0.25 * inch)
                row_num += 1

            # If on the third row, go to a new page and reset the row.
            if row_num == 3:
                # draw_margins()
                c.showPage()
                row_num = 0

            line_count += 1

    print(OK + 'Processed {} Badges to {}'.format(line_count, PDF_PATH))
    c.save()
