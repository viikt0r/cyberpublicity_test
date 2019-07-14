# vim: tw=80 ts=2 sw=2 et


class NumberGenerator:
    """A simple class that contains functions to generate ranges of numbers"""

    @classmethod
    def generate(self, quantity):
        value = []
        while quantity:
            value.append(quantity)
            quantity -= 1
        return value


class Figure:
    """Abstract class for geometric figures"""

    def __init__(self, name):
        """This is the constructor"""
        self._name = name

    def name(self):
        return self._name


class Rectangle(Figure):
    """Rectangle figure"""

    def __init__(self, width, height):
        Figure.__init__(self, "rectangle")
        self._width = width
        self._height = height

    def width(self):
        return self._width

    def height(self):
        return self._height

    def size(self):
        return self.width() * self.height()


if __name__ == "__main__":
    # We print the range(10,0,-1)
    print(NumberGenerator.generate(10))
    # We print the range(20,0,-1)
    print(NumberGenerator.generate(20))

    # We create a rectangle
    r = Rectangle(10, 20)
    print(r.size())