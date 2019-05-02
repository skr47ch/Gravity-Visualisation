# from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.interpolate import interp1d
import scipy as sp

# TODO - Interpolation

MASS_ = .7
plt.axis([-10, 10, 0, 10])
object_ = [0, 4]
points = []



for i in range(-10, 10):
    points.append([[x, y] for x in range(i, i+1) for y in range(0, 11)])

points = np.array(points, dtype='f')

for i in range(len(points)):
    plt.plot(points[i, :, 0], points[i, :, 1], color='pink')


for index_, value_ in enumerate(points):
    for index, value in enumerate(points[index_]):
        try:
            d = MASS_ * 1 / sqrt((object_[0] - value[0]) ** 2 + (object_[1] - value[1]) ** 2)
        except ZeroDivisionError:
            d = 0
            # print('Divide by zero? ダメだ!!')
        if object_[0] < value[0]:
            points[index_, index] = value[0]-d**2, value[1]
        elif object_[0] > value[0]:
            points[index_, index] = value[0]+d**2, value[1]

for i in range(len(points)):
    plt.plot(points[i, :, 0], points[i, :, 1], color='green')

plt.plot(object_[0], object_[1], 'o')

plt.show()