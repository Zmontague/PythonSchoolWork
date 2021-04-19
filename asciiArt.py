"""
Author: Zachary Montague
Date: 4/19/2021
Description: Program which prompts user for file name, reads the file
name in, line by line iterates through the file and then decrypts the text, finally displaying the art and asking the
user if they wish to read more files, until blank line is entered
"""

# CONSTANT DECLARATION
DISTANCE = 1

# Variable declaration
fileText = ""
decryptedText = ""

# Ask the user for input (file name) and explain how to exit
fileName = input("Enter a file name to read, or just Enter to quit: ")

# Loop through opening a file until the user gives an empty string
while fileName != "":
    # Open file with the file name the user provided
    f = open(fileName, 'r')
    # Read the file line by line and store in variable
    fileText = f.readline()
    # Close the file when finished using it
    f.close()

    # Decrypt the file
    for letter in fileText:
        ordValue = ord(letter)
        cipherValue = ordValue - DISTANCE
        decryptedText += chr(cipherValue)

    # Print the decrypted ASCII art
    print(decryptedText)

    # Ask the user if they want to save the file
    userAnswer = input("Would you like to save the file? (Y/N) ")
    # If the user enters Y or YES, move to asking the user for the file name
    userAnswer = userAnswer.upper()
    if userAnswer == 'Y' or userAnswer == 'YES':
        saveFileName = input("Enter the new file name: ")
        # open/create the file
        f = open(saveFileName, 'x')
        # write the contents of the ascii art to the new file
        f.write(decryptedText)
        # finished with the file, close it now
        f.close()
    # if the user enters N or No, move to asking the user for the next file name.
    elif userAnswer == 'N' or userAnswer == 'NO':
        fileName = input("Enter the next file name to read, or just Enter to quit: ")

# Say goodbye to the user.
print("All done! Goodbye!")
