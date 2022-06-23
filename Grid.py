from Coordinate import Coordinate

class Grid:

    # constructor of grid class
    def __init__(self, columns = 10, rows = 10):
        self.columns = columns + 1 # since start from 0, add 1
        self.rows = rows + 1 # since start from 0, add 1
        self.layout = self.createLayout()

    # creates layout based on the number of colummns and rows
    # that was defined
    def createLayout(self):

        # creates a 2D array
        layout = []
        for row in range(self.rows):
            layout.append(["." for column in range(self.columns)])

        return layout

    # maps relative coordinate to actual coordinate
    # or actual coordinate to relative coordinate
    def mapCoordinate(self, coordinate):

        column = coordinate.x
        row = (self.rows - 1) - coordinate.y

        return Coordinate(column,row)

    # updates grid's layout with a symbol based on the relative coordinate
    def updateLayout(self, relativeCoordinate, symbol):

        actualCoordinate = self.mapCoordinate(relativeCoordinate)

        column = actualCoordinate.x
        row = actualCoordinate.y

        self.layout[row][column] = symbol

    # overrides toString method to print grid's layout
    def __str__(self):

        space = " "

        layout = (space * 19) + "NORTH\n"

        rowNumber = self.rows - 1
        middle = rowNumber // 2
        for row in range(self.rows):

            layout += space * 4

            if rowNumber == middle:
                layout += "WEST " + str(rowNumber) + space
            elif rowNumber < 10:
                layout += (space * 5) + str(rowNumber) + space
            else:
                layout += (space * 4) + str(rowNumber) + space

            for column in range(self.columns):
                layout += str(self.layout[row][column]) + space

            if rowNumber == middle:
                layout += "EAST"

            layout += "\n"
            rowNumber -= 1

        layout += space * 11

        for columnNumber in range(self.columns):
            layout += str(columnNumber) + space

        layout += "\n" + (space * 19) + "SOUTH"

        return layout