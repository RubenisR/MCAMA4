# Write a Python program which calculates the formula of the conic section for 5 given points in the plane.
# The file “input as2.csv” should be used as an input.The output should be in the same format as the file “output as2.csv”

import csv
import numpy as np
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def print(self):
        print("{0} {1}".format(self.x, self.y))

    def conic_sq(self):
        return [self.x**2, self.y**2, 1]

    def conic_eq(self):
        return [self.x * self.y, self.x, self.y]

    x = 0
    y = 0


def dictionary(self):
    return self.__dict__


inputarray = []
with open(r"input as2.csv", "r") as input:
    locations = csv.DictReader(input)
    for pointentry in locations:
        point = Point(pointentry["x"], pointentry["y"])
        inputarray.append(point)

calcarray = np.array(inputarray)
numrows = calcarray.shape[0]
sol = []
eq = []

if numrows == 5:
    print("Given five points an elipse will be calculated")
    eqarray = np.zeros((5, 5))
    solarray = np.zeros(5)
    for i in range(5):
        eqarray[i, :3] = inputarray[i].conic_eq()
        eqarray[i, 3:] = [-1, 0]
        solarray[i] = -inputarray[i].conic_sq()[2]
    solution, residuals, rank, s = np.linalg.lstsq(eqarray, solarray, rcond=None)


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
    pr_sol4 = abs(solution[4])

Equation = [
    "Equation:",
    "{0}x^2{1}xy{2}y^2{3}x{4}y+1 = 0".format(
        pr_sol0, pr_sol1, pr_sol2, pr_sol3, pr_sol4
    ),
]
print(Equation[0], Equation[1])


f = open("output AS2.csv", "w")

writer = csv.writer(f)
writer.writerow(Equation)

f.close()
