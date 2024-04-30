from lib.slowprint import slowprint
from lib.color import Color

translate_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                  'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
                  '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                  ',': '--..--', ':': '---...', ';': '-.-.-.', '.': '.-.-.-',
                  '"': '.-..-.', '(': '-----.', ')': '.-----', "'": '-.--.-',
                  '@': '.--.-.', '?': '..--..', '!': '-.-.--', "/": '-..-.',
                  '&': '.-...', '?': '..--..', '=': '-...-', "+": '.-.-.',
                  '-': '-...-', '_': '..--.-', '$': '...-..-', "F": '.-.-.',
                  ' ': '-.-.-.-'}

def morse(message: any) -> str:
    """
    Encode text into Morse code.
    
    Args:
    message (any): The message to be encoded.
    
    Returns:
    str: The Morse code representation of the input text.
    """
    try:
        message = " ".join(translate_dict[c] for c in message.upper())
        print(f"└─[Output: {message}]")
    except KeyError:
        slowprint("└─["+Color.BRed+"Invalid character detected"+Color.End+"]")

def morsetext(text: str)-> str:
    """
    Decode Morse code into text.
    
    Args:
    text (str): The Morse code to be decoded.
    
    Returns:
    str: The decoded text.
    """
    try:
        reverse_dict = {v: k for k, v in translate_dict.items()}
        reverse_message = "".join(reverse_dict[c] for c in text.split(" "))
        print(f"└─[Output: {reverse_message.lower()}]")
    except KeyError:
        slowprint("└─["+Color.BRed+"Invalid character detected"+Color.End+"]")