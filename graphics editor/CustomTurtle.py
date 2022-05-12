from turtle import RawTurtle, TurtleScreen
import Drawable
from tkinter import *


class CustomTurtle(Drawable.Drawable):
    def __init__(self, root):
        # Create turtle inside tk
        can = Canvas(root, width=800, height=500, bg="black")  # a canvas what will turn into turtle screen
        tsc = TurtleScreen(can)
        tur = RawTurtle(tsc)
        can.pack()
        self.t = tur

    def forward(self, distance):
        self.t.forward(distance)

    def circle(self, radius):
        self.t.circle(radius)

    def right(self, angle):
        self.t.right(angle)

    def left(self, angle):
        self.t.left(angle)
