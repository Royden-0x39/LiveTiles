import tkinter as tk

# Main application
class AppConstruct(object):
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master)
        self.canvas.pack(fill = 'both', expand = True)
    

# A tile object i.e. a square on canvas
class Tile(object):
    def __init__(self, canvas, x1, y1, x2, y2):
        self.master = canvas
        self.coords = (x1, y1, x2, y2)
        self.fill = 'black'

    def create(self):
        ID = self.master.create_rectangle(self.coords, fill = self.fill, outline = 'grey')
        self.master.tag_bind(ID, '<Button-1>', self.change_state)

    def change_state(self, event):
        if self.fill == 'black':
            self.fill = 'white'
        elif self.fill == 'white':
            self.fill = 'black'
        self.create()

#    def step(self, event):
