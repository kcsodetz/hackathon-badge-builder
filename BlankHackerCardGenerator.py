"""
Python script to generate the blank Hacker badges for Boilermake VI

Author: Ken Sodetz
Since: 10/17/2018
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Constant Values.
edge_offset = .15 * inch
bottom_offset = 1 * inch
AC_width = 4*inch
AC_height = 3.25 * inch
jpg_path = "Resources/AccessCardsJpg/AC_Hacker.jpg"

# Define our canvas.
c = canvas.Canvas('hackers_blank.pdf')


# Left row of cards.
def draw_left():
    """
    Draws the left half of the badges per one page.
    :return: None.
    """
    for i in range(3):
        c.drawImage(jpg_path, edge_offset, bottom_offset + i * AC_height, width=AC_width,
                    height=AC_height, mask=None)


# Right row of cards.
def draw_right():
    """
    Draws the right half of the badges per one page.
    :return: None.
    """
    for i in range(3):
        c.drawImage(jpg_path, edge_offset + AC_width, bottom_offset + i * AC_height, width=AC_width,
                    height=AC_height, mask=None)


# Determine how many pages to draw (6 cards per page), which gives 6 * page_num badges
page_num = 5

for j in range(page_num):
    draw_left()
    draw_right()
    c.showPage()

c.save()
