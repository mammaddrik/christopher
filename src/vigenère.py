def vigenère_encrypt(plain_text, key):
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