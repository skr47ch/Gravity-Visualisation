from matrix_transformations import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

plt.grid()
plt.axis([-10, 10, -10, 10])

x = radians(20)

A = np.array([[2, 2],
              [3, 4]])

C = rotate_matrix_2d(matrix=A, angle_in_rad=x)

plt.plot(A[:,0], A[:,1])
plt.plot(C[:,0], C[:,1])

plt.show()