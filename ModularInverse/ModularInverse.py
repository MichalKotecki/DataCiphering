# Title: Modular Inverse in Python
# Author: Michał Kotecki
# Date: 5/09/2020
# Description:


class TableRow:
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s

    def __str__(self) -> str:
        return f"q: {self.q}, r: {self.r}, s: {self.s} \n"

    def __repr__(self) -> str:
        return f"q: {self.q}, r: {self.r}, s: {self.s} \n"


# This is used to find S in (a S) mod b = 1 given that a and b are known.
def modularInverse(a, b):

    r0 = 0
    r1 = 0
    # TO-DO is this correct?
    if (a > b):
        r1 = 1
    else:
        r0 = 1

    table = []
    table.append(TableRow(0,a,r0))
    table.append(TableRow(0,b,r1))

    while True:
        # calculating current row
        q = int(table[-2].r / table[-1].r)
        r = table[-2].r - (q * table[-1].r)
        s = table[-2].s - (q * table[-1].s)

        table.append(TableRow(q,r,s))

        if r == 1:
            print(table)
            return s if s > 0 else s + a
        elif r == 0:
            print(table)
            return -1

    return -1

if __name__ == '__main__':
    a = 10
    b = 7

    print("Modular Inverse Algorithm")
    filterResult = lambda num: f"The solution is {num}." if num > 0 else "There is no solution."
    print(filterResult(modularInverse(a, b)))