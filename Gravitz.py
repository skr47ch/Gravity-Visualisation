import tkinter as tk
from collections import namedtuple
import math
import numpy as np

INTERVAL = 25
SIZE = 10
SIZE_MAX = 20
MASS = 5
MASS_MAX = 500
G = 5
G_MAX = 500

GRID_SIZE = 24
GRID_SEPARATION = 35

Point = namedtuple('point', ['x', 'y'])

GRID = []
GRID_SUB = []
HORIONTAL_GRID = []
VERTICAL_GRID = []

# Grid 1 = All point in 2D space
for y in range(0, GRID_SIZE):
    GRID_SUB = []
    for x in range(0, GRID_SIZE):
        GRID_SUB.append(Point(x*GRID_SEPARATION, y*GRID_SEPARATION))
    GRID.append(GRID_SUB)
    HORIONTAL_GRID.append(GRID_SUB)

for y in range(0, GRID_SIZE):
    GRID_SUB = []
    for x in range(0, GRID_SIZE):
        GRID_SUB.append(Point(y*GRID_SEPARATION, x*GRID_SEPARATION))
    GRID.append(GRID_SUB)
    VERTICAL_GRID.append(GRID_SUB)

class MassiveObject:
    def __init__(self, x, y, mass, color, size):
        self.coordinates = Point(x, y)
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color
        self.size = size

class AppWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        self.object_list = []
        self.object_1 = MassiveObject(x=100, y=100, mass=5, color='white', size=5)
        self.object_2 = MassiveObject(x=200, y=250, mass=5, color='yellow', size=8)
        self.object_3 = MassiveObject(x=500, y=500, mass=5, color='blue', size=5)
        self.object_4 = MassiveObject(x=700, y=400, mass=5, color='magenta', size=5)
        self.object_list.append(self.object_1)
        self.object_list.append(self.object_2)
        self.object_list.append(self.object_3)
        self.object_list.append(self.object_4)
        self.gui()
    def gui(self):
        self.pack(fill= 'both', expand= True)
        self.left_pane = tk.Frame(self, width=200)
        self.left_pane.pack(anchor='w', fill='y', expand=False, side='left')
        size_slider = tk.Scale(self.left_pane, label='Object Size', from_=0, to=SIZE_MAX, resolution=1, orient='horizontal', command=self.on_slide_size)
        size_slider.set(SIZE)
        size_slider.pack()
        mass_slider = tk.Scale(self.left_pane, label='Object Mass', from_=0, to=MASS_MAX, resolution=1, orient='horizontal', command=self.on_slide_mass)
        mass_slider.set(MASS)
        mass_slider.pack()
        gravity_slider = tk.Scale(self.left_pane, label='Gravitaional Constant', from_=0, to=G_MAX, resolution=1, orient='horizontal', command=self.on_slide_gravitationa_constant)
        gravity_slider.set(G)
        gravity_slider.pack()

        self.right_pane = tk.Canvas(self, bg="pink")
        self.right_pane.pack(anchor='w', fill='both', expand=True, side='left')

        self.canvas = tk.Canvas(self.right_pane)
        self.canvas.configure(background= 'black')
        self.canvas.pack(fill= 'both', expand= True)

    def on_slide_size(self, size):
        """Change object size and refresh canvas"""
        for object_ in self.object_list:
            object_.size = int(size)
        self.refresh_canvas()

    def on_slide_gravitationa_constant(self, g):
        """Change the gravitational constant and refresh canvas"""
        global G
        G = int(g)
        self.refresh_canvas()

    def on_slide_mass(self, mass):
        """Change object mass and refresh canvas"""
        global MASS
        MASS = int(mass)
        self.refresh_canvas()

    def refresh_canvas(self):
        self.canvas.delete('all')
        self.calculate_stuff()

    def calculate_stuff(self):

        GRID_LOCAL = VERTICAL_GRID.copy()

        for object_ in self.object_list:
            self.draw_object(object_)

        for object_ in self.object_list:
            for index_1, line_ in enumerate(GRID_LOCAL):
                for index_2, point_ in enumerate(line_):
                    # print(object_.coordinates, point_, self.get_distance(object_, point_), GRID[index_1][index_2])
                    distance = self.get_distance(object_, point_)
                    distance = distance if distance != 0 else 1

                    delta = G*MASS/distance*2

                    if point_.x <= object_.x and point_.y <= object_.y:
                        GRID_LOCAL[index_1][index_2] = Point(object_.x if point_.x + delta > object_.x else point_.x + delta,
                                                object_.y if point_.y + delta > object_.y else point_.y + delta)
                    elif point_.x <= object_.x and point_.y > object_.y:
                        GRID_LOCAL[index_1][index_2] = Point(object_.x if point_.x + delta > object_.x else point_.x + delta,
                                            object_.y if point_.y - delta < object_.y else point_.y - delta)
                    elif point_.x > object_.x and point_.y <= object_.y:
                        GRID_LOCAL[index_1][index_2] = Point(object_.x if point_.x - delta < object_.x else point_.x - delta,
                                            object_.y if point_.y + delta > object_.y else point_.y + delta)
                    else:
                        GRID_LOCAL[index_1][index_2] = Point(object_.x if point_.x - delta < object_.x else point_.x - delta,
                                            object_.y if point_.y - delta < object_.y else point_.y - delta)

        self.draw_line(GRID_LOCAL)

    def draw_object(self, object_):
        """Creates a Point on our canvas"""
        x_, y_ = object_.x, object_.y
        size = object_.size
        color = object_.color
        obj = self.canvas.create_oval(x_-size/2, y_-size/2, x_+size/2, y_+size/2, fill= color)
        self.canvas.tag_raise(obj)

    def draw_line(self, grid):
        for line_ in grid:
            flattened = [(x, y) for x, y in line_]
            line_bg = self.canvas.create_line(flattened, fill='#145A32', smooth=1, width=2.4)
            line = self.canvas.create_line(flattened, fill='#0B5345', smooth=1, width=2.1)
            self.canvas.tag_lower(line)
            self.canvas.tag_lower(line_bg)

    @staticmethod
    def get_distance(a, b):
        return math.sqrt((a.x  - b.x)**2 + (a.y - b.y) ** 2)


root = tk.Tk()
root.title('Gravity Visualisation')
root.minsize(900, 800)
root.update_idletasks()
AppWindow()
root.mainloop()