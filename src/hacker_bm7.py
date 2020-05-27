"""
Python script to generate the Hacker badges for BoilerMake VI

Author: Ken Sodetz
Since: 10/16/2018
"""
import csv
import pyqrcode
import string
from os import remove, removedirs, makedirs, path
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# BACKGROUND AND CSV FILES (Change as needed)
# ----------------------------------
background_file = "Hacker_m.jpg"
csv_file = "hackers.csv"
# ----------------------------------

# Terminal Colors
OK = '\033[92m'

# Font values
hacker_font_name = "Roboto-Black"
university_font_name = "Roboto-Medium"
info_font_name = "Roboto-Light"
hacker_font_path = "../res/Fonts/Roboto/Roboto-Black.ttf"
info_font_path = "../res/Fonts/Roboto/Roboto-Light.ttf"
university_font_path = "../res/Fonts/Roboto/Roboto-Medium.ttf"

# Constant Values. DO NOT CHANGE
BOTTOM_OFFSET = 1 * inch
CARD_WIDTH = 4 * inch
CARD_HEIGHT = 3 * inch
PDF_PATH = "out/hackers.pdf"
CSV_FILE_PATH = "data/" + csv_file
BACKGROUND_PATH = "../res/Background_JPGs/" + background_file
TMP_DIR = "tmp/"
QR_EXT = ".png"

# Define our canvas.
c = canvas.Canvas(PDF_PATH, pagesize=letter)

# Import font from .ttf file.
pdfmetrics.registerFont(TTFont(hacker_font_name, hacker_font_path))
pdfmetrics.registerFont(TTFont(info_font_name, info_font_path))
pdfmetrics.registerFont(TTFont(university_font_name, university_font_path))


class Person:
    def __init__(self, name, university, qr):
        """
        Constructor for the Person Object.
        :param name: Full name of the person.
        :param university: University the person attends.
        :param qr: QR code
        """
        self.name = string.capwords(name)
        self.name_len = len(name)

        # qr code, integer format
        self.qr = qr

        # Set font size based on name length, or shorten names if needed
        c.setFont(hacker_font_name, 18)
        if 16 <= self.name_len < 20:
            c.setFont(hacker_font_name, 16)
        elif 20 <= self.name_len < 23:
            c.setFont(hacker_font_name, 14)
        elif self.name_len >= 23:
            c.setFont(hacker_font_name, 14)
            if len(self.name.split()) == 2:
                self.name = self.name.split()[0][0] + ". " + self.name.split()[1]
            elif len(self.name.split()) == 3:
                self.name = self.name.split()[0][0] + "." + self.name.split()[1][0] + ". " + self.name.split()[2]
            elif len(self.name.split()) == 4:
                self.name = self.name.split()[0][0] + "." + self.name.split()[1][0] + ". " + self.name.split()[2] + \
                            " " + self.name.split()[3]
            elif len(self.name.split()) == 5:
                self.name = self.name.split()[0][0] + "." + self.name.split()[1][0] + "." + self.name.split()[2][0] + \
                            "." + self.name.split()[3][0] + ". " + self.name.split()[4]

        # Edits the school name to fit on the badge.
        if university == "Other/School not listed":
            self.university = " "
        elif university == "Indiana University/Purdue University at Indianapolis":
            self.university = "IUPUI"
        elif university == "Indiana University/Purdue University at Fort Wayne":
            self.university = "IPFW"
        elif university == "Illinois Institute of Technology":
            self.university = "IIT"
        elif university == "University of Illinois-Chicago":
            self.university = "UIC"
        elif university == "University of Illinois-Urbana-Champaign":
            self.university = "UIUC"
        elif university == "University of Wisconsin-Madison":
            self.university = "UW Madison"
        elif university == "University of California-Berkeley":
            self.university = "UC Berkeley"
        elif university == "Rochester Institute of Technology":
            self.university = "RIT"
        elif university == "Indiana University-Bloomington":
            self.university = "IU"
        elif university == "Michigan State University":
            self.university = "Michigan State"
        elif university == "University of California-Merced":
            self.university = "UC Merced"
        elif university == "Ivy Tech Community College":
            self.university = "Ivy Tech"
        elif university == "Ohio Wesleyan University":
            self.university = "Ohio Wesleyan"
        elif university == "The University of Mississippi":
            self.university = "Ole Miss"
        elif university == "University of Western Ontario":
            self.university = "Western University"
        elif university == "Missouri University of Science and Technology":
            self.university = "Missouri S&T"
        elif university == "Purdue University - West Lafayette" or university == "Purdue" or \
                university == "Purdue University/UC Berkeley":
            self.university = "Purdue University"
        elif university == "University of California-San Diego":
            self.university = "UCSD"
        elif university == "Colorado School of Mines":
            self.university = "CO School of Mines"
        elif university == "Franklin and Marshall College":
            self.university = "F&M"
        elif university == "University of Pennsylvania":
            self.university = "UPenn"
        elif university == "Southern Illinois University-Edwardsville":
            self.university = "SIU Edwardsville"
        elif university == "Georgia Institute of Technology":
            self.university = "Georgia Tech"
        elif university == "University of Maryland - Baltimore County":
            self.university = "UMBC"
        elif university == "Florida International University":
            self.university = "FIU"
        elif university == "University Of Minnesota - Twin Cities":
            self.university = "University of Minnesota"
        elif university == "The University of Texas at Dallas":
            self.university = "UT Dallas"
        elif university == "Virginia Polytechnic Institute & State University":
            self.university = "Virginia Tech"
        elif university == "University of science and technology Houari Boumediene.":
            self.university = "USTHB"
        elif university == "Higher School of Computer Science":
            self.university = "ESI"
        else:
            self.university = university


