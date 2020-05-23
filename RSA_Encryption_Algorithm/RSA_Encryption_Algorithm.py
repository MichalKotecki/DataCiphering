# Title: RSA Encryption Algorithm in Python
# Author: Michał Kotecki
# Date: 5/11/2020
# Description:
# The best, most popular encryption algorithm.
# It is an important part of the Internet security system.
# It relies on the time complexity of 'Prime Factorization'.
# RSA stands for Rivesta Shamira Adleman - 3 people, who invented the algorithm.
#
# Concept:
# This is an asymetric algorithm.
#
# RSA uses:
# 1. Diffie-Helman Key Exchange
# 2. Modular Inverse algorithm
# 3. Euler's Phi Function
#
# Algorithm
#  1. Choose p and q. Both of them must be prime numbers.
#  2. Calculate p * q
#  3. Calculate Euler's totient function / Phi function.
#  phi(n) = (p-1) * (q-1)
#  4. Find e. e needs to satisfy 2 conditions:
#                   *   1 < e < phi(p,q)
#                   *   GCD(e, phi(p,q)) = 1
#   To find e we pick some number from the given range.
#   We try to find privateKey, such that (e * privateKey) mod phi(p,q) = 1. This is Modular Inverse algorithm.
#   If d exists, the number e is okay. If the number is not okay, we pick different e and try again.
#   My implementation of Modular Inverse algorithm returns -1, if solution does not exist.
#   6. We determine the encryptedNumber by calculating encryptedNumber = (numberToEncrypt^e) mod n
#   7. We determine the decryptedNumber by calculating decryptedNumber = (numberToDecrypt^privateKey mod n)
#
#   Side note: Only the steps 6 and 7 are different between RSA Encryption and RSA Decryption.
#
#   To encrypt text, instead of plain numbers, we need to convert text to numbers.
#   Converting and encrypting entire text at once would be have a very high time complexity, so the text must be split into smaller blocks (2-3 characters).
#   A block of a few characters can be converted to a number, by using bit operations and mapping to ASCII codes.


import secrets
from ModularInverse import ModularInverse
from Key_Exchange import Diffie_Helman_Key_Exchange


# Euler's totient function / Phi function.
# If n is equivalent to n = p * q (where p ang q are prime numbers), than phi(N) = (p - 1) * (q - 1)
def phi(p, q):
    return (p - 1) * (q - 1)


def RSA_Encryption(n, e, numberToEncrypt):
    encryptedNumber = Diffie_Helman_Key_Exchange.smartModulo(numberToEncrypt, e, n)
    # print("Encrypted number:", encryptedNumber)
    return encryptedNumber


def RSA_Decryption(n, privateKey, numberToDecrypt):
#   Only the last few lines are different between RSA Encryption and Decryption.
    decryptedNumber = Diffie_Helman_Key_Exchange.smartModulo(numberToDecrypt, privateKey, n)
    # print("Decrypted number:", decryptedNumber)
    return decryptedNumber


def splitTextIntoBlocksOfLength_N(text, lengthOfSingleBlock):
    arrayOfSplit = []

    for i in range(0, len(text), lengthOfSingleBlock):
        arrayOfSplit.append(text[i: i + lengthOfSingleBlock])

    numberOfLackingCharactersInLastBlock = arrayOfSplit[-1].__len__() < lengthOfSingleBlock
    if(numberOfLackingCharactersInLastBlock > 0):
        for i in range(numberOfLackingCharactersInLastBlock):
            arrayOfSplit[-1] += chr(0)

    return arrayOfSplit


def textToBits(text):
    bits = int()
    for i in reversed(range(len(text))):
        bits += ord(text[-i -1]) << (i*8)
    return bits


def bitsToText(bits, lenghtOfTextToGet):
    text = ""
    for i in reversed(range(0, lenghtOfTextToGet)):
        text += chr(int(bits / pow(2, 8 * i)) % pow(2,8))
    return text

if __name__ == '__main__':

    # Example prime numbers: 5333, 5557

    print("RSA Algorithm")
    print("")

    endEncryptionLoop = False

    while not endEncryptionLoop:
        print("Please enter a prime number: ")
        p = int(input())
        while not Diffie_Helman_Key_Exchange.isPrimeNumber(p):
            print(p, "is NOT a prime number. Try again.")
            print("Please enter a prime number: ")
            p = int(input(p))

        print("Please enter another prime number: ")
        q = int(input())
        while not Diffie_Helman_Key_Exchange.isPrimeNumber(q):
            print(q, "is NOT a prime number. Try again.")
            print("Please enter a prime number: ")
            q = int(input(q))


        n = p * q
        print("n:", n)

        # Calculating private key
        e = 0
        privateKey = -1
        while True:
            e = secrets.choice(range(1, phi(p, q)))
            privateKey = ModularInverse.modularInverse(e, phi(p, q))
            if privateKey > 0:
                break

        print("phi:", phi(p, q))
        print("e:", e)
        print("d:", privateKey)

        print("Please enter text to be encrypted: ")
        textToEncrypt = input()

        print("Please enter length of text blocks: ")
        lengthOfTextBlocks = int(input())
        listOfSplitTextBlocks = splitTextIntoBlocksOfLength_N(textToEncrypt, lengthOfTextBlocks)

        asciList = list(map(lambda block: list(map(lambda character: ord(character), block)), listOfSplitTextBlocks))
        print("Plain text version of blocks:", listOfSplitTextBlocks)
        print("ASCI version of text blocks:", asciList)
        bitBlocksList = [] # this is only for printing purpose


        listOfEncryptedTextBlocks = []
        for block in listOfSplitTextBlocks:
            bits = textToBits(block)

            if bits > n - 1:
                print("ERROR. You can not encrypt this text, because your prime numbers are too small. Please start again.")
                break
            else:
                endEncryptionLoop = True

            listOfEncryptedTextBlocks.append(RSA_Encryption(n,e,bits))
            bitBlocksList.append(bits)  # this is only for printing purpose

        print("Bit version of blocks:", bitBlocksList)

    print("Encrypted text blocks:", listOfEncryptedTextBlocks)

    decryptedBitBlocksList = []  # this is only for printing purpose
    decryptedText = ""
    for block in listOfEncryptedTextBlocks:
        decryptedBitBlock = RSA_Decryption(n, privateKey, block)
        decryptedBitBlocksList.append(decryptedBitBlock) # this is only for printing purpose
        decryptedText += bitsToText(decryptedBitBlock, lengthOfTextBlocks)

    print("Decrypted bit blocks:", decryptedBitBlocksList)
    print("Decrypted text:", decryptedText)