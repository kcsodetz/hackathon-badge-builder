# Hackathon Badge Builder


Python script to create name badges for BoilerMake VII, as well as formatted table 
cards for hacker demos. 

## Badge Spec
The badges are output as a PDF. The script is set up to be 3 inches tall and 4.25 inches wide, layed out on US letter 
sized paper from the top left corner down, with a 2 inch margin offset at the bottom of the page. This gives a total of 
6 badges per page.  

## Getting Started

These instructions will get a functional copy on your local machine.

### Installing

Clone the repository using the command line and navigate to its directory. In order for the script to run properly, you
need both a `data` and an `out` directory, as well as the reportlab, pyqrcode, and pypng python libraries. To set up 
the environment, run

```sh
$ ./setup.sh
```

This will install the reportlab, pyqrcode, and pypng libraries as well as create the directories above. 

### Importing Data

The script reads data from `.csv` files. They will be placed in the `data` directory, in the following format:

#### Hackers

The script expects data in the csv to be formatted as such:

```
name_1 name_2 name_3 ... name_n, email, school, qr_id
```

Where the hacker can have as many `names` as they want on their badge, provided that each name is separated by a white 
space. Names are truncated as needed (anything above 22 characters), and the way they are presented are found in the 
`Person` class in `hacker.py`.

The `email` is expected to come next, but is not used in the badge itself.

The `school` will be displayed on the badge, but due to character restraints, school names greater than 22 characters 
will have to be added to the truncation list starting at line 87 in `hackers.py`.

The `qr_id` is a unique integer passed on by the dev team which is used to generate a unique qr code for each hacker.

A sample entry will look like the following:

```
Purdue Pete Somelastname, pete@purdue.edu, Purdue University, 0123456798
```

#### Execs

```
"Full_Name"
```

You will need to change the file names in both `hacker.py` and `exec.py` to match the paths for the csv files.

### Changing Background Assets

The background assets are stored in `res/Background_JPGs`. If adding new backgrounds, either make sure they are named 
as such:

1) Hacker Background = `hacker_bkgd.jpg`
2) Sponsor Background = `sponsor_bkgd.jpg`
3) Exec Background = `exec_bkgd.jpg`

Alternatively, you can change the background names in the python files themselves. For example, in `hacker.py`

```python3
...

# BACKGROUND AND CSV FILES (Change as needed)
# ----------------------------------
background_file = "hacker_bkgd.jpg"
csv_file = "rsvp_badges_2.csv"
# ----------------------------------

...
```

### Changing Table Card Logo

The logo for the Table Cards is located in the root of the `res/` directory. The default logo can be changed by adding 
your logo to this directory and changing the name in `table-cards.py` if needed.

## Running the Scripts

All scripts should be run through the command line.

### Badges

After adding the files and checking the file paths, you can run get the hacker badges by running

```sh
$ python3 hacker.py
```

To generate the exec badges, run

```sh
$ python3 organizer.py
```

To generate the sponsor badges, run

```sh
$ python3 sponsors.py
```

### Table Cards

To for table cards, run `table-cards.py` with any positive integer argument for the number of cards needed.

```sh
$ python3 table-cards.py [number]
```

## Final PDF's

All completed pdf's can be found in the `out/` directory.