def draw(row_offset, hacker, left_right_offset):
    """
    Draws the Access Cards on the page.
    :param row_offset: Row to draw on, from 0 to 2.
    :param hacker: Person object
    :param left_right_offset: Offset for drawing on the left or right side of the page
    :return: none
    """
    # Draws an empty badge on the canvas.
    c.drawImage(BACKGROUND_PATH, left_right_offset, BOTTOM_OFFSET + row_offset * CARD_HEIGHT, width=CARD_WIDTH,
                height=CARD_HEIGHT, mask=None)

    c.setFillColorRGB(1, 1, 1)

    # Draw Hacker's full name
    c.drawString(x=0.6 * inch + left_right_offset, y=BOTTOM_OFFSET + 0.4 * inch + row_offset * CARD_HEIGHT,
                 text=hacker.name)

    # Draws Boilermake website
    c.setFont(info_font_name, 10.5)
    c.drawString(x=(.7 + 2.15) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.365 * inch + row_offset * CARD_HEIGHT,
                 text="Boilermake.org")

    # Draws Boilermake slack
    c.drawString(x=(.7 + 1.59) * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                 text="boilermakevii.slack.com")

    # Draw Hacker's university - 0.6" offset from the left, 0.175" offset from the bottom
    c.setFont(university_font_name, 10.5)
    c.drawString(x=0.6 * inch + left_right_offset, y=BOTTOM_OFFSET + 0.175 * inch + row_offset * CARD_HEIGHT,
                 text=hacker.university)

    # Draw qr code - 1" x 1" qr code drawn on the center of the badge
    qr_path = get_qr(hacker.qr)
    c.drawImage(qr_path, 1.5 * inch + left_right_offset,
                BOTTOM_OFFSET + 0.93 * inch + row_offset * CARD_HEIGHT, width=1 * inch, height=1 * inch, mask=None)

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
    """
    Draws margins on canvas for debugging
    :return: none
    """
    c.setFillColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(0, 1 * inch, 8.5 * inch, 1 * inch)
    c.line(0, 10 * inch, 8.5 * inch, 10 * inch)
    c.line(0.25 * inch, 0, 0.25 * inch, 11.5 * inch)
    c.line(4.25 * inch, 0, 4.25 * inch, 11.5 * inch)
    c.line(8.25 * inch, 0, 8.25 * inch, 11.5 * inch)


if __name__ == '__main__':
    # Create temporary directory to save qr codes
    # makedirs(TMP_DIR, False)
    if not path.isdir(TMP_DIR):
        makedirs(TMP_DIR)
    # Open CSV file.
    print('Reading from {}'.format(CSV_FILE_PATH))
    with open(CSV_FILE_PATH, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_num = 0
        # For each row in the csv file.
        for row in csv_reader:
            # Create instance of a person object to pass to either the left draw or right draw function.
            person = Person(name=row[0].strip(), university=row[2].strip(), qr=row[3].strip())
            # If line is even, draw on the left. Else draw on the right.
            if line_count % 2 == 0:
                draw(row_num, person, 0.25 * inch)
            else:
                draw(row_num, person, CARD_WIDTH + 0.25 * inch)
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
