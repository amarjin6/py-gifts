from point import Point


class Cluster:
    def __init__(self, center=Point()):
        self.center = center
        self.points = []

    def __str__(self):
        return f'({self.center.x}, {self.center.y})'
