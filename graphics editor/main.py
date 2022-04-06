from tkinter import *
from turtle import RawTurtle, TurtleScreen


def main():
    """
    Will make a tk window and a TurtleScreen with a turtle in it
    That will be Graphics Editor
    """
    # Create tk window
    root = Tk()  # the tk window
    root.geometry('800x600')

    # Create turtle inside tk
    can = Canvas(root)  # a canvas what will turn into turtle screen
    tsc = TurtleScreen(can)
    tur = RawTurtle(tsc)

    # Create buttons
    btn = Button(root, text='Click me !',
                 command=root.destroy)
    btn.pack(side='right')
    root.mainloop()


if __name__ == '__main__':
    main()
