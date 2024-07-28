def revers(text: str) -> str:
    """
    Reverses the given text and prints the reversed result.

    Parameters:
    text (str): The string to be reversed.

    Returns:
    None: The function does not return any value. It prints the reversed text directly.

    Example:
        >>> revers("christopher")
        'rehpotsirhc'
    """
    reversed_text = text[::-1]
    print(f"└─[Output: {reversed_text}]")