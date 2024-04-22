from detect.detectenglish import isEnglish
import string
import os
def affine_encryption(plaintext: any, a: int, b: int) -> str:
    """
    Encrypts the given message using the Affine cipher method.

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


def extended_gcd(a: int, b: int) -> tuple:
    """
    Extended Euclidean Algorithm to find the greatest common divisor
    and coefficients x, y such that ax + by = gcd(a, b).
    
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

def affine_decrypt(ciphertext: any, a: int, b: int) -> str:
    """
    Decrypt a message encrypted with the Affine Cipher using
    the given key components a and b.
    
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

def affine_brute_force(ciphertext: any) -> str:
    """Brute-force attack to find possible keys for an Affine Cipher
    and print potential decryptions for manual inspection.
    
    Parameters:
    ciphertext (str): The ciphertext to be decrypted.

    Returns:
    str: A list containing all possible decrypted plaintexts.
    """
    alphabet = string.ascii_lowercase
    m = len(alphabet)
    path = r"./out"
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = "AffineCipher.txt"
    os.chdir("./out")
    with open(file_name, "w") as file:
        file.write("Brute Force Decryption:\n\n")
        for a in range(1, m):
            if extended_gcd(a, m)[0] == 1:
                for b in range(0, m):
                    decrypted_text = affine_decrypt(ciphertext, a, b)
                    file.write(f"Slope(a)={a} Intercept(b)={b} : {decrypted_text}\n")
                    if isEnglish(decrypted_text):
                        print(f"├─[Slope(a) = {a} Intercept(b) = {b}]\n├─[The plaintext may be this: {decrypted_text}]")
    os.chdir("..")