import tkinter as tk
import Point
import math

INTERVAL = 25
MASS = 5
TARGET = Point.Point(400, 400)

class Canvas(tk.Frame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.pack(fill= 'both', expand= True)
        self.canvas = tk.Canvas(self)
        self.canvas.configure(background= 'black')
        self.canvas.pack(fill= 'both', expand= True)

        # self.create_coordinates()
        self.test_gravity()
        self.create_point(TARGET, 'white', size=MASS*2)

    def test_gravity(self):
        for item in Point.LIST_ARRAY:
            for point in item:
                num = 1
                self.create_point(point, size=4)
                distance = self.get_distance(TARGET, point)
                delta = distance - distance * 0.25
                # self.canvas.create_text(item.x + 60, item.y, text=f"d = {distance:.2f}, n={num}" , font=("Purisa", 10), fill='white')
                new_point = Point.Point(point.x + delta, point.y)
                self.create_point(new_point, 'blue', 4)
                num += 1


    @staticmethod
    def get_distance(a, b):
        return math.sqrt((a.x  - b.x)**2 + (a.y - b.y) ** 2)

    def create_point(self, point, color= None, size= None):
        """Creates a Point on our canvas"""
        if color is None:
            color = 'orange'
        if size is None:
            size = 2

        self.canvas.create_oval(point.x, point.y, (point.x + size), (point.y + size), fill= color)

    def create_coordinates(self):
        # get current window size
        self.update_idletasks()
        screen_width = self.winfo_width()
        screen_height = self.winfo_height()

        for y in range(int(screen_height / INTERVAL)):
            for x in range(int(screen_width / INTERVAL)):
                self.create_point(Point.Point(x * INTERVAL, y * INTERVAL))

def main():
    root = tk.Tk()
    root.title('Gravity Visualisation')
    root.minsize(900, 800)
    root.update_idletasks()
    example = Canvas()
    root.mainloop()

if __name__ == '__main__':
    main()
