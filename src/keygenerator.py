import random
from src import primenumber
from src import cryptomath

def generateKeys(keysize = 1024):
    """
    Generates a pair of RSA public and private keys.
    
    Parameters:
    keysize int: The size (in bits) of the keys to generate. Default is 1024 bits.

    Returns:
    tuple
        A tuple containing two elements:
        - publickey: A tuple (n, e) where n is the modulus and e is the public exponent.
        - privatekey: A tuple (n, d) where n is the modulus and d is the private exponent.

    Examples:
    >>> publickey, privatekey = generateKeys(1024)
    
    >>> print(publickey)
    (n_value, e_value)
    
    >>> print(privatekey)
    (n_value, d_value)
    """
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
    """
    Saves the generated RSA public and private keys to files.

    Parameters:
    -----------
    keysize : int
        The size (in bits) of the keys.
    publickey : tuple
        The public key tuple (n, e).
    privatekey : tuple
        The private key tuple (n, d).
    filename : str
        The base name for the files. The function will create <filename>_Public.key 
        and <filename>_Private.key.

    Returns:
    None

    Examples:

    >>> publickey, privatekey = generateKeys(1024)
    >>> writeKeysToFile(1024, publickey, privatekey, "mykeys")

    This will create the files mykeys_Public.key and mykeys_Private.key.
    """
    publicFile = open(f"{filename}_Public.key", 'w')
    privateFile = open(f"{filename}_Private.key", 'w')

    publicFile.write(f"{keysize}, {publickey[0]}, {publickey[1]}")
    privateFile.write(f"{keysize}, {privatekey[0]}, {privatekey[1]}")
    publicFile.close()
    privateFile.close()