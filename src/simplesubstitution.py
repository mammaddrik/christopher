import string
import random
from src.makewordpatterns import getWordPattern
from src.wordpatterns import wordPatterns
from detect.detectenglish import removeNonLetters

SYMBOLS = string.ascii_uppercase

def generateKey() -> str:
    """
    Generates a random key for a simple substitution cipher.

    Returns:
        str: A randomly shuffled key consisting of the same characters as SYMBOLS.
    """
    key = list(SYMBOLS)
    random.shuffle(key)
    return "".join(key)

def simple_substitution_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts the plaintext using a simple substitution cipher.

    Parameters:
    plaintext (str): The text to be encrypted.
    key (str): The key used for encryption.

    Returns:
    str: The encrypted ciphertext.

    Example:
        >>> simple_substitution_encrypt("christopher", "CAGYMDUPNEXBHOWQVLFZSIRKTJ")
        'gplnfzwqpml'
    """
    return translateMessage(plaintext, key, "encrypt")

def simple_substitution_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts the ciphertext using a simple substitution cipher.

    Parameters:
    ciphertext (str): The text to be decrypted.
    key (str): The key used for decryption.

    Returns:
    str: The decrypted plaintext.

    Example:
        >>> simple_substitution_decrypt("gplnfzwqpml", "CAGYMDUPNEXBHOWQVLFZSIRKTJ")
        'christopher'
    """
    return translateMessage(ciphertext, key, "decrypt")

def translateMessage(text: str, key: str, mode: str) -> str:
    """
    Encrypts or decrypts a message using a simple substitution cipher.

    Parameters:
    text (str): The text to be encrypted or decrypted.
    key (str): The key used for substitution.
    mode (str): Determines whether to encrypt or decrypt ('encrypt' or 'decrypt').

    Returns:
    str: The translated message after applying the substitution cipher.
    """
    symbols = SYMBOLS
    if mode == "decrypt":
        symbols, key = key, symbols
    output = ""
    for char in text:
        if char.upper() in symbols:
            index = symbols.find(char.upper())
            if char.isupper():
                output += key[index].upper()
            else:
                output += key[index].lower()
        else:
            output += char
    return output

def getEmptyMapping() -> dict:
    """
    Creates an empty mapping of characters to lists.

    Returns:
        dict: A dictionary where each character in SYMBOLS is a key, and the value is an empty list.
    """
    mapping = {}
    for char in SYMBOLS:
        mapping[char] = []
    return mapping

def getCipherWordMapping(cipherword: str) -> dict:
    """
    Generates a mapping of characters in a cipherword to possible corresponding characters.

    Parameters:
    cipherword (str): The ciphered word for which to generate a mapping.

    Returns:
    dict: A dictionary where each character in the cipherword maps to a list of possible corresponding characters based on known word patterns.
    """
    mapping = getEmptyMapping()
    cipherword = removeNonLetters(cipherword).upper()
    pattern = getWordPattern(cipherword)
    if pattern not in wordPatterns:
        return mapping
    possibleWords = wordPatterns[pattern]
    for i in range(len(cipherword)):
        char = cipherword[i]
        for word in possibleWords:
            mapping[char].append(word[i])
    for char in mapping:
        mapping[char] = list(set(mapping[char]))
    return mapping

def combineTwoMapping(mappingA: dict, mappingB: dict) -> dict:
    """
    Combines two character mappings into a single mapping.

    Parameters:
    mappingA (dict): The first character mapping.
    mappingB (dict): The second character mapping.

    Returns:
    dict: A combined mapping with the intersection of possible characters.
    """
    mapping = getEmptyMapping()
    for char in SYMBOLS:
        if len(mappingA[char]) == 0:
            mapping[char] = mappingB[char]
        elif len(mappingB[char]) == 0:
            mapping[char] = mappingA[char]
        else:
            charA = set(mappingA[char])
            charB = set(mappingB[char])
            result = charA.intersection(charB)
            mapping[char] = list(result)
    return mapping

def removeSolvedLetters(mapping: dict) -> dict:
    """
    Updates the character mapping by removing solved letters from other mappings.

    Parameters:
    mapping (dict): The character mapping to be updated.

    Returns:
    dict: The updated mapping with solved letters removed from other entries.
    """
    for char in mapping:
        if len(mapping[char]) == 1:
            solved = mapping[char][0]
            for char2 in mapping:
                if char2 != char:
                    if solved in mapping[char2]:
                        mapping[char2].remove(solved)
    return mapping

def crack(ciphertext: str) -> None:
    """
    Attempts to crack a simple substitution cipher by analyzing the ciphertext.

    Parameters:
    ciphertext (str): The encrypted text to be analyzed.

    Returns:
    None: Prints the plaintext and character mapping.
    Example:
        >>> crack("gplnfzwqpml")
        'christopher'
    """
    cipherwords = ciphertext.split(' ')
    letterMapping = getEmptyMapping()
    for cipherword in cipherwords:
        mapping = getCipherWordMapping(cipherword)
        letterMapping = combineTwoMapping(letterMapping, mapping)
    letterMapping = removeSolvedLetters(letterMapping)
    plaintext = ''
    for char in ciphertext:
        if char.upper() in SYMBOLS:
            if len(letterMapping[char.upper()]) == 1:
                if char.isupper():
                    plaintext += letterMapping[char][0]
                else:
                    plaintext += letterMapping[char.upper()][0].lower()
            else:
                plaintext += "_"
        else:
            plaintext += char
    print(f"└─[Plaintext: {plaintext}]")
    print(f"\n[{letterMapping}]")