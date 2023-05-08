# Import necessary libraries
import csv
import numpy as np
from typing import List


# Define a class for points in the 2D plane
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Print the point coordinates
    def print(self):
        print("{0} {1}".format(self.x, self.y))

    # Returns a list containing x^2, y^2, and 1 for the conic equation
    def conic_sq(self):
        return [self.x**2, self.y**2, 1]

    # Returns a list containing xy, x, and y for the conic equation
    def conic_eq(self):
        return [self.x * self.y, self.x, self.y]

    x = 0
    y = 0


# Read input points from CSV file
inputarray = []
with open(r"input as2.csv", "r") as input:
    locations = csv.DictReader(input)
    for pointentry in locations:
        point = Point(pointentry["x"], pointentry["y"])
        inputarray.append(point)

# Check if there are exactly five points
numrows = len(inputarray)

if numrows == 5:
    print("Given five points an elipse will be calculated")
    eqarray = np.zeros((5, 5))
    solarray = np.zeros(5)
    for i in range(5):
        eqarray[i, :3] = inputarray[i].conic_eq()
        eqarray[i, 3:] = [-1, 0]
        solarray[i] = -inputarray[i].conic_sq()[1]

    # Add small value to the diagonal to avoid singularity
    eqarray = eqarray + np.eye(5) * 1e-9

    # Solve the linear system of equations
    solution = np.linalg.solve(eqarray, solarray)

    # Format the coefficients of the conic equation
    pr_solutions = [str(x) if x < 0 else "+" + str(x) for x in solution[:-1]]
    pr_solutions.append("+" + str(abs(solution[-1])))

    # Create the conic equation string
    Equation = [
        "Equation:",
        "{0}x^2{1}xy{2}y^2{3}x{4}y+1 = 0".format(*pr_solutions),
    ]
    print(Equation[0], Equation[1])

    # Write the conic equation to the output CSV file
    with open("output AS2.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(Equation)
