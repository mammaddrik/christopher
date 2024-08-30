import string
import sys

SYMBOL = string.printable
BLOCKSIZE = 16

def blockToString(blocks: list)-> str:
    """
    Converts a list of integer blocks into a string using a custom encoding based on `SYMBOL`.

    Parameters:
    blocks (list): A list of integer blocks to be converted into a string.

    Returns:
    str
        The resulting string after converting all the integer blocks.

    Examples:
    >>> blockToString([12345, 67890])
    'dXiYgk'
    """
    output = ""
    for block in blocks:
        while block:
            index = block % len(SYMBOL)
            block = block // len(SYMBOL)
            output += SYMBOL[index]
    return output

def stringToBlock(plaintext: str)-> list:
    """
    Converts a plaintext string into a list of integer blocks using a custom encoding based on `SYMBOL`.

    Parameters:
    plaintext (str): The input string to be converted into integer blocks.

    Returns:
    list: A list of integer blocks representing the encoded `plaintext`.

    Examples:
    >>> stringToBlock("hello world")
    [311912601413, 975537]
    """
    output = []
    while plaintext:
        block_number = 0
        block_string = None
        if len(plaintext) >= BLOCKSIZE:
            block_string = plaintext[0:BLOCKSIZE]
            plaintext = plaintext[BLOCKSIZE:]
        else:
            block_string = plaintext
            plaintext = ''
        for i in range(len(block_string)):
            index = SYMBOL.find(block_string[i])
            block_number += (index * (len(SYMBOL) ** i))
        output.append(block_number)
    return output

def publickey_encrypt(plaintext, publicKey, outputfile):
    """
    Encrypts a plaintext string using an RSA public key and writes the ciphertext to a file.

    Parameters:
    plaintext : str
        The input string to be encrypted.
    publicKey : tuple
        The RSA public key, a tuple `(n, e)` where `n` is the modulus and `e` is the public exponent.
    outputfile : str
        The name of the file where the encrypted ciphertext will be written.

    Returns:
    None

    Examples:
    >>> publicKey = (2357, 17)
    >>> publickey_encrypt("hello world", publicKey, "ciphertext")
    """
    plainblocks = stringToBlock(plaintext)
    cipherblocks = []
    for block in plainblocks:
        C = pow(block, publicKey[1], publicKey[0])
        cipherblocks.append(str(C))
    file = open(outputfile, 'w')
    file.write(",".join(cipherblocks))
    file.close()

def publickey_decrypt(encrypted_file, privateKey):
    """
    Decrypts a ciphertext file using an RSA private key and returns the resulting plaintext.

    Parameters:
    encrypted_file : str
        The name of the file containing the encrypted ciphertext.
    privateKey : tuple
        The RSA private key, a tuple `(n, d)` where `n` is the modulus and `d` is the private exponent.

    Returns:
    str
        The decrypted plaintext string.

    Examples:
    >>> privateKey = (2357, 157)
    >>> plaintext = publickey_decrypt("ciphertext", privateKey)
    >>> print(plaintext)
    'hello world'
    """
    try:
        file = open(encrypted_file, 'r')
    except FileNotFoundError:
        print("└─[File not find]")
        sys.exit()
    cipherblocks = file.read()
    file.close()
    cipherblocks = cipherblocks.split(',')
    plainblocks = []
    for block in cipherblocks:
        M = pow(int(block), privateKey[1], privateKey[0])
        plainblocks.append(M)
    return blockToString(plainblocks)

def readKeysFromFile(filename):
    """
    Reads RSA public and private keys from files and returns them as tuples.

    Parameters:
    filename : str
        The base name of the files containing the keys (without extensions).

    Returns:
    tuple
        A tuple containing two elements:
        - publicKey: A tuple `(n, e)` where `n` is the modulus and `e` is the public exponent.
        - privateKey: A tuple `(n, d)` where `n` is the modulus and `d` is the private exponent.

    Examples:
    >>> publicKey, privateKey = readKeysFromFile("mykeys")
    >>> print(publicKey)
    (2357, 17)
    >>> print(privateKey)
    (2357, 157)
    """
    try:
        publicFile = open(f"{filename}_public.key", "r")
        privateFile = open(f"{filename}_private.key", "r")
    except FileNotFoundError:
        print("└─[File not find]")
        sys.exit()
    publicKey = publicFile.read()
    privateKey = privateFile.read()
    try:
        publicKey = publicKey.split(",")
        publicKey = int(publicKey[1]), int(publicKey[2])
        privateKey = privateKey.split(",")
        privateKey = int(privateKey[1]), int(privateKey[2])
    except IndexError:
        print("└─[Public file or Private File is Empty]")
        sys.exit()
    publicFile.close()
    privateFile.close()
    return publicKey, privateKey