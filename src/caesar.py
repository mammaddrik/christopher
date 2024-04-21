def caesar_cipher_encryption(text: any, shift: int) -> str:
    """
    Encrypts the given text using the Caesar Cipher with the specified shift.

    Parameters:
    text (str): The plaintext to be encrypted.
    shift (int): The shift value to use for encryption.

    Returns:
    str: The encrypted ciphertext.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_brute_force(ciphertext: any) -> str:
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