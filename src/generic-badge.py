"""
Python script to generate the blank Hacker and Sponsor badges for BoilerMake VII

Author: Ken Sodetz
Since: 10/17/2018
"""
import sys
from os import remove, removedirs, makedirs
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import pyqrcode
import png

# BACKGROUND FILE NAMES (Change as needed)
# ----------------------------------------
hacker_background_file = "Hacker.jpg"
sponsor_background_file = "sponsor_bkgd.jpg"
# ----------------------------------------

# Terminal Colors
OK = '\033[92m'
FAIL = '\033[91m'
WARN = '\033[93m'
NC = '\033[0m'

# QR Data Path
QR_DATA_PATH = "blank_qr.csv"

# Constant Values. DO NOT CHANGE
BOTTOM_OFFSET = 2 * inch
CARD_WIDTH = 4.25 * inch
CARD_HEIGHT = 3 * inch
BACKGROUND_PATH = "../res/Background_JPGs/"
TMP_DIR = "tmp/"
QR_EXT = ".png"

# Check number of args
if len(sys.argv) != 3:
    print(FAIL + "[ERROR] Missing argument(s)")
    print(NC + "Usage: python3 generic-badge.py [type] [num_page(s)]")
    print("Possible types include `hacker` and `sponsor`")
    print("Sets of badges are defined as num_page(s) (1 page = 6 badges)")
    sys.exit(1)

# Choose file path based on badge type specified
if sys.argv[1] == 'hacker':
    jpg_path = BACKGROUND_PATH + hacker_background_file
    pdf_path = "out/hackers_blank.pdf"
elif sys.argv[1] == 'sponsor':
    jpg_path = BACKGROUND_PATH + sponsor_background_file
    pdf_path = "out/sponsors.pdf"
else:
    print(FAIL + "[ERROR] Argument 1 " + WARN + sys.argv[1] + FAIL + " does not match `hacker` or `sponsor`.")
    sys.exit(2)

# Save page number argument
try:
    PAGE_NUM = int(sys.argv[2])
except ValueError:
    print(FAIL + "[ERROR] Argument 2 " + WARN + sys.argv[2] + FAIL + " is not an integer.")
    sys.exit(3)

# Define our canvas.
c = canvas.Canvas(pdf_path, pagesize=letter)


def draw(left_right_offset):
    """
    Draws half of the badges per one page, 3 in a column
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: None.
    """
    for i in range(3):
        c.drawImage(jpg_path, left_right_offset, BOTTOM_OFFSET + i * CARD_HEIGHT, width=CARD_WIDTH,
                    height=CARD_HEIGHT, mask=None)

    # Draw qr code
    # qr_path = get_qr(hacker)
    # c.drawImage(qr_path, 1 * inch + left_right_offset,
    #             BOTTOM_OFFSET + 0.1 * inch + i * CARD_HEIGHT, width=30, height=30, mask=None)

    # Delete qr code png when finished
    # remove(qr_path)


def get_qr(qr_data):
    """
    Builds qr code from hacker data
    :param qr_data: QR ID
    :return: Qr code file path
    """
    qr_code = pyqrcode.create(qr_data)
    file_path = TMP_DIR + qr_data + QR_EXT
    qr_code.png(file_path, scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    return file_path


# Draw left column (offset of 0) and right column (offset of CARD_WIDTH)
for j in range(PAGE_NUM):
    draw(0)
    draw(CARD_WIDTH)
    c.showPage()

print(OK + "Processed {} Badges to {}".format(PAGE_NUM * 6, pdf_path))
c.save()
