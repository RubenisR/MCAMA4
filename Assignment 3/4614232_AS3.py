import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Define the time and voltage data
t = np.array([0.025, 0.05, 0.075, 0.1, 0.125])  # time(x-axis)
u = np.array([3.43, 0.99, 0.22, 0.10, 0.02])  # Voltage


def expon_func(t, A, B):
    print(A)
    return A * np.exp(B * t)


x, y = opt.curve_fit(expon_func, t, u, p0=(12, 0.05))

# Calculate the best fit for UC(t) using the optimized parameter values
UC = expon_func(t, *x)
# Calculate RC
RC = 1 / abs(x[1])

print("RC =", RC)

# Plot the data and the fitted function
plt.plot(t, u, "ro", label="Data")
plt.plot(t, UC, "b-", label="Fitted function")
plt.xlabel("t")
plt.ylabel("U")
plt.legend()
plt.show()
