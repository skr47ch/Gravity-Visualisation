from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])
GRID_SIZE = 20
GRID_SEPARATION = 40

GRID = []
GRID_SUB = []

# Grid 1 = All point in 2D space
for y in range(1, GRID_SIZE):
    GRID_SUB = []
    for x in range(1, GRID_SIZE):
        GRID_SUB.append(Point(x*GRID_SEPARATION, y*GRID_SEPARATION))
    GRID.append(GRID_SUB)

for y in range(1, GRID_SIZE):
    GRID_SUB = []
    for x in range(1, GRID_SIZE):
        GRID_SUB.append(Point(y*GRID_SEPARATION, x*GRID_SEPARATION))
    GRID.append(GRID_SUB)

print(GRID)




# Grid 2 = Vertical points
# for y in range(1, GRID_SIZE):
#     for x in  [100, 200, 300, 400, 500, 600]:
#         GRID.append(Point(x, y*GRID_SEPARATION))

# Grid 3 = Horizontal points
# for x in range(1, GRID_SIZE):
#     for y in  [100, 200, 300, 400, 500, 600]:
#         GRID.append(Point(x*GRID_SEPARATION, y))