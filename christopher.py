#!/usr/bin/env python
#
#    \ \  16  21  05  22  06  07  02  03  21  18  05  / /
#     \ \ Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee / /
#      \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
#       \      abcd efgh ijkl m-n opqr stuv wxyz     /
#        \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
#        /Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr\
#        \__________________________________________/
#              Tool for Encryption & Decryption
#                     Github: mammaddrik

#::::: Library :::::
from lib.banner import Banner
from lib.color import Color, color_banner
from lib.clearscr import clearScr
from lib.slowprint import slowprint

#::::: Detect :::::
from detect.detectenglish import isEnglish

#::::: Src :::::
from src.atbash import atbash
from src.caesar import caesar_encryption, caesar_decryption, caesar_crack
from src.affine import affine_encryption, affine_decryption, affine_crack, extended_gcd
from src.vigenère import vigenère_encrypt, vigenère_decrypt
from src.revers import revers
from src.playfair import playfair_encrypt, playfair_decrypt
from src.railfence import railfence_encrypt, railfence_decrypt
from src.scytale import scytale_encrypt, scytale_decrypt
from src.polybiussquare import polybius_square_encrypt, polybius_square_decrypt
from src.columnar import columnar_encrypt, columnar_decrypt
from src.simplesubstitution import simple_substitution_encrypt, simple_substitution_decrypt, generateKey, crack
from src.makewordpatterns import getWordPattern
from src.baconian import baconian_encryption, baconian_decryption
from src.morsecode import morse, morsetext
from src.rot13 import rot13
from src.hashgenerator import hashgenerator
from src.hashid import hashid
from src.keyboard import Keyboard
from src.plugboard import Plugboard
from src.rotor import Rotor
from src.reflector import Reflector
from src.enigma import Enigma
from src.aes import aes_encrypt, aes_decrypt, generate_key
from src.keygenerator import generateKeys, writeKeysToFile
from src.publickeycipher import publickey_encrypt, publickey_decrypt, readKeysFromFile
from src.image import image_encrypt, image_decrypt
from src.audio import audio_encrypt, audio_decrypt

#::::: Tools :::::
from src.wordlist import wordlist
from src.customwordlist import interactive
from src.passwordgenerator import passwordgenerate
from src.passwordmanager import get_master_password, encrypt, decrypt, create_csv, add, edit, delete
from src.frequencyanalysis import getFrequencyOrder, getFrequencyScore

#::::: Default Library :::::
import os
import sys
import time
import hashlib
import string
import re
import secrets
from datetime import datetime
from itertools import product
from hmac import compare_digest

#::::: Libraries to be installed :::::
try:
    import pandas as pd
    import rsa
    from pwinput import pwinput
except ImportError:
    os.system("pip install -r requirements.txt")

