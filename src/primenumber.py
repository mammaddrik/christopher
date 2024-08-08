import math
import random
def isPrimeTrialDiv(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrtn(n)) + 1):
        if n % i == 0:
            return False
    return True

def primSieve(size):
    output = []
    sieve = [True] * size
    sieve[0] = False
    for i in range(2, int(math.sqrt(size)) + 1):
        index = (i * 2) - 1
        while index < size:
            sieve[index] = False
            index += 1
    for i in range(size):
        if sieve[i]:
            output.append(i+1)
    return output

def rabinMiller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t -1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

first_100 = primSieve(100)
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    if n < 100:
        if n in first_100:
            return True
        else:
            return False
    else:
        for prime in first_100:
            if n % prime == 0:
                return False
    return rabinMiller(n)

def generateLargePrimeNumber(size = 1024):
    number = random.randint(2 ** (size - 1), 2 ** (size))
    while not isPrime(number):
        number = random.randint(2 ** (size - 1), 2 ** (size))
    return number