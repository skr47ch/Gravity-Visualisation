# from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import matplotlib.pyplot as plt
from math import *

# TODO - Interpolation
plt.axis([-10, 10, -10, 10])
origin = [0, 0]
# points = np.array([[x, y] for x in range(1, 6) for y in range(-20, 20, 1)], dtype='f')

A = []
for i in range(5):
    A.append([[x, y] for x in range(i, i+1) for y in range(-9, 9)])

points = np.array(A)

for i in range(len(points)):
    plt.plot(points[i, :, 0], points[i, :, 1])

# for i in range(len(points)):
#     for index, value in enumerate(points[i]):
#         d = 1/sqrt(value[i, 0]**2 + value[i, 1]**2)
#         points[i, index] = [value[i, 0]-d**2, value[i, 1]]
#         print(d, points[i, index])

for i in range(len(points)):
    plt.plot(points[i, :, 0], points[i, :, 1])

plt.show()