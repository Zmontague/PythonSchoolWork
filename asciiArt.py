"""
Author: Zachary Montague
Date: 4/19/2021
Description: Program which prompts user for file name, reads the file
name in, line by line iterates through the file and then decrypts the text, finally displaying the art and asking the
user if they wish to read more files, until blank line is entered
"""

# Variable declaration
fileText = ""

# Ask the user for input (file name) and explain how to exit
fileName = input("Enter a file name to read, or just Enter to quit: ")

# Loop through opening a file until the user gives an empty string
while fileName != "":
    # Open file with the file name the user provided
    f = open(fileName, 'r')
    fileText = f.readlines()
    f.close()
    print(fileText)
