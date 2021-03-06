from math import sqrt

# Title: 'Lucas-Lehmer primality test' in Python
# Author: Michał Kotecki
# Date: 4/26/2020

# Function returns 1, if a number is prime. Otherwise, function returns 0.
def isPrimeNumber(number):
    if number % 2 == 0:
        return 0

    squaredRoot = int(sqrt(number))
    for potentialDivisor in range(3, squaredRoot + 1, 2):
        if number % potentialDivisor == 0:
            return 0
    return 1

def getAllPrimeNumbersInRange(rangeEnd):

    searchRange = list(range(2, rangeEnd + 1))

    for number in searchRange:
        if not isPrimeNumber(number):
            for subnumber in range(number * 2, rangeEnd+1, number):
                if subnumber % number == 0 and subnumber in searchRange:
                    searchRange.remove(subnumber)
    return  searchRange


def Lucas_Lehmer_primality_test(primeNumber):
    mersenneNumber = pow(2, primeNumber) - 1
    lastNumber = 4
    for temp in range(0, primeNumber - 2):
        lastNumber = (pow(lastNumber, 2) - 2) % mersenneNumber
    return lastNumber == 0


if __name__ == '__main__':

    lambdaAnswer = lambda isPrime: "Prime Number" if isPrime else "Composite Number"
    primeNumbersList = getAllPrimeNumbersInRange(32)
    primeNumbersList.remove(2)
    for i, primeNumber in enumerate(primeNumbersList):
        print("2^", primeNumber, " -1 =", pow(2,primeNumber) - 1, ",", lambdaAnswer(Lucas_Lehmer_primality_test((primeNumber)))  )