def atbash(message: any) -> str:
    """
    Encrypts the given message using the Atbash cipher method.

    Parameters:
    message (str): The plaintext to be encrypted.

    Returns:
    str: The encrypted ciphertext.
    """
    lookup_table = {'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'}
    cipher = ''
    for letter in message:
        if(letter != ' '):
            try:
                cipher += lookup_table[letter]
            except KeyError:
                cipher += letter
        else:
            cipher += ' '
    return cipher