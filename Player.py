from Coordinate import Coordinate

class Player:

    # constructor of coordinate class
    def __init__(self):
        self.coordinate = None # user's entered coordinate
        self.previousInputs = [] # user's input history of previously entered coordinates
        self.numOfGuess = 5 # user's number of guesses
        self.isWin = False # user's status if they win or not
        self.isQuit = False # user's status if they quit or not

    # gets the user to enter a relative coordinate
    def enterCoordinate(self):

        # keeps looping until the user enters a valid coordinate
        while True:
            try:
                column, row = input("Enter coordinate (column, row): ").split(" ")

                # typecast column and row values from String to Integer value
                column = int(column)
                row = int(row)

            # display error to the user if the coordinate is not an Integer
            except ValueError:
                print("Enter a valid input!!")

            # break out of loop if user enters a valid coordinate
            else:
                break

        # assigns the relative coordinate entered by the user to the
        # player's coordinate
        self.coordinate = Coordinate(column, row)

    # decreases the number of guesses made by the player
    # after each turn
    def decreaseNumOfGuess(self):
        self.numOfGuess -= 1

    # overrides toString method to print player's number of guess
    def __str__(self):
        return "NumOfGuess: {}".format(self.NumOfGuess)