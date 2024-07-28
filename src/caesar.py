def caesar_encryption(plaintext: any, shift: int) -> str:
    """
    Encrypts the given plaintext using the Caesar Cipher with the specified shift.

    Parameters:
    plaintext (str): The plaintext to be encrypted.
    shift (int): The shift value to use for encryption.

    Returns:
    str: The encrypted ciphertext.

    Example:
        >>> caesar_encryption("christopher", 3)
        'fkulvwrskhu'
    """
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decryption(ciphertext: any, shift: int) -> str:
    """
    Decrypt the given ciphertext using the Caesar Cipher with the specified shift.

    Parameters:
    ciphertext (str): The ciphertext to be decrypted.
    shift (int): The shift value to use for decryption.

    Returns:
    str: The decrypted ciphertext.

    Example:
        >>> caesar_decryption("fkulvwrskhu", 3)
        'christopher'
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def caesar_crack(ciphertext: any) -> str:
    """
    Brute-force decrypts the given ciphertext using all possible Caesar Cipher shifts.

    Parameters:
    ciphertext (str): The ciphertext to be decrypted.

    Returns:
    str: A list containing all possible decrypted plaintexts.
    """
    decrypted_texts = []
    for shift in range(1, 26):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decrypted_text += char
        decrypted_texts.append(decrypted_text)
    return decrypted_texts