import tkinter as tk
import generations

def mouse_press(event):
    widget = event.widget
    x = widget.canvasx(event.x)
    y = widget.canvasy(event.y)
    x = int(x // widget.scale);
    y = int(y // widget.scale);
    widget.automaton.buf[y][x] = 3;
    widget.redraw()
    pass

class CellWidget(tk.Canvas):
    def __init__(self, master, width, height, scale = 16):
        super().__init__(master, width=width*scale, height=height*scale)
        self.scale = scale
        self.palette = ['#000', '#300', '#900', '#f00']
        self.bind("<Button-1>", mouse_press)
        self.automaton = generations.Automaton(width, height)
        self.redraw()

    def redraw(self):
        buffer = self.automaton.buf;
        scale = self.scale;
        self.delete('all')
        for (y, row) in enumerate(buffer):
            for (x, cell) in enumerate(row):
                scaled_x = x*scale
                scaled_y = y*scale
                colour = self.palette[cell]
                self.create_rectangle(
                    scaled_x, scaled_y,
                    scaled_x + scale, scaled_y + scale,
                    fill = colour)

