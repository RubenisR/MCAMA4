import csv
import numpy as np


def fetchcsv(filename_points, filename_connections):
    # Read points matrix
    with open(filename_points, "r") as file:
        reader = csv.reader(file)
        r_points = np.array([row for row in reader])

    labels_points = list(map(str, r_points[0][1:]))
    dictionary_points = {}

    # Convert points matrix into a dictionary
    for i in range(1, len(r_points)):
        point = r_points[i][0]
        values = list(map(float, r_points[i][1:]))
        dictionary_points[point] = {
            label: value for label, value in zip(labels_points, values)
        }

    # Read connection matrix
    with open(filename_connections, "r") as file:
        reader = csv.reader(file)
        r_connections = np.array([row for row in reader])

    labels_connections = list(map(str, r_connections[0][1:]))
    dictionary_connections = {}

    # Convert connection matrix into a dictionary
    for i in range(1, len(r_connections)):
        point = r_connections[i][0]
        values = []
        for value in r_connections[i][1:]:
            if value == "-":
                values.append(0)
            else:
                values.append(float(value))
        dictionary_connections[point] = {
            label: value for label, value in zip(labels_connections, values)
        }

    # Calculate location matrix based on formula
    location_matrix = {}
    for point, connections in dictionary_connections.items():
        if point in dictionary_points:
            x1 = dictionary_points[point].get(
                "x", 0
            )  # Get x coordinate, default to 0 if not found
            y1 = dictionary_points[point].get(
                "y", 0
            )  # Get y coordinate, default to 0 if not found
            locations = {}
            for connected_point, connection_strength in connections.items():
                if connected_point in dictionary_points:
                    x2 = dictionary_points[connected_point].get(
                        "x", 0
                    )  # Get x coordinate, default to 0 if not found
                    y2 = dictionary_points[connected_point].get(
                        "y", 0
                    )  # Get y coordinate, default to 0 if not found
                    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                    locations[connected_point] = distance
            location_matrix[point] = locations

    return dictionary_points, dictionary_connections, location_matrix


points_file = "points.csv"
connections_file = "connection_matrix.csv"

points, connections, location = fetchcsv(points_file, connections_file)

print("Points Matrix:")
for point, attributes in points.items():
    print(f"{point}: {attributes}")

print("\nConnection Matrix:")
for point, connections in connections.items():
    print(f"{point}: {connections}")

print("\nLocation Matrix:")
for point, locations in location.items():
    print(f"{point}: {locations}")
