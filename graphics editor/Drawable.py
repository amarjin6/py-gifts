from abc import ABC, abstractmethod


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
