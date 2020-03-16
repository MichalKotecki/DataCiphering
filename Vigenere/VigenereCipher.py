import codecs
import string
import numpy as np

# Title: Vigenère Cipher in Python
# Author: Michał Kotecki
# Date: 3/16/2020
# Description:
# Program uses predefined alphabet which consists of 0 ... 9 and a ... z. The alphabet can be easily changed.
# Characters from the outside of the alphabet are kept, but not encrypted.
# There is no difference between encrypting lowercase and uppercase characters.
# User can: Specify action (encrypting/decrypting) and specify keyword used for that action.
# Input text is read from a file. Output text is written to a file.

# Side note:  in polish you read the name Vigenere as 'wiżyniir'

def listOfNums():
    numList = list(map(str, list(range(0, 10))))
    return numList

alphabet = listOfNums() + list(string.ascii_lowercase)

def moveAlphabet(text):
    alphabetMoved = text[1:] + [text[0]]
    return alphabetMoved

def makeEncryptionTable():
    EncryptionTable = np.array((alphabet))
    alphabetMoved = alphabet
    for i in range(1, alphabet.__len__()):
        alphabetMoved = moveAlphabet(alphabetMoved)
        EncryptionTable = np.vstack([EncryptionTable, alphabetMoved])
    return EncryptionTable


EncryptionTable = makeEncryptionTable()


def readFileToString(filePath):
    content = ""
    with codecs.open(filePath, 'r', 'utf-8') as f:
        lineList = f.readlines()
        for line in lineList:
            content += line.upper()
    return content

def writeStringToFile(filePath, string):
    with codecs.open(filePath, 'w', 'utf-8') as f:
        f.write(string)

def CipherVigenere(keyword, text):
    cipheredText = ""
    for charKeyword, charText in zip(keyword, text):
        if alphabet.__contains__(charKeyword):
            keywordIndex = alphabet.index(charKeyword)
            textIndex = alphabet.index(charText)
            # TODO If this does not encrypt as expected, you probably need to switch the order of: [keywordIndex, textIndex] below.
            cipheredText = cipheredText + EncryptionTable[keywordIndex, textIndex]
        else:
            cipheredText = cipheredText + charKeyword
    return cipheredText


def DecipherVigenere(keyword, cipheredText):
    decipheredText = ""
    for charKeyword, charText in zip(keyword, cipheredText):
        if alphabet.__contains__(charKeyword):
           tabelRow_0 = list(EncryptionTable[0])
           indexKeyword = tabelRow_0.index(charKeyword)
           tabelColumn = list(EncryptionTable[:, indexKeyword])
           indexCiphered = tabelColumn.index(charText)
           # TODO If this does not encrypt as expected, you probably need to switch the order of: [keywordIndex, textIndex] below.
           decipheredText = decipheredText + EncryptionTable[indexCiphered, 0]
        else:
           decipheredText = decipheredText + charKeyword
    return decipheredText


def repeatTextToLength(text, desiredLength):
    return (text * (desiredLength//len(text) + 1))[:desiredLength]

def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

def insertNonAlphabetChars(keyword, text):
    for index, char in enumerate(text):
        if not alphabet.__contains__(char):
            keyword = insert(keyword, char, index)
    return keyword

def cutStringToMatchLenght(length, stringToCut):
    cuttedString = stringToCut[:length]
    return cuttedString

def prepareKeyword(keyword, text):
    extendedkeyword = repeatTextToLength(keyword, len(text))
    extendedKeywordByCharsFromOutsideAlphabet = insertNonAlphabetChars(extendedkeyword, text)
    readyKeyword = cutStringToMatchLenght(len(inputText), extendedKeywordByCharsFromOutsideAlphabet)
    return readyKeyword

if __name__ == '__main__':

    inputFilePath = 'D:\Projekty\DataSecurity\DataCiphering\Vigenere\inputVigenere.txt'
    inputText = readFileToString(inputFilePath).lower()
    print(inputText)

    cipheredFilePath = 'D:\Projekty\DataSecurity\DataCiphering\Vigenere\cipheredVigenere.txt'
    cipheredText = readFileToString(cipheredFilePath).lower()
    print(cipheredText)

    decipheredFilePath = 'D:\Projekty\DataSecurity\DataCiphering\Vigenere\decipheredVigenere.txt'

    print('Encryption Table: ')
    print(EncryptionTable, '\n', '\n')

#   #   #   #   #   #   #   #

    print('Enter Keyword: ')
    keyword = input().lower()
    keyword = prepareKeyword(keyword, inputText)
    print(keyword)

    while(1):
        print('Vigenère Cipher')
        print('Press C to Cipher text')
        print('or press D to Decipher text.')
        cipheringAction = input()
        if cipheringAction == 'C' or cipheringAction == 'c':
            cipheredText = CipherVigenere(keyword, inputText)
            writeStringToFile(cipheredFilePath, cipheredText)
            print(cipheredText)
            break
        if cipheringAction == 'D' or cipheringAction == 'd':
            decipheredText = DecipherVigenere(keyword, cipheredText)
            writeStringToFile(decipheredFilePath, decipheredText)
            print(decipheredText)
            break
        print('You pressed wrong key. Try again.')