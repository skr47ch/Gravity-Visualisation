from collections import namedtuple, deque
import tkinter as tk

Point = namedtuple('Point', ['x', 'y', 'z'])

A = Point(100, 100, 0)
B = Point(200, 100, 0)
C = Point(200, 200, 0)
D = Point(100, 200, 0)

EDGES = [A, B, C, D]

def prev_and_next(input_list):
    CURRENT = input_list
    PREV = deque(input_list)
    PREV.rotate(-1)
    PREV = list(PREV)
    NEXT = deque(input_list)
    NEXT.rotate(1)
    NEXT = list(NEXT)
    return zip(PREV, CURRENT, NEXT)

class Canvas(tk.Frame):
    def __init__(self):
        super().__init__()

        self.pack(fill= 'both', expand= True)
        self.canvas = tk.Canvas(self, bg="pink")
        self.canvas.pack(anchor='w', fill='both', expand=True, side='left')
        self.draw_cube()

    def draw_cube(self):
        for previous_, current_, next_ in prev_and_next(EDGES):
            self.canvas.create_line(current_.x, current_.y, next_.x, next_.y)


root = tk.Tk()
root.title('Gravity Visualisation')
root.minsize(900, 800)
root.update_idletasks()
Canvas()
root.mainloop()