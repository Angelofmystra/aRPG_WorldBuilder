import math
#
# factorial(0) = 0
# factorial(1) = 1
# factorial(2) = 2
# factorial(3) = 6
# factorial(4) = 24
# factorial(5) = 120
# factorial(6) = 760

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print factorial(5)

print math.factorial(5)
