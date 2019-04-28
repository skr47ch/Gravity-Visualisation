from matrix_transformations import *
from plot_functions import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

plt.grid()
plt.axis([0, 10, 0, 10])

x = 20

A = np.array([[2, 2],
              [4, 4]])
B = np.arange(10).reshape(5, 2)
C = rotate_matrix_2d(matrix=A, angle_in_degree=x, clockwise=False)

plot_multiple(A, C, B)

plt.show()