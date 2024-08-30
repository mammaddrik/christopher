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
    """
    Encrypts a given message using the Baconian cipher.

    Parameters:
    message (str): The plaintext message to be encrypted. The message will be converted 
        to uppercase during processing.

    Returns:
    str: The encrypted message where each letter is replaced by its corresponding 
        Baconian cipher sequence. Non-alphabet characters remain unchanged.

    Example:
        >>> baconian_encryption("christopher")
        'AAABAAABBBBAABBABAAABABAABABABBAAAABAAABAABBBAABAABAABB'
    """
    encoded_message = ''
    message = message.upper()
    for char in message:
        if char in baconian_alphabet:
            encoded_message += baconian_alphabet[char] + ''
        else:
            encoded_message += char
    return encoded_message.strip()

def baconian_decryption(encoded_message):
    """
    Decrypts a given message encoded with the Baconian cipher.

    Parameters:
    encoded_message (str): The message encoded with the Baconian cipher. The encoded message should 
        consist of sequences of 'A's and 'B's separated by spaces.

    Returns:
    str: The decoded plaintext message where each sequence of 'A's and 'B's is 
        converted back to its corresponding letter. Non-cipher sequences remain 
        unchanged.

    Example:
        >>> baconian_decryption("AAABA AABBB BAABB ABAAA BABAA BABAB BAAAA BAAAB AABBB AABAA BAABB")
        'christopher'
    """
    decoded_message = ''
    encoded_message = encoded_message.split()
    for block in encoded_message:
        if block in reverse_baconian_alphabet:
            decoded_message += reverse_baconian_alphabet[block]
        else:
            decoded_message += block
    return decoded_message
