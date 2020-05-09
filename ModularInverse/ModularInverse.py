# Title: Modular Inverse in Python
# Author: Michał Kotecki
# Date: 5/09/2020
# Description:
# This algorithm is used to find S in (a * S) mod b = 1, given that a and b are known.
# This kind of problem is called 'Prime Factorization'.

class TableRow:
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s

    def __str__(self) -> str:
        return f"q: {self.q}, r: {self.r}, s: {self.s} \n"

    def __repr__(self) -> str:
        return f"q: {self.q}, r: {self.r}, s: {self.s} \n"



def modularInverse(a, b):

    correctPositions = lambda a, b: (a, b, 1, 0) if a > b else (b, a, 0, 1)
    r0, r1, s0, s1 = correctPositions(a,b)

    table = []
    table.append(TableRow(0,r0,s0))
    table.append(TableRow(0,r1,s1))

    while True:
        # calculating current row
        q = int(table[-2].r / table[-1].r)
        r = table[-2].r - (q * table[-1].r)
        s = table[-2].s - (q * table[-1].s)

        table.append(TableRow(q,r,s))

        if r == 1:
            # print(table)
            return s if s > 0 else s + b
        elif r == 0:
            # print(table)
            return -1


if __name__ == '__main__':

    print("Modular Inverse Algorithm")
    print("This is used to find S in (a * S) mod b = 1 given that a and b are known.")
    print("Enter a:")
    a = int(input())
    print("Enter b:")
    b = int(input())

    filterResult = lambda num: f"The solution is {num}." if num > 0 else "There is no solution."
    print(filterResult(modularInverse(a, b)))