from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])

LIST1, LIST2, LIST3, LIST4, LIST5, LIST6, LIST7 = [], [], [], [], [], [], []
for x in range(1, 50):
    LIST1.append(Point(500, x * 20))
    LIST2.append(Point(550, x * 20))
    LIST3.append(Point(600, x * 20))
    LIST4.append(Point(650, x * 20))
    LIST5.append(Point(700, x * 20))
    LIST6.append(Point(750, x * 20))
    LIST7.append(Point(100, x * 20))

LIST_ARRAY = [LIST1, LIST2, LIST3, LIST4, LIST5, LIST6, LIST7]
