"""
Python script to generate the blank Hacker badges for Boilermake VI

Author: Ken Sodetz
Since: 10/17/2018
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Constant Values
BOTTOM_OFFSET = 2 * inch
CARD_WIDTH = 4.25 * inch
CARD_HEIGHT = 3 * inch

# File paths
jpg_path = "../res/AccessCardsJpg/AC_Hacker.jpg"
pdf_path = "out/hackers_blank.pdf"

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

print("Processed {} Badges to {}".format(page_num * 6, pdf_path))
c.save()
