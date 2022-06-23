from Coordinate import Coordinate

import random

class Hurkle:

    # constructor of hurkle class
    def __init__(self, grid):
        self.symbol = "O" # symbol representing the hurkle on the grid's layout
        self.coordinate = self.setCoordinate(grid) # relative coordinate

    # sets the relative coordinate of the hurkle
    def setCoordinate(self, grid):

        # sets the hurkle's column range between 0 to maximum layout columns
        column = random.randrange(0, grid.columns)

        # sets the hurkle's row range between 0 to maximum layout rows
        row = random.randrange(0, grid.rows)

        return Coordinate(column, row)

    # overrides toString method to print hurkle's coordinate and symbol
    def __str__(self):
        return "coordinate: {}\nsymbol: {}".format(self.coordinate, self.symbol)