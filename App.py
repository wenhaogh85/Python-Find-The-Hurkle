from Coordinate import Coordinate
from Grid import Grid
from Hurkle import Hurkle
from Player import Player

import utility as util

def game():

    # initialses objects such as gird, hurkle, and player
    grid = Grid()
    hurkle = Hurkle(grid)
    player = Player()

    # initialses welcome message when playing the game
    message = "Find the Hurkle"

    # keeps the game going until:
    # - player runs out of guesses
    # - player correctly guessed the location (coordinate) of the hurkle
    # - player quits the game
    while player.numOfGuess > 0 and player.isWin == False and player.isQuit == False:

        # displays the game current condition to the user
        print(
                "\n=============================================\n" +
                message +
                "\n=============================================\n" +
                str(grid) +
                "\n---------------------------------------------" +
                "\nEnter coordinate (-1,-1) to quit the game"
                "\n\nNumber of guesses left: " + str(player.numOfGuess)
            )

        # gets the user to enter coordinate
        player.enterCoordinate()

        # checks if the player want to quite the game
        # by entering coordinate -1 -1
        if player.coordinate.x == -1 and player.coordinate.y == -1:
            message = "Game Over"
            player.isQuit = True

        else:

            # checks if the user entered coordinate is out of range
            if util.isOutOfRange(player.coordinate, grid) != True:

                # checks if the user entered coordinate has not been entered before
                if util.isDuplicate(player.coordinate, player.previousInputs) != True:

                    # adds newly entered coordinate into input history
                    player.previousInputs.append(player.coordinate)

                    # checks if the player successfully guessed the location of the hurkle
                    # by checking if their coordinate matches in terms of row and column values
                    if player.coordinate == hurkle.coordinate:

                        # updates user's win status
                        player.isWin = True

                        # updates the grid's layout with the hurkle's location
                        # and its symbol
                        grid.updateLayout(hurkle.coordinate, hurkle.symbol)

                        # updates message to display to the user
                        message = "Yay! you found the hurkle!"

                    else:
                        # decreases the number of guesses if the player
                        # fail to guess the location of the hurkle
                        player.decreaseNumOfGuess()

                        # updates the grid's layout with the players's location
                        # and "X" symbol
                        grid.updateLayout(player.coordinate, "X")

                        # gets the direction in words to guide the player
                        # in finding the hurkle's location
                        direction = util.getApproximateDirection(player, hurkle)

                        # updates message to display to the user
                        message = "Hurkle is somewhere in " + direction

                else:
                    # updates message to display to the user
                    message = "You have guessed this coordinate before"

            else:
                # updates message to display to the user
                message = "Your coordinate is out of range"

    # checks if the player has win
    if player.isWin == True:
        print(
                "\n=============================================\n" +
                message +
                "\n=============================================\n" +
                str(grid) +
                "\n---------------------------------------------" +
                "\nNumber of guesses left: " + str(player.numOfGuess) + "\n"
            )

    # checks if the player has quit
    elif player.isQuit == True:
        grid.updateLayout(hurkle.coordinate, hurkle.symbol)
        print(
                "\n=============================================\n" +
                message +
                "\nHurkle was at coordinate: " + str(hurkle.coordinate) +
                "\n=============================================\n" +
                str(grid) +
                "\n---------------------------------------------" +
                "\nNumber of guesses left: " + str(player.numOfGuess) + "\n"
            )

    # checks if the player has lost
    elif player.numOfGuess == 0:
        message = "You lose :'("
        grid.updateLayout(hurkle.coordinate, hurkle.symbol)
        print(
                "\n=============================================\n" +
                message +
                "\nHurkle was at coordinate: " + str(hurkle.coordinate) +
                "\n=============================================\n" +
                str(grid) +
                "\n---------------------------------------------" +
                "\nNumber of guesses left: " + str(player.numOfGuess) + "\n"
            )

# ----------------------------------
# implementation

keepPlaying = True
while keepPlaying == True:

    print(
            "=============================================" +
            "\nFind the Hurkle" +
            "\n=============================================" +
            "\n- A Hurkle is hiding in a 10 by 10 grid" +
            "\n- Try to guess the Hurkle's location" +
            "\n- You have 5 guesses" +
            "\n=============================================\n"
        )

    answer = input("Would you like to play the game? [y/n]: ").lower()

    if answer == "y":
        game()

        keepAsking = True
        while keepAsking == True:

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            confirmation = input("Would you like to play again? [y/n]: ").lower()

            if confirmation == "y":
                game()

            elif confirmation == "n":
                keepAsking = False
                keepPlaying = False

            else:
                print("Invalid input!\n")

    elif answer == "n":
        keepPlaying = False

    else:
        print("Invalid input!\n")

print("\nThank you for playing Find The Hurkle! Have a nice day!!")