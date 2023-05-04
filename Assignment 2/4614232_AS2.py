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

    def elipse_eq(self):
        return [self.x**2, self.y**2, self.x * self.y, self.x, self.y, 1]

    def elipse_sq(self):
        return self.x**2 + self.y**2 - 1

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
    for i in range(5):
        eq.append(inputarray[i].elipse_eq())
        sol.append(inputarray[i].elipse_sq())
    eqarray = np.array(eq)
    solarray = np.array(sol)
    solution = np.linalg.solve(eqarray, solarray)


Equation = ["Equation:", "{0}y^2,{1}x^2+{2}xy+{3}x+{4}y=1"]
print(Equation[0], Equation[1])

f = open("output AS1.csv", "w")

writer = csv.writer(f)
writer.writerow(Equation)

f.close()
