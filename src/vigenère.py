def vigenère_encrypt(plain_text: str, key: str):
    """
    Encrypts the given plaintext using the Vigenère cipher.

    Parameters:
    plain_text (str): The text to be encrypted.
    key (str): The key used for encryption. It should be a string of alphabetic characters.

    Returns:
    str: The encrypted ciphertext.

    Example:
        >>> vigenère_encrypt("christopher", "key")
        'mlpswrytfov'
    """
    encrypted_text = ''
    key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if plain_text[i].isupper():
                encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += plain_text[i]
    return encrypted_text

def vigenère_decrypt(cipher_text, key):
    """
    Decrypts the given ciphertext using the Vigenère cipher.

    Parameters:
    cipher_text (str): The text to be decrypted.
    key (str): The key used for decryption.
    
    Returns:
    str: The decrypted ciphertext.

    Example:
        >>> vigenère_decrypt("mlpswrytfov", "key")
        'mlpswrytfov'
    """
    decrypted_text = ''
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if cipher_text[i].isupper():
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += cipher_text[i]
    return decrypted_text