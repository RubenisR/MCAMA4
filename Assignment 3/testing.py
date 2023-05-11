import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Define the time and voltage data
t = np.array([0.025, 0.05, 0.075, 0.1, 0.125])  # time(x-axis)
u = np.array([8.57, 11.01, 11.78, 11.90, 11.98])  # Voltage(y-axis)


# Define the model function to fit the data
def decay_linear_func(t, A, B, C, D):
    # Optional: Print the parameter values for debugging
    # print(A, B)
    return A * np.exp(-t / B) + C * t + D


# Fit the model function to the data using curve_fit
x, y = opt.curve_fit(decay_linear_func, t, u, p0=(12, 0.05, 0, 0))

# Calculate the best fit for UC(t) using the optimized parameter values
UC = decay_linear_func(t, *x)

# Extract the RC value from the optimized parameter values
RC = x[1]

# Plot the data and the fitted function
plt.plot(t, u, "ro", label="Data")
plt.plot(t, UC, "b-", label="Fitted function")
plt.xlabel("t")
plt.ylabel("U")
plt.legend()
plt.show()

# Print the calculated value of RC
print("RC = ", RC)
