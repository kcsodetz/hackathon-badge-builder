"""
Python script to generate the Hacker badges for BoilerMake VI

Author: Ken Sodetz
Since: 10/16/2018
"""
import csv
import pyqrcode
import png
from os import remove, removedirs, makedirs
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# BACKGROUND AND CSV FILES (Change as needed)
# ----------------------------------
background_file = "blank.jpg"
csv_file = "qr_test.csv"
# ----------------------------------

# Terminal Colors
OK = '\033[92m'

# Font values
font_name = "Lato-Regular"
font_path = "../res/Lato/Lato-Regular.ttf"

# Constant Values. DO NOT CHANGE
BOTTOM_OFFSET = 2 * inch
CARD_WIDTH = 4.25 * inch
CARD_HEIGHT = 3 * inch
PDF_PATH = "out/hackers.pdf"
CSV_FILE_PATH = "data/" + csv_file
ICON_PATH = "../res/language_icons_JPGs/"
BACKGROUND_PATH = "../res/Background_JPGs/" + background_file

# Define our canvas.
c = canvas.Canvas(PDF_PATH, pagesize=letter)

# Import font from .ttf file.
pdfmetrics.registerFont(TTFont(font_name, font_path))


class Person:
    def __init__(self, first_name, last_name, university, skills, qr):
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
        self.skills = [skill.strip('\"').strip('\\') for skill in skills]
        self.name_len = len(first_name) + len(last_name) + 1

        # Checks if the First name is longer than 18 characters. If so, then shorten.
        if len(self.first_name) > 18:
            words = self.first_name.split()
            letters = [word[0] for word in words]
            self.first_name = "".join(letters)

        # set font size based on name length
        c.setFont(font_name, 14)
        if self.name_len <= 22:
            c.setFont(font_name, 16)

        # Edits the school name to fit on the badge.
        if university == "Other/School not listed":
            self.university = " "
        elif university == "Indiana University/Purdue University at Indianapolis":
            self.university = "IUPUI"
        elif university == "Indiana University/Purdue University at Fort Wayne":
            self.university = "IPFW"

        # qr code, integer format
        self.qr = qr


def draw(i, hacker, left_right_offset):
    """
    Draws the Access Cards on the page.
    :param i: Row offset to draw on, from 0 to 2.
    :param hacker: Person object to reference to.
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: none
    """
    # Draws an empty badge on the canvas.
    c.drawImage(BACKGROUND_PATH, left_right_offset, BOTTOM_OFFSET + i * CARD_HEIGHT, width=CARD_WIDTH,
                height=CARD_HEIGHT, mask=None)

    # Draws the full name on the badge.
    c.drawCentredString(x=2.9 * inch + left_right_offset, y=BOTTOM_OFFSET + 2 * inch + i * CARD_HEIGHT,
                        text=hacker.first_name + " " + hacker.last_name)

    # Draws the school on the badge.
    c.setFont(font_name, 10)
    c.drawCentredString(x=2.9 * inch + left_right_offset, y=BOTTOM_OFFSET + 1.75 * inch + i * CARD_HEIGHT,
                        text=hacker.university)

    # Draws the skill icon(s) on the badge, depending if they have 1, 2, or 3 skills.
    # if len(hacker.skills) == 2:
    #     start = 1.425
    #     step = .9
    # elif len(hacker.skills) == 3:
    #     start = 1.175
    #     step = .7
    # else:
    #     start = 1.875
    #     step = 0
    #
    # for skill in hacker.skills:
    #     if skill == "null" or skill == "":
    #         break
    #     c.drawImage(ICON_PATH + skill + ".jpg", start * inch + left_right_offset,
    #                 BOTTOM_OFFSET + 0.1 * inch + i * CARD_HEIGHT, width=30, height=30, mask=None)
    #     start += step

    qr_path = get_qr(hacker)

    # Draw qr code
    c.drawImage(qr_path, 1 * inch + left_right_offset,
                BOTTOM_OFFSET + 0.1 * inch + i * CARD_HEIGHT, width=30, height=30, mask=None)
    remove(qr_path)


def get_qr(hacker):
    qr_data = hacker.qr
    print(hacker.qr)
    qr_code = pyqrcode.create(qr_data)
    file_path = 'tmp/' + qr_data + '.png'
    qr_code.png(file_path, scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    return file_path


if __name__ == '__main__':
    makedirs("tmp", False)
    # Open CSV file.
    print('Reading from {}'.format(CSV_FILE_PATH))
    with open(CSV_FILE_PATH, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_num = 0
        # For each row in the csv file.
        for row in csv_reader:
            # Create instance of a person object to pass to either the left draw or right draw function.
            person = Person(first_name=row[0], last_name=row[1], university=row[2], qr=row[3], skills=row[4:7])
            # If line is even, draw left. Else draw right.
            if line_count % 2 == 0:
                draw(row_num, person, 0)
            else:
                draw(row_num, person, CARD_WIDTH)
                row_num += 1

            # If on the third row, go to a new page and reset the row.
            if row_num == 3:
                c.showPage()
                row_num = 0

            line_count += 1

    removedirs("tmp")
    print(OK + 'Processed {} Badges to {}'.format(line_count, PDF_PATH))
    c.save()
