import string
import os

letters = string.ascii_letters
LETTERS_AND_SPACE = letters + ' \t\n'

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

def loadDictionary() -> dict:
    """
    Loads a dictionary of English words from a file.

    Returns:
    dict: A dictionary where each key is an English word from the file.
    """
    if os.name == "nt":
        dictionaryFile = open(r'.\detect\dictionary.txt')
    else:
        try:
            dictionaryFile = open(r'/usr/local/sbin/detect/dictionary.txt')
        except FileNotFoundError:
            dictionaryFile = open(r'/detect/dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message: str)-> float:
    """
    Calculates the proportion of words in a message that are English words.

    Parameters:
    message (str): The message to be analyzed.

    Returns:
    float: The proportion of words in the message that are recognized English words.
    """
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message: str) -> str:
    """
    Removes non-letter characters from a message.

    Parameters:
    message (str): The message to be cleaned.

    Returns:
    str: The message with only letters and spaces.
    """
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message: str, wordPercentage=20, letterPercentage=85) -> bool:
    """
    Determines if a message is likely in English based on word and letter percentages.

    Parameters:
    message (str): The message to be analyzed.
    wordPercentage (float): The minimum percentage of English words required.
    letterPercentage (float): The minimum percentage of letters required.

    Returns:
    bool: True if the message meets the criteria for being in English, False otherwise.
    """
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch