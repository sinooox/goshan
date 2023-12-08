from tkinter import W


class Human:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y

    def getName(self):
        return self._name

    def display(self):
        self._DrawName()
        self._DrawHead()
        self._DrawBody()
        self._DrawLeggs()
        self._DrawHands()
        self._DrawFace()
        self._DrawName()
        self._DrawName()

    def _DrawName(self):
        self.canvas.create_text(self.x+1.5, self.y-230, text="Гошан!",
                                font="Times 18", anchor=W, fill="black")

    def _DrawHead(self):
        self.canvas.create_oval(self.x+20, self.y-200, self.x+80,
                                self.y-140, width=2)

    def _DrawBody(self):
        self.canvas.create_line(self.x+50, self.y-50, self.x+50,
                                self.y-140, width=2)

    def _DrawLeggs(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50,
                                self.x+100, self.y, width=2)

    def _DrawHands(self):
        self.canvas.create_line(self.x, self.y-140, self.x+50, self.y-100,
                                self.x+100, self.y-140, width=2)

    def _DrawFace(self):
        self.canvas.create_oval(self.x+35, self.y-185, self.x+45, self.y-175,
                                width=5, outline="light gray", fill="black")
        self.canvas.create_oval(self.x+55, self.y-185, self.x+65, self.y-175,
                                width=5, outline="light gray", fill="black")
        self.canvas.create_arc(self.x+30, self.y-190, self.x+70, self.y-150,
                               start=0, extent=-180, outline="red", width=2)
