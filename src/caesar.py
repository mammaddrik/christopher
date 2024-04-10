def caesar_cipher_encrypt(text: any, shift: int) -> str:
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
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_brute_force_decrypt(ciphertext: any) -> str:
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
                if char.isupper():
                    decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decrypted_text += char
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

# Example usage:
ciphertext = "lm qc reqi mw qsleqqeh"
decrypted_texts = caesar_brute_force_decrypt(ciphertext)
print("Brute Force Decryption:")
for i, text in enumerate(decrypted_texts):
    print(f"Shift {i+1}: {text}")