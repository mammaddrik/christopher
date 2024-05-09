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
#* ::::: Classic Cipher :::::
from src.atbash import atbash
from src.caesar import caesar_encryption, caesar_decrypt
from src.affine import affine_encryption, affine_decrypt
from src.vigenère import vigenère_encrypt, vigenère_decrypt
from src.revers import revers
from src.playfair import playfair_encrypt, playfair_decrypt
from src.railfence import railfence_encrypt, railfence_decrypt
from src.scytale import scytale_encrypt, scytale_decrypt


#* :::::  Modern Cipher :::::
from src.hashgenerator import hashgenerator
from src.hashid import hashid
from src.morsecode import morse, morsetext
from src.rot13 import rot13

#* ::::: Tools :::::
from src.wordlist import wordlist
from src.customwordlist import interactive
from src.passwordgenerator import passwordgenerate
from src.passwordmanager import get_master_password, encrypt, decrypt, create_csv, add, edit, delete

#::::: Default Library :::::
import os
import sys
import time
import hashlib
import string
import re
from datetime import datetime
from itertools import product
from hmac import compare_digest

#::::: Libraries to be installed :::::
try:
    import pandas as pd
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
    choice = input("\n┌───(christopher)─[~/christopher]\n└─"+color_banner[0]+"$ "+Color.End)

    #::::: Classic Cipher :::::
    if (choice == "1" or choice == "01"):
        clearScr()
        time.sleep(0.4)
        print(Banner.classic_banner)
        select = input("\n┌───(christopher)─[~/christopher/Classic Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Atbash Cipher :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Atbash Cipher]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Classic Cipher/Caesar Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                text = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Caesar Cipher/Encryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(text) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                elif text.isdigit():
                    slowprint("└─["+Color.BRed+"plaintext cannot be only number"+Color.End+"]")
                    again()
                try:
                    shift = int(input("├─[Enter your shift number]"+color_banner[1]+"$ "+Color.End))
                    if shift >= 1 and shift <= 25:
                        print(f"└─[Output: {caesar_encryption(text,shift)}]")
                        again()
                    else:
                        slowprint("├─["+Color.BRed+"Shift value must be a number Between 1 and 25 (Default: 3)"+Color.End+"]")
                        shift = 3
                        print(f"└─[Output: {caesar_encryption(text,shift)}]")
                        again()
                except ValueError:
                    slowprint("├─["+Color.BRed+"Shift value must be a number (Default: 3)"+Color.End+"]")
                    shift = 3
                    print(f"└─[Output: {caesar_encryption(text,shift)}]")
                    again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Caesar Cipher/Decryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                path = "./out"
                if not os.path.exists(path):
                    os.makedirs(path)
                file_name = "CaesarCipher.txt"
                os.chdir("./out")
                with open(file_name, "w") as file:
                    file.write("Brute Force Decryption:\n\n")
                    decrypted_texts = caesar_decrypt(ciphertext)
                    for i, text in enumerate(decrypted_texts):
                        file.write(f"Shift {i+1}: {text}\n")
                        if isEnglish(text):
                            print("├─[Shift: "+Color.BGreen+f"{i+1}"+Color.End+f"]\n├─[The plaintext may be this: {text}]")
                os.chdir("..")
                print("└─[The file was saved at the ./out path as CaesarCipher.txt]")
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
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Classic Cipher/Affine Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Affine Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                elif plaintext.isdigit():
                    slowprint("└─["+Color.BRed+"Plaintext cannot be only number"+Color.End+"]")
                    again()
                try:
                    slope = int(input("├─[Enter your slope(a) number]"+color_banner[1]+"$ "+Color.End))
                    if slope % 2 == 0:
                        slowprint("├─["+Color.BRed+"Slope(a) value must be a number Between 1 and 25 (The number must be odd)"+Color.End+"]")
                        again()
                    intercept = int(input("├─[Enter your intercept(b) number]"+color_banner[1]+"$ "+Color.End))
                    if (slope >= 1 and slope <= 25):
                        print(f"└─[Output: {affine_encryption(plaintext, slope, intercept)}]")
                        again()
                    else:
                        slowprint("├─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number Between 1 and 25"+Color.End+"]")
                        again()
                except ValueError:
                    slowprint("├─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number (Slope(a) number must be odd)"+Color.End+"]")
                    again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Affine Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                affine_decrypt(ciphertext)
                print("└─[The file was saved at the ./out path as AffineCipher.txt]")
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
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Classic Cipher/Vigenère Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Vigenère Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
                print("├─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                ciphertext = vigenère_encrypt(plaintext, key)
                print(f"└─[Ciphertext: {ciphertext}]")
                again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Vigenère Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                path = "./out"
                if not os.path.exists(path):
                    os.makedirs(path)
                file_name = "VigenèreCipher.txt"
                os.chdir("./out")
                character = string.ascii_lowercase
                for i in range(1, 1000):
                    for j in product(character, repeat=i):
                        key = "".join(j)
                        key = re.sub(r'\d+', '', key)
                        print(f"├─[Key: {key}]", end='\r')
                        plaintext = vigenère_decrypt(ciphertext, key).upper()
                        if isEnglish(plaintext):
                            print(f"├─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                            print(f"├─[Plaintext: {plaintext.lower()}]")
                            keep()
                print("└─[The file was saved at the ./out path as VigenèreCipher.txt]")
                with open(file_name, "w") as file:
                    file.write("Brute Force Decryption:\n\n")
                    file.write(f"key {key}: {plaintext.lower()}\n")
                    os.chdir("..")
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
                message = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Revers Text]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Classic Cipher/Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Playfair Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Playfair Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).strip()
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
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Classic Cipher/Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Rail Fence Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(plaintext) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                try:
                    key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                    ciphertext = railfence_encrypt(plaintext, key)
                    print(f"└─[Ciphertext: {ciphertext}]")
                    again()
                except ValueError:
                    slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                    again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Rail Fence Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                path = "./out"
                if not os.path.exists(path):
                    os.makedirs(path)
                file_name = "RailFenceCipher.txt"
                os.chdir("./out")
                for i in range(2, len(ciphertext)):
                    key = i
                    plaintext = railfence_decrypt(ciphertext, key).upper()
                    if isEnglish(plaintext):
                        print(f"├─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                        print(f"├─[Plaintext: {plaintext.lower()}]")
                        print("└─[The file was saved at the ./out path as RailFenceCipher.txt]")
                        with open(file_name, "w") as file:
                            file.write("Brute Force Decryption:\n\n")
                            file.write(f"key {key}: {plaintext.lower()}\n")
                os.chdir("..")
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
            pick = input("    [01]Encryption              [02]Decryption\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Classic Cipher/Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Scytale Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic Cipher/Scytale Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
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

        #::::: Back to Main Menu :::::
        elif select == "99":
            christopher()
        else:
            again()

    #::::: Modern Cipher :::::
    elif (choice == "2" or choice == "02"):
        clearScr()
        time.sleep(0.4)
        print(Banner.modern_banner)
        select = input("\n┌───(christopher)─[~/christopher/Modern Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Hash Function :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("   [01]Hash Generator    [02]Hash Cracker\n   [03]Hash Identifier   [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Modern Cipher/Hash Function]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Hash Generator :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                password = input("\n┌───(christopher)─[~/christopher/Modern Cipher/Hash Function/Hash Generator]\n├─[Enter the password]"+color_banner[1]+"$ "+Color.End).lower().strip()
                hashvalue = input("├───────────────┬───────────────┬───────────────┐\n├─[01]MD2       ├─[2]MD4        ├─[03]MD5       │\n├─[04]SHA1      ├─[05]SHA224    ├─[06]SHA256    │\n├─[07]SHA384    ├─[08]SHA512    ├─[09]sha3-224  │\n├─[10]sha3-256  ├─[11]sha3-384  ├─[12]sha3-512  │\n├─[13]shake-128 ├─[14]shake-256 ├─[15]blake2b   │\n├─[16]blake2s   ├─[17]NTLM      ├─[18]adler32   │\n├─[19]crc32     ├─[20]all       ├─[21]Back      │\n├───────────────┴───────────────┴───────────────┘\n├─[Select the function]"+color_banner[1]+"$ "+Color.End)
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
                    slowprint(Color.BRed +"Enter the Available Algorithm.")
                    again()
                hashgenerator(password, hashvalue)
                again()

            #::::: Hash Cracker :::::
            elif (pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                pick = input("    [01]All Situations              [02]Custom\n    [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Modern Cipher/Hash Function/Hash Cracker]\n└─"+color_banner[1]+"$ "+Color.End)

                #::::: All Situations :::::
                if (pick == "1" or pick == "01"):
                    clearScr()
                    time.sleep(0.4)
                    print(Banner.banner)
                    Hash = input("\n┌───(christopher)─[~/christopher/Modern Cipher/Hash Function/Hash Cracker/All Situations]\n├─[Enter the hash]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
                            counter+=1
                            print(f"├─[Password number {counter}: {word.strip()}]")
                            if compare_digest(Hash, hashedguess):
                                t2 = datetime.now()
                                t3 = t2 - t1
                                print(f"├─[Finishing Time: {t3}]")
                                print("└─[Password: "+Color.BGreen+f"{word}"+Color.End+"]")
                                again()
                    else:
                        slowprint("└─["+Color.BRed+"Password Not Found"+Color.End+"]")
                        again()

                #::::: Custom :::::
                elif (pick == "2" or pick == "02"):
                    clearScr()
                    time.sleep(0.4)
                    print(Banner.banner)
                    Hash = input("\n┌───(christopher)─[~/christopher/Modern Cipher/Hash Function/Hash Cracker/Custom]\n├─[Enter the hash]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
                                print(f"├─[Password number {counter}: {password.strip()}]")
                                counter += 1
                                if compare_digest(Hash, hashedguess):
                                    t2 = datetime.now()
                                    t3 = t2 - t1
                                    print(f"├─[Finishing Time: {t3}]")
                                    print("└─[Password: "+Color.BGreen+f"{password}"+Color.End+"]")
                                    again()
                            else:
                                slowprint("└─["+Color.BRed+"Password Not Found"+Color.End+"]")
                                again()
                    except FileNotFoundError:
                        slowprint("└─["+Color.BRed+"File Not Found"+Color.End+"]")
                        again()

                #::::: Back to Main Menu :::::
                elif (pick == "99"):
                    christopher()
                else:
                    again()

            #::::: Hash Identifier :::::
            elif (pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                h = input("\n┌───(christopher)─[~/christopher/Modern Cipher/Hash Function/Hash Identifier]\n├─[Enter your Hash]"+color_banner[1]+"$ "+Color.End)
                hashid(h)
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Morse Code :::::
        elif (select == "2" or select == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            pick = input("    [01]Text to Morse        [02]Morse to Text\n    [99]Back to Main Menu\n┌───(christopher)─[~/christopher/Modern Cipher/Morse Code]\n└─"+color_banner[1]+"$ "+Color.End)

            #:::::Text to Morse :::::
            if pick == "1" or pick == "01":
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                message = input("\n┌───(christopher)─[~/christopher/Modern Cipher/Morse Code/Text to Morse]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper()
                morse(message)
                again()

            #::::: Morse to Text :::::
            elif (pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                message = input("\n┌───(christopher)─[~/christopher/Modern Cipher/Morse Code/Morse to Text]\n├─[Enter your morse code]"+color_banner[1]+"$ "+Color.End).upper()
                morsetext(message)
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Rot13 Cipher :::::
        elif (select == "3" or select == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[~/christopher/Modern Cipher/Rot13]\n├─[Enter your text]"+color_banner[1]+"$ "+Color.End)
            text = rot13(message)
            print(f"└─[Output: {text}]")
            again()

        #::::: Back to Main Menu :::::
        elif select == "99":
            christopher()
        else:
            again()

    #::::: Quantum Cipher :::::
    elif (choice == "3" or choice == "03"):
        clearScr()
        time.sleep(0.4)
        print(Banner.quantum_banner)
        select = input("\n┌───(christopher)─[~/christopher/Quantum]\n└─"+color_banner[1]+"$ "+Color.End)
        if select == "99":
            christopher()
        again()

    #::::: Tools :::::
    elif (choice == "4" or choice == "04"):
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