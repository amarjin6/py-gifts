from tkinter import *
from tkinter.ttk import *
from turtle import RawTurtle, TurtleScreen
from abc import ABC, abstractmethod
import circle
import ellipse
import line
import polygon
import rectangle


class Drawable(ABC):
    @abstractmethod
    def forward(self, distance):
        ...

    @abstractmethod
    def circle(self, radius, extent=None, steps=None):
        ...

    @abstractmethod
    def right(self, angle):
        ...

    @abstractmethod
    def left(self, angle):
        ...


class CustomTurtle(Drawable):
    def __init__(self):
        # Create turtle inside tk
        can = Canvas(root, width=800, height=500, bg="black")  # a canvas what will turn into turtle screen
        tsc = TurtleScreen(can)
        tur = RawTurtle(tsc)
        can.pack()
        self.t = tur

    def forward(self, distance):
        self.t.forward(distance)

    def circle(self, radius, extent=None, steps=None):
        self.t.circle(radius)

    def right(self, angle):
        self.t.right(angle)

    def left(self, angle):
        self.t.left(angle)


class Figures:
    def __init__(self, figure, i, t: Drawable):
        lst = []
        for j in range(i):
            print(f"Enter {j + 1} argument:")
            lst.append(int(input()))

        self.figure = figure(lst, t)

    def draw(self):
        self.figure.draw()


# Create tk window
root = Tk()  # the tk window
root.title('Graphics editor')
root.iconbitmap('icon.ico')
root.geometry('800x650')
root.configure(bg='grey')

# Create entryText
entryText1 = StringVar()
entryText2 = StringVar()

tur = CustomTurtle()


def lines():
    figure = Figures(line.Line, 1, tur)
    tur.t.color('red')
    figure.draw()
    tur.t.setpos(0, 0)


def rectangles():
    figure = Figures(rectangle.Rectangle, 2, tur)
    tur.t.color('green')
    figure.draw()
    tur.t.setpos(0, 0)


def polygons():
    figure = Figures(polygon.Polygon, 2, tur)
    tur.t.color('blue')
    figure.draw()
    tur.t.setpos(0, 0)


def circles():
    figure = Figures(circle.Circle, 1, tur)
    tur.t.color('purple')
    figure.draw()
    tur.t.setpos(0, 0)


def ellipses():
    figure = Figures(ellipse.Ellipse, 1, tur)
    tur.t.color('orange')
    figure.draw()
    tur.t.setpos(0, 0)


def main():
    """
    Will make a tk window and a TurtleScreen with a turtle in it
    That will be Graphics Editor
    """

    # Create style Object
    style = Style()

    style.configure('TButton', font=
    ('calibri', 20, 'bold'),
                    borderwidth='4')

    # Changes will be reflected
    # by the movement of mouse.
    style.map('TButton', foreground=[('active', '!disabled', 'purple')],
              background=[('active', 'blue')])

    # Create entry
    entryText1.set("Param 1")
    entryText2.set("Param 2")
    width = Entry(root, font=('calibri', 24), width=14, textvariable=entryText1)
    height = Entry(root, font=('calibri', 24), width=14, textvariable=entryText2)
    width.pack()
    height.pack()
    var = lambda: print(entryText1.get())

    # Create buttons
    buttons = {'Line': lines, 'Rectangle': rectangles, 'Circle': circles, 'Polygon': polygons, 'Ellipse': ellipses}
    for button, comm in buttons.items():
        btn = Button(root, text=button,
                     command=comm)
        btn.pack(side=LEFT)

    root.mainloop()


if __name__ == '__main__':
    main()
