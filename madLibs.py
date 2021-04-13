"""
Author: Zachary Montague
Date: 4/13/2021
Description: Program to ask the user for input and forming a story using string methods to create a madlib.
"""

# Constant declaration
LETTER_TO_ADD = "s"


# Print statement to announce beginning of game
print("Let's play MadLibs!")

# User inputs
playerName = input("Give me a name: ")
playerNoun = input("Give me a noun: ")
playerPlant = input("Give me a type of plant: ")
playerAnimal = input("Give me a type of animal: ")
playerEmotion = input("Give me an emotion: ")

# String manipulation
# First letter extraction
nameFirstLetter = playerName[:1]
# Length of name
nameLength = len(playerName)
# Create name in reverse with loop
reversedName = ""
for character in playerName:
    reversedName = character + reversedName
# Add an 's' to plant to make it plural
plantWithAddedCharacter = "".join((playerPlant, LETTER_TO_ADD))
# Make the emotion all uppercase
uppercaseEmotion = playerEmotion.upper()

# Print the story
print(reversedName + " is my favorite " + playerNoun + " but I just call him " + nameFirstLetter + ".")
print("He has " + str(nameLength) + " eyes and moves like a herd of wild " + plantWithAddedCharacter + ".")
print("When he speaks " + playerAnimal + " I feel so " + uppercaseEmotion + "!")
