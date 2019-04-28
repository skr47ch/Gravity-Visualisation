import numpy as np
from math import *

def rotate_matrix_2d(matrix, angle_in_rad):
    """Rotation matrix for the 2d plane
       # TODO -  add param for rotation orientation
              -  add code to rotate along a given point
    """
    rotation_matrix = np.array([[cos(angle_in_rad), sin(angle_in_rad)],
                         [-sin(angle_in_rad), cos(angle_in_rad)]])
    return np.matmul(matrix, rotation_matrix)



