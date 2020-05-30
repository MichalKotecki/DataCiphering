from math import sqrt

# Title: Diffie-Helman Key Exchange in Python
# Author: Michał Kotecki
# Date: 4/29/2020
# Description:
# In the case, where two people want to send ciphered messages to one another, they both need to have the same key in order to cipher or decipher messages.
# One of the ways to achieve this is Diffie-Helman.
# Diffie-Helman is good, because the information they share as public is not enough to decipher messages.
# Modulo operation makes it very difficult to guess, what are the secret keys.
# Modulo function is kind of a 'Trap Door' function, because it is easy to do and hard to undo.
# Huge vulnerability: somebody can act as a middle-man between both sides of the communication.
# That person just establish his own secret key and act as thought, he is supposted to receive those messages.
# Than he decipher them and ciphers them again with his secret key and sends them to the proper receiver.
# Nobody can tell anything is wrong and Diffie-Helman does not provide any way to deal with this problem.

def Diffie_Helman_DEMO():
    # Numbers p and g are not secret. They can be public.
    p = 11  # p must be a prime number
    g = 4  # g can be any number

    # Number a_secret is secret, only one person in two-side communication knows it and NEVER shares it with anybody.
    # a_secret can be any number.
    a_secret = 8

    # Number is b_secret is only known by the other person.
    # b_secret can be any number.
    b_secret = 17

    # A_send will be send from owner of a_secret to the owner of b_secret.
    # B_send will be send from owner of b_secret to the owner of a_secret.
    A_send = pow(g, a_secret) % p
    B_send = pow(g, b_secret) % p

    # When both sides of the communication receive number A_send and B_send,
    # Both sides calculate their keys.
    A_key = pow(B_send, a_secret) % p
    B_key = pow(A_send, b_secret) % p

    # A_key should be equal B_key.

    print("p: ", p)
    print("g: ", g)

    print("a_secret: ", a_secret)
    print("b_secret: ", b_secret)

    print("A_send", A_send)
    print("B_send", B_send)

    print("A_key", A_key)
    print("B_key", B_key)


# # Function smartModulo is a significantly faster way of calculating: pow(number, power) % modulo
# def smartModulo(number, power, modulo):
#     result = number % modulo
#     current_exponent = 1
#
#     while(current_exponent != power):
#         result = ((result % modulo) * (number % modulo) % modulo)
#         current_exponent += 1
#
#     return result


# Function smartModulo is a significantly faster way of calculating: pow(number, power) % modulo
def smartModulo(number, power, modulo):
    result = 1
    current_exponent = number % modulo
    step = 1

    for i in range(1, power + 1, step):
        step = step << 1
        if i == power:
            result = (result * current_exponent) % modulo
        current_exponent = (current_exponent * current_exponent) % modulo

    return result

def isPrimeNumber(number):
    squaredRoot = int(sqrt(number))
    for potentialDivisor in range(2,squaredRoot + 1):
        if number % potentialDivisor == 0:
            return 0
    return 1

def clientDiffie_Helman():
    print("Please enter a prime number: ")
    p = int(input())
    while not isPrimeNumber(p):
        print(p, "is NOT a prime number. Try again.")
        print("Please enter a prime number: ")
        p = int(input(p))

    print("Please enter any number: ")
    g = int(input())

    print("Please enter your SECRET NUMBER: ")
    secret_number = int(input())
    number_to_send = smartModulo(g, secret_number, p)
    print("This number will be send to the other client: ", number_to_send)

    print("Please enter the number you received from the other client:")
    received_number = int(input())
    key = pow(received_number, secret_number, p)
    print("Your key is:", key)

if __name__ == '__main__':
    clientDiffie_Helman()

