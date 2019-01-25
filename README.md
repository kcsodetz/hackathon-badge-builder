# Hackathon Badge Builder
[![Maintainability](https://api.codeclimate.com/v1/badges/e4d3a4dc967cbb05df5b/maintainability)](https://codeclimate.com/github/kcsodetz/AccessCardGenerator/maintainability)

Python script to create name badges for BoilerMake VI (and future BoilerMake Hackathons as well)

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

After adding the files and checking the file paths, you can run the `hacker.py` or `exec.py` with just 

```sh
$ python3 hacker.py
Reading from data/rsvp_badges_2.csv
Processed 597 Badges to out/hackers.pdf
```







