def letteronly(text: str)-> str:
    """
    Filters the input text to include only uppercase letters (A-Z), 
    excluding the letter 'J', which is replaced with 'I'.

    Parameters:
    text (str): The input string from which only uppercase letters will be retained.

    Returns:
    str: A new string consisting of only uppercase letters from the input, 
        with 'J' replaced by 'I'.
    """
    output = ''
    for char in text:
        if 64 < ord(char) < 91:
            if char == 'J':
                char = 'I'
            output += char
    return output

def massageKey(txt: str)-> str:
    """
    Processes the input text to create a unique key by retaining only 
    distinct uppercase letters (A-Z) and removing duplicates.

    Parameters:
    txt (str): The input string from which a unique key will be generated.

    Returns:
    str: A string consisting of distinct uppercase letters from the input, 
        with duplicates removed and 'J' replaced by 'I'.
    """
    user_key=letteronly(txt)
    key=''
    for char in user_key:
        if char not in key:
            key+=char
    return(key)

def massageMessage(txt: str)-> str:
    """
    Converts the input text into a string with digraphs (two-letter groups), 
    replacing consecutive duplicate letters with 'X'.

    This function filters the input text using the `letteronly` function to retain 
    only uppercase letters, replacing 'J' with 'I'. It then processes the text 
    by:
    - Adding the first character of each digraph to the result.
    - Inserting 'X' between consecutive duplicate letters.
    - Ensuring that every digraph is correctly placed without repeating or upsetting the sequence.

    Example:
    - "HELLO" becomes "HE LX LO"
    - "ALLOWS" becomes "AL LO W"

    Parameters:
    txt (str): The input string to be processed.

    Returns:
    str: A string where consecutive duplicate letters are replaced by 'X' and 
        the text is formatted into digraphs.
    """
    user_massage = letteronly(txt)
    massage = ''
    First = True
    for i in range(len(user_massage)):
        if First:
            massage += user_massage[i]
            if i + 1 == len(user_massage):
                massage += 'X'
            else:
                if user_massage[i] == user_massage[i+1]:
                    massage += 'X'
                else:
                    First = False
        else:
            massage += user_massage[i]
            First = True
    return massage

def showgrid(key: list)-> None:
    """
    Displays the Playfair cipher grid.

    Parameters:
    key (list or str): A sequence of 25 characters representing the Playfair 
                    cipher grid, which will be displayed in a 5x5 format.

    Returns:
    None
    """
    print('\nPlayfair Grid:')
    for j in range(5):
        for i in range(5):
            print(key[i+j*5], '', end='')
        print()
    print()
    return

def showmassage(massage: str)-> None:
    """
    Displays the input string formatted into digraphs.

    Parameters:
    massage (str): The input string to be formatted and displayed.

    Returns:
    None
    """
    space = True
    for char in massage:
        print(char, end='')
        space = not space
        if space:
            print(' ', end='')
    print()
    return

def playfair(enc: bool, massage: str, key: str)-> str:
    """
    Encrypts or decrypts a message using the Playfair cipher.

    This function applies the Playfair cipher to the input message based on 
    the provided key. It processes the message in digraphs (two-letter groups) 
    and performs encryption or decryption depending on the `enc` flag. 

    - If `enc` is True, the function performs encryption.
    - If `enc` is False, the function performs decryption.

    The function handles digraphs differently based on their positions in the 
    Playfair cipher grid. It adjusts the coordinates of the letters according 
    to Playfair cipher rules: same row, same column, or rectangle.

    Parameters:
    enc (bool): A flag indicating whether to encrypt (True) or decrypt (False).
    massage (str): The input string to be encrypted or decrypted, which should 
                be formatted into digraphs.
    key (str): A 25-character string representing the Playfair cipher grid.

    Returns:
    str: The resulting string after applying the Playfair cipher, either 
        encrypted or decrypted based on the `enc` flag.
    """
    offset =- 1
    if enc:
        offset =+ 1
    output = ''
    for i in range(0,len(massage),2):
        lett1 = massage[i]
        lett2 = massage[i+1]
        pos1 = key.find(lett1)
        pos2 = key.find(lett2)
        coord1 = [pos1 % 5, pos1 // 5]
        coord2 = [pos2 % 5, pos2 // 5]
        if coord1[0] == coord2[0]:
            coord1[1] = (coord1[1] + offset) % 5
            coord2[1] = (coord2[1] + offset) % 5
        elif coord1[1] == coord2[1]:
            coord1[0] = (coord1[0] + offset) % 5
            coord2[0] = (coord2[0] + offset) % 5
        else:
            tmp = coord2[0]
            coord2[0] = coord1[0]
            coord1[0] = tmp
        pos1 = coord1[0] + 5 * coord1[1]
        pos2 = coord2[0] + 5 * coord2[1]
        lett1 = key[pos1]
        lett2 = key[pos2]
        output += lett1
        output += lett2
    return output

def showres(massage1: str, massage2: str)-> None:
    """
    Displays two messages side by side, with each message split into lines of 
    a specified length.

    Parameters:
    massage1 (str): The first message to be displayed.
    massage2 (str): The second message to be displayed.

    Returns:
    None
    """
    linesize = 50
    for i in range(0, len(massage1), linesize):
        showmassage(massage1[i:i+min(linesize,len(massage1)-i)])
        showmassage(massage2[i:i+min(linesize,len(massage2)-i)])
        print()
    return