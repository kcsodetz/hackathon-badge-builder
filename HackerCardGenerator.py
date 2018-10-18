"""
Python script to generate the Hacker badges for Boilermake VI

Author: Ken Sodetz
Since: 10/16/2018
"""
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Constant Values. Do not change
bottom_offset = 2 * inch
AC_width = 4.25 * inch
AC_height = 3 * inch

# Variable Values, change depending on the needs / paths.
font_name = "Lato-Regular"
font_path = "Resources/Lato/Lato-Regular.ttf"
jpg_path = "Resources/AccessCardsJpg/AC_Hacker.jpg"
icon_path = "Resources/language_icons_jpg/"
pdf_file_name = "hackers.pdf"
csv_file_path = "rsvp_badges_2.csv"

# Define our canvas.
c = canvas.Canvas(pdf_file_name, pagesize=letter)

# Import font from .ttf file.
pdfmetrics.registerFont(TTFont(font_name, font_path))


class Person:
    def __init__(self, first_name, last_name, university, skills):
        """
        Constructor for the Person Object.
        :param first_name: First name of the person.
        :param last_name: Last name of the person.
        :param university: University the person attends.
        :param skills: Skills list that the person has. Can be from 0 to 3 skills.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.skills = [skill.strip('\"') for skill in skills]
        self.name_len = len(first_name) + len(last_name) + 1

        # Checks if the First name is longer than 18 characters. If so, then shorten.
        if len(self.first_name) > 18:
            words = self.first_name.split()
            letters = [word[0] for word in words]
            self.first_name = "".join(letters)

        # Edits the school name to fit on the badge.
        if university == "Other/School not listed":
            self.university = " "
        elif university == "Indiana University/Purdue University at Indianapolis":
            self.university = "IUPUI"
        elif university == "Indiana University/Purdue University at Fort Wayne":
            self.university = "IPFW"


def draw_left(i, hacker):
    """
    Draws the Access Cards on the left-hand side of the page.
    :param i: Row offset to draw on, from 0 to 2.
    :param hacker: Person object to reference to.
    :return: none
    """

    # Draws an empty badge on the canvas.
    c.drawImage(jpg_path, 0, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)

    # Check length of hacker name to set the font.
    if hacker.name_len <= 22:
        c.setFont(font_name, 16)
    else:
        c.setFont(font_name, 14)

    # Draws the first and last name on the badge.
    c.drawCentredString(x=2.9 * inch, y=bottom_offset + 2 * inch + i * AC_height,
                        text=hacker.first_name + " " + hacker.last_name)

    # Draws the school on the badge.
    c.setFont(font_name, 10)
    c.drawCentredString(x=0 + 2.9 * inch, y=bottom_offset + 1.75 * inch + i * AC_height,
                        text=hacker.university)

    # Draws the skill icon(s) on the badge, depending if they have 1, 2, or 3 skills.
    if len(hacker.skills) == 1 and hacker.skills[0] != "null" and hacker.skills[0].strip('\\') != "":
        c.drawImage(icon_path + hacker.skills[0].strip('\\') + ".jpg", 1.875 * inch,
                    bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
    elif len(hacker.skills) == 2:
        n = 0
        for skill in hacker.skills:
            if n == 1:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 1.425 * inch,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            else:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 2.325 * inch,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            n += 1
    elif len(hacker.skills) == 3:
        n = 0
        for skill in hacker.skills:
            if n == 0:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 1.175 * inch,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            elif n == 1:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 1.875 * inch,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            else:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 2.575 * inch,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            n += 1


def draw_right(i, hacker):
    """
    Draws the Access Cards on the right-hand side of the page.
    :param i: Row offset to draw on, from 0 to 2.
    :param hacker: Person object to reference to.
    :return: none
    """

    # Draws an empty badge on the canvas.
    c.drawImage(jpg_path, AC_width, bottom_offset + i * AC_height, width=AC_width,
                height=AC_height, mask=None)

    # Checks for the length of the name to set the font size.
    if hacker.name_len <= 22:
        c.setFont(font_name, 16)
    else:
        c.setFont(font_name, 14)

    # Draws the full name on the badge.
    c.drawCentredString(x=2.9 * inch + AC_width, y=bottom_offset + 2 * inch + i * AC_height,
                        text=hacker.first_name + " " + hacker.last_name)

    # Draws the school on the badge.
    c.setFont(font_name, 10)
    c.drawCentredString(x=2.9 * inch + AC_width, y=bottom_offset + 1.75 * inch + i * AC_height,
                        text=hacker.university)

    # Draws the skill icon(s) on the badge, depending if they have 1, 2, or 3 skills.
    if len(hacker.skills) == 1 and hacker.skills[0] != "null" and hacker.skills[0].strip('\\') != "":
        c.drawImage(icon_path + hacker.skills[0].strip('\\') + ".jpg", 1.875 * inch + AC_width,
                    bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
    elif len(hacker.skills) == 2:
        n = 0
        for skill in hacker.skills:
            if n == 1:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 1.425 * inch + AC_width,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            else:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 2.325 * inch + AC_width,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            n += 1
    elif len(hacker.skills) == 3:
        n = 0
        for skill in hacker.skills:
            if n == 0:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 1.175 * inch + AC_width,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            elif n == 1:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 1.875 * inch + AC_width,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            else:
                c.drawImage(icon_path + skill.strip('\\') + ".jpg", 2.575 * inch + AC_width,
                            bottom_offset + 0.1 * inch + i * AC_height, width=30, height=30, mask=None)
            n += 1


# Open CSV file.
print(f'Reading from {csv_file_path}')
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    row_num = 0
    # For each row in the csv file.
    for row in csv_reader:
        # Create instance of a person object to pass to either the left draw or right draw function.
        person = Person(first_name=row[0], last_name=row[1], university=row[2], skills=row[3:6])
        # If line is even, draw left. Else draw right.
        if line_count % 2 == 0:
            draw_left(row_num, person)
        else:
            draw_right(row_num, person)
            row_num += 1

        # If on the third row, go to a new page and reset the row.
        if row_num == 3:
            c.showPage()
            row_num = 0

        line_count += 1

print(f'Processed {line_count} Badges to {pdf_file_name}')

c.save()
