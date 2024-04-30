import math

def scytale_encrypt(plaintext: str, diameter: int) -> str:
    """
    Encrypts a plaintext using the Scytale cipher.

    Args:
    plaintext (str): The plaintext to be encrypted.
    diameter (int): The diameter of the Scytale cylinder.

    Returns:
    str: The encrypted ciphertext.
    """
    chars = [c.lower() for c in plaintext if c not in (' ',',','.','?','!',':',';',"'")]
    chunks = math.ceil(len(chars) / float(diameter))
    inters, i, j = [], 1, 1
    while i <= chunks:
        inters.append(tuple(chars[j - 1:(j + diameter) - 1]))
        i += 1
        j += diameter
    cipher, k = [], 0
    while k < diameter:
        l = 0
        while l < chunks:
            if k >= len(inters[l]):
                cipher.append('|')
            else:
                cipher.append(inters[l][k])
            l += 1
        k += 1
    return ''.join(cipher)

def scytale_decrypt(ciphertext:str , diameter: int) -> str:
    """
    Decrypts a Scytale ciphertext.

    Args:
    ciphertext (str): The ciphertext to be decrypted.
    diameter (int): The diameter of the Scytale cylinder.

    Returns:
    str: The decrypted plaintext.
    """
    chars = [c for c in ciphertext]
    chunks = int(math.ceil(len(chars) / float(diameter)))
    inters, i, j = [], 1, 1
    while i <= diameter:
        inters.append(tuple(chars[j - 1:(j + chunks) -1]))
        i += 1
        j += chunks
    plain, k = [], 0
    while k < chunks:
        l = 0
        while l < len(inters):
            plain.append(inters[l][k])
            l += 1
        k += 1
    return ''.join(plain)