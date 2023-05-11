import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

t = np.array([0.025, 0.05, 0.075, 0.1, 0.125])  # time
u = np.array([3.43, 0.99, 0.22, 0.10, 0.02])  # Voltage


def expon_func(t, A, B):
    return A * np.exp(-t / B)


x, y = opt.curve_fit(expon_func, t, u, p0=(12, 0.05))

UC = expon_func(t, *x)

plt.plot(t, u, "ro", label="Data")
plt.plot(t, UC, "b-", label="Fitted function")
plt.xlabel("t")
plt.ylabel("U")
plt.legend()
plt.show()
