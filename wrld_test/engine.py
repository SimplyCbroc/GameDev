#Aetherial Engine V.1
from tkinter import *
tk = Tk()

def create_window(x, y, title):
    #Creates a new window
    global canvas
    canvas = Canvas(tk, width=(x), height=(y))
    canvas.pack()
    tk.title(title)

def create_animated(file, frames, index):
    #creates an animated sprite
    global sprites
    sprites = []
    for x in range(0, frames):
        sprites.append(str(x) + str(index))
    print(sprites)
    for y in range(0, len(sprites)):
        sprites[y] = PhotoImage(file=(file), format="gif -index " + str(y))
        
    


