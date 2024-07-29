def railfence_encrypt(plaintext: str, key: int) -> str:
    """
    Encrypt plaintext using the Rail Fence Cipher.
    
    Parameters:
    plaintext (str): The plaintext to be encrypted.
    rails (int): The number of rails (rows) in the rail fence.
    
    Returns:
    str: The encrypted ciphertext.

    Example:
        >>> railfence_encrypt("christopher", 5)
        'chhperorits'
    """
    rail = [['\n' for i in range(len(plaintext))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(plaintext)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = plaintext[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("".join(result))

def railfence_decrypt(ciphertext: str, key: int) -> str:
    """
    Decrypt ciphertext using the Rail Fence ciphertext.
    
    Parameters:
    ciphertext (str): The ciphertext to be decrypted.
    rails (int): The number of rails (rows) in the rail fence.
    
    Returns:
    str: The decrypted plaintext.

    Example:
        >>> railfence_decrypt("chhperorits", 5)
        'christopher'
    """
    rail = [['\n' for i in range(len(ciphertext))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '*') and (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))