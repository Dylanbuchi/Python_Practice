class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._check_width_and_height_values_are_valid()

    def _check_width_and_height_values_are_valid(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError(
                "The width and height values must be greater than 0")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._check_width_and_height_values_are_valid()
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._check_width_and_height_values_are_valid()
        self._height = height

    def __str__(self):
        return f"Rectange: width: {self.width} height: {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, other):
        if self._is_rectangle(other):
            return self.height == other.height and self.width == other.width
        return False

    def _is_rectangle(self, object):
        return isinstance(object, Rectangle)


if __name__ == "__main__":
    r1 = Rectangle(34, 12)
    r2 = Rectangle(34, 12)

    print(repr(r1))
    print(r1 == r2)
