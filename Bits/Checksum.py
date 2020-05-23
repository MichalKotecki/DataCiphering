# Title: Checksum in Python
# Author: Michał Kotecki
# Date: 5/23/2020
# Description:
# Checksum is a hash number of a text. Checksum is commonly used in data transmission.
#
# Example
# User A sends a message to user B.
# They want to be sure message did not get corrupted, while being send (by internet connection problems)
# and user B got the EXACT message user A sent.
# User A calculates a checksum and sends it with message to user B.
# User B receives the text message and uses it to calculate checksum.
# User B compares his/her checksum with the checksum he/she got from user A.
# If the checksum is identical, then the probability data got corrupted during the transmission is very low.
# If the checksum is different, it is CERTAIN that the data got corrupted.
#
# It is very important to create the checksum in such a way, that the probability of getting the same number for different text is very low.
#
# Hash function are used to get a hash number (checksum). There are many hash functions.
# Below I implemented two of them:
# 1. DJB / Bernstein hash / Chris Torek hash
# 2. Adler-32

import string
import random


def DJB(data):
    hash = 5381
    for character in data:
        hash = (hash << 5) + hash + ord(character)
    return hash


def Adler32(data):
    A = 1
    B = 0
    # 65521 is the biggest prime number smaller than 2^16
    P = 65521

    for character in data:
        A = (A + ord(character)) % P
        B = (B + A) % P

    return (B << 16) + A

alphabet = list(string.ascii_uppercase) + list(string.ascii_lowercase)

def randomString(lengthOfStringToGenerate):
    randString = ""
    for i in range(lengthOfStringToGenerate):
        randString += random.choice(alphabet)
    return randString


def checksum_test(stringLength, hashFunction):
    checksumAndStringDictionary = {}
    numOfCollisions = 0

    for i in range(100_000):
        randString = randomString(stringLength)
        checksum = hashFunction(randString)
        if checksum in checksumAndStringDictionary:
            checksumAndStringDictionary[checksum].append(randString)
        else:
            tempList = []
            tempList.append(randString)
            checksumAndStringDictionary[checksum] = tempList

    for checksum, randStringList in checksumAndStringDictionary.items():
        if len(randStringList) > 1:
            numOfCollisions += (len(randStringList) * (len(randStringList)-1)) // 2
    print("Number of collisions:", numOfCollisions)

    for checksum, randStringList in checksumAndStringDictionary.items():
        if len(randStringList) > 1:
            print(randStringList[0], randStringList[1], checksum)
            break

if __name__ == '__main__':

    print("Checksum \n\n")

    print("Adler32 D=8, N=100 000")
    checksum_test(8,Adler32,)

    print("\nAdler32 D=100, N=100 000")
    checksum_test(100,Adler32)

    print("\nDJB D=8, N=100 000")
    checksum_test(8,DJB)

    print("\nDJB D=100, N=100 000")
    checksum_test(100,DJB)


