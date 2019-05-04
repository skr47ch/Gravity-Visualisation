import tkinter as tk
from collections import namedtuple

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

# Grid 1 = All point in 2D space
for y in range(0, GRID_SIZE):
    GRID_SUB = []
    for x in range(0, GRID_SIZE):
        GRID_SUB.append(Point(x*GRID_SEPARATION, y*GRID_SEPARATION))
    GRID.append(GRID_SUB)

for y in range(0, GRID_SIZE):
    GRID_SUB = []
    for x in range(0, GRID_SIZE):
        GRID_SUB.append(Point(y*GRID_SEPARATION, x*GRID_SEPARATION))
    GRID.append(GRID_SUB)

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
        global SIZE
        SIZE = int(size)
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
        self.object_1 = MassiveObject(100, 100, 5, 'white', 5)
        self.object_2 = MassiveObject(x=200, y=250, mass=5, color='yellow', size=8)
        self.draw_object(self.object_1)
        self.draw_object_(self.object_2)

    def draw_object_(self, object_):
        """Creates a Point on our canvas"""
        x_, y_ = object_.x, object_.y
        size = object_.size
        color = object_.color
        self.canvas.create_oval(x_-size/2, y_-size/2, x_+size/2, y_+size/2, fill= color)

    def draw_object(self, point= None, color= None, size= None):
        """Creates a Point on our canvas"""
        if point is None:
            point = Point(GRID_SIZE * GRID_SEPARATION / 2, GRID_SIZE * GRID_SEPARATION / 2)
        if color is None:
            color = 'white'
        if size is None:
            size = SIZE

        self.canvas.create_oval(point.x - size/2, point.y - size/2, (point.x + size/2), (point.y + size/2), fill= color)


root = tk.Tk()
root.title('Gravity Visualisation')
root.minsize(900, 800)
root.update_idletasks()
AppWindow()
root.mainloop()