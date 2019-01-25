"""
Python script to generate table numbers for BoilerMake VI

Author: Ken Sodetz
Since: 10/17/2018
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# IMAGE NAME (Change as needed)
# ---------------------------------------------------------
img_name = "BM_Logo.jpg"
# ---------------------------------------------------------

# Terminal Colors
OK = '\033[92m'
FAIL = '\033[91m'
WARN = '\033[93m'
NC = '\033[0m'

# Check number of args
if len(sys.argv) != 2:
    print(FAIL + "[ERROR] Missing argument `number`")
    print(NC + "Enter the number of table cards to create")
    print("Usage: python3 table-cards.py [number]")
    sys.exit(1)

# Check is argument is an integer
if not sys.argv[1].isdigit():
    print(FAIL + "[ERROR] Argument " + WARN + sys.argv[1] + FAIL + " is not a positive integer")
    sys.exit(1)
else:
    num_table_cards = int(sys.argv[1])

# Constant Values.
PDF_PATH = "out/tables.pdf"
IMG_PATH = "../res/" + img_name

# Font values
font_name = "Lato-Regular"
font_path = "../res/Lato/Lato-Regular.ttf"

# Set font
pdfmetrics.registerFont(TTFont(font_name, font_path))

# Define our canvas.
c = canvas.Canvas(PDF_PATH, pagesize=letter)
# from 1 to 86 (non inclusive, 85)
for i in range(1, num_table_cards + 1):
    c.setFont(font_name, 60)
    c.rotate(90)
    c.drawCentredString(6.5 * inch, 6.375 * -inch, "Table " + str(i))
    c.drawImage(IMG_PATH, 3 * inch, 6.9 * -inch, 1.5 * inch, 1.5 * inch)
    c.rotate(180)
    c.drawCentredString(6.5 * -inch, 2.375 * inch, "Table " + str(i))
    c.drawImage(IMG_PATH, 4.5 * -inch, 2 * inch, 1.5 * inch, 1.5 * inch)
    c.showPage()

print(OK + 'Processed {} Table cards to {}'.format(num_table_cards, PDF_PATH))
c.save()
