import numpy as np
import matplotlib.pyplot as plt

t = np.array([0.025, 0.05, 0.075, 0.1, 0.125])  # time
u = np.array([8.57, 11.01, 11.78, 11.90, 11.98])  # Voltage

A = np.vstack(
    [t, np.ones(len(t))]
).T  # create a matrix with the time values and a column of ones
T, U = np.linalg.lstsq(A, u, rcond=None)[0]  # perform least squares fitting
# plot the data and the fitted line
plt.plot(t, u, "o", label="Original data", markersize=10)
plt.plot(t, T * t + U, "r", label="Fitted line")
# print the linear function above the graph
plt.text(0.05, 13, "U = {0}t + {1}".format(T, U))
plt.legend()
plt.show()
