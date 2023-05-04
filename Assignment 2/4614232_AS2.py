# These lines are importing necessary modules for the code to run.
import csv
import numpy as np
from typing import List


# The class "Point" represents a point in a 2D plane and has methods to print its coordinates and
# return coefficients of a conic equation.
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def print(self):
        """
        prints the values of the attributes "x" and "y".
        """
        print("{0} {1}".format(self.x, self.y))

    def conic_eq(self):
        return [self.x**2, self.x * self.y, self.y**2, self.x, self.y]

    def conic_constant(self):
        return -1

    x = 0
    y = 0


def dictionary(self):
    """
    The function returns the dictionary representation of an object's attributes.
    :return: The method `dictionary` is returning the dictionary representation of the object's
    attributes using the `__dict__` attribute.
    """
    return self.__dict__


# This code is reading data from a CSV file named "input as2.csv" and creating a list of Point objects
# called "inputarray". The CSV file contains x and y coordinates of points in a 2D plane. The code
# uses the csv module to read the file and csv.DictReader to create a dictionary for each row in the
# file. Then, it creates a Point object for each row using the x and y values from the dictionary and
# appends it to the inputarray list.
inputarray = []
with open(r"input as2.csv", "r") as input:
    locations = csv.DictReader(input)
    for pointentry in locations:
        point = Point(pointentry["x"], pointentry["y"])
        inputarray.append(point)

# `calcarray = np.array(inputarray)` is converting the list of Point objects `inputarray` into a numpy
# array called `calcarray`.
calcarray = np.array(inputarray)
numrows = calcarray.shape[0]
sol = []
eq = []
# This code block checks if the number of rows in the `calcarray` numpy array is equal to 5. If it is,
# it assumes that the points represent an ellipse and calculates the coefficients of the conic
# equation of the ellipse using the least squares method. It creates two lists `eq` and `sol` to store
# the coefficients of the conic equation and the constant term respectively for each point. It then
# converts these lists into numpy arrays `eqarray` and `solarray` and uses the `np.linalg.lstsq()`
# function to calculate the coefficients of the conic equation. The resulting coefficients are stored
# in the `solution` variable.
if numrows == 5:
    print("Given five points an elipse will be calculated")
    for i in range(5):
        eq.append(inputarray[i].conic_eq())
        sol.append(inputarray[i].conic_constant())
    eqarray = np.array(eq)
    solarray = np.array(sol)
    solution, _, _, _ = np.linalg.lstsq(eqarray, solarray, rcond=None)


# This code block is formatting the coefficients of the conic equation calculated using the least
# squares method. It checks if each coefficient is negative or positive and adds a "+" sign if it is
# positive. It then converts each coefficient to a string and stores it in variables `pr_sol0`,
# `pr_sol1`, `pr_sol2`, `pr_sol3`, and `pr_sol4`. These variables are used later to print the equation
# of the ellipse in a formatted way.
if solution[0] < 0:
    pr_sol0 = str(solution[0])
else:
    pr_sol0 = "+" + str(solution[0])
if solution[1] < 0:
    pr_sol1 = str(solution[1])
else:
    pr_sol1 = "+" + str(solution[1])
if solution[2] < 0:
    pr_sol2 = str(solution[2])
else:
    pr_sol2 = "+" + str(solution[2])
if solution[3] < 0:
    pr_sol3 = str(solution[3])
else:
    pr_sol3 = "+" + str(solution[3])
if solution[4] < 0:
    pr_sol4 = str(solution[4])
else:
    pr_sol4 = "+" + str(solution[4])

# This code block is creating a list called `Equation` which contains two strings. The first string is
# "Equation:" and the second string is a formatted string that represents the equation of the ellipse
# calculated using the least squares method. The formatted string contains placeholders `{0}`, `{1}`,
# `{2}`, `{3}`, and `{4}` which are replaced with the values of `pr_sol0`, `pr_sol1`, `pr_sol2`,
# `pr_sol3`, and `pr_sol4` respectively.
Equation = [
    "Equation:",
    "{0}x^2{1}xy{2}y^2{3}x{4}y+1 = 0".format(
        pr_sol0, pr_sol1, pr_sol2, pr_sol3, pr_sol4
    ),
]
print(Equation[0], Equation[1])


# These lines of code are creating a new CSV file named "output AS2.csv" and writing the equation of
# the ellipse calculated using the least squares method to the file.
f = open("output AS2.csv", "w")

writer = csv.writer(f)
writer.writerow(Equation)

f.close()
