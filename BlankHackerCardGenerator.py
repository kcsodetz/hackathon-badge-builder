"""
Python script to generate the blank Hacker badges for Boilermake VI

Author: Ken Sodetz
Since: 10/17/2018
"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Constant Values.
bottom_offset = 2 * inch
AC_width = 4.25 * inch
AC_height = 3 * inch
jpg_path = "Resources/AccessCardsJpg/AC_Hacker.jpg"
pdf_path = "hackers_blank.pdf"

# Define our canvas.
c = canvas.Canvas(pdf_path, pagesize=letter)


def draw_left():
    """
    Draws the left half of the badges per one page.
    :return: None.
    """
    for i in range(3):
        c.drawImage(jpg_path, 0, bottom_offset + i * AC_height, width=AC_width,
                    height=AC_height, mask=None)


def draw_right():
    """
    Draws the right half of the badges per one page.
    :return: None.
    """
    for i in range(3):
        c.drawImage(jpg_path, AC_width, bottom_offset + i * AC_height, width=AC_width,
                    height=AC_height, mask=None)


# Determine how many pages to draw (6 cards per page), which gives 6 * page_num badges
page_num = 5
print(f'Printing {page_num * 6} Badges to {pdf_path}...')
for j in range(page_num):
    draw_left()
    draw_right()
    c.showPage()
print(f'Processed {page_num * 6} Badges')
c.save()
