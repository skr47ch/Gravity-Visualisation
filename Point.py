from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])

LIST = []
for x in range(0, 150):
    LIST.append(Point(500, x*40))
