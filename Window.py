import tkinter as tk

# toplevel widget 'root'
root = tk.Tk()
root.attributes("-fullscreen", True)

# canvas inside 'root'
screen = tk.Canvas(root, height = 500, width = 500, bg = 'white')

# obtain boundaries of the monitor screen
scrnwdth = root.winfo_screenwidth()
scrnhght = root.winfo_screenheight()

# grid of empty tiles filling the screen but no more
tilesize = 20
for y in range(0, scrnhght, tilesize):
    for x in range(0, scrnwdth, tilesize):
        tile = screen.create_rectangle(x, y, (x + tilesize), (y + tilesize), fill = 'black', outline = 'grey' )

screen.pack(fill = 'both', expand = 1)

# Event Mainloop
screen.mainloop()

