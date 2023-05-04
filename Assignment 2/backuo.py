import csv
from typing import List

import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def print(self):
        print("{0} {1}".format(self.x, self.y))

    def ellipse_eq(self):
        return [self.x**2, self.y**2, self.x * self.y, self.x, self.y]

    x = 0
    y = 0


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
    print("Given five points an ellipse will be calculated")
    for n in range(5):
        eq.append(inputarray[n].ellipse_eq())
        sol.append(-1)
    eqarray = np.array(eq)
    solarray = np.array(sol)
    solution = np.linalg.lstsq(eqarray, solarray, rcond=None)[0]

a, b, c, d, e = solution
ellipse_equation = f"{a:.3f}x^2 + {b:.3f}y^2 + {c:.3f}xy + {d:.3f}x + {e:.3f}y = -1"

print("Equation:", ellipse_equation)

f = open("output as2.csv", "w")

writer = csv.writer(f)
writer.writerow(["Equation:", ellipse_equation])

f.close()
