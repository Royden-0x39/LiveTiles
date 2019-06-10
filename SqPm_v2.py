import tkinter as tk
import math as m

print("\nUse [ctrl+C] to stop program execution,\n or [alt+F4] to exit window\n")
print("Watch the spiral unfold? (slow)\t\t[1]\nOr view the final result? (less slow)\t[2]\n")
choice = input(":")
print("please wait...")

# toplevel widget 'root'
root = tk.Tk()
root.attributes("-fullscreen", True)

# canvas inside 'root'
screen = tk.Canvas(root, height = 500, width = 500, bg = 'white')

# reference values and starting points
Ts = 5                          # length (no. of pixels) of Tile side
Sw = root.winfo_screenwidth()   # Screen width
Sh = root.winfo_screenheight()  # Screen height
x  = (Sw/2) - (Ts/2)    # x-coordinate
y  = (Sh/2) - (Ts/2)    # y-coordinate
sprl = 0

# A function to generate new (x,y) coordinates in a spiral pattern
def generate_coordinates():    
    global x, y, sprl

    while True:
        sprl += 1
        for j in range(sprl):   # North
            y -= Ts
            yield x
            yield y

        for j in range(sprl):   # West
            x -= Ts
            yield x
            yield y

        sprl += 1        
        for j in range(sprl):   # South
            y += Ts
            yield x
            yield y
        
        for j in range(sprl):   # East
            x += Ts
            yield x
            yield y

# tile 1 centered in screen
screen.create_rectangle(x, y, (x + Ts), (y + Ts), fill = 'grey', outline = 'grey')
screen.pack(fill = 'both', expand = 1)

# populate screen with an anti-clockwise spiral of black-and-white tiles;
#  Black if not prime & White if prime
num = 0
xy = generate_coordinates()
while (x > (0 - Ts)):
    X = next(xy)
    Y = next(xy)

    num += 1
    Prime = True
    sqrt = m.ceil(m.sqrt(num))      # square root of 'num' rounded up
    for i in range(sqrt, 1, -1):
        if (num / i).is_integer():
            Prime = False
            break
    
    if Prime:
        screen.create_rectangle(X, Y, (X + Ts), (Y + Ts), fill = 'white', outline = 'white')
    else:
        screen.create_rectangle(X, Y, (X + Ts), (Y + Ts), fill = 'black', outline = 'black')

    screen.pack(fill = 'both', expand = 1)

    if choice == '1':
        screen.update()

# Event Mainloop
screen.mainloop()
