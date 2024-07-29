import string
import random
from src.makewordpatterns import getWordPattern
from src.wordpatterns import wordPatterns
from detect.detectenglish import removeNonLetters

SYMBOLS = string.ascii_uppercase

def generateKey():
    key = list(SYMBOLS)
    random.shuffle(key)
    return "".join(key)

def simple_substitution_encrypt(plaintext, key):
    return translateMessage(plaintext, key, "encrypt")

def simple_substitution_decrypt(ciphertext, key):
    return translateMessage(ciphertext, key, "decrypt")

def translateMessage(text, key, mode):
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

def getEmptyMapping():
    mapping = {}
    for char in SYMBOLS:
        mapping[char] = []
    return mapping

def getCipherWordMapping(cipherword):
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

def combineTwoMapping(mappingA, mappingB):
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

def removeSolvedLetters(mapping):
    for char in mapping:
        if len(mapping[char]) == 1:
            solved = mapping[char][0]
            for char2 in mapping:
                if char2 != char:
                    if solved in mapping[char2]:
                        mapping[char2].remove(solved)
    return mapping

def crack(ciphertext):
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
    print(f"├─[{letterMapping}]")