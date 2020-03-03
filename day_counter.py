
# [ ] Write a program that reads a date from the command line as numbers (month  then day then year),
# if the date entered is in the past, a message saying "The date has passed" should be printed
# if the date is in the future the program should display the number of days remaining from today till that date,
# there should be an optional command line flag that displays the results in total number of seconds instead of days

# help message should look like:
'''
usage: day_counter.py [-h] [-s] month day year

positional arguments:
  month                Month as a number (1, 12)
  day                  Day as a number (1, 31) depending on the month
  year                 Year as a 4 digits number (2018)

optional arguments:
  -h, --help           show this help message and exit
  -s, --total_seconds  Show the time difference in total number of seconds
'''
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('month', action = 'store', type = int, help = 'Month as a number (1, 12)')
parser.add_argument('day', action = 'store', type = int, help = 'Day as a number (1, 31) depending on the month')
parser.add_argument('year', action = 'store', type = int, help = 'Year as a 4 digit number (2018)')

# Add optional arguments
parser.add_argument('-s', '--total_seconds', action = 'store_true', help = 'Show the time difference in total number of seconds')

# Parse command-line arguments
args = parser.parse_args()

# Program
t = datetime(month = args.month, day = args.day, year = args.year)
td = abs(t - datetime.today())

if t < datetime.today():
    print("The date has passed")   
else:
    print("There is",td.days,"days left until this date")

# If args.total_seconds is used, print the date with the complete format
if args.total_seconds:
        print("There is",int(td.total_seconds()),"seconds difference between this date and today")