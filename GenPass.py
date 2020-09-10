import numpy as np
import string

def masterModifier(masterAvgs):
    """Calculates the master value used to modify password values
    that correspond to printable character in the genPass function"""
    
    masterMod = sum(masterAvgs) / len(masterAvgs)
    return masterMod


def getAverages(imageData):
    """Returns an array containing the average of RGB values within
    a separate array that holds image data"""

    averages = [sum(i) / len(i) for i in imageData]
    return averages


def getMaxPass(averages):
    """Calculates the maximum password length possible, according
    to the width of the image"""

    maxLength = len(averages)
    return maxLength


def passwordLength(maxLength):
    """User selects a desired password length. The password length
    must be an integer greater than 0"""

    while True:
        print("\nMaximum password length allowed by file: " + str(maxLength))
        passLength = input("Select desired password length (recommend 12+): ")
        try:
            passLength = int(passLength)
        except(ValueError):
            print("Invalid password length")
        if type(passLength) == int:
            if passLength > 0:
                return passLength
            else:
                print("Password length must be greater than 0")


def defineChunks(averages, maxPassSize, passLength):
    """Separates RGB averages into separate arrays according to
    password length, then returns those arrays within an array"""

    return [averages[i * maxPassSize // passLength: (i + 1) * maxPassSize // passLength] for i in range(passLength)]


def genPass(passValues, masterMod):
    """Takes a list of password values of type int and the master
    modification value. The two values are multiplied, then converted
    to integers, then mod 95 for the 95 printable characters"""

    modValues = [int(i * masterMod) for i in passValues]
    modValues = [i % 95 for i in modValues]
    password = [string.printable[i] for i in modValues]
    return ''.join(password)
