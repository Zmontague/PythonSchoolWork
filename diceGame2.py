"""
Author: Zachary Montague
Date: 5/4/2021
Description: User inputs number of dice rolls, program tracks box cars and snake eyes achieved when random number is rolled. Refactored with functions.
"""

# import statements
import random

# Constants declaration
SNAKE_EYES = 2
BOXCARS = 12
DICE_MAXIMUM_SIDES = 6
DICE_MINIMUM_SIDES = 1

# Dice roll function to calculate the sum of two dice, taking parameter of number of rolls
def rollDice(rollNum):
    for rolls in range(0, rollNum):
        diceRollOne = random.randint(DICE_MINIMUM_SIDES, DICE_MAXIMUM_SIDES)
        diceRollTwo = random.randint(DICE_MINIMUM_SIDES, DICE_MAXIMUM_SIDES)
        diceRollTotal = diceRollOne + diceRollTwo

        # Print outputs
        print("---------------------------")
        print("Roll        Dice      Sum")
        print(rollNum, "         ", diceRollOne, diceRollTwo, "     ", diceRollTotal)
        print("----------------------------")
        return diceRollTotal
# snake eyes function checks to see if the user has rolled 1-1 for the dice.
def snakeEyes():
    # Declare snake eyes variables
    snakeEyeTimes = 0

    # Game 1 introduction print statement
    print("Game 1: Snake Eyes")

    # User input
    inputDiceRollsNumber = int(input("Enter the number of times you wish to roll the dice: "))

    # Iterate through the snake eye rolls
    for snakeEyesRolls in range(0,inputDiceRollsNumber):
        snakeEyesPotential = rollDice(snakeEyesRolls)

        # Check each loop if the roll gives snake eyes
        if snakeEyesPotential == SNAKE_EYES:
            snakeEyeTimes += 1

    # Print snake eyes tally
    return print("You rolled snake eyes ", snakeEyeTimes, " time(s)")

# Boxcars function checks if the user has rolled boxcars (6-6) during their dice roll
def boxcars():

    # Declare boxcar variables
    boxCarTimes = 0
    rollNumber = 0
    boxCarSum = 0

    # Game 2 introduction print statement
    print("----------------------------")
    print("Game 2: Boxcars")

    # While loop through and see how many times it takes until boxcar is reached
    while boxCarTimes < 1:

        # Advance roll number by 1 each time loop begins
        rollNumber += 1
        boxCarSum = rollDice(rollNumber)

        # Check to see if dice rolls reached box cars, end game by updating boxCarTimes to 1 for when loop finishes.
        if boxCarSum == BOXCARS:
            boxCarTimes += 1

    # Game 2 end print statement.
    return print("It took ", rollNumber, " rolls for you to roll boxcars!")

# main function to print game information and accept input from users until anything but 1-3 is entered.
def main():
    print("Lets play a dice game!")
    print("--------------------------------------")
    print("1 = Roll a pair of dice\n2 = Play Snake Eyes\n3 = Play Boxcars")
    while True:
        userSelection = int(input("Choose an option (1-3) or 0 to exit: "))
        if userSelection == 3:
            boxcars()
        elif userSelection == 2:
            snakeEyes()
        elif userSelection == 1:
            rollDice(1)
        else:
            print("Thanks for playing!")
            break
main()
