import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

t = np.array([0.025, 0.05, 0.075, 0.1, 0.125])  # time(x-axis)
u = np.array([8.57, 11.01, 11.78, 11.90, 11.98])  # Voltage(y-axis)

# x = np.vstack(  # create a matrix with the time values and a column of ones
#    [t, np.ones(len(t))]
# ).T
# A, B = np.linalg.lstsq(x, u, rcond=None)[0]  # perform least squares fitting
## plot the data and the fitted line
# plt.plot(t, u, "o", label="Original data", markersize=10)
# plt.plot(t, A * t + B, "r", label="Fitted line")
## print the linear function above the graph
# plt.text(0.05, 13, "U = {0}t + {1}".format(A, B))
# plt.legend()
# plt.show()

# calculate the sum of t*u, sum of t, sum of u, sum of t^2, and i
# sumtu = np.sum(t * u)
# sumt = np.sum(t)
# sumu = np.sum(u)
# sumt2 = np.sum(t**2)
# i = len(t)
#
# B = (i * sumtu - sumt * sumu) / (i * sumt2 - sumt * sumu)  # calculate B constant
# A1 = (1 / i) * (sumu - B * sumt)  # calculate A constant
# A = np.exp(A1)  # calculate A constant
## plot the data and the fitted line
# plt.plot(t, u, "o", label="Original data", markersize=10)
## plot the exponential function U=e^A*e^Bt
# plt.plot(t, A * np.exp(B * t), "r", label="Fitted line")
## print the exponential function above the graph
# plt.text(0.05, 13, "U = {0}*e^{1}t".format(A, B))
# plt.legend()
# plt.show()

# A, B = np.polyfit(t, np.log(u), 1, w=np.sqrt(u))
### plot the data and the fitted line
# plt.plot(t, u, "o", label="Original data", markersize=10)
### plot the exponential function U=e^A*e^Bt
# plt.plot(t, np.exp(A) * np.exp(B * t), "r", label="Fitted line")
### print the exponential function above the graph
# plt.text(0.05, 13, "U = {0}*e^{1}t".format(A, B))
# plt.legend()
# plt.show()
x, y = opt.curve_fit(lambda t, A, B: A * np.exp(B * t), t, u, p0=(4, 0.1))
A, B = x
### plot the data and the fitted line
plt.plot(t, u, "o", label="Original data", markersize=10)
### plot the exponential function U=e^A*e^Bt
plt.plot(t, A * np.exp(B * t), "r", label="Fitted line")
### print the exponential function above the graph
plt.text(0.05, 13, "U = {0}*e^{1}t".format(A, B))
plt.legend()
plt.show()
