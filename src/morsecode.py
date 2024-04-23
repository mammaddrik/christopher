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

def morse(message):
    try:
        message = " ".join(translate_dict[c] for c in message.upper())
        print(f"└─[Output: {message}]")
    except KeyError:
        slowprint("└─["+Color.BRed+"Invalid character detected"+Color.End+"]")

def morsetext(text):
    try:
        reverse_dict = {v: k for k, v in translate_dict.items()}
        reverse_message = "".join(reverse_dict[c] for c in text.split(" "))
        print(f"└─[Output: {reverse_message.lower()}]")
    except KeyError:
        slowprint("└─["+Color.BRed+"Invalid character detected"+Color.End+"]")