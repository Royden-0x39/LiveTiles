import tkinter as tk
from objects import AppConstruct, Tile

def step(event):
    for y in range(0, Sh, Ts):
        for x in range(0, Sw, Ts):
            tile['{}_{}'.format(x, y)].change_state(event)

# toplevel widget 'root'
root = tk.Tk()
root.attributes("-fullscreen", True)

# sublevel widgets defined in class 'AppConstruct'
mainwin = AppConstruct(root)
canvas = mainwin.canvas

# obtain boundaries of the monitor screen
Sw = root.winfo_screenwidth()
Sh = root.winfo_screenheight()

# grid of empty tiles filling the screen but no more
Ts = 15
tile = {}

for y in range(0, Sh, Ts):
    for x in range(0, Sw, Ts):
        newtile = '{}_{}'.format(x, y)
        tile[newtile] = Tile(canvas, x, y, (x + Ts), (y + Ts))
        tile[newtile].create()

root.bind('<Shift-Return>', step)

# Event Mainloop
root.mainloop()
