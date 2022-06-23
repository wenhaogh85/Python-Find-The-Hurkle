from typing import Coroutine
from Coordinate import Coordinate
from Grid import Grid
from Hurkle import Hurkle
from Player import Player

# checks for duplicate coordinate
def isDuplicate(targetCoordinate, coordinates):

    # loops through a list of coordinates
    # to see if the coordinate matches the target coordinate
    for coordinate in coordinates:

        # checks if the coordinate is equal the target coordinate
        # in terms of row and column values
        if coordinate == targetCoordinate:
            return True
    return False

# gets the approximate direction in words to guide
# the player in finding the hurkle
def getApproximateDirection(player, hurkle):

    player_column = player.coordinate.x
    player_row = player.coordinate.y

    hurkle_column = hurkle.coordinate.x
    hurkle_row = hurkle.coordinate.y

    # north
    if player_column == hurkle_column and player_row < hurkle_row:
        return "North"

    # northeast
    elif player_column < hurkle_column and player_row < hurkle_row:
        return "NorthEast"

    # east
    elif player_column < hurkle_column and player_row == hurkle_row:
        return "East"

    # southeast
    elif player_column < hurkle_column and player_row > hurkle_row:
        return "SouthEast"

    # south
    elif player_column == hurkle_column and player_row > hurkle_row:
        return "South"

    # southwest
    elif player_column > hurkle_column and player_row > hurkle_row:
        return "SouthWest"

    # west
    elif player_column > hurkle_column and player_row == hurkle_row:
        return "West"

    # northwest
    elif player_column > hurkle_column and player_row < hurkle_row:
        return "NorthWest"

# checks if relative coordinate entered by the user is out of range
def isOutOfRange(coordinate, grid):

    column = coordinate.x
    row = coordinate.y

    if column < 0 or column > grid.columns - 1:
        return True
    if row < 0 or row > grid.rows - 1:
        return True

    return False