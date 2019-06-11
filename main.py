import tkinter as tk
from objects import screen, tile

# toplevel widget 'root'
root = tk.Tk()
root.attributes("-fullscreen", True)

# canvas inside 'root'
screen = screen(root)

# obtain boundaries of the monitor screen
scrnwdth = root.winfo_screenwidth()
scrnhght = root.winfo_screenheight()

# grid of empty tiles filling the screen but no more
tilesize = 15
for y in range(0, scrnhght, tilesize):
    for x in range(0, scrnwdth, tilesize):
        tile1 = tile(screen, x, y, (x + tilesize), (y + tilesize))
        screen.parent.update()

# Event Mainloop
root.mainloop()
