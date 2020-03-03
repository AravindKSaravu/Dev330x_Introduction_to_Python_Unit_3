
# [ ] Write a program that reads a date (month, day, year) as command-line arguments in order
# then prints the day of the week for that date.
# If an optional flag (-c or --complete) is specified, the program should print the full date (not only the day of the week).

# The help message should look like:

'''
usage: day_finder.py [-h] [-c] month day year

positional arguments:
  month           Month as a number (1, 12)
  day             Day as a number (1, 31) depending on the month
  year            Year as a 4 digits number (2018)

optional arguments:
  -h, --help      show this help message and exit 
  -c, --complete  Show complete formatted date
'''

# HINT: Use a date object with strftime
import argparse
from datetime import datetime

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('month', action = 'store', type = int, help = 'Month as a number (1, 12)')
parser.add_argument('day', action = 'store', type = int, help = 'Day as a number (1, 31) depending on the month')
parser.add_argument('year', action = 'store', type = int, help = 'Year as a 4 digit number (2018)')

# Add optional arguments
parser.add_argument('-c', '--complete', action = 'store_true', help = 'Show complete formatted date')

# Parse command-line arguments
args = parser.parse_args()

# Program
t = datetime(month = args.month, day = args.day, year = args.year)
print(t.strftime("%A"), end = " ")

# If args.complete is used, print the date with the complete format

if args.complete:
    print(t.strftime("%B, %d, %Y"))
