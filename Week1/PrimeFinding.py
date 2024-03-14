# program that returns a list of all primes up to a given number
# Sabelo Dlamini
# 12 March 2024

import math


def allPrimesUpTo(num):
    primes = []
    for i in range(2, num+1):
        numroot = math.isqrt(i) + 1
        for j in range(3, numroot):
            if (i % j == 0):
                break
        else:
            primes.append(i)
    
    return primes


print(allPrimesUpTo(100))