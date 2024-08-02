def rot13(text: str) -> str:
    """
    Encrypts & Decrypt the text using the ROT13 cipher.

    Parameters:
    text (str): The input string to be encrypted or decrypted.

    Returns:
    str: The encrypted or decrypted string with ROT13 applied.

    Examples:
        >>> rot13("christopher")
        'puevfgbcure'

        >>> rot13("puevfgbcure")
        'christopher'
    """
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 13) % 26 + base)
        else:
            result += char
    return result