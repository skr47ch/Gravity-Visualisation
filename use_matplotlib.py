# from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import matplotlib.pyplot as plt
from math import *

# TODO - Interpolation

plt.axis([-10, 10, 0, 10])
mass = [0, 4]
points = []



for i in range(-10, 10):
    points.append([[x, y] for x in range(i, i+1) for y in range(0, 11)])

points = np.array(points, dtype='f')

for i in range(len(points)):
    plt.plot(points[i, :, 0], points[i, :, 1], color='pink')


for index_, value_ in enumerate(points):
    for index, value in enumerate(points[index_]):
        try:
            d = 1/sqrt((mass[0] - value[0]) ** 2 + (mass[1] - value[1]) ** 2)
        except ZeroDivisionError:
            d = 0
            # print('Divide by zero? ダメだ!!')
        if mass[0] < value[0]:
            points[index_, index] = value[0]-d**2, value[1]
        elif mass[0] > value[0]:
            points[index_, index] = value[0]+d**2, value[1]

for i in range(len(points)):
    plt.plot(points[i, :, 0], points[i, :, 1], color='green')

plt.plot(mass[0], mass[1], 'o')
plt.show()