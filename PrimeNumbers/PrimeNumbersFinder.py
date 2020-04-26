from math import sqrt

# Title: 'Finding all Prime Numbers in a specified range' in Python
# Author: Michał Kotecki
# Date: 4/19/2020


def FindAllPrimeNumbersInRange(rangeStart, rangeEnd):

    primes = list(range(2, int(sqrt(rangeEnd)) + 1))

    for prime in primes:
        number = prime * 2
        while number in primes:
            primes.remove(number)
            number += prime

    num = rangeEnd - rangeStart + 1

    for number in range(rangeStart, rangeEnd + 1):
        for prime in primes:
            if number % prime == 0:
                num -= 1
                break
    return  num


if __name__ == '__main__':

    rangeStart = 8_000_000
    rangeEnd = 9_000_000

    NumOfPrimes = FindAllPrimeNumbersInRange(rangeStart, rangeEnd)
    print("There are", NumOfPrimes, "prime numbers in the range starting at", rangeStart, "and ending at", rangeEnd)

    # The result for range (8_000_000, 9_000_000) is 62712.