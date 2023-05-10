import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

t = np.array([0.025, 0.05, 0.075, 0.1, 0.125])  # time(x-axis)
u = np.array([8.57, 11.01, 11.78, 11.90, 11.98])  # Voltage(y-axis)


def decay_linear_func(t, A, B, C, D):
    print(A, B)
    return A * np.exp(-t / B) + C * t + D


x, y = opt.curve_fit(decay_linear_func, t, u, p0=(12, 0.05, 0, 0))

# Calculate the best fit for UC(t)
UC = decay_linear_func(t, *x)

# Plot the data and the fitted function
plt.plot(t, u, "ro", label="Data")
plt.plot(t, UC, "b-", label="Fitted function")
plt.xlabel("t")
plt.ylabel("U")
plt.legend()
plt.show()
