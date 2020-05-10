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


import secrets
from ModularInverse import ModularInverse
from Key_Exchange import Diffie_Helman_Key_Exchange

# GCD stand for Greatest Common Divisor
def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)


# Euler's totient function / Phi function.
# If n is equivalent to n = p * q (where p ang q are prime numbers), than phi(N) = (p - 1) * (q - 1)
def phi(num):
    result = num
    p = 2

    while (p * p <= num):

        if (num % p == 0):
            while (num % p == 0):

                num = num // p

            result = result * (1.0 - (1.0 / (float)(p)))

        p = p + 1

    if (num > 1):
        result = result * (1.0 - (1.0 / (float)(num)))
    return (int)(result)



def RSA_Encryption(p, q, numberToEncrypt):
#  1. Choose p and q. Both of them must be prime numbers.
#  2. Calculate p * q
    n = p * q
    if numberToEncrypt > n-1:
        print("ERROR. You can not encrypt this, because your prime numbers are too small. Please choose bigger prime numbers.")

#   3. Calculate Euler's totient function / Phi function.
    # phi(n) = (p-1) * (q-1)

    # print("phi(n)" ,phi(n))
    # print("(p-1) * (q-1)", (p-1) * (q-1))

#   4. Find e. e needs to satisfy 2 conditions:
#                   *   1 < e < phi(n)
#                   *   GCD(e, phi(n)) = 1
#   To find e we pick some number from the given range.
#   We try to find d, such that (e * d) mod phi(n) = 1. This is Modular Inverse algorithm.
#   If d exists, the number e is okay. If the number is not okay, we pick different e and try again.
#   My implementation of Modular Inverse algorithm returns -1, if solution does not exist.
    d = -1
    e = 0
    while True:
        e = secrets.choice(range(1, phi(n)))
        d = ModularInverse.modularInverse(e, phi(n))
        if d > 0:
            break
#   6. We determine the number c by calculating c = (numberToEncrypt^e) mod n
    print("Number before encryption: ", numberToEncrypt)
    encryptedNumber = Diffie_Helman_Key_Exchange.smartModulo(numberToEncrypt, e, n)
    print("Encrypted number:", encryptedNumber)
    return (encryptedNumber, d)



def RSA_Decryption(p, q, d, numberToDecrypt):
    n = p * q
#   Only the last few lines are different between RSA Encryption and Decryption.
    decryptedNumber = Diffie_Helman_Key_Exchange.smartModulo(numberToDecrypt, d, n)
    print("Decrypted number:", decryptedNumber)
    return decryptedNumber




def splitTextIntoBlocksOfLength_N(text, lengthOfSingleBlock):
    arrayOfSplitted = []

    for i in range(0, len(text), lengthOfSingleBlock):
        arrayOfSplitted.append(text[i: i + lengthOfSingleBlock])

    numberOfLackingCharactersInLastBlock = arrayOfSplitted[-1].__len__() < lengthOfSingleBlock
    if(numberOfLackingCharactersInLastBlock > 0):
        for i in range(numberOfLackingCharactersInLastBlock):
            arrayOfSplitted[-1] += chr(0)

    return arrayOfSplitted


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

    print("Please enter text to be encrypted: ")
    textToEncrypt = input()
    
    print("Please enter length of text blocks: ")
    lengthOfTextBlocks = int(input())
    
    
    listOfSplittedTextBlocks = splitTextIntoBlocksOfLength_N(textToEncrypt, lengthOfTextBlocks)
    print(listOfSplittedTextBlocks)

    listOfEncryptedTextBlocks = []
    for block in listOfSplittedTextBlocks:
        bits = textToBits(block)
        listOfEncryptedTextBlocks.append(RSA_Encryption(p,q,bits))

    print(listOfEncryptedTextBlocks)

    # TO-DO decryption does not work
    decryptedText = ""
    for block_and_e in listOfEncryptedTextBlocks:
        decryptedText += bitsToText(RSA_Decryption(p, q, block_and_e[1], block_and_e[0]), lengthOfTextBlocks)
    print(decryptedText)