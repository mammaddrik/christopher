def getWordPattern(word):
    pattern = ""
    char_number = {}
    i = 0
    for char in word:
        if char not in char_number:
            char_number[char] = i
            i += 1
        pattern += f"{char_number[char]}."
    return pattern[0:-1]