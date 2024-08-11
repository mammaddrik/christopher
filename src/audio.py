import stepic
from eyed3 import load
from PIL import Image
import os

def audio_encrypt(text, audio, image):
    audio = load(audio)
    img = Image.open(image)
    img_stegano = stepic.encode(img, text.encode())
    img_stegano.save(image)
    audio.initTag()
    audio.tag.images.set(3, open(image, "rb").read(), "image/png")
    audio.tag.save()

def audio_decrypt(audio):
    audio = load(audio)
    img = open("temp_img.png", "wb")
    img.write(audio.tag.images[0].image_data)
    img.close()
    img= Image.open("temp_img.png")
    text = stepic.decode(img)
    if os.name == "nt":
        os.system("del temp_img.png")
    else:
        os.system("rm temp_img.png")
    print(f"└─[Text is: {text}]")