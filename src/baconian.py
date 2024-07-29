baconian_alphabet = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
    'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
    'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBBA', 'N': 'ABBBB', 'O': 'BAAAA',
    'P': 'BAAAB', 'Q': 'BAABA', 'R': 'BAABB', 'S': 'BABAA', 'T': 'BABAB',
    'U': 'BABBA', 'V': 'BABBB', 'W': 'BBAAA', 'X': 'BBAAB', 'Y': 'BBABA',
    'Z': 'BBABB', ' ': 'BBBBB'
}

reverse_baconian_alphabet = {v: k for k, v in baconian_alphabet.items()}

def baconian_encryption(message):
    encoded_message = ''
    message = message.upper()
    for char in message:
        if char in baconian_alphabet:
            encoded_message += baconian_alphabet[char] + ''
        else:
            encoded_message += char
    return encoded_message.strip()

def baconian_decryption(encoded_message):
    decoded_message = ''
    encoded_message = encoded_message.split()
    for block in encoded_message:
        if block in reverse_baconian_alphabet:
            decoded_message += reverse_baconian_alphabet[block]
        else:
            decoded_message += block
    return decoded_message