def prepare_text(text: str) -> str:
    """
    Prepare the plaintext or ciphertext by removing non-alphabetic characters and converting to uppercase.
    
    Parameters:
    text (str): The plaintext or ciphertext to be prepared.
    
    Returns:
    str: The prepared text with non-alphabetic characters removed and converted to uppercase.
    """
    text = ''.join(filter(str.isalpha, text)).upper()
    return text

def generate_key_square(key: str) -> list:
    """
    Generate the key square for the Playfair Cipher.
    
    Parameters:
    key (str): The keyword used for generating the key square.
    
    Returns:
    list: A 5x5 matrix (list of lists) representing the key square.
    """
    alphabet = "abcdefghiklmnopqrstuvwxyz".upper()
    key = prepare_text(key)
    key = key.replace("J", "I")
    key_square = []
    for char in key:
        if char not in key_square and char in alphabet:
            key_square.append(char)
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    key_square = [key_square[i:i+5] for i in range(0, 25, 5)]
    return key_square

def find_position(matrix: list, char: str) -> tuple:
    """
    Find the position of a character in the key square matrix.
    
    Parameters:
    matrix (list): The key square matrix.
    char (str): The character to find.
    
    Returns:
    tuple: A tuple containing the row and column index of the character in the matrix.
    """
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypt plaintext using the Playfair Cipher.
    
    Parameters:
    plaintext (str): The plaintext to be encrypted.
    key (str): The keyword used for generating the key square.
    
    Returns:
    str: The encrypted ciphertext.

    Example:
        >>> playfair_encrypt("christopher", "key")
        'DCPMTPITDBSW'
    """
    key_square = generate_key_square(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        if len(pair) == 1:
            pair += 'X'
        row1, col1 = find_position(key_square, pair[0])
        row2, col2 = find_position(key_square, pair[1])
        if row1 == row2:
            ciphertext += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_square[row1][col2] + key_square[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypt ciphertext using the Playfair Cipher.
    
    Parameters:
    ciphertext (str): The ciphertext to be decrypted.
    key (str): The keyword used for generating the key square.
    
    Returns:
    str: The decrypted plaintext.

    Example:
        >>> playfair_decrypt("DCPMTPITDBSW", "key")
        'CHRISTOPHERX'
    """
    key_square = generate_key_square(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        row1, col1 = find_position(key_square, pair[0])
        row2, col2 = find_position(key_square, pair[1])
        if row1 == row2:
            plaintext += key_square[row1][(col1 - 1) % 5] + key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_square[(row1 - 1) % 5][col1] + key_square[(row2 - 1) % 5][col2]
        else:
            plaintext += key_square[row1][col2] + key_square[row2][col1]
    return plaintext

def generate_playfair_matrix(key: str) -> list:
    """
    Generates a Playfair cipher matrix based on the given key.

    Parameters:
        key (str): The keyword used to generate the matrix. It is converted to uppercase, and any 'J's are replaced with 'I'. Duplicate letters are removed.

    Returns:
        list of list of str: A 5x5 matrix represented as a list of lists, where each inner list contains 5 characters.

    Example:
        >>> generate_playfair_matrix("KEYWORD")
        [['K', 'E', 'Y', 'W', 'O'],
         ['R', 'D', 'A', 'B', 'C'],
         ['F', 'G', 'H', 'I', 'L'],
         ['M', 'N', 'P', 'Q', 'R'],
         ['S', 'T', 'U', 'V', 'X']]
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    key = "".join(dict.fromkeys(key))
    matrix = []
    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

def encrypt_playfair(plaintext: str, key: str) -> str:
    """
    Encrypts the given plaintext using the Playfair cipher.

    Parameters:
    plaintext (str): The text to be encrypted. All 'J's are replaced with 'I', and the plaintext is converted to uppercase. The text is processed in pairs of characters.
    key (str): The keyword used to generate the Playfair cipher matrix. It is converted to uppercase, and any 'J's are replaced with 'I'.

    Returns:
        str: The encrypted ciphertext. Characters are processed in pairs according to the Playfair cipher rules.

    Example:
        >>> playfair_encrypt("christopher", "key")
        'DCPMTPITDBSW'
    """
    plaintext = plaintext.upper().replace("J", "I")
    key = key.upper().replace("J", "I")
    matrix = generate_playfair_matrix(key)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        if char1 == char2:
            char2 = 'X'
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext