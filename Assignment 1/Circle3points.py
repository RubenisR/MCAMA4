import csv  # importing CSV library to use csv functions
from typing import List

import numpy as np  # importing CSV library to use matrix-calculations


# The class Point initializes an object with x and y coordinates as float values.
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # [\]

    def print(self):
        """
        prints the values of the attributes "x" and "y".
        """
        print("{0} {1}".format(self.x, self.y))

    # [\]
    def circeq(self):
        return [self.x, self.y, -1]

    def circsq(self):
        return -self.x**2 - self.y**2

    x = 0
    y = 0


# [?????????????????????]
def dictionary(self):
    """
    The function returns the dictionary representation of an object's attributes.
    :return: The method `dictionary` is returning the dictionary representation of the object's
    attributes using the `__dict__` attribute.
    """
    return self.__dict__


# [\]

# [?????????????????????]
# `inputarray = []` initializes an empty list called `inputarray`. This list will be used to store
# `Point` objects created from the data in the input file.
inputarray = []
# [\]

# [?????????????????????]
# This code is opening a CSV file named "inputfile AS1.csv" in read mode using the `open()` function
# and assigning it to the variable `input`. Then, it is using the `csv.DictReader()` function to read
# the contents of the CSV file and convert them into a dictionary format. The resulting dictionary is
# assigned to the variable `locations`. The `with` statement is used to ensure that the file is
# properly closed after it has been read.
with open(r"inputfile AS1.csv", "r") as input:
    locations = csv.DictReader(input)
    # [\]

    # [?????????????????????]
    # This code is iterating through each row of the `locations` dictionary (which was created by reading
    # the contents of the input CSV file), and for each row, it is creating a new `Point` object with the
    # `x` and `y` values from that row. The `Point` object is then added to the `inputarray` list.
    # Essentially, this code is converting the data from the input CSV file into a list of `Point` objects
    # that can be used for further calculations.
    for pointentry in locations:
        point = Point(pointentry["x"], pointentry["y"])
        inputarray.append(point)
# [\]

# [?????????????????????]
# `calcarray = np.array(inputarray)` is converting the list of `Point` objects stored in `inputarray`
# into a numpy array called `calcarray`. This allows for easier manipulation and calculation of the
# data using numpy functions.
calcarray = np.array(inputarray)
# [\]

# [?????????????????????]
# `numOfRows = calcarray.shape[0]` is calculating the number of rows in the numpy array `calcarray`
# and assigning it to the variable `numOfRows`. This value is used later in the code to determine if
# there are exactly three points in the input file, in which case a circle will be calculated.
numOfRows = calcarray.shape[0]
# [\]

sol = []
eq = []
# [?????????????????????]
# This code block checks if the number of rows in the input CSV file is equal to 3. If it is, then it
# assumes that the input file contains three points and calculates the equation of the circle that
# passes through those three points.
if numOfRows == 3:
    print("Given three points a circle will be calculated")
    for n in range(3):
        # `eq.append(inputarray[n].circeq())` is appending the coefficients of the equation of the
        # circle passing through the three points to the list `eq`. The coefficients are obtained by
        # calling the `circeq()` method of the `Point` object corresponding to the `n`th point in the
        # `inputarray`.
        eq.append(inputarray[n].circeq())
        sol.append(inputarray[n].circsq())
    # `eqarray = np.array(eq)` is converting the list `eq` into a numpy array called `eqarray`. The
    # `eq` list contains the coefficients of the equation of the circle passing through the three
    # points in the input file. Converting the list to a numpy array allows for easier manipulation
    # and calculation of the data using numpy functions.
    eqarray = np.array(eq)
    solarray = np.array(sol)
    # `solution = np.linalg.solve(eqarray, solarray)` is using the `np.linalg.solve()` function from
    # the numpy library to solve a system of linear equations represented by the `eqarray` and
    # `solarray` numpy arrays. The `eqarray` array contains the coefficients of the equations, while
    # the `solarray` array contains the solutions to those equations. The `np.linalg.solve()` function
    # returns an array containing the solutions to the system of linear equations. In this specific
    # code, `solution` contains the coefficients of the equation of the circle passing through the
    # three points in the input file, if there are exactly three points.
    solution = np.linalg.solve(eqarray, solarray)
# [\]

# additional +/- formatting  (You do not need to implement this but it is recommended to do)
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
    pr_sol2 = abs(solution[2])

Equation = ["Equation:", "x^2+y^2{0}x{1}y = {2}".format(pr_sol0, pr_sol1, pr_sol2)]
print(Equation[0], Equation[1])

# [?????????????????????]
# This code is creating a new CSV file named "outputfile AS1.csv" in write mode using the `open()`
# function and assigning it to the variable `f`. Then, it is using the `csv.writer()` function to
# create a writer object called `writer` that can be used to write data to the CSV file. The
# `writer.writerow()` function is used to write the contents of the `Equation` list (which contains
# the equation of the circle calculated earlier) to the CSV file. Finally, the `f.close()` function is
# used to close the CSV file. Essentially, this code is writing the equation of the circle calculated
# earlier to a new CSV file named "outputfile AS1.csv".
f = open("outputfile AS1.csv", "w")

writer = csv.writer(f)
writer.writerow(Equation)

f.close()
# [\]
