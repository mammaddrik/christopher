def polybius_square_encrypt(message: str) -> str:
    """
    Encrypts a message using the Polybius Square cipher.

    Parameters:
    message (str): The message to be encrypted.

    Returns:
    str: The encrypted message.

    Example:
        >>> polybius_square_encrypt("christopher")
        '1323422443443435231542'
    """
    polybius_grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    message = message.upper()
    encrypted_message = ""
    for char in message:
        if char == 'J':
            char = 'I'  # Replace 'J' with 'I'
        if char.isalpha():
            for row in range(len(polybius_grid)):
                if char in polybius_grid[row]:
                    col = polybius_grid[row].index(char)
                    encrypted_message += str(row + 1) + str(col + 1)
        else:
            encrypted_message += char
    return encrypted_message

def polybius_square_decrypt(message: str) -> str:
    """
    Decrypts a message encrypted using the Polybius Square cipher.

    Parameters:
    message (str): The encrypted message.

    Returns:
    str: The decrypted message.

    Example:
        >>> polybius_square_decrypt("1323422443443435231542")
        'christopher'
    """
    polybius_grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    decrypted_message = ""
    i = 0
    while i < len(message):
        if message[i].isdigit():
            row = int(message[i]) - 1
            col = int(message[i + 1]) - 1
            decrypted_message += polybius_grid[row][col]
            i += 2
        else:
            decrypted_message += message[i]
            i += 1
    return decrypted_message