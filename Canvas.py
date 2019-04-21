import tkinter as tk
import Point
import math

INTERVAL = 25
MASS = 3
TARGET = Point.Point(200, 200)

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
        num = 1
        for item in Point.LIST:
            self.create_point(item, size=5)
            distance = self.get_distance(TARGET, item)
            self.canvas.create_text(item.x + 50, item.y, text=f"d = {distance:.2f}" , font=("Purisa", 10), fill='white')

            delta = MASS*distance/2**num
            newx = item.x - delta
            newy = item.y + delta
            # self.create_point(Point.Point(newx, newy), 'red')
            num += 1

    @staticmethod
    def get_distance(a, b):
        return math.sqrt(abs(a.x ** 2 - b.x ** 2) + abs(a.y ** 2 - b.y ** 2))

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
    root.minsize(900, 500)
    root.update_idletasks()
    example = Canvas()
    root.mainloop()

if __name__ == '__main__':
    main()
