import codecs
import functools
import operator
import string
import re


# Title: Breaking Vigenère Cipher in Python
# Author: Michał Kotecki
# Date: 3/19/2020
# Description:
# Program uses predefined alphabet which consists of 0 ... 9 and a ... z. The alphabet can be easily changed.
# There is no difference between encrypting lowercase and uppercase characters.
# Input text is read from a file.
# There is an assumption made that keyword length is between 2 and 20.

# Vigenère Cipher is easy to break in most cases. Only if the keyword is the same length as plaintext, this cipher is unbreakable.
# To break this Cipher, the length of the keyword must be know.
# To determine the length of the keyword we can use method called The Kasiski Examination.

# The Kasiski Examination
# Find repeating patterns in the text and keep distances between them. The longer the patterns are, the better.
# For short (2 or 3 letter patterns), pattern may appear the same by accident.
# Statistically, the chance of patterns being the same by random decreases with the length of the pattern.

# Example
# Text is Stephen King's novel titled 'A Death' and keyword is '9dd41zk0ne', the output numbers of The Kasiski Examination clearly indicate, that the keyword's length is 10.

def readFileToString(filePath):
    content = ""
    with codecs.open(filePath, 'r', 'utf-8') as f:
        lineList = f.readlines()
        for line in lineList:
            content += line.upper()
    return content

def listOfNums():
    numList = list(map(str, list(range(0, 10))))
    return numList

alphabet = listOfNums() + list(string.ascii_uppercase)

def excludeNonAlphabetCharactersFromPlaintext(plaintext):
    textafterremoval = re.sub("[^A-Z0-9]", "", plaintext)
    return textafterremoval

def getDictionaryOfOccurences(minimumPatternLenth, plaintext):
    patternDict = {}
    maximumPatternLenth = len(plaintext) // 2

    for patternLenth in range(minimumPatternLenth, maximumPatternLenth):
        for i in range(0, len(plaintext) - patternLenth + 1):
            pattern = plaintext[i:i + patternLenth]
            tempIndexList = []
            distanceList = []
            for x in re.finditer(pattern, plaintext):
                tempIndexList.append(x.start())
            for j in range(0, len(tempIndexList) -1):
                distanceList.append(tempIndexList[j+1] - tempIndexList[j])
            if tempIndexList.__len__() >= 2:
                patternDict[pattern] = distanceList.copy()

    # for patternName, indexList in zip(patternDict.keys(), patternDict.values()):
    #     print(patternName, indexList)
    return patternDict


def theKasiskiExamination(minimumPatternLenth, plaintext):
    occurenceDict = getDictionaryOfOccurences(minimumPatternLenth, plaintext)

    occurencesOfDividers = {}
    for key in range(2, 21):
        occurencesOfDividers[key] = 0

    for distanceLength in functools.reduce(operator.iconcat, occurenceDict.values(), []):
        for divider in range(2, 21):
            if(distanceLength % divider) == 0:
                occurencesOfDividers[divider] += 1

    for divider, numberOfOccurences in zip(occurencesOfDividers.keys(), occurencesOfDividers.values()):
        print('N=', divider, ',', numberOfOccurences)

if __name__ == '__main__':

    plaintext = readFileToString('D:\Projekty\DataSecurity\DataCiphering\Vigenere\cipheredVigenere.txt')
    # print(plaintext)
    #   For breaking cipher, I do not need any characters, that are not in the alphabet, so I just exclude them.
    plaintext = excludeNonAlphabetCharactersFromPlaintext(plaintext)
    # print(plaintext)
    print('Breaking Vigenere Cipher')
    print('What is the minimum length of a pattern you want to search for?')
    minimumPatternLenth = int(input())
    theKasiskiExamination(minimumPatternLenth,plaintext)



