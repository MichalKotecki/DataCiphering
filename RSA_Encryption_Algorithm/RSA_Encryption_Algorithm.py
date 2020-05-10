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
# Everybody owns two keys: a private key and a public key.
#
# RSA uses:
# 1. Diffie-Helman Key Exchange
# 2. Modular Inverse algorithm
# 3. Euler's Phi Function
# 4. Euler's Theorem

import secrets
from ModularInverse import ModularInverse
from Key_Exchange import Diffie_Helman_Key_Exchange

# GCD stand for Greatest Common Divisor
def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)

# Euler's totient function / Phi function.
#
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



def RSA():
#  1. Choose p and q. Both of them must be prime numbers.
    p = 3
    q = 11
#  2. Calculate p * q
    n = p * q
#   3. Calculate Euler's totient function / Phi function.
    # phi(n) = (p-1) * (q-1)
    print("phi(n)" ,phi(n))
    print("(p-1) * (q-1)", (p-1) * (q-1))
#   4. Find e. e needs to satisfy 2 conditions:
#                   *   1 < e < phi(n)
#                   *   GCD(e, phi(n)) = 1
#   To find e we pick some number from the given range.
#   We try to find d, such that (e * d) mod phi(n) = 1. This is Modular Inverse algorithm.
#   If d exists, the number e is okay. If the number is not okay, we pick different e and try again.
#   My implementation of Modular Inverse algorithm returns -1, if solution does not exist.
    d = -1
    e = 7
    while True:
        # e = secrets.choice(range(1, phi(n)))
        d = ModularInverse.modularInverse(e, phi(n))
        if d > 0:
            break
#   6. We determine the number c by calculating c = (m^e) mod n
#      m is the number to be encrypted.
    m = 2
    c = Diffie_Helman_Key_Exchange.smartModulo(m, e, n)
    print("Encrypted number:", c)
#   7. Decryption:
    m = Diffie_Helman_Key_Exchange.smartModulo(c, d, n)
    print("Decrypted number:", m)


def splitTextIntoPiecesOfLength_N(text, lengthOfSinglePiece):
    arrayOfSplitted = []

    for i in range(0, len(text), lengthOfSinglePiece):
        arrayOfSplitted.append(text[i: i + lengthOfSinglePiece])

    numberOfLackingCharactersInLastPiece = arrayOfSplitted[-1].__len__() < lengthOfSinglePiece
    if(numberOfLackingCharactersInLastPiece > 0):
        for i in range(numberOfLackingCharactersInLastPiece):
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

    # a = ord('a')
    # b = ord('b')
    # # to change it back from ASCII to char: chr(b)
    # binary = (a << 8) + b

    listOfSplittedTextPieces = splitTextIntoPiecesOfLength_N("michal_kotecki", 3)
    for piece in listOfSplittedTextPieces:
        print(piece)
        bits = textToBits(piece)
        print(bits)
        print(bitsToText(bits,3))
        print()

    # print("binary:", binary)
    # RSA()