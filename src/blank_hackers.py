"""
Python script to generate the Hacker badges for BoilerMake VII

Author: Ken Sodetz
Since: 10/16/2018
"""
import csv
import pyqrcode
from os import remove, removedirs, makedirs
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# BACKGROUND AND CSV FILES (Change as needed)
# ----------------------------------
background_file = "Hacker_m.jpg"
csv_file = "blank_qr.csv"
# ----------------------------------

# Terminal Colors
OK = '\033[92m'

# Font values
font_name = "Roboto-Black"
hacker_font_name = "Roboto-Black"
info_font_name = "Roboto-Light"
hacker_font_path = "../res/Fonts/Roboto/Roboto-Black.ttf"
info_font_path = "../res/Fonts/Roboto/Roboto-Light.ttf"

# Constant Values. DO NOT CHANGE
BOTTOM_OFFSET = 1 * inch
CARD_WIDTH = 4 * inch
CARD_HEIGHT = 3 * inch
PDF_PATH = "out/blank_hackers.pdf"
CSV_FILE_PATH = "data/" + csv_file
BACKGROUND_PATH = "../res/Background_JPGs/" + background_file
TMP_DIR = "tmp/"
QR_EXT = ".png"

# Define our canvas.
c = canvas.Canvas(PDF_PATH, pagesize=letter)

# Import font from .ttf file.
pdfmetrics.registerFont(TTFont(font_name, hacker_font_path))
pdfmetrics.registerFont(TTFont(info_font_name, info_font_path))


def draw(i, qr_data, left_right_offset):
    """
    Draws the Access Cards on the page.
    :param i: Row offset to draw on, from 0 to 2.
    :param qr_data: QR string
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: none
    """
    # Draws an empty badge on the canvas.
    c.drawImage(BACKGROUND_PATH, left_right_offset, BOTTOM_OFFSET + i * CARD_HEIGHT, width=CARD_WIDTH,
                height=CARD_HEIGHT, mask=None)

    c.setFillColorRGB(1, 1, 1)
    c.setFont(info_font_name, 10.5)

    # Draws the full name on the badge.
    c.drawString(x=(.7 + 2.15) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.365 * inch + i * CARD_HEIGHT,
                 text="Boilermake.org")

    # Draws the full name on the badge.
    c.drawString(x=(.7 + 1.59) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + i * CARD_HEIGHT,
                 text="boilermakevii.slack.com")
    # Draw qr code
    qr_path = get_qr(qr_data)
    c.drawImage(qr_path, 1.5 * inch + left_right_offset,
                BOTTOM_OFFSET + 0.93 * inch + i * CARD_HEIGHT, width=1 * inch, height=1 * inch, mask=None)

    # Delete qr code png when finished
    remove(qr_path)


def get_qr(qr_data):
    """
    Builds qr code from hacker data
    :param qr_data: QR ID string
    :return: Qr code file path
    """
    qr_code = pyqrcode.create(qr_data)
    file_path = TMP_DIR + qr_data + QR_EXT
    qr_code.png(file_path, scale=4, quiet_zone=0, module_color=[255, 255, 255, 128], background=(118, 138, 211, 0))
    return file_path


def draw_margins():
    c.setFillColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(0, 1 * inch, 8.5 * inch, 1 * inch)
    c.line(0, 10 * inch, 8.5 * inch, 10 * inch)
    c.line(0.25 * inch, 0, 0.25 * inch, 11.5 * inch)
    c.line(4.25 * inch, 0, 4.25 * inch, 11.5 * inch)
    c.line(8.25 * inch, 0, 8.25 * inch, 11.5 * inch)


if __name__ == '__main__':
    # Create temporary directory to save qr codes
    makedirs(TMP_DIR, False)
    # Open CSV file.
    print('Reading from {}'.format(CSV_FILE_PATH))
    with open(CSV_FILE_PATH, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_num = 0
        # For each row in the csv file.
        for row in csv_reader:

            qr_id = row[0]
            # If line is even, draw left. Else draw right.
            if line_count % 2 == 0:
                draw(row_num, qr_id, 0.25 * inch)
            else:
                draw(row_num, qr_id, CARD_WIDTH + 0.25 * inch)
                row_num += 1

            # If on the third row, go to a new page and reset the row.
            if row_num == 3:
                # draw_margins()
                c.showPage()
                row_num = 0

            line_count += 1

    # Remove when no longer needed
    removedirs(TMP_DIR)

    print(OK + 'Processed {} Badges to {}'.format(line_count, PDF_PATH))
    c.save()
