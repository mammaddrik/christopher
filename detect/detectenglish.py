import string
import os

letters = string.ascii_letters
LETTERS_AND_SPACE = letters + ' \t\n'

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
def loadDictionary():
    path = os.getcwd()
    if os.name == "nt":
        dictionaryFile = open(path+'/detect/dictionary.txt')
    else:
        try:
            dictionaryFile = open('/usr/local/sbin/detect/dictionary.txt')
        except FileNotFoundError:
            dictionaryFile = open(path+'/detect/dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
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

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch