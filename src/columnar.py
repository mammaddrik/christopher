def columnar_encrypt(text, key):
    output = [''] * key
    for columnIndex in range(key):
        textIndex = columnIndex
        while textIndex < len(text):
            output[columnIndex] += text[textIndex]
            textIndex += key
    return "".join(output)

def columnar_decrypt(ciphertext, key):
    column = key
    row = int(len(ciphertext) / column) + 1
    row , column = column, row
    shaded_count = (row * column) - len(ciphertext)
    ciphertext = list(ciphertext)
    ciphertext.reverse()
    for i in range(shaded_count):
        index = i * column
        ciphertext.insert(index, chr(0))
    ciphertext.reverse()
    ciphertext = "".join(ciphertext)
    
    output = [''] * column
    for columnIndex in range(column):
        ciphertextIndex = columnIndex
        while ciphertextIndex < len(ciphertext):
            output[columnIndex] += ciphertext[ciphertextIndex]
            ciphertextIndex += column
    output = "".join(output)
    return output.replace(chr(0), "")