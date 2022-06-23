class Coordinate:

    # constructor of coordinate class
    def __init__(self, x, y):
        self.x = x # column
        self.y = y # row

    # updates the coordinate object's values in terms of x (column) and y (row)
    def setCoordinate(self, x, y):
        self.x = x
        self.y = y

    # overrides equal method to check
    # if coordinate objects are equal
    # in terms of x (column) and y (row)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # overrides toString method to print coordinate values
    def __str__(self):
        return "({},{})".format(self.x, self.y)