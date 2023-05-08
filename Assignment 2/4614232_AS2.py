import csv
from typing import List
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def print(self):
        print("{0} {1}".format(self.x, self.y))

    def coniceq(self):
        return [self.y**2, self.x * self.y, self.x, self.y, -1]

    def conicsq(self):
        return -self.x**2


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


if numOfRows == 5:
    print("Given five points a circle will be calculated")
    for n in range(5):
        eq.append(inputarray[n].coniceq())
        sol.append(inputarray[n].conicsq())
    eqarray = np.array(eq)
    solarray = np.array(sol)
    solution = np.linalg.solve(eqarray, solarray)
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
    "x^2{0}y^2{1}xy{2}x{3}y = 0".format(pr_sol0, pr_sol1, pr_sol2, pr_sol3, pr_sol4),
]
print(Equation[0], Equation[1])

f = open("out AS2.csv", "w")

writer = csv.writer(f)
writer.writerow(Equation)

f.close()
