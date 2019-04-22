from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])
GRID_SIZE = 20
GRID_SEPARATION = 50

GRID = []
for y in range(1, GRID_SIZE):
    for x in range(1, GRID_SIZE):
        GRID.append(Point(x*GRID_SEPARATION, y*GRID_SEPARATION))

