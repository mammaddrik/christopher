import random
from src import primenumber
from src import cryptomath

def generateKeys(keysize = 1024):
    p = q = 0
    while p == q:
        p = primenumber.generateLargePrimeNumber(keysize)
        q = primenumber.generateLargePrimeNumber(keysize)
    n = p * q

    pq = (p - 1) * (q - 1)
    e = random.randint(2 ** (keysize - 1), 2 ** (keysize))
    while cryptomath.gcd(e, pq) != 1:
        e = random.randint(2 ** (keysize - 1), 2 ** (keysize))

    d = cryptomath.findModInverse(e, pq)

    publickey = (n, e)
    privatekey = (n, d)

    return publickey, privatekey

def writeKeysToFile(keysize, publickey, privatekey, filename):
    publicFile = open(f"{filename}_Public.key", 'w')
    privateFile = open(f"{filename}_Private.key", 'w')

    publicFile.write(f"{keysize}, {publickey[0]}, {publickey[1]}")
    privateFile.write(f"{keysize}, {privatekey[0]}, {privatekey[1]}")
    publicFile.close()
    privateFile.close()