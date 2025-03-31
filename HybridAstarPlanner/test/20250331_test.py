import numpy as np
import matplotlib.pyplot as plt

car = np.array([[-1.0, -1.0, 4.5, 4.5, -1.0],
                [1.5, -1.5, -1.5, 1.5, 1.5]])
wheel = np.array([[-0.5, -0.5, 0.5, 0.5, -0.5],
                [0.25, -0.25, -0.25, 0.25, 0.25]])
rlWheel = wheel.copy()
rrWheel = wheel.copy()
frWheel = wheel.copy()
flWheel = wheel.copy()

frWheel += np.array([[3.5], [-1.05]])
flWheel += np.array([[3.5], [1.05]])
rrWheel[1, :] -= 1.05
rlWheel[1, :] += 1.05

plt.plot(car[0, :], car[1, :], 'dimgray')
plt.plot(frWheel[0, :], frWheel[1, :], 'dimgray')
plt.plot(rrWheel[0, :], rrWheel[1, :], 'dimgray')
plt.plot(flWheel[0, :], flWheel[1, :], 'dimgray')
plt.plot(rlWheel[0, :], rlWheel[1, :], 'dimgray')
plt.show()