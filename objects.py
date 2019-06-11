import tkinter as tk

# Main application
class screen(object):
    def __init__(self, master):
        self.parent = master
        self.canvas = tk.Canvas(master)
        self.canvas.pack(fill = 'both', expand = True)
    

# A tile object i.e. a square on canvas

class tile(object):
    def __init__(self, master, x1, y1, x2, y2):
        self.parent = master
        self.parent.canvas.create_rectangle(x1, y1, x2, y2, fill = 'black', outline = 'grey')
                
