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

#::::: Data :::::
from detect.detectenglish import isEnglish

#::::: Src :::::
#* ::::: Classic :::::
from src.atbash import atbash
from src.caesar import caesar_cipher_encryption, caesar_brute_force
from src.affine import affine_encryption, affine_brute_force

#* :::::  Modern  :::::
from src.hashid import hashid
from src.hashgenerator import hashgenerator
#* ::::: Tools :::::
from src.wordlist import wordlist
from src.passwordgenerator import passwordgenerate

#::::: Default Library :::::
import os
import sys
import time

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

#::::: Main Menu :::::
def christopher():
    "The main function of christoper."
    clearScr()
    time.sleep(0.4)
    print(Banner.christopher_banner)
    choice = input("\n┌───(christopher)─[~/christopher]\n└─"+color_banner[0]+"$ "+Color.End)

    #::::: Classic :::::
    if (choice == "1" or choice == "01"):
        clearScr()
        time.sleep(0.4)
        print(Banner.classic_banner)
        select = input("\n┌───(christopher)─[~/christopher/Classic]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Atbash Cipher :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[~/christopher/Classic/Atbash Cipher]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
            print("    [1]Encryption     [2]Decryption\n    [99]Back to Main Menu")
            pick = input("\n┌───(christopher)─[~/christopher/Classic/Caesar Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                text = input("\n┌───(christopher)─[~/christopher/Classic/Caesar Cipher/Encryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(text) == 0:
                    slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                    again()
                elif text.isdigit():
                    slowprint("└─["+Color.BRed+"plaintext cannot be only number"+Color.End+"]")
                    again()
                try:
                    shift = int(input("├─[Enter your shift number]"+color_banner[1]+"$ "+Color.End))
                    if shift >= 1 and shift <= 25:
                        print(f"└─[Output: {caesar_cipher_encryption(text,shift)}]")
                        again()
                    else:
                        slowprint("├─["+Color.BRed+"Shift value must be a number Between 1 and 25 (Default: 3)"+Color.End+"]")
                        shift = 3
                        print(f"└─[Output: {caesar_cipher_encryption(text,shift)}]")
                        again()
                except ValueError:
                    slowprint("├─["+Color.BRed+"Shift value must be a number (Default: 3)"+Color.End+"]")
                    shift = 3
                    print(f"└─[Output: {caesar_cipher_encryption(text,shift)}]")
                    again()

            #::::: Decryption :::::
            elif(pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic/Caesar Cipher/Decryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
                    decrypted_texts = caesar_brute_force(ciphertext)
                    for i, text in enumerate(decrypted_texts):
                        file.write(f"Shift {i+1}: {text}\n")
                        if isEnglish(text):
                            print(f"├─[Shift = {i+1}]\n├─[The plaintext may be this: {text}]")
                os.chdir("..")
                print("└─[The file was saved at the ./out path as CaesarCipher.txt]")
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        #::::: Affine Cipher :::::
        elif (select == "3" or select == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            print("    [1]Encryption     [2]Decryption\n    [99]Back to Main Menu")
            pick = input("\n┌───(christopher)─[~/christopher/Classic/Affine Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("\n┌───(christopher)─[~/christopher/Classic/Affine Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
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
                ciphertext = input("\n┌───(christopher)─[~/christopher/Classic/Affine Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
                if len(ciphertext) == 0:
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                    again()
                elif ciphertext.isdigit():
                    slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                    again()
                affine_brute_force(ciphertext)
                print("└─[The file was saved at the ./out path as AffineCipher.txt]")
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        elif select == "99":
            christopher()
        again()

    #::::: Modern :::::
    elif (choice == "2" or choice == "02"):
        clearScr()
        time.sleep(0.4)
        print(Banner.modern_banner)
        select = input("\n┌───(christopher)─[~/christopher/Modern]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Hash Function :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            print("   [1]Hash Generator    [2]Hash Cracker\n   [3]Hash Identifier   [99]Back to Main Menu")
            pick = input("\n┌───(christopher)─[~/christopher/Modern/Hash Function]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: Hash Generator :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                password = input("\n┌───(christopher)─[~/christopher/Modern/Hash Function/Hash Generator]\n├─[Enter the password]"+color_banner[1]+"$ "+Color.End).lower().strip()
                hashvalue = input("├────────────┬────────────┬────────────┐\n├─[1]MD5     ├─[2]SHA1    ├─[3]SHA224  │\n├─[4]SHA256  ├─[5]SHA384  ├─[6]SHA512  │\n├────────────┴────────────┴────────────┘\n├─[Select the function]"+color_banner[1]+"$ "+Color.End)

                if(hashvalue == "1" or hashvalue == "01"):
                    hashvalue = "md5"
                elif(hashvalue == "2" or hashvalue == "02"):
                    hashvalue = "sha1"
                elif(hashvalue == "3" or hashvalue == "03"):
                    hashvalue = "sha224"
                elif(hashvalue == "4" or hashvalue == "04"):
                    hashvalue = "sha256"
                elif(hashvalue == "5" or hashvalue == "05"):
                    hashvalue = "sha384"
                elif(hashvalue == "6" or hashvalue == "06"):
                    hashvalue = "sha512"
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
                #TODO: Hash Cracker
                again()

            #::::: Hash Identifier :::::
            elif (pick == "3" or pick == "03"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                h = input("\n┌───(christopher)─[~/christopher/Modern/Hash Function/Hash Identifier]\n├─[Enter your Hash]"+color_banner[1]+"$ "+Color.End)
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
            print("    [1]Text to Morse Code     [2]Morse Code to Text\n    [99]Back to Main Menu")
            pick = input("\n┌───(christopher)─[~/christopher/Modern/Morse Code]\n└─"+color_banner[1]+"$ "+Color.End)
            if pick == "1" or pick == "01":
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                #TODO: Text to Morse Code
                again()
            elif (pick == "2" or pick == "02"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                #TODO: Morse Code to Text
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "99"):
                christopher()
            else:
                again()

        elif select == "99":
            christopher()
        else:
            again()

    #::::: Quantum :::::
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
            print("    [1]All Situations     [2]Custom\n    [99]Back to Main Menu")
            pick = input("\n┌───(christopher)─[~/christopher/Tools/Password List]\n└─"+color_banner[1]+"$ "+Color.End)

            #::::: All Situations :::::
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                try:
                    min_len = int(input("\n┌───(christopher)─[~/christopher/Tools/Password List/All Situations]\n├─[Enter minimum length of password]"+color_banner[1]+"$ "+Color.End))
                    max_len = int(input("├─[Enter maximum length of password]"+color_banner[1]+"$ "+Color.End))
                except ValueError:
                    slowprint("├─["+Color.BRed+"minimum length and maximum length must be a number"+Color.End+"]")
                    again()
                wordlist(min_len, max_len)
                again()

            #::::: Custom :::::
            elif(pick == "2" or pick == "02"):
                #TODO: Password List Custom
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
            #TODO: Password Manager
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