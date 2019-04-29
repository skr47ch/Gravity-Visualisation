# from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import matplotlib.pyplot as plt
from math import *

# TODO - Interpolation
plt.axis([-10, 10, -10, 10])
points = np.array([[5, 3],
          [5, 2],
          [5, 1],
          [5, 0],
          [5, -1],
          [5, -2],
          [5, -3]], dtype='f')

origin = [0, 0]

plt.plot(points[:, 0], points[:, 1])

for index, value in enumerate(points):
    d = 5 * 1/sqrt(value[0]**2 + value[1]**2)
    points[index] = [value[0]-d**2, value[1]]
    print(d, points[index])

plt.plot(points[:, 0], points[:, 1])
plt.show()