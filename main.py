from tkinter import Tk, Canvas
from human import Human

window = Tk()
canvas = Canvas(window)
canvas.pack()
h = Human(canvas, 100, 250)
h.display()
window.mainloop()
