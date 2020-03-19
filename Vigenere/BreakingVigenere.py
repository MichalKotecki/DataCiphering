import codecs
import string
import numpy as np
import re

# Title: Breaking Vigenère Cipher in Python
# Author: Michał Kotecki
# Date: 3/19/2020
# Description:
# Program uses predefined alphabet which consists of 0 ... 9 and a ... z. The alphabet can be easily changed.
# Characters from the outside of the alphabet are kept, but not encrypted.
# There is no difference between encrypting lowercase and uppercase characters.
# User can: Specify action (encrypting/decrypting) and specify keyword used for that action.
# Input text is read from a file. Output text is written to a file.


# Vigenère Cipher is easy to break in most cases. Only if the keyword is the same length as plaintext, this cipher is unbreakable.
# To break this Cipher, the length of the keyword must be know.
# To determine the length of the keyword we can use method called The Kasiski Examination.


# The Kasiski Examination
# Find repeating patterns in the text and keep distances between them. The longer the patterns are, the better.
# For short (2 or 3 letter patterns), pattern may appear the same by accident.
# Statistically, the chance of patterns being the same decreases with the length of the pattern.


def listOfNums():
    numList = list(map(str, list(range(0, 10))))
    return numList

alphabet = listOfNums() + list(string.ascii_lowercase)

def excludeNonAlphabetCharactersFromPlaintext(plaintext):
    textafterremoval = re.sub("[^a-z0-9]", "", plaintext)
    return textafterremoval

def getDictionaryOfOccurences(patternLenth, plaintext):
    patternDict = {}

    for i in range(0, len(plaintext) - patternLenth + 1):
        pattern = plaintext[i:i + patternLenth]
        tempIndexList = []
        for x in re.finditer(pattern, plaintext):
            tempIndexList.append(x.start())
        if tempIndexList.__len__() >= 2:
            patternDict[pattern] = tempIndexList.copy()

    for patternName, indexList in zip(patternDict.keys(), patternDict.values()):
        print(patternName, indexList)
    return patternDict

if __name__ == '__main__':

    plaintext = 'Programming in Python is cool. Pythons are snakes. Python, C#, C++ and SmallTalk are object oriented programming languages.'
    plaintext = plaintext.lower()
    print(plaintext)
    #   For breaking cipher, I do not need any characters, that are not in the alphabet, so I just exclude them.
    plaintext = excludeNonAlphabetCharactersFromPlaintext(plaintext)
    print(plaintext)


    patternLenth = 4


    getDictionaryOfOccurences(patternLenth, plaintext)

    #
    # patternDict = {}
    #
    # for i in range(0, len(plaintext) - patternLenth + 1):
    #     pattern = plaintext[i:i + patternLenth]
    #     tempIndexList = []
    #     for x in re.finditer(pattern, plaintext):
    #         tempIndexList.append(x.start())
    #     if tempIndexList.__len__() >= 2:
    #         patternDict[pattern] = tempIndexList.copy()
    #
    # for patternName, indexList in zip(patternDict.keys(), patternDict.values()):
    #     print(patternName, indexList)