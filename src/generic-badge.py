"""
Python script to generate the blank Hacker badges for Boilermake VI

Author: Ken Sodetz
Since: 10/17/2018
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Terminal Colors
OK = '\033[92m'
FAIL = '\033[91m'
WARN = '\033[93m'
NC = '\033[0m'

# Constant Values
BOTTOM_OFFSET = 2 * inch
CARD_WIDTH = 4.25 * inch
CARD_HEIGHT = 3 * inch

if len(sys.argv) != 2:
    print(FAIL + "[ERROR] Missing argument `type`")
    print(NC + "Possible types include `hacker` and `sponsor`")
    print("Usage: python3 generic-badge.py `type`")
    sys.exit(1)

# Choose file path based on badge type specified
if sys.argv[1] == 'hacker':
    jpg_path = "../res/AccessCardsJpg/AC_Hacker.jpg"
    pdf_path = "out/hackers_blank.pdf"
elif sys.argv[1] == 'sponsor':
    jpg_path = "../res/AccessCardsJpg/AC_Sponsor.jpg"
    pdf_path = "out/sponsors.pdf"
else:
    print(FAIL + "[ERROR] Argument " + WARN + sys.argv[1] + FAIL + " does not match `hacker` or `sponsor`")
    sys.exit(1)

# Define our canvas.
c = canvas.Canvas(pdf_path, pagesize=letter)


def draw(left_right_offset):
    """
    Draws the right half of the badges per one page.
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: None.
    """
    for i in range(3):
        c.drawImage(jpg_path, left_right_offset, BOTTOM_OFFSET + i * CARD_HEIGHT, width=CARD_WIDTH,
                    height=CARD_HEIGHT, mask=None)


# Determine how many pages to draw (6 cards per page), which gives 6 * page_num badges
page_num = 5
for j in range(page_num):
    draw(0)
    draw(CARD_WIDTH)
    c.showPage()

print(OK + "Processed {} Badges to {}".format(page_num * 6, pdf_path))
c.save()
