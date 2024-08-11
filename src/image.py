import stepic
import sys
from PIL import Image

def image_encrypt(text, file):
    try:
        img = Image.open(file)
    except FileNotFoundError:
        print("└─[The image Not Found]")
        sys.exit()
    img_stegano = stepic.encode(img, text.encode())
    img_stegano.save("stegano.png")
    print("└─[The image stegano.png is saved]")

def image_decrypt(file):
    try:
        img = Image.open(file)
    except FileNotFoundError:
        print("└─[The image Not Found]")
        sys.exit()
    decoded = stepic.decode(img)
    print(f"└─[Text is: {str(decoded)}]")