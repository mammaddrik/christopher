import string

ETAOIN = 'ETAOIN'
VKJXQZ = 'VJJXQZ'
chars = string.ascii_uppercase

def getLetterCount(text):
    output = {}
    for char in chars:
        output[char] = 0
    for char in text:
        if char.upper() in output:
            output[char.upper()] += 1
    return output

def getMaxCount(letterCount):
    max_char = None
    max_count = -1
    for char in letterCount:
        count = letterCount[char]
        if count > max_count:
            max_count = count
            max_char = char
    return max_char

def getFrequencyOrder(text):
    output = ""
    letterCount = getLetterCount(text)
    for i in range(len(chars)):
        max_char = getMaxCount(letterCount)
        output += max_char
        del letterCount[max_char]
    return output

def getFrequencyScore(text):
    score = 0
    freqOrder = getFrequencyOrder(text)
    for char in freqOrder[0:6]:
        if char in ETAOIN:
            score += 1
    for char in freqOrder[-6:]:
        if char in VKJXQZ:
            score += 1
    return score