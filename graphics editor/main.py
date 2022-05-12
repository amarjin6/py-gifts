from tkinter import *
from tkinter.ttk import *
import CustomTurtle
import Drawable
import circle
import ellipse
import line
import polygon
import rectangle


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
root.iconbitmap('img/icon.ico')
root.geometry('800x650')
root.configure(bg='grey')

tur = CustomTurtle.CustomTurtle(root)


def lines():
    figure = Figures(line.Line, 1, tur.t)
    tur.t.color('red')
    figure.draw()
    tur.t.setpos(0, 0)


def rectangles():
    figure = Figures(rectangle.Rectangle, 2, tur.t)
    tur.t.color('green')
    figure.draw()
    tur.t.setpos(0, 0)


def polygons():
    figure = Figures(polygon.Polygon, 2, tur.t)
    tur.t.color('blue')
    figure.draw()
    tur.t.setpos(0, 0)


def circles():
    figure = Figures(circle.Circle, 1, tur.t)
    tur.t.color('purple')
    figure.draw()
    tur.t.setpos(0, 0)


def ellipses():
    figure = Figures(ellipse.Ellipse, 1, tur.t)
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

    # Create buttons
    buttons = {'Line': lines, 'Rectangle': rectangles, 'Circle': circles, 'Polygon': polygons, 'Ellipse': ellipses}
    for button, comm in buttons.items():
        btn = Button(root, text=button,
                     command=comm)
        btn.pack(side=LEFT)

    root.mainloop()


if __name__ == '__main__':
    main()
