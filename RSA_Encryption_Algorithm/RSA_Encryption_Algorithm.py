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


from ModularInverse import ModularInverse
from Key_Exchange import Diffie_Helman_Key_Exchange

# GCD stand for Greatest Common Divisor
def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)

# Euler's totient function / Phi function.
#
def phiFunction(num):
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
    p = 11
    q = 17
#  2. Calculate p * q
    n = p * q
#   3. Calculate Euler's totient function / Phi function.


if __name__ == '__main__':
    print(phiFunction(766420))