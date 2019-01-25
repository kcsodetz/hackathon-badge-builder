# Hackathon Badge Builder
[![Maintainability](https://api.codeclimate.com/v1/badges/e4d3a4dc967cbb05df5b/maintainability)](https://codeclimate.com/github/kcsodetz/AccessCardGenerator/maintainability)

Python script to create name badges for BoilerMake VI (and future BoilerMake Hackathons as well), as well as formatted table cards for hacker demos. 

## Badge Spec
The badges are output as a PDF. The script is set up to be 3 inches tall and 4.25 inches wide, layed out on US letter sized paper from the top left corner down, with a 2 inch margin offset at the bottom of the page. This gives a total of 6 badges per page.  

## Getting Started

These instructions will get a functional copy on your local machine.

### Installing

Clone the repository using the command line and navigate to its directory. In order for the script to run properly, you need both a `data` and `out` directory, as well as the reportlab python library. To set up the environment, run

```sh
$ ./setup.sh
```

This will install the reportlab library as well as create the directories above. 

### Importing Data

The script reads data from `.csv` files. They will be placed in the `data` directory, in the following format:

#### Hackers

```
"Last_Name","First_Name","School","\"skill_1,skill_2,skill_3\""
```

#### Execs

```
"Full_Name"
```

You will need to change the file names in both `hacker.py` and `exec.py` to match the paths for the csv files.

### Changing Background Assets

The background assets are stored in `res/Background_JPGs`. If adding new backgrounds, either make sure they are named as such:

1) Hacker Background = hacker_bkgd.jpg
2) Sponsor Background = sponsor_bkgd.jpg
3) Exec Background = exec_bkgd.jpg

Alternatively, you can change the background names in the python files themselves. For example, in `hacker.py`

```python
...

# BACKGROUND AND CSV FILES (Change as needed)
# ----------------------------------
background_file = "hacker_bkgd.jpg"
csv_file = "rsvp_badges_2.csv"
# ----------------------------------

...
```

### Changing Table Card Logo

The logo for the Table Cards is located in the root of the `res/` directory. The default logo can be changed by adding your logo to this directory and changing the name in `table-cards.py` if needed.

## Running Scripts

All scripts should be run through the command line.

### Badges

After adding the files and checking the file paths, you can run get the hacker badges by running

```sh
$ python3 hacker.py
```

To generate the exec badges, run

```sh
$ python3 exec.py
```

For blank hacker or sponsor bagdes, run the `generic-badge.py` script with the argument being either `hacker` or `sponsor`

```sh
$ python3 generic-badge.py [type]
```

### Table Cards

To for table cards, run `table-cards.py` with any positive integer argument for the number of cards needed.

```sh
$ python3 table-cards.py [number]
```

## Final PDF's

All completed pdf's can be found in the `out/` directory.
