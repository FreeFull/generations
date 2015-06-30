import tkinter as tk
import generations

def left_press(event):
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
        self.bind("<Button-1>", left_press)
        self.automaton = generations.Automaton(width, height)
        self.image = tk.PhotoImage(width = width, height = height)
        self.redraw()

    def redraw(self):
        self.delete('all')
        buffer = self.automaton.buf;
        for (y, row) in enumerate(buffer):
            for (x, cell) in enumerate(row):
                self.image.put(self.palette[cell], (x,y))
        self.image_zoomed = self.image.zoom(self.scale);
        self.create_image(0, 0, image = self.image_zoomed, anchor = 'nw')
