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

#::::: Src :::::
#* ::::: Classic :::::
from src.atbash import atbash
from src.caesar import caesar_cipher_encryption, caesar_brute_force
from src.affine import affine_encryption, affine_brute_force

#* :::::  Modern  :::::

#* ::::: Tools :::::
from src.wordlist import wordlist

#::::: Default Library :::::
import os
import sys
import time

#::::: Again :::::
def again():
    "A Function To Ask The User To Restart The Program."
    christopher_again = input(Color.BCyan+"""\nDo You Want To Continue?"""+Color.End+"""\n    ┌───(christopher)─[~/again]─[Y/n]
    └─"""+color_banner[0]+"""$ """+Color.End)
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
    choice = input("""
┌───(christopher)─[~/christopher]
└─"""+color_banner[0]+"""$ """+Color.End)

    #::::: Classic :::::
    if (choice == "1" or choice == "01"):
        clearScr()
        time.sleep(0.4)
        print(Banner.classic_banner)
        select = input("""
┌───(christopher)─[~/christopher/Classic]
└─"""+color_banner[1]+"""$ """+Color.End)

        #::::: Atbash Cipher :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("""
┌───(christopher)─[~/christopher/Classic/Atbash Cipher]
├─[Enter your message]"""+color_banner[1]+"""$ """+Color.End).lower().strip()
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
            print("""    [1]Encryption     [2]Decryption
    [3]Back to Main Menu""")
            pick = input("""
┌───(christopher)─[~/christopher/Classic/Caesar Cipher]
└─"""+color_banner[1]+"""$ """+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                text = input("""
┌───(christopher)─[~/christopher/Classic/Caesar Cipher/Encryption]
├─[Enter your Text]"""+color_banner[1]+"""$ """+Color.End).lower().strip()
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
                ciphertext = input("""
┌───(christopher)─[~/christopher/Classic/Caesar Cipher/Decryption]
├─[Enter your Text]"""+color_banner[1]+"""$ """+Color.End).lower().strip()
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
                os.chdir("..")
                print("└─[The file was saved at the ./out path as CaesarCipher.txt]")
                again()

            #::::: Back to Main Menu :::::
            elif (pick == "3" or pick == "03"):
                christopher()
            else:
                again()

        #::::: Affine Cipher :::::
        elif (select == "3" or select == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            print("""    [1]Encryption     [2]Decryption
    [3]Back to Main Menu""")
            pick = input("""
┌───(christopher)─[~/christopher/Classic/Affine Cipher]
└─"""+color_banner[1]+"""$ """+Color.End)

            #::::: Encryption :::::
            if (pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                plaintext = input("""
┌───(christopher)─[~/christopher/Classic/Affine Cipher/Encryption]
├─[Enter your Plaintext]"""+color_banner[1]+"""$ """+Color.End).lower().strip()
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
                ciphertext = input("""
┌───(christopher)─[~/christopher/Classic/Affine Cipher/Decryption]
├─[Enter your Ciphertext]"""+color_banner[1]+"""$ """+Color.End).lower().strip()
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
            elif (pick == "3" or pick == "03"):
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
        select = input("""
┌───(christopher)─[~/christopher/Modern]
└─"""+color_banner[1]+"""$ """+Color.End)
        if select == "99":
            christopher()
        again()

    #::::: Quantum :::::
    elif (choice == "3" or choice == "03"):
        clearScr()
        time.sleep(0.4)
        print(Banner.quantum_banner)
        select = input("""
┌───(christopher)─[~/christopher/Quantum]
└─"""+color_banner[1]+"""$ """+Color.End)
        if select == "99":
            christopher()
        again()

    #::::: Tools :::::
    elif (choice == "4" or choice == "04"):
        clearScr()
        time.sleep(0.4)
        print(Banner.tool_banner)
        select = input("""
┌───(christopher)─[~/christopher/Tools]
└─"""+color_banner[1]+"""$ """+Color.End)
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            print("""    [1]All Situations     [2]Custom
    [3]Back to Main Menu""")
            pick = input("""
┌───(christopher)─[~/christopher/Tools/Password List]
└─"""+color_banner[1]+"""$ """+Color.End)
            if(pick == "1" or pick == "01"):
                clearScr()
                time.sleep(0.4)
                print(Banner.banner)
                try:
                    min_len = int(input("""
┌───(christopher)─[~/christopher/Tools/Password List/All Situations]
├─[Enter minimum length of password]"""+color_banner[1]+"""$ """+Color.End))
                    max_len = int(input("├─[Enter maximum length of password]"+color_banner[1]+"$ "+Color.End))
                except ValueError:
                    slowprint("├─["+Color.BRed+"minimum length and maximum length must be a number"+Color.End+"]")
                    again()
                wordlist(min_len, max_len)

            elif(pick == "2" or pick == "02"):
                pass
            #::::: Back to Main Menu :::::
            elif (pick == "3" or pick == "03"):
                christopher()
            else:
                again()

        if select == "99":
            christopher()
        again()

    #::::: Exit :::::
    elif (choice == "99"):
        print("\nGoodBye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()

    else:
        print(Color.BRed +"Choose one of the algorithms.")
        again()
    again()

try:
    christopher()
    again()
except KeyboardInterrupt:
    slowprint(Color.BRed+"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()