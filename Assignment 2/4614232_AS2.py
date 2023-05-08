# Import necessary libraries
import csv
from typing import List
import numpy as np


# Define a class for points in the 2D plane
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Print the point coordinates
    def print(self):
        print("{0} {1}".format(self.x, self.y))

    # Returns a list of elements for the conic equation
    def coniceq(self):
        return [self.y**2, self.x * self.y, self.x, self.y, -1]

    # Returns the square of the x-coordinate for the conic equation
    def conicsq(self):
        return -self.x**2


# Read input points from CSV file
inputarray = []
with open(r"input as2.csv", "r") as input:
    locations = csv.DictReader(input)
    for pointentry in locations:
        point = Point(pointentry["x"], pointentry["y"])
        inputarray.append(point)

calcarray = np.array(inputarray)
numOfRows = calcarray.shape[0]

sol = []
eq = []

# Check if there are exactly five points
if numOfRows == 5:
    print("Given five points a circle will be calculated")
    for n in range(5):
        eq.append(inputarray[n].coniceq())
        sol.append(inputarray[n].conicsq())
    eqarray = np.array(eq)
    solarray = np.array(sol)
    # Solve the linear system of equations
    solution = np.linalg.solve(eqarray, solarray)

    # Format the coefficients of the circle equation
    pr_solutions = [str(x) if x < 0 else "+" + str(x) for x in solution]

    # Create the circle equation string
    Equation = [
        "Equation:",
        "x^2{0}y^2{1}xy{2}x{3}y = 0".format(*pr_solutions),
    ]
    print(Equation[0], Equation[1])

    # Write the circle equation to the output CSV file
    with open("out AS2.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(Equation)
