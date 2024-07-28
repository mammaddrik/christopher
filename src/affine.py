import string

def extended_gcd(a: int, b: int) -> tuple:
    """
    Extended Euclidean Algorithm to find the greatest common divisor and coefficients x, y such that ax + by = gcd(a, b).
    
    Parameters:
    a (int): The slope value to use for encryption.
    b (int): The intercept value to use for encryption.

    Returns:
    tuple: Greatest common divisor.
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modular_inverse(a: int, m: int) -> int:
    """
    Compute the modular multiplicative inverse of a modulo m.
    Raises an exception if the modular inverse does not exist.

    Returns:
    raise: Modular inverse does not exist.
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def affine_encryption(plaintext: any, a: int, b: int) -> str:
    """
    Encrypts the given plaintext using the Affine cipher method.

    Parameters:
    plaintext (str): The plaintext to be encrypted.
    a (int): The slope value to use for encryption.
    b (int): The intercept value to use for encryption.

    Returns:
    str: The encrypted ciphertext.
    """
    alphabet = string.ascii_lowercase
    m = len(alphabet)
    ciphertext = ''
    for char in plaintext:
        if char in alphabet:
            p = alphabet.index(char)
            c = (a * p + b) % m
            ciphertext += alphabet[c]
        else:
            ciphertext += char
    return ciphertext

def affine_decryption(ciphertext: any, a: int, b: int) -> str:
    """
    Decrypt the given ciphertext using the Affine cipher method.

    Parameters:
    ciphertext (str): The ciphertext to be decrypted.
    a (int): The slope value to use for decrypted.
    b (int): The intercept value to use for decrypted.

    Returns:
    str: The decrypted ciphertext.
    """
    alphabet = string.ascii_lowercase
    m = len(alphabet)
    plaintext = ''
    a_inv = modular_inverse(a, m)
    for char in ciphertext:
        if char in alphabet:
            c = alphabet.index(char)
            p = (a_inv * (c - b)) % m
            plaintext += alphabet[p]
        else:
            plaintext += char
    return plaintext

def affine_crack(ciphertext: any, a: int, b: int) -> str:
    """
    Decrypt a message encrypted with the Affine Cipher using the given key components a and b.
    
    Parameters:
    ciphertext (str): The ciphertext to be decryption.
    a (int): The slope value to use for encryption.
    b (int): The intercept value to use for encryption.

    Returns:
    str: The Decrypt ciphertext.
    """
    alphabet = string.ascii_lowercase
    m = len(alphabet)
    plaintext = ''
    a_inv = modular_inverse(a, m)
    for char in ciphertext:
        if char in alphabet:
            c = alphabet.index(char)
            p = (a_inv * (c - b)) % m
            plaintext += alphabet[p]
        else:
            plaintext += char
    return plaintext