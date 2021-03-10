import math


class Polygon:
    def __init__(self, edges, circumradius):
        self._check_polygon_is_valid(edges)
        self._edges = edges

        self._circumradius = circumradius
        self._vertices = self._edges

# methods

    def _check_polygon_is_valid(self, edges):
        if edges < 3:
            raise ValueError("Polygon has to have 3+ edges")
        return True

    def _is_polygon(self, object):
        return isinstance(object, self.__class__)

# fields

    @property
    def interior_angle(self):
        n = self._edges
        return (n - 2) * (180 / n)

    @property
    def edge_length(self):
        return (2 * self._circumradius) * math.sin(math.pi / self._edges)

    @property
    def apothem(self):
        return self._circumradius * math.cos(math.pi / self._edges)

    @property
    def area(self):
        return (self._edges / 2) * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self._edges * self.edge_length

    @property
    def vertices(self):
        return self._edges

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def edges(self):
        return self._edges

# magic methods

    def __len__(self):
        return self._edges - 2

    def __repr__(self):
        return f"Polygon({self._edges}, {self._circumradius})"

    def __eq__(self, other):
        # equality
        if not self._is_polygon:
            return NotImplemented

        return self._vertices == other.vertices and self._circumradius == other.circumradius

    def __gt__(self, other):
        # greater than: '>'
        if not self._is_polygon:
            return NotImplemented

        return self._vertices > other.vertices


# main
if __name__ == "__main__":
    polygon1 = Polygon(edges=6, circumradius=1)

    print(polygon1.perimeter)
    print(polygon1.area)
    print(polygon1.interior_angle)
    print(polygon1.apothem)
    print(polygon1.edges)
    print(polygon1.edge_length)

    print(polygon1 > Polygon(5, 1))
