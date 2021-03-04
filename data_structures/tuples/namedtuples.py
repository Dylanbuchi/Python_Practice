from collections import namedtuple


def main():
    Point = namedtuple('Point', ['x', 'y'])
    coords = Point(x=20, y=20)

    print(coords)


if __name__ == "__main__":
    main()
