from singleton import Singleton
from transient import Transient


class Container:
    def __init__(self):
        self.singleton = None
        self.transient = []

    def getSingletonInterface(self):
        self.singleton = Singleton()
        return self.singleton

    def getTransientInterface(self):
        self.transient.append(Transient())
        return self.transient[-1]

    def hasSingletonInterface(self, obj):
        return isinstance(obj, self.singleton)

    def hasTransientInterface(self, obj):
        for cls in self.transient:
            if isinstance(cls, obj):
                return True
        return False


if __name__ == "__main__":
    container = Container()
