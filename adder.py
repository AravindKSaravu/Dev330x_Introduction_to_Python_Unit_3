# [x] Write a program that reads an unspecified number of integers from the command line,
# then prints out the sum of all the numbers
# the program should also have an optional argument to show the product of the numbers (in addition to the sum)
# help message should look like:
'''
usage: adder.py [-h] [-p] [numbers [numbers ...]]

positional arguments:
  numbers        numbers to be added (or multiplied)

optional arguments:
  -h, --help     show this help message and exit
  -p, --product  show the product of the numbers (in addition to the displayed
                 sum)
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('numbers', action = 'store', nargs = '*', type = int, help = 'numbers to be added (or multiplied)')
parser.add_argument('-p', '--product', action = 'count', help = 'show the product of the numbers (in addition to the displayed sum)')
args = parser.parse_args()
print(sum(args.numbers))
if args.product:
    a = 1
    for b in args.numbers:
        a *= b
    print(a)