#::::: Again :::::
def again():
    "A Function To Ask The User To Restart The Program."
    christopher_again = input(Color.BCyan+"\nDo You Want To Continue?"+Color.End+"\n┌───(christopher)─[~/again]─[Y/n]\n└─"+color_banner[0]+"$ "+Color.End)
    if (christopher_again.upper() == "Y" or christopher_again == ""):
        clearScr()
        time.sleep(0.4)
        christopher()
    elif (christopher_again.upper() == "N"):
        print("\n\tGoodbye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()
    else:
        clearScr()
        christopher()

#::::: Keep :::::
def keep():
    "A Function To Ask The User To Decrypt with different keys."
    christopher_keep = input(Color.BCyan+"\nDo You Want To try more keys?"+Color.End+"\n┌───(christopher)─[~/continue]─[Y/n]\n└─"+color_banner[0]+"$ "+Color.End)
    if (christopher_keep.upper() == "Y" or christopher_keep == ""):
        pass
    elif (christopher_keep.upper() == "N"):
        again()
    else:
        again()

#::::: Christopher :::::
def christopher():
    "The function of christoper."
    clearScr()
    time.sleep(0.4)
    print(Banner.christopher_banner)
    choice = input("\n┌───(christopher)─[~/christopher]─[99]Exit\n└─"+color_banner[0]+"$ "+Color.End)

    #::::: Cryptography :::::
    if (choice == "1" or choice == "01"):
        clearScr()
        time.sleep(0.4)
        print(Banner.cipher_banner)
        select = input("\n┌───(christopher)─[~/christopher/Cryptography]─[99]Back to Main Menu\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Atbash Cipher :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[~/christopher/Cryptography/Atbash Cipher]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(message) == 0:
                slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                again()
            elif message.isdigit():
                slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
                again()
            else:
                print(f"└─[Output: {atbash(message)}]")
                again()

        #::::: Caesar Cipher :::::
        elif (select == "2" or select == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Crack            [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Caesar Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Caesar Cipher/Encryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                elif plaintext.isdigit():
                    slowprint("└─["+Color.BRed+"plaintext cannot be only number"+Color.End+"]")
                    again()
                try:
                    shift = int(input("├─[Enter your shift number]"+color_banner[1]+"$ "+Color.End))
                    if shift >= 1 and shift <= 25:
                        print(f"└─[Output: {caesar_encryption(plaintext, shift)}]")
                        again()
                    else:
                        slowprint("├─["+Color.BRed+"Shift value must be a number Between 1 and 25 (Default: 3)"+Color.End+"]")
                        shift = 3
                        print(f"└─[Output: {caesar_encryption(plaintext, shift)}]")
                        again()
                except ValueError:
                    slowprint("├─["+Color.BRed+"Shift value must be a number (Default: 3)"+Color.End+"]")
                    shift = 3
                    print(f"└─[Output: {caesar_encryption(plaintext, shift)}]")
                    again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Caesar Cipher/Decryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                try:
                    shift = int(input("├─[Enter your shift number]"+color_banner[1]+"$ "+Color.End))
                    if shift >= 1 and shift <= 25:
                        print(f"└─[Output: {caesar_decryption(ciphertext, shift)}]")
                        again()
                    else:
                        slowprint("├─["+Color.BRed+"Shift value must be a number Between 1 and 25 (Default: 3)"+Color.End+"]")
                        shift = 3
                        print(f"└─[Output: {caesar_decryption(ciphertext, shift)}]")
                        again()
                except ValueError:
                    slowprint("├─["+Color.BRed+"Shift value must be a number (Default: 3)"+Color.End+"]")
                    shift = 3
                    print(f"└─[Output: {caesar_decryption(ciphertext, shift)}]")
                    again()

            #::::: Crack :::::
            elif(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Caesar Cipher/Crack]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                decrypted_texts = caesar_crack(ciphertext)
                for i, text in enumerate(decrypted_texts):
                    if isEnglish(text):
                        print("├─[Shift: "+Color.BGreen+f"{i+1}"+Color.End+f"]\n└─[The plaintext may be this: {text}]")
                again()

            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Affine Cipher :::::
        elif (select == "3" or select == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Crack            [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Affine Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Affine Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                elif plaintext.isdigit():
                    slowprint("└─["+Color.BRed+"Plaintext cannot be only number"+Color.End+"]")
                    again()
                try:
                    slope = int(input("├─[Enter your slope(a) number (The number must be odd)]"+color_banner[1]+"$ "+Color.End))
                    if slope % 2 == 0:
                        slowprint("└─["+Color.BRed+"Slope(a) value must be a number Between 1 and 25 (The number must be odd)"+Color.End+"]")
                        again()
                    intercept = int(input("├─[Enter your intercept(b) number]"+color_banner[1]+"$ "+Color.End))
                    if (slope >= 1 and slope <= 25):
                        print(f"└─[Output: {affine_encryption(plaintext, slope, intercept)}]")
                        again()
                    else:
                        slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number Between 1 and 25"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number (Slope(a) number must be odd)"+Color.End+"]")
                    again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Affine Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                try:
                    slope = int(input("├─[Enter your slope(a) number (The number must be odd)]"+color_banner[1]+"$ "+Color.End))
                    if slope % 2 == 0:
                        slowprint("└─["+Color.BRed+"Slope(a) value must be a number Between 1 and 25 (The number must be odd)"+Color.End+"]")
                        again()
                    intercept = int(input("├─[Enter your intercept(b) number]"+color_banner[1]+"$ "+Color.End))
                    if (slope >= 1 and slope <= 25):
                        print(f"└─[Output: {affine_decryption(ciphertext, slope, intercept)}]")
                        again()
                    else:
                        slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number Between 1 and 25"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number (Slope(a) number must be odd)"+Color.End+"]")
                    again()
            #::::: Crack :::::
            elif(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Affine Cipher/Crack]\n└─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                alphabet = string.ascii_lowercase
                m = len(alphabet)
                for a in range(1, m):
                    if extended_gcd(a, m)[0] == 1:
                        for b in range(0, m):
                            decrypted_text = affine_crack(ciphertext, a, b)
                            if isEnglish(decrypted_text):
                                print("┌─[Slope(a) = "+Color.BGreen+f"{a} "+Color.End+"Intercept(b) = "+Color.BGreen+f"{b}"+Color.End+f"]\n└─[The plaintext may be this: {decrypted_text}]")
                                keep()
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Vigenère Cipher :::::
        elif (select == "4" or select == "04"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Crack            [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Vigenère Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Vigenère Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if key.isdigit():
                    slowprint("└─["+Color.BRed+"Key cannot be number"+Color.End+"]")
                    again()
                elif len(key) == 0:
                    slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                    again()
                key = re.sub(r'\d+', '', key)
                ciphertext = vigenère_encrypt(plaintext, key)
                print(f"└─[Ciphertext: {ciphertext}]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Vigenère Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).lower().strip()
                plaintext = vigenère_decrypt(ciphertext, key)
                print(f"└─[Plaintext: {plaintext.lower()}]")
                again()

            #::::: Crack :::::
            elif(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Vigenère Cipher/Crack]\n└─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                character = string.ascii_lowercase
                for i in range(1, 1000):
                    for j in product(character, repeat=i):
                        key = "".join(j)
                        key = re.sub(r'\d+', '', key)
                        print(f"├─[Key: {key}]", end='\r')
                        plaintext = vigenère_decrypt(ciphertext, key).upper()
                        if isEnglish(plaintext):
                            print(f"┌─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                            print(f"└─[The plaintext may be this: {plaintext.lower()}]")
                            keep()
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Revers Text :::::
        elif (select == "5" or select == "05"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                message = input("\n┌───(christopher)─[~/christopher/Cryptography/Revers Text]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(message) == 0:
                    slowprint("└─["+Color.BRed+"message cannot be empty"+Color.End+"]")
                    again()
                revers(message)
                again()

        #::::: Playfair Cipher :::::
        elif (select == "6" or select == "06"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Playfair Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End)
                if key.isdigit():
                    slowprint("└─["+Color.BRed+"Key cannot be number"+Color.End+"]")
                    again()
                elif len(key) == 0:
                    slowprint("└─["+Color.BRed+"Key cannot be empty"+Color.End+"]")
                    again()
                ciphertext = playfair_encrypt(plaintext, key)
                print(f"└─[Ciphertext: {ciphertext}]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Playfair Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).strip()
                if key.isdigit():
                    slowprint("└─["+Color.BRed+"Key cannot be number"+Color.End+"]")
                    again()
                elif len(key) == 0:
                    slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                    again()
                plaintext = playfair_decrypt(ciphertext, key)
                print(f"└─[Plaintext: {plaintext}]")
                again()

            #::::: Back to Main Menu :::::
            elif(pick == "99"):
                christopher()
            else:
                again()

        #::::: Rail Fence Cipher :::::
        elif (select == "7" or select == "07"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Crack            [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Rail Fence Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                try:
                    key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                    if key >= 2 and key <= len(plaintext):
                        ciphertext = railfence_encrypt(plaintext, key)
                        print(f"└─[Ciphertext: {ciphertext}]")
                        again()
                    else:
                        slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(plaintext)}"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                    again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Rail Fence Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                try:
                    key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                    if key >= 2 and key <= len(ciphertext):
                        plaintext = railfence_decrypt(ciphertext, key)
                        print(f"└─[Plaintext: {plaintext}]")
                        again()
                    else:
                        slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(plaintext)}"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                    again()

            #::::: Crack :::::
            elif(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Rail Fence Cipher/Crack]\n└─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                for i in range(2, len(ciphertext)):
                    key = i
                    plaintext = railfence_decrypt(ciphertext, key).upper()
                    if isEnglish(plaintext):
                        print(f"┌─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                        print(f"└─[Plaintext: {plaintext.lower()}]")
                        keep()
                again()

            #::::: Back to Main Menu :::::
            elif(pick == "99"):
                christopher()
            else:
                again()

        #::::: Scytale Cipher :::::
        elif (select == "8" or select == "08"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Scytale Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                try:
                    diameter = int(input("├─[Enter the diameter number]"+color_banner[1]+"$ "+Color.End))
                    ciphertext = scytale_encrypt(plaintext, diameter)
                    print(f"└─[Ciphertext: {ciphertext}]")
                    again()
                except ValueError:
                    slowprint("├─["+Color.BRed+"diameter value must be a number"+Color.End+"]")
                    again()

            #::::: Decryption :::::
            if(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Scytale Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                try:
                    diameter = int(input("├─[Enter the diameter number]"+color_banner[1]+"$ "+Color.End))
                    plaintext = scytale_decrypt(ciphertext, diameter)
                    print(f"└─[Ciphertext: {plaintext}]")
                    again()
                except ValueError:
                    slowprint("├─["+Color.BRed+"diameter value must be a number"+Color.End+"]")
                    again()

            #::::: Back to Main Menu :::::
            elif(pick == "99"):
                christopher()
            else:
                again()

        #::::: Polybius Square Cipher :::::
        elif (select == "9" or select == "09"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Polybius Square Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Polybius Square Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                elif plaintext.isdigit():
                    slowprint("└─["+Color.BRed+"plaintext cannot be only number"+Color.End+"]")
                    again()
                ciphertext = polybius_square_encrypt(plaintext)
                print(f"└─[Ciphertext: {ciphertext}]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Polybius Square Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                ciphertext = ciphertext.replace(' ', '')
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit() == False:
                    slowprint("└─["+Color.BRed+"Ciphertext must be only number"+Color.End+"]")
                    again()
                plaintext = polybius_square_decrypt(ciphertext)
                print(f"└─[Plaintext: {plaintext.lower()}]")
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Columnar Cipher :::::
        elif (select == "10"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Crack            [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Columnar Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Columnar Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                try:
                    key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                    if key >= 2 and key <= len(plaintext):
                        ciphertext = columnar_encrypt(plaintext, key)
                        print(f"└─[Ciphertext: {ciphertext}]")
                        again()
                    else:
                        slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(plaintext)}"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                    again()
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Columnar Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                try:
                    key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                    if key >= 2 and key <= len(ciphertext):
                        plaintext = columnar_decrypt(ciphertext, key)
                        print(f"└─[Ciphertext: {plaintext}]")
                        again()
                    else:
                        slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(ciphertext)}"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                    again()

            #::::: Crack :::::
            elif(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Columnar Cipher/Crack]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                for key in range(1, len(ciphertext)):
                    plaintext = columnar_decrypt(ciphertext, key).upper()
                    if isEnglish(plaintext):
                        print(f"├─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                        print(f"└─[Plaintext: {plaintext.lower()}]")
                        keep()
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Simple Substitution  Cipher :::::
        elif (select == "11"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Crack            [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Simple Substitution Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Simple Substitution Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                elif plaintext.isdigit():
                    slowprint("└─["+Color.BRed+"Plaintext cannot be only number"+Color.End+"]")
                    again()
                key = generateKey()
                print(f"├─[key: {key}]")
                print(f"└─[Ciphertext: {simple_substitution_encrypt(plaintext, key)}]")
                again()

            #::::: Decryption :::::
            if(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Simple Substitution Cipher/Decryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                key = input(f"├─[Enter your Key]"+color_banner[1]+"$ "+Color.End).strip()
                contains_number = any(char.isdigit() for char in key)
                if contains_number:
                    slowprint("└─["+Color.BRed+"The key must be 26 characters without numbers"+Color.End+"]")
                    again()
                if len(key) == 26:
                    print(f"└─[Plaintext: {simple_substitution_decrypt(ciphertext, key)}]")
                    again()
                else:
                    slowprint("└─["+Color.BRed+"The key must be 26 characters without numbers"+Color.End+"]")
                    again()

            #::::: Crack :::::
            if(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/Simple Substitution Cipher/Crack]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                patterns = input("├─[Do you have a Word Pattern file]─[Y/n]"+color_banner[1]+"$ "+Color.End).strip()
                if (patterns.upper() == "Y" or patterns == ""):
                    crack(ciphertext)
                    again()
                elif (patterns.upper() == "N"):
                    wordPatterns = {}
                    file = input("├─[Enter the file]"+color_banner[1]+"$ "+Color.End).strip()
                    try:
                        with open(file, "r") as f:
                            filesize = os.path.getsize((pwfile))
                            if filesize == 0:
                                slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                                again()
                    except FileNotFoundError:
                        slowprint("└─["+Color.BRed+"File Not Found"+Color.End+"]")
                        again()
                    path = os.getcwd()
                    if os.name == "nt":
                        with open(file, "r") as f:
                            for word in f:
                                word = word.strip()
                                pattern = getWordPattern(word)
                                if pattern in wordPatterns:
                                    wordPatterns[pattern].append(word)
                                else:
                                    wordPatterns[pattern] = [word]
                            with open(path+"/src/wordpatterns.py", "w") as f:
                                f.write(f"wordPatterns = {wordPatterns}")
                    else:
                        try:
                            with open(path+"/src/wordpatterns.py", "w") as f:
                                f.write(f"wordPatterns = {wordPatterns}")
                        except FileNotFoundError:
                            dictionaryFile = open(path+'/src/wordpatterns.py')
                    crack(ciphertext)
                    again()
                else:
                    again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Baconian Cipher :::::
        elif (select == "12"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[~/christopher/Cryptography/Baconian Cipher]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper().strip()
            if len(message) == 0:
                slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                again()
            elif message.isdigit():
                slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
                again()
            elif re.fullmatch(r'[AB]*', message):
                chunk_size = 5
                print(f"└─[Plaintext: ", end='')
                for i in range(0, len(message), chunk_size):
                    decoded = baconian_decryption(message[i:i + chunk_size])
                    print(f"{decoded.lower()}",end='')
                print("]")
                again()
            else:
                print(f"└─[Ciphertext: {baconian_encryption(message)}]")
                again()

        #::::: Morse Code :::::
        elif (select == "13"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[~/christopher/Cryptography/Morse Code]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper()
            if len(message) == 0:
                slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                again()
            elif message.isdigit():
                slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
                again()
            characters = {'-', '.', ' '}
            pick = all(char in characters for char in message)
            if pick:
                morsetext(message)
                again()
            else:
                morse(message)
                again()

        #::::: Rot13 Cipher :::::
        elif (select == "14"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[~/christopher/Cryptography/Rot13]\n├─[Enter your text]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(message) == 0:
                slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                again()
            elif message.isdigit():
                slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
                again()
            else:
                print(f"└─[Output: {rot13(message)}]")
                again()

        # One-Time Pad Cipher
        elif (select == "15"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/One-Time Pad Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/One-Time Pad Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                SYMBOLS = string.ascii_letters
                key = ""
                for i in range(len(plaintext)):
                    key += secrets.choice(SYMBOLS)
                print(f"├─[Key: {key}]")
                ciphertext = vigenère_encrypt(plaintext, key)
                print(f"└─[Ciphertext: {ciphertext}]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/One-Time Pad Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).lower().strip()
                plaintext = vigenère_decrypt(ciphertext, key)
                print(f"└─[Plaintext: {plaintext.lower()}]")
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Hash Function :::::
        elif (select == "16"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("   [01]Hash Generator    [02]Hash Cracker\n   [03]Hash Identifier   [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Hash Function]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Hash Generator :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                password = input("\n┌───(christopher)─[~/christopher/Cryptography/Hash Function/Hash Generator]\n├─[Enter the password]"+color_banner[1]+"$ "+Color.End).strip()
                if len(password) == 0:
                    slowprint("└─["+Color.BRed+"Password cannot be empty"+Color.End+"]")
                    again()
                hashvalue = input("├───────────────┬───────────────┬───────────────┐\n├─[01]MD2       ├─[2]MD4        ├─[03]MD5       │\n├─[04]SHA1      ├─[05]SHA224    ├─[06]SHA256    │\n├─[07]SHA384    ├─[08]SHA512    ├─[09]sha3-224  │\n├─[10]sha3-256  ├─[11]sha3-384  ├─[12]sha3-512  │\n├─[13]shake-128 ├─[14]shake-256 ├─[15]blake2b   │\n├─[16]blake2s   ├─[17]NTLM      ├─[18]adler32   │\n├─[19]crc32     ├─[20]all       ├─[21]Back      │\n├───────────────┴───────────────┴───────────────┘\n└─[Select the function]"+color_banner[1]+"$ "+Color.End)
                if len(hashvalue) == 0:
                    slowprint("└─["+Color.BRed+"Hashvalue cannot be empty"+Color.End+"]")
                    again()
                if (hashvalue == "1" or hashvalue == "01"):
                    hashvalue = "md2"
                elif (hashvalue == "2" or hashvalue == "02"):
                    hashvalue = "md4"
                elif (hashvalue == "3" or hashvalue == "03"):
                    hashvalue = "md5"
                elif (hashvalue == "4" or hashvalue == "04"):
                    hashvalue = 'sha1'
                elif (hashvalue == "5" or hashvalue == "05"):
                    hashvalue = 'sha224'
                elif (hashvalue == "6" or hashvalue == "06"):
                    hashvalue = 'sha256'
                elif (hashvalue == "7" or hashvalue == "07"):
                    hashvalue = 'sha384'
                elif (hashvalue == "8" or hashvalue == "08"):
                    hashvalue = 'sha512'
                elif (hashvalue == "9" or hashvalue == "09"):
                    hashvalue = 'sha3_224'
                elif (hashvalue == "10"):
                    hashvalue = 'sha3_256'
                elif (hashvalue == "11"):
                    hashvalue = 'sha3_384'
                elif (hashvalue == "12"):
                    hashvalue = 'sha3_512'
                elif (hashvalue == "13"):
                    hashvalue = 'shake_128'
                elif (hashvalue == "14"):
                    hashvalue = 'shake_256'
                elif (hashvalue == "15"):
                    hashvalue = 'blake2b'
                elif (hashvalue == "16"):
                    hashvalue = 'blake2s'
                elif (hashvalue == "17"):
                    hashvalue = 'NTLM'
                elif (hashvalue == "18"):
                    hashvalue = 'adler32'
                elif (hashvalue == "19"):
                    hashvalue = 'crc32'
                elif (hashvalue == "20"):
                    hashvalue = 'all'
                elif (hashvalue == "21"):
                    christopher()
                else:
                    slowprint("└─["+Color.BRed+"Enter the Available Function"+Color.End+"]")
                    again()
                hashgenerator(password, hashvalue)
                again()

            #::::: Hash Cracker :::::
            elif (pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                Hash = input("\n┌───(christopher)─[~/christopher/Cryptography/Hash Function/Hash Cracker]\n├─[Enter the hash]"+color_banner[1]+"$ "+Color.End).strip()
                if len(Hash) == 32:
                    hashvalue = "md5"
                elif len(Hash) == 40:
                    hashvalue = "sha1"
                elif len(Hash) == 64:
                    hashvalue = "sha256"
                elif len(Hash) == 96:
                    hashvalue = "sha384"
                elif len(Hash) == 128:
                    hashvalue = "sha512"
                else:
                    slowprint("└─["+Color.BRed+"Hash Function: Unknown"+Color.End+"]")
                    again()
                pick = input("├─[Do you have a passwordlist]─[Y/n]"+color_banner[1]+"$ "+Color.End)
                if (pick.upper() == "Y" or pick == ""):
                    pwfile = input("├─[Enter the password file name]"+color_banner[1]+"$ "+Color.End)
                    try:
                        with open(pwfile, "r") as f:
                            filesize = os.path.getsize((pwfile))
                            if filesize == 0:
                                slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                                again()
                        with open(pwfile, "r") as f:
                            counter = 1
                            t1 = datetime.now()
                            for password in f:
                                h = hashlib.new(hashvalue)
                                setpass = bytes(password.strip(), "utf-8")
                                h.update(setpass)
                                hashedguess = h.hexdigest()
                                counter += 1
                                print(f"├─[Password number {counter}: {password.strip()}]")
                                if compare_digest(Hash, hashedguess):
                                    t2 = datetime.now()
                                    t3 = t2 - t1
                                    print(f"├─[Finishing Time: {t3}]")
                                    print("└─[Password: "+Color.BGreen+f"{password.strip()}"+Color.End+"]")
                                    again()
                            else:
                                slowprint("└─["+Color.BRed+"Password Not Found"+Color.End+"]")
                                again()
                    except FileNotFoundError:
                        slowprint("└─["+Color.BRed+"File Not Found"+Color.End+"]")
                        again()
                    except OSError:
                        slowprint("└─["+Color.BRed+"File Not Found Check the filename"+Color.End+"]")
                        again()
                elif (pick.upper() == "N"):
                    counter = 0
                    character = string.ascii_letters+string.digits+string.punctuation
                    t1 = datetime.now()
                    for i in range(1, 1000):
                        for j in product(character, repeat=i):
                            word = "".join(j)
                            h = hashlib.new(hashvalue)
                            setpass = bytes(word.strip(), "utf-8")
                            h.update(setpass)
                            hashedguess = h.hexdigest()
                            counter += 1
                            print(f"├─[Password number {counter}: {word.strip()}]", end='\r')
                            if compare_digest(Hash, hashedguess):
                                t2 = datetime.now()
                                t3 = t2 - t1
                                print(f"├─[Password number {counter}: {word.strip()}]")
                                print(f"├─[Finishing Time: {t3}]")
                                print("└─[Password: "+Color.BGreen+f"{word}"+Color.End+"]")
                                again()
                    else:
                        slowprint("└─["+Color.BRed+"Password Not Found"+Color.End+"]")
                        again()
                else:
                    clearScr()
                    christopher()

            #::::: Hash Identifier :::::
            elif (pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                h = input("\n┌───(christopher)─[~/christopher/Cryptography/Hash Function/Hash Identifier]\n├─[Enter your Hash]"+color_banner[1]+"$ "+Color.End)
                hashid(h)
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Enigma Machine :::::
        elif (select == "17"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
            II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
            III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
            IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
            V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
            A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
            B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
            C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
            KB = Keyboard()
            PB = Plugboard(["AB", "CD", "EF"])
            ENIGMA = Enigma(A, I, II, III, PB, KB)
            ENIGMA.set_rings((1,1,1))
            message = input("\n┌───(christopher)─[~/christopher/Cryptography/Enigma Machine]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper().strip()
            if len(message) == 0:
                slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                again()
            elif message.isdigit():
                slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
                again()
            message = ''.join(c for c in message if c.isalpha() or c.isspace())
            key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).upper().strip()
            if len(key) == 0:
                slowprint("└─["+Color.BRed+"Key cannot be empty"+Color.End+"]")
                again()
            elif key.isdigit():
                slowprint("└─["+Color.BRed+"Key cannot be only number"+Color.End+"]")
                again()
            key = ''.join(c for c in key if c.isalpha() or c.isspace())
            if len(key) == 3:
                ENIGMA.set_key(key)
                ciphertext = ""
                for letter in message:
                    ciphertext = ciphertext + ENIGMA.encipher(letter)
                print(f"└─[Output: {ciphertext}]")
                again()
            else:
                slowprint("└─["+Color.BRed+"The key must be exactly three characters long."+Color.End+"]")
                again()

        #::::: AES(CBC) :::::
        elif (select == "18"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/AES(CBC)]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/AES(CBC)/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                key_length = int(input("├─[Enter key length (16, 24, or 32 bytes)]"+color_banner[1]+"$ "+Color.End).strip())
                if key_length not in [16, 24, 32]:
                    slowprint("└─["+Color.BRed+"Key length must be 16, 24, or 32 bytes long"+Color.End+"]")
                    again()
                key = generate_key(key_length)
                print(f"├─[Key (hex): {key.hex()}]")
                iv, ciphertext = aes_encrypt(plaintext, key)
                print(f"├─[Initialization Vector: {iv}]")
                print(f"└─[Ciphertext: {ciphertext}]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Cryptography/AES(CBC)/Decryption]\n├─[Enter the base64 encoded ciphertext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                if len(ciphertext) % 4 != 0:
                    slowprint("└─["+Color.BRed+"The ciphertext is not Base64 encoded"+Color.End+"]")
                    again()
                iv = input("├─[Enter the Initialization Vector]"+color_banner[1]+"$ "+Color.End).strip()
                if len(iv) == 0:
                    slowprint("└─["+Color.BRed+"Initialization Vector cannot be empty"+Color.End+"]")
                    again()
                key_hex = input("├─[Enter the key as a hexadecimal]"+color_banner[1]+"$ "+Color.End).strip()
                if len(key_hex) == 0:
                    slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                    again()
                try:
                    key = bytes.fromhex(key_hex)
                except ValueError:
                    slowprint("└─["+Color.BRed+"non-hexadecimal number found"+Color.End+"]")
                    again()
                if len(key) not in [16, 24, 32]:
                    slowprint("└─["+Color.BRed+"Key length must be 16, 24, or 32 bytes long"+Color.End+"]")
                    again()
                plaintext = aes_decrypt(iv, ciphertext, key)
                print(f"└─[Plaintext: {plaintext}]")
                again()

        #::::: Public Key Cipher :::::
        elif (select == "19"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Key Generator    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Public Key Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/Public Key Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                keyfile = input("├─[Enter the key file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(keyfile) == 0:
                    slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                    again()
                outputfile = input("├─[Enter the output file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(outputfile) == 0:
                    slowprint("└─["+Color.BRed+"output file be empty"+Color.End+"]")
                    again()
                public, private = readKeysFromFile(keyfile)
                publickey_encrypt(plaintext,public,outputfile)
                print(f"└─[The ciphertext was saved in file {outputfile}]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                encrypted_file = input("\n┌───(christopher)─[~/christopher/Cryptography/Public Key Cipher/Decryption]\n├─[Enter your Encrypted file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(encrypted_file) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                keyfile = input("├─[Enter the key file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(keyfile) == 0:
                    slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                    again()
                public, private = readKeysFromFile(keyfile)
                print(f"└─[Plaintext: {publickey_decrypt(encrypted_file, private)}]")
                again()

            #::::: Key Generator :::::
            elif(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                try:
                    keysize = int(input("\n┌───(christopher)─[~/christopher/Cryptography/Public Key Cipher/Key Generator]\n├─[Enter the key size]"+color_banner[1]+"$ "+Color.End))
                    if keysize <= 1:
                        slowprint("└─["+Color.BRed+"The key size value must be greater than 1"+Color.End+"]")
                        again()
                    filename = input("├─[Enter the name of the file]"+color_banner[1]+"$ "+Color.End).strip()
                    if len(filename) == 0:
                        slowprint("└─["+Color.BRed+"File name cannot be empty"+Color.End+"]")
                        again()
                    publickey, privatekey = generateKeys(keysize)
                    writeKeysToFile(keysize, publickey, privatekey, filename)
                    print(f"└─[Public key and Private key saved on {filename}_Public.key and {filename}_Private.key]")
                    again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Key Size value must be a number"+Color.End+"]")
                    again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        # ::::: RSA :::::
        elif (select == "20"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption       [02]Decryption\n    [03]Key Generator    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/RSA]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                try:
                    with open("public.pem", 'rb') as f:
                        publickey = rsa.PublicKey.load_pkcs1(f.read())
                        filesize = os.path.getsize((publickey))
                        if filesize == 0:
                            slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                            again()
                    with open("private.pem", 'rb') as f:
                        publickey = rsa.PrivateKey.load_pkcs1(f.read())
                        filesize = os.path.getsize((publickey))
                        if filesize == 0:
                            slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                            again()
                except FileNotFoundError:
                    slowprint("└─["+Color.BRed+"File Not Found"+Color.End+"]")
                    again()
                plaintext = input("\n┌───(christopher)─[~/christopher/Cryptography/RSA/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                encrypted_message = rsa.encrypt(plaintext.encode(), publickey)
                with open("encrypted.message", "wb") as f:
                    f.write(encrypted_message)
                print(f"└─[Ciphertext saved on encrypted.message]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                try:
                    with open("public.pem", 'rb') as f:
                        publickey = rsa.PublicKey.load_pkcs1(f.read())
                        filesize = os.path.getsize((publickey))
                        if filesize == 0:
                            slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                            again()
                    with open("private.pem", 'rb') as f:
                        publickey = rsa.PrivateKey.load_pkcs1(f.read())
                        filesize = os.path.getsize((publickey))
                        if filesize == 0:
                            slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                            again()
                except FileNotFoundError:
                    slowprint("└─["+Color.BRed+"File Not Found"+Color.End+"]")
                    again()
                encrypted_message = open("encrypted.message", "rb").read()
                clear_message = rsa.decrypt(encrypted_message, publickey)
                print("\n┌───(christopher)─[~/christopher/Cryptography/RSA/Decryption]")
                print(f"Plaintext: {clear_message.decode()}]")
                again()

            #::::: Key Generator :::::
            elif(pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                publickey, privatekey = rsa.newkeys(1024)
                with open("public.pem", 'wb') as f:
                    f.write(publickey.save_pkcs1("PEM"))
                with open("private.pem", 'wb') as f:
                    f.write(privatekey.save_pkcs1("PEM"))
                print("\n┌───(christopher)─[~/christopher/Cryptography/RSA/Key Generator]")
                print(f"└─[Public key and Private key saved on public.pem and private.pem]")
                again()

        #::::: Back to Main Menu :::::
        elif select == "99":
            christopher()
        else:
            again()

    #::::: Steganography :::::
    elif (choice == "2" or choice == "02"):
        clearScr()
        time.sleep(0.4)
        print(Banner.steganography_banner)
        select = input("\n┌───(christopher)─[~/christopher/Steganography]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Image :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Steganography/Image]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                message = input("\n┌───(christopher)─[~/christopher/Steganography/Image/Encryption]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).strip()
                if len(message) == 0:
                    slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                    again()
                file = input("├─[Enter your image file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(file) == 0:
                    slowprint("└─["+Color.BRed+"Image file cannot be empty"+Color.End+"]")
                    again()
                image_encrypt(message, file)
                again()

            #::::: Decryption :::::
            elif (pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                file = input("\n┌───(christopher)─[~/christopher/Steganography/Image/Decryption]\n├─[Enter your image file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(file) == 0:
                    slowprint("└─["+Color.BRed+"Image file cannot be empty"+Color.End+"]")
                    again()
                image_decrypt(file)
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Audio :::::
        if (select == "2" or select == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Steganography/Audio]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                message = input("\n┌───(christopher)─[~/christopher/Steganography/Audio/Encryption]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).strip()
                if len(message) == 0:
                    slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                    again()
                audiofile = input("├─[Enter your audio file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(audiofile) == 0:
                    slowprint("└─["+Color.BRed+"Audio file cannot be empty"+Color.End+"]")
                    again()
                imagefile = input("├─[Enter your image file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(imagefile) == 0:
                    slowprint("└─["+Color.BRed+"Image file cannot be empty"+Color.End+"]")
                    again()
                audio_encrypt(message, audiofile, imagefile)
                print(f"└─[The audio {audiofile} is saved]")
                again()

            #::::: Decryption :::::
            elif (pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                audiofile = input("\n┌───(christopher)─[~/christopher/Steganography/Image/Decryption]\n├─[Enter your audio file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(audiofile) == 0:
                    slowprint("└─["+Color.BRed+"Audio file cannot be empty"+Color.End+"]")
                    again()
                audio_decrypt(audiofile)
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        elif select == "99":
            christopher()

    #::::: Tools :::::
    elif (choice == "3" or choice == "03"):
        clearScr()
        time.sleep(0.4)
        print(Banner.tool_banner)
        select = input("\n┌───(christopher)─[~/christopher/Tools]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Password List :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]All Situations              [02]Custom\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Tools/Password List]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: All Situations :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                try:
                    min_len = int(input("\n┌───(christopher)─[~/christopher/Tools/Password List/All Situations]\n├─[Enter minimum length of password]"+color_banner[1]+"$ "+Color.End))
                    max_len = int(input("├─[Enter maximum length of password]"+color_banner[1]+"$ "+Color.End))
                    if max_len < min_len:
                        slowprint("└─["+Color.BRed+"The maximum length must be greater than the minimum length"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"minimum length and maximum length must be a number"+Color.End+"]")
                    again()
                wordlist(min_len, max_len)
                again()

            #::::: Custom :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                name = input("\n┌───(christopher)─[~/christopher/Tools/Password List/Custom]\n├─[Enter the first name]"+color_banner[1]+"$ "+Color.End).lower()
                while len(name) == 0 or name == " " or name == "  " or name == "   ":
                    slowprint("├─["+Color.BRed+"You must enter a name at least"+Color.End+"]")
                    name = input("├─[Enter the first name]"+color_banner[1]+"$ "+Color.End).lower()
                surname = input("├─[Enter the surname]"+color_banner[1]+"$ "+Color.End).lower()
                birth = input("├─[Birthdate (DDMMYYYY)]"+color_banner[1]+"$ "+Color.End).lower()
                while len(birth) != 0 and len(birth) != 8:
                    slowprint("├─["+Color.BRed+"You must enter 8 digits for birthday"+Color.End+"]")
                    birth = input("├─[Birthdate (DDMMYYYY)]"+color_banner[1]+"$ "+Color.End)
                birth_d = birth[:2]
                birth_m = birth[2:4]
                birth_y = birth[4:]
                combinations = [name, birth_d, surname, birth_m, birth, birth_y]
                interactive(combinations)
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Password Manager :::::
        elif (select == "2" or select == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            try:
                master_password = get_master_password()
            except:
                slowprint("\n["+Color.BRed+"Master password consists of letters and numbers only"+Color.End+"]")
                again()
            pathcsv = "./storage"
            if not os.path.exists(pathcsv):
                os.makedirs(pathcsv)
                create_csv()
            def passwordmanager():
                def search(url=''):
                    path = os.getcwd()
                    df = pd.read_csv(path+'/storage/password.csv')
                    dfS = df[df['Url/App name'].str.contains(url, na=False, case=False)]
                    index_d = dfS.index.values
                    password = []
                    dfS = dfS.reset_index()
                    for index, row in dfS.iterrows():
                        find_password = dfS.loc[index, 'Password']
                        dec_password = decrypt(find_password, master_password)
                        password.append(dec_password)
                    dfS = dfS.set_index(index_d)
                    dfS['Password'] = password
                    return dfS
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                menu_option = input("\n┌───(christopher)─[~/christopher/Tools/Password Manager]\n├───────────────────────┐\n├─[01]Add new account   │\n├─[02]Search account    │\n├─[03]Edit account      │\n├─[04]Delete account    │\n├─[99]Back to Main Menu │\n├───────────────────────┘\n├─[Select an option]"+color_banner[1]+"$ "+Color.End)

                #::::: Add new account :::::
                if (menu_option == "1" or menu_option == "01"):
                    clearScr()
                    time.sleep(0.4)
                    print(Banner.banner)
                    name = input("\n┌───(christopher)─[~/christopher/Tools/Password Manager/Add new account]\n├─[Enter Username]"+color_banner[1]+"$ "+Color.End)
                    password = pwinput(prompt ="├─[Enter Password]"+color_banner[1]+"$ "+Color.End, mask="*")
                    url = input("├─[Enter Url or App name]"+color_banner[1]+"$ "+Color.End)
                    if (name == ''):
                        name = 'Unavailable'
                    if (password == ''):
                        password = 'Unavailable'
                    if (len(url) == 0 or url == " " or url == "  " or url == "   "):
                        while (url == ''):
                            url = input("\n├─[Enter Url or App name]"+color_banner[1]+"$ "+Color.End)
                    encrypted_pass = encrypt(password, master_password)
                    add(name, encrypted_pass, url)
                    time.sleep(1)
                    passwordmanager()

                #::::: Search account :::::
                elif (menu_option == "2" or menu_option == "02"):
                    clearScr()
                    time.sleep(0.4)
                    print(Banner.banner)
                    sub_option = input("\n┌───(christopher)─[~/christopher/Tools/Password Manager/Search account]\n├────────────────────────────┐\n├─[01]See a specific account │\n├─[02]See all account        │\n├────────────────────────────┘\n├─[Select an option]"+color_banner[1]+"$ "+Color.End)

                    #::::: See a specific account :::::
                    if (sub_option == "1" or sub_option == "01"):
                        url = input("├─[Enter Url or App Name]"+color_banner[1]+"$ "+Color.End)
                        show_result = search(url)
                        show_in_md = show_result.to_markdown(tablefmt="orgtbl", index=False)
                        print("│\n"+show_in_md+"\n│")
                        input("└─[Press Any Key]")
                        passwordmanager()

                    #::::: See all account :::::
                    if (sub_option == "2" or sub_option == "02"):
                        show_result = search()
                        show_in_md = show_result.to_markdown(tablefmt="orgtbl", index=False)
                        print("│\n"+show_in_md+"\n│")
                        input("└─[Press Any Key]")
                        passwordmanager()

                #::::: Edit account :::::
                elif (menu_option == "3" or menu_option == "03"):
                    clearScr()
                    time.sleep(0.4)
                    print(Banner.banner)
                    url = input("\n┌───(christopher)─[~/christopher/Tools/Password Manager/Edit account]\n├─[Enter Url or App name]"+color_banner[1]+"$ "+Color.End)
                    show_result = search(url)
                    show_in_md = show_result.to_markdown(tablefmt="orgtbl", index=False) 
                    print("│\n"+show_in_md+"\n│")
                    if (len(show_result) > 1):
                        index = int(input("├─[Select an Index value]"+color_banner[1]+"$ "+Color.End))
                    else:
                        index = int(show_result.index.values[0])
                    new_name = input("├─[Enter new Username]"+color_banner[1]+"$ "+Color.End)
                    new_password = pwinput(prompt ="├─[Enter new Password]"+color_banner[1]+"$ "+Color.End, mask="*")
                    if (new_name == ''):
                        old_name = show_result.loc[index, 'Username']
                        new_name = old_name
                    if (new_password == ''):
                        old_password = show_result.loc[index, 'Password']
                        new_password = old_password
                    new_password = encrypt(new_password, master_password)
                    edit(index, new_name, new_password)
                    time.sleep(1)
                    passwordmanager()

                #::::: Delete account :::::
                elif (menu_option == "4" or menu_option == "04"):
                    clearScr()
                    time.sleep(0.4)
                    print(Banner.banner)
                    url = input("\n┌───(christopher)─[~/christopher/Tools/Password Manager/Delete account]\n├─[Enter Url or App name]"+color_banner[1]+"$ "+Color.End)
                    show_result = search(url)
                    show_in_md = show_result.to_markdown(tablefmt="orgtbl", index=False)
                    print("│\n"+show_in_md+"\n│")
                    if (len(show_result) > 1):
                        index = int(input("├─[Select an Index value]"+color_banner[1]+"$ "+Color.End))
                    else:
                        index = int(show_result.index.values[0])
                    confirm = input("├─[Do you want to continue [Y/n]")
                    if (confirm.upper() == 'Y' or confirm == ""):
                        delete(index)
                        time.sleep(1)
                    passwordmanager()

                #::::: Back to Main Menu :::::
                elif (menu_option == "99"):
                    christopher()
                else:
                    again()
            passwordmanager()
            again()

        #::::: Password generator :::::
        elif (select == "3" or select == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            try:
                length = int(input("\n┌───(christopher)─[~/christopher/Tools/Password generator]\n├─[Enter password length]"+color_banner[1]+"$ "+Color.End))
            except ValueError:
                slowprint("└─["+Color.BRed+"Length must be number]")
                again()
            if (length == 0):
                slowprint("└─["+Color.BRed+"Length must be more than one]")
                again()
            try:
                quantity = int(input("├─[How many passwords do you want]"+color_banner[1]+"$ "+Color.End))
            except ValueError:
                slowprint("└─["+Color.BRed+"Quantity must be number]")
                again()
            if (quantity == 0):
                slowprint("└─["+Color.BRed+"Quantity must be more than one]")
                again()
            lowercase = input("├─[Include Lowercase Characters]─[Y/n]"+color_banner[1]+"$ "+Color.End)
            uppercase = input("├─[Include Uppercase Characters]─[Y/n]"+color_banner[1]+"$ "+Color.End)
            number = input("├─[Include Numbers]─[Y/n]"+color_banner[1]+"$ "+Color.End)
            symbol = input("├─[Include Symbols]─[Y/n]"+color_banner[1]+"$ "+Color.End)
            excludesimilar = input("├─[Exclude Similar Characters]─[Y/n]"+color_banner[1]+"$ "+Color.End)
            textfile = input("├─[Do you want use save file]─[Y/n]"+color_banner[1]+"$ "+Color.End)
            passwordgenerate(length, quantity,lowercase, uppercase, number, symbol, excludesimilar, textfile)
            again()

        #::::: Frequency Analysis :::::
        elif (select == "4" or select == "04"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            text = input("\n┌───(christopher)─[~/christopher/Tools/Frequency Analysis]\n├─[Enter your text]"+color_banner[1]+"$ "+Color.End).upper().strip()
            if len(text) == 0:
                slowprint("└─["+Color.BRed+"Text cannot be empty"+Color.End+"]")
                again()
            elif text.isdigit():
                slowprint("└─["+Color.BRed+"Text cannot be only number"+Color.End+"]")
                again()
            else:
                print("├─[Frequency Order: "+getFrequencyOrder(text)+"]")
                print("└─[Frequency Score: "+str(getFrequencyScore(text))+"]")
                again()

        #::::: Back to Main Menu :::::
        elif (select == "99"):
            christopher()
        else:
            again()

    #::::: Exit :::::
    elif (choice == "99"):
        print("\n\tGoodBye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()

    else:
        again()

try:
    christopher()
    again()
except KeyboardInterrupt:
    slowprint(Color.BRed+"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()
    sys.exit()