from collections import namedtuple
import tkinter as tk

Point = namedtuple('point', ['x', 'y'])

class Example(tk.Frame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.pack(fill= 'both', expand= True)

        self.canvas = tk.Canvas(self)
        self.canvas.configure(background= 'black')
        self.canvas.pack(fill= 'both', expand= True)

        for x, y in zip(range(0,50), range(0, 50)):
            self.create_point(Point(x*10, 10))


    def create_point(self, point, color= None):
        """Creates a Point on our canvas"""
        if color is None:
            color = 'orange'
        self.canvas.create_line(point.x, point.y, (point.x + 1), point.y, fill= color)



def main():
    root = tk.Tk()
    root.title('Some Graphics Inc.')
    root.minsize(300, 200)
    example = Example()
    root.mainloop()

if __name__ == '__main__':
    main()
