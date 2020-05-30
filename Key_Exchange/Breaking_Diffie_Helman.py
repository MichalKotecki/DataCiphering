# Title: Breaking Diffie-Helman in Python
# Author: Michał Kotecki
# Date: 5/27/2020
# Description:
# Breaking Diffie-Helman means finding tge exponent_X in the equation: (base^exponent_X) % modulo = someNumber
# given that all the other number (base, modulo, someNumber) are known.
# 'exponent_X' is somebody's secret / private key.
# 'base' is public. It can be any number.
# 'modulo' is public. It must be a prime number.
# 'someNumber' is a number sent to a message receiver. It can be captured by somebody, but it is not enough to encode message without the secret / private key.
#
# Side note: this is related to the problem of solving a 'Discrete Logarithm'.
#
# There are 2 approaches to this problem:
# 1. Naive approach
# This approach means trying to put every number as exponent_X in the equation and checking if it satisfies the equation.
# The naive approach takes incredible amount of time to find the result, so it does not get applied in the real life scenerios.
#
# 2. Baby Step - Giant Step Algorithm
# For this algorithm the basic equation:
# (base^exponent_X) % modulo = someNumber
# must be transformed into different, equivalent equation:
# exponent_X = (i * sqrt( modulo )) + j
# Another condition must be satisfied: both 'i' and 'j' can only be numbers from range (0, sqrt(modulo) - 1)
# So the equation looks like this: (base^((i * sqrt( modulo )) + j)) % modulo = someNumber
# This can be transformed to: (base^j) % modulo = (someNumber * ((base^(- sqrt( modulo )))^i ))) % modulo
# We can transform this further by introducing a new variable 'baseReplacement'. We replace (base^(- sqrt( modulo )) with (baseReplacement^(sqrt( modulo ))
# To do this the following condition must be satisfied: (base * baseReplacement) % modulo = 1
# So in order to find baseReplacement we need to use ModularInverse Algorithm.
#
# So the equation we actually need to solve is:
# (base^j) % modulo = (someNumber * ((baseReplacement^(sqrt( modulo )))^i ))) % modulo
#
# To do this, we need to try out different i, j from range (0, sqrt(modulo) - 1).
# If we have a pair of 'i' and 'j' satisfying this equation we can calculate exponent_X, because as it was said before:
# exponent_X = (i * sqrt( modulo )) + j
#
#
# The algorithm itself goes like this:
# STEP 1
# First we calculate the left side of the equation for every 'j' in range (0, sqrt(modulo) - 1).
# Left side: (base^j) % modulo
# We save the all the results inside a list. Let's call this leftResultList.
#
# STEP 2
# Analogically to STEP 1, we calculate the left side of the equation for every 'i' in range (0, sqrt(modulo) - 1).
# Right side: (someNumber * ((baseReplacement^(sqrt( modulo )))^i ))) % modulo
# As we calculate this we get rightSideResult. We check if there is the same number as rightSideResult ANYWHERE inside leftResultList.
# If we find the equal results, we found a pair of 'i' and 'j' satisfying the equation.
#
# STEP 3
# We need to calculate this:
# exponent_X = (i * sqrt( modulo )) + j
#
#
# OPTIMIZATION
# To optimize / speed up the search in leftResultList we can make a hash table.
# To create a hash function, we choose a prime number, close to sqrt(modulo).
# It does not matter weather the chosen prime number is bigger/smaller/the-same-size as sqrt(modulo).
# We create hashTable - a list of list. It has length of that prime number.
# To calculate the index in the hashTable we do: ( numberWeWantToCalculateHash ) % primeNumber
# The benefit of introducing this optimization is we do not need to check whole leftResultList for every rightResult.
# We only need to check the number inside a list at index of a hashtable, which is much shorter list.
#
# OPTIMIZATION EXAMPLE
# For some left side result we get some number leftResult:
# We do: leftIndex = ( leftResult ) % primeNumber
# We save it inside the list at HashTable[leftIndex]
# When we are done with, all left side results, we start calculating the right side results.
# We do: rightIndex = ( rightResult ) % primeNumber
# If any number at the list at HashTable[rightIndex] equals to rightResult, than we can stop.
# We found correct 'i' and 'j'.


from math import sqrt, ceil
import time
from Key_Exchange.Diffie_Helman_Key_Exchange import smartModulo
from PrimeNumbers.Lucas_Lehmer_primality_test import isPrimeNumber
from ModularInverse.ModularInverse import modularInverse


# Function finds the first prime number in range (0, number + 100) starting from the end of this range.
def findPrimeNumberCloseToNumber(number):
    if number <= 0:
        return 2

    j = 1
    while True:
        for i in range(number - (100 * j-100), number - (100 * j), -1):
            if isPrimeNumber(i) == 1:
                return i
        j += 1
    return None

def BreakingDiffieHelman(base, modulo, someNumber):

    sqrtOfModulo = int(ceil(sqrt(modulo)))
    primeNumber = findPrimeNumberCloseToNumber(sqrtOfModulo)
    hashTable = [None] * primeNumber

    # Left side of the equation
    for j in range(sqrtOfModulo):
        leftResult = smartModulo(base, j, modulo)
        leftIndex = leftResult % primeNumber

        if hashTable[leftIndex] is None:
            hashTable[leftIndex] = []
        hashTable[leftIndex].append((leftResult, j))


    # Right side of the equation
    speedUpHack = someNumber
    baseReplacement = modularInverse(base, modulo)
    powOfBaseReplacementAndSqrtOfModulo = smartModulo(baseReplacement, sqrtOfModulo, modulo)
    for i in range(sqrtOfModulo):
        rightResult = speedUpHack % modulo
        rightIndex = rightResult % primeNumber
        if hashTable[rightIndex] is not None:
            for leftResultAndJ in hashTable[rightIndex]:
                if leftResultAndJ[0] == rightResult:
                    # FOUND i and j.
                    # Calculating exponent_X
                    # print("FOUND answer is j = ", leftResultAndJ[1], "i =", i)
                    return (i * sqrtOfModulo) + leftResultAndJ[1]
        speedUpHack = (speedUpHack % modulo) * powOfBaseReplacementAndSqrtOfModulo

    return -1


if __name__ == '__main__':

    print("Breaking Diffie-Helman Key Exchange Protocol\n\n")

    timeMeasureStart = int(round(time.time() * 1000))
    checkForError = lambda number: f"Result: {number}." if number != -1 else "No solution for those numbers."
    # print(checkForError(BreakingDiffieHelman(3, 17, 2)))
    print(checkForError(BreakingDiffieHelman(1294953865, 1569834481, 1344305451)))
    timeMeasureEnd = int(round(time.time() * 1000))

    print("The calculations took", (timeMeasureEnd - timeMeasureStart), "miliseconds.")
