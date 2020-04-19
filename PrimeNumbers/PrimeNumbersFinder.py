from math import sqrt


def isPrimeNumber(number):
    squaredRoot = int(sqrt(number))

    for potentialDivisor in range(1,squaredRoot + 1):
        if number % potentialDivisor == 0:
            return 0
    return 1


def FindAllPrimeNumbersInRange(rangeStart, rangeEnd):

    searchRange = list(range(rangeStart, rangeEnd + 1))

    for number in searchRange:
        if not isPrimeNumber(number):
            # searchRange.remove(number)
        #     pass
        # else:
            for subnumber in range(number * 2, rangeEnd+1, number):
                if subnumber % number == 0 and subnumber in searchRange:
                    searchRange.remove(subnumber)

    print(searchRange)
    return  searchRange


if __name__ == '__main__':

    rangeStart = 2
    rangeEnd = 8_000_000

    NumOfPrimeNumsFrom2To8_000_000 = FindAllPrimeNumbersInRange(rangeStart, rangeEnd).__len__()

    rangeEnd = 9_000_000
    NumOfPrimeNumsFrom2To9_000_000 = FindAllPrimeNumbersInRange(rangeStart, rangeEnd).__len__()

    NumOfPrimeNumsInGivenRange = NumOfPrimeNumsFrom2To9_000_000 - NumOfPrimeNumsFrom2To8_000_000
    print("There is ", NumOfPrimeNumsInGivenRange, "in the range starting at ", rangeStart, " and ending at ", rangeEnd, "."  )

    # Kotecki Michał: 8_000_000     9_000_000
    
    