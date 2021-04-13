"""
Author: Zachary Montague
Date: 4/5/2021
Description: User inputs number of dice rolls, program tracks box cars and snake eyes achieved when random number is rolled.
"""

# import statements
import random

# Constants declaration
SNAKE_EYES = 2
BOXCARS = 12
DICE_MAXIMUM_SIDES = 6
DICE_MINIMUM_SIDES = 1

# Variable declaration
diceRollOne = 0
diceRollTwo = 0
diceRollTotal = 0
rollNumber = 0
snakeEyeTimes = 0
boxCarTimes = 0


# Game 1 introduction print statement
print("Game 1: Snake Eyes")

# User input
inputDiceRollsNumber = int(input("Enter the number of times you wish to roll the dice: "))

# For loop through the user input dice rolls and calculate snake eyes
for roll in range(0, inputDiceRollsNumber):
    # Have dice generate random int between 1-6
    diceRollOne = random.randint(DICE_MINIMUM_SIDES, DICE_MAXIMUM_SIDES)
    diceRollTwo = random.randint(DICE_MINIMUM_SIDES, DICE_MAXIMUM_SIDES)
    # Calculate dice total after each roll
    diceRollTotal = diceRollOne + diceRollTwo
    # Store number of times snake eyes was rolled
    if diceRollTotal == 2:
        snakeEyeTimes += 1
    # Print outputs
    print("---------------------------")
    print("Roll        Dice      Sum")
    print(roll+1, "         ", diceRollOne, diceRollTwo, "     ", diceRollTotal)
    print("----------------------------")

# Print snake eyes tally
print("You rolled snake eyes ", snakeEyeTimes, " time(s)")

# Reset variables
diceRollOne = 0
diceRollTwo = 0
diceRollTotal = 0

# Game 2 introduction print statement
print("----------------------------")
print("Game 2: Boxcars")

# While loop through and see how many times it takes until boxcar is reached
while boxCarTimes < 1:
    # Advance roll number by 1 each time loop begins
    rollNumber += 1
    # Have dice generate random int between 1-6
    diceRollOne = random.randint(DICE_MINIMUM_SIDES, DICE_MAXIMUM_SIDES)
    diceRollTwo = random.randint(DICE_MINIMUM_SIDES, DICE_MAXIMUM_SIDES)
    # Calculate dice total after each roll
    diceRollTotal = diceRollOne + diceRollTwo
    # Check to see if dice rolls reached box cars, end game by updating boxCarTimes to 1 for when loop finishes.
    if diceRollTotal == 12:
        boxCarTimes += 1
    # Print outputs of the rolls, dice, and sum.
    print("---------------------------")
    print("Roll        Dice       Sum")
    print(rollNumber, "         ", diceRollOne, diceRollTwo, "      ", diceRollTotal)
    print("----------------------------")

# Game 2 end print statement.
print("It took ", rollNumber, " rolls for you to roll boxcars!")






