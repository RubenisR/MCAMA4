import csv
import numpy as np


def fetchcsv(filename):
    # using the NumPy library to read a CSV file and convert it into a NumPy array of integers.
    r = np.genfromtxt(filename, delimiter=",", dtype=int, names=True)

    #
    # This code is reading a CSV file and converting it into a numpy array of strings.
    reader = csv.reader(open(filename, "r"), delimiter=",")
    x = list(reader)
    result = np.array(x).astype("str")

    Labels = []
    # Delete the first element of the array which is the labels
    for i in range(len(result[0])):
        Labels.append(result[0][i])
    del Labels[0]

    dictionary = {}

    keys = []
    values = []

    # retrieves the corresponding values from the Labels list and appends them to the keys list.

    for i in range(len(r[0]) - 1):
        keys.append(Labels[i])

    temp_dic = {}

    sub_keys = []

    sub_values = []

    # Iterate over the rows of the matrix
    for j in range(len(r[0]) - 1):
        # Iterate over the rows of the matrix
        for i in range(len(r[0]) - 1):
            # Check if the value at position (j, i+1) is not equal to -1
            if r[j][i + 1] != -1:
                # Append the label associated with the column index to sub_keys
                sub_keys.append(Labels[i])
                # Append the value at position (j, i+1) to sub_values
                sub_values.append(r[j][i + 1])
        # Create a dictionary from sub_keys and sub_values using zip() and assign it to the temp_dic variable
        for key, value in zip(sub_keys, sub_values):
            temp_dic[key] = value
        # Append the temp_dic dictionary to the values list
        values.append(temp_dic)

        sub_values = []
        sub_keys = []
        temp_dic = {}

    # For each iteration, it assigns the value of the
    # `value` variable to the key of the `key` variable in the `dictionary`. Finally, it returns the
    # `dictionary`.
    for key, value in zip(keys, values):
        dictionary[key] = value

    return dictionary


points = fetchcsv("points.csv")
# connection = fetchcsv("Connection_matrix.csv")
print(points)
# print(connection)
