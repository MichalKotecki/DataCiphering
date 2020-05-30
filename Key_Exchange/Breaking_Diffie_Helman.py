# Title: Breaking Diffie-Helman in Python
# Author: Michał Kotecki
# Date: 5/27/2020
# Description:
# Breaking Diffie-Helman means finding tge exponent_X in the equation: (base^exponent_X) % modulo = someNumber
# given that all the other number (base, modulo, someNumber) are known.
#
# Side note: this is related to problem of solving a Discrete Logarithm.
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
# The Algorithm itself goes like this:
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
import datetime
from Key_Exchange.Diffie_Helman_Key_Exchange import smartModulo
from ModularInverse.ModularInverse import modularInverse




def BreakingDiffieHelman(number, modulo, d):

    return -1


if __name__ == '__main__':

    print("Breaking Diffie-Helman Key Exchange Protocol")

    timeMeasureStart = datetime.datetime.now()
    # BreakingDiffieHelman(3, 17)
    print(BreakingDiffieHelman(1294953865, 1569834481, 1344305451))
    timeMeasureEnd = datetime.datetime.now()

    print("The calculations took ", (timeMeasureEnd - timeMeasureStart).total_seconds() * 1000_000, "microseconds.")
