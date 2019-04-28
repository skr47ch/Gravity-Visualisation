import numpy as np
from math import *

def rotate_matrix_2d(matrix, angle_in_degree, clockwise= False):
    """Rotation matrix for the 2d plane
        parameters -
        matrix : a nX2 matrix
        angle_in_degree : self explanatory
        clockwise : rotation orientation. Anticlockwise by default

       # TODO -  add code to rotate along a given point
    """
    if clockwise:
        angle_in_degree = 360 - angle_in_degree
    angle = radians(angle_in_degree)

    rotation_matrix = np.array([[cos(angle), sin(angle)],
                         [-sin(angle), cos(angle)]])

    return np.matmul(matrix, rotation_matrix)


def shear_matrix_2d(matrix, shearx, sheary):
    """Not available yet"""
    pass
