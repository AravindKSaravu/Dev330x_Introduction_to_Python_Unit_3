
# [ ] Write a program that reads an unspecified number of integers from the command line,
# then prints out the numbers in an ascending order
# The program should have an optional argument to save the sorted numbers as a file named `sorted_numbers.txt`

# The help message should look like:
'''
usage: sort_numbers.py [-h] [-s] [numbers [numbers ...]]

positional arguments:
  numbers     int to be sorted

optional arguments:
  -h, --help  show this help message and exit
  -s, --save  save the sorted numbers on a file (sorted_numbers.txt)
'''

#HINT: use nargs = '*' in an add_argument method
import argparse

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('numbers', action = 'store', nargs = '*', type = int, help = 'int to be sorted')

# Add optional arguments
parser.add_argument('-s', '--save', action = 'store', type = str, help = 'save the sorted numbers on a file (sorted_numbers.txt)')

# Parse command-line arguments
args = parser.parse_args()

# Program
arranged = sorted(args.numbers)
print(*arranged)
 
if args.save:
    with open("sorted_numbers.txt", 'w+') as f:
        for a in arranged:
            f.write(str(a)+" ")