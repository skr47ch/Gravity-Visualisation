import tkinter as tk
import Point
import math

INTERVAL = 25
SIZE = 10
MASS = 5
G = 10
TARGET = Point.Point(Point.GRID_SIZE*Point.GRID_SEPARATION/2, Point.GRID_SIZE*Point.GRID_SEPARATION/2)

class Canvas(tk.Frame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.pack(fill= 'both', expand= True)

        self.left_pane = tk.Frame(self, width=200)
        self.left_pane.pack(anchor='w', fill='y', expand=False, side='left')
        self.create_control_panel(self.left_pane)

        self.right_pane = tk.Canvas(self, bg="pink")
        self.right_pane.pack(anchor='w', fill='both', expand=True, side='left')

        self.canvas = tk.Canvas(self.right_pane)
        self.canvas.configure(background= 'black')
        self.canvas.pack(fill= 'both', expand= True)

        # self.create_coordinates()
        self.draw_canvas()

    def draw_canvas(self):
        self.canvas.delete('all')
        self.create_object()
        self.test_gravity()

    def create_control_panel(self, parent):
        size_slider = tk.Scale(parent, label='Object Size', from_=0, to=100, resolution=1, orient='horizontal', command=self.on_slide_size)
        size_slider.set(SIZE)
        size_slider.pack()
        mass_slider = tk.Scale(parent, label='Object Mass', from_=0, to=5000, resolution=10, orient='horizontal', command=self.on_slide_mass)
        mass_slider.set(MASS)
        mass_slider.pack()
        gravity_slider = tk.Scale(parent, label='Gravitaional Constant', from_=0, to=5000, resolution=10, orient='horizontal', command=self.on_slide_gravitationa_constant)
        gravity_slider.set(G)
        gravity_slider.pack()

    def on_slide_size(self, size):
        """Change object size and refresh object"""
        global SIZE
        SIZE = int(size)
        self.draw_canvas()

    def on_slide_gravitationa_constant(self, g):
        """Change the gravitational constant"""
        global G
        G = int(g)
        self.draw_canvas()

    def on_slide_mass(self, mass):
        """Change object mass and refresh canvas"""
        global MASS
        MASS = int(mass)
        self.draw_canvas()

    def test_gravity(self):
        new_grid = []
        for line in Point.GRID:
            new_sub_grid = []
            for point in line:
                self.create_object(point, size=3, color='blue')
                distance = self.get_distance(TARGET, point)
                distance = distance if distance != 0 else 1
                delta = G*MASS/distance*2

                if point.x <= TARGET.x and point.y <= TARGET.y:
                    point = Point.Point(TARGET.x if point.x + delta > TARGET.x else point.x + delta,
                                            TARGET.y if point.y + delta > TARGET.y else point.y + delta)
                elif point.x <= TARGET.x and point.y > TARGET.y:
                    point = Point.Point(TARGET.x if point.x + delta > TARGET.x else point.x + delta,
                                            TARGET.y if point.y - delta < TARGET.y else point.y - delta)
                elif point.x > TARGET.x and point.y <= TARGET.y:
                    point = Point.Point(TARGET.x if point.x - delta < TARGET.x else point.x - delta,
                                            TARGET.y if point.y + delta > TARGET.y else point.y + delta)
                else:
                    point = Point.Point(TARGET.x if point.x - delta < TARGET.x else point.x - delta,
                                            TARGET.y if point.y - delta < TARGET.y else point.y - delta)

                new_sub_grid.append(point)
            new_grid.append(new_sub_grid)

        for grid in new_grid:
            flatenned = [(x, y) for x, y in grid]
            self.canvas.create_line(flatenned, smooth=True, width=1, fill='orange')


    @staticmethod
    def get_distance(a, b):
        return math.sqrt((a.x  - b.x)**2 + (a.y - b.y) ** 2)

    def create_object(self, point= None, color= None, size= None):
        """Creates a Point on our canvas"""
        if point is None:
            point = TARGET
        if color is None:
            color = 'white'
        if size is None:
            size = SIZE

        object_ = self.canvas.create_oval(point.x - size/2, point.y - size/2, (point.x + size/2), (point.y + size/2), fill= color)
        if point is None:
            self.canvas.tag_raise(object_)
        else:
            self.canvas.tag_lower(object_)

    def create_coordinates(self):
        # get current window size
        self.update_idletasks()
        screen_width = self.winfo_width()
        screen_height = self.winfo_height()

        for y in range(int(screen_height / INTERVAL)):
            for x in range(int(screen_width / INTERVAL)):
                self.create_object(Point.Point(x * INTERVAL, y * INTERVAL))

def main():
    root = tk.Tk()
    root.title('Gravity Visualisation')
    root.minsize(900, 800)
    root.update_idletasks()
    Canvas()
    root.mainloop()

if __name__ == '__main__':
    main()
