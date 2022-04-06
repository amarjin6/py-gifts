from tkinter import *
from turtle import RawTurtle, TurtleScreen
from tkinter.ttk import *


def main():
    """
    Will make a tk window and a TurtleScreen with a turtle in it
    That will be Graphics Editor
    """
    # Create tk window
    root = Tk()  # the tk window
    root.title('Graphics editor')
    root.iconbitmap('icon.ico')
    root.geometry('800x650')
    root.configure(bg='grey')

    # Create turtle inside tk
    can = Canvas(root, width=800, height=500, bg="black")  # a canvas what will turn into turtle screen
    tsc = TurtleScreen(can)
    tur = RawTurtle(tsc)
    can.pack()

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
    entryText1 = StringVar()
    entryText1.set("WIDTH")
    entryText2 = StringVar()
    entryText2.set("HEIGHT")
    width = Entry(root, font=('calibri', 24), width=14, textvariable=entryText1)

    height = Entry(root, font=('calibri', 24), width=14, textvariable=entryText2)
    width.pack()
    height.pack()

    buttons = {'Line': print(width.get), 'Rectangle': 2, 'Circle': 3, 'Polygon': 4, 'Ellipse': 5}

    for button, comm in buttons.items():
        btn = Button(root, text=button,
                     command=comm)
        btn.pack(side=LEFT)

    root.mainloop()


if __name__ == '__main__':
    main()
