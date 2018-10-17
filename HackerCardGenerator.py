"""
Python script to generate the Hacker badges for Boilermake VI

Author: Ken Sodetz
Since: 10/16/2018
"""
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Constant Values
font_name = "Lato-Regular"
font_path = "Lato/Lato-Regular.ttf"
edge_offset = .15 * inch
bottom_offset = 1 * inch
AC_width = 4 * inch
AC_height = 3.25 * inch

# Variable Values
jpg_path = "AccessCardsJpg/AC_Hacker.jpg"
pdf_file_name = "hackers.pdf"

# Define our canvas
c = canvas.Canvas(pdf_file_name)

# Import font from .ttf file
pdfmetrics.registerFont(TTFont(font_name, font_path))


# Person/Hacker Class
class Person:
    def __init__(self, first_name, last_name, university):
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.name_len = len(first_name) + len(last_name) + 1

        if len(self.first_name) > 18:
            words = self.first_name.split()
            letters = [word[0] for word in words]
            self.first_name = "".join(letters)

        if university == "Other/School not listed":
            self.university = " "
        elif university == "Indiana University/Purdue University at Indianapolis":
            self.university = "IUPUI"
        elif university == "Indiana University/Purdue University at Fort Wayne":
            self.university = "IPFW"
        elif university == "University of Illinois-Urbana-Champaign":
            self.university = "UIUC"
        elif university == "Rose-Hulman Institute of Technology":
            self.university = "RHIT"


# Left row of cards
def draw_left(i, hacker):
    c.drawImage(jpg_path, edge_offset, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)

    if hacker.name_len <= 18:
        c.setFont(font_name, 16)
    else:
        c.setFont(font_name, 12)

    c.drawCentredString(x=edge_offset + 2.9 * inch, y=bottom_offset + 2.25 * inch + i * AC_height,
                        text=hacker.first_name + " " + hacker.last_name)
    c.setFont(font_name, 10)
    c.drawCentredString(x=edge_offset + 2.9 * inch, y=bottom_offset + 2 * inch + i * AC_height,
                        text=hacker.university)


# Right row of cards
def draw_right(i, hacker):
    c.drawImage(jpg_path, edge_offset + AC_width, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)
    if hacker.name_len <= 18:
        c.setFont(font_name, 16)
    else:
        c.setFont(font_name, 12)
    c.drawCentredString(x=edge_offset + 2.9 * inch + AC_width, y=bottom_offset + 2.25 * inch + i * AC_height,
                        text=hacker.first_name + " " + hacker.last_name)
    c.setFont(font_name, 10)
    # If a listed school, print onto badge
    c.drawCentredString(x=edge_offset + 2.9 * inch + AC_width, y=bottom_offset + 2 * inch + i * AC_height,
                        text=hacker.university)


with open('rsvp_badges.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    row_num = 0
    for row in csv_reader:
        person = Person(first_name=row[0], last_name=row[1], university=row[2])
        if line_count % 2 == 0:
            draw_left(row_num, person)
        else:
            draw_right(row_num, person)
            row_num += 1

        if row_num == 3:
            c.showPage()
            row_num = 0

        line_count += 1

print(f'Processed {line_count} lines.')

c.save()
