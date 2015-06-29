#!/usr/bin/env python3

import tkinter as tk

import widget

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()

        self.automaton = widget.CellWidget(master=self, width = 64, height = 64)
        self.automaton.grid(columnspan = 2)
        self.start = tk.Button(self)
        self.start["text"] = "Run/Pause"
        self.start.grid(column = 0, row = 1)
        self.step = tk.Button(self)
        self.step["text"] = "Step"
        self.step.grid(column = 1, row = 1)


if __name__ == "__main__":
    app = App()
    app.master.title("Generations")
    app.mainloop()
