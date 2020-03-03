# [ ] The following program asks the user for a circle radius then display the area and circumference
# Modify the program so it only displays the information when executed directly
# The program should not display anything if it is imported as a module 
from math import pi

def circle_area(r):
    return pi * (r ** 2)

def circle_circumference(r):
    return 2 * pi * r

radius = float(input("Enter radius: "))
print("Area =", circle_area(radius))
print("Circumference =", circle_circumference(radius))
