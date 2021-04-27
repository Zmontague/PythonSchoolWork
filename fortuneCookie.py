"""
Author: Zachary Montague
Date: 4/27/2021
Description: Program to provide the user with a fortune and magic number, prompting the user until they state no in the prompt.
"""
# Import statements
import random


# Variable declaration
fileName = "fortunes.txt"
randomFortune = ""
randomMagicNumber = 0 # if num shows up as 0, error with program
userInput = ""


# List declaration
fortunes = []

# Dictionary declaration
usedFortunesAndMagicNums = {}

# Open provided fortune file
f = open(fileName, 'r')
# Read file into list
for line in f:
    fortunes.append(line)

# close file
f.close()

# Begin looping and randomly selecting magic numbers and fortunes and testing if the user wishes to continue getting
# fortunes.
while True:
    # Select random fortune from the fortunes list.
    randomFortune = random.choice(fortunes)
    # Remove random fortune from the list
    fortunes.remove(randomFortune)
    # Strip white spaces from the fortune
    randomFortune = randomFortune.strip()
    # Generate random magic number
    randomMagicNumber = random.randint(1, 100)
    # Add magic number and fortune to dictionary
    usedFortunesAndMagicNums.update({randomFortune : randomMagicNumber})

    # Print fortune and magic number
    print("Fortune: ", randomFortune)
    print("Magic number: ", randomMagicNumber)

    # Check if the user wishes to continue
    userInput = input("Would you like another fortune cookie (Y/N)? ")
    # If user enters 'n' or 'N' or the fortunes list runs out of fortunes, the program will print the recieved
    # fortune and magic number before ending the program.
    if userInput.lower() == 'n' or len(fortunes) == 0:
        print("Here are all the fortunes you received: ")
        for key, value in usedFortunesAndMagicNums.items():
            print(key, " Magic Number: ", value)
        break
    # Sanity check to prevent any strange occurrences where the program may end. Not required, but nice to have.
    else:
        continue
