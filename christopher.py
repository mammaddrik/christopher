#!/usr/bin/env python
#
#    \ \  16 21 05 22 06 07 02 03 21 18 05 / /
#     \ \ p  u  e  v  f  g  b  c  u  r  e / /
#      \ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ /
#       \   abcdefghijklm-nopqrstuvwxyz   /
#        \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
#        /c  h  r  i  s  t  o  p  h  e  r\
#        \_______________________________/
#        Tool for Encryption & Decryption
#               Github: mammaddrik       

#::::: Library :::::
from lib.banner import Banner
from lib.color import Color, color_banner
from lib.clearscr import clearScr
from lib.slowprint import slowprint

#::::: Src :::::
from src.atbash import atbash
from src.caesar import caesar_cipher_encrypt, caesar_brute_force_decrypt

#::::: Default Library :::::
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

def printf():
    printf = input(Color.BCyan+"""\nDo you want to create a text file?"""+Color.End+"""\n    ┌───(christopher)─[~/file]─[Y/n]
    └─"""+color_banner[0]+"""$ """+Color.End)
    if (printf.upper() == "Y" or printf == ""):
        file_name = input("Enter the name of the file: ")
        with open(file_name, 'w') as file:
            file.write("This is a new text file.")
        print(f"Text file '{file_name}' has been created. on /out")
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
        
        #::::: Atbash :::::
        if (select == "1" or select == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("""
┌───(christopher)─[~/christopher/Classic/Atbash Cipher]
├─[Enter your message]"""+color_banner[1]+"""$ """+Color.End).lower()
            if len(message) == 0:
                slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                again()
            elif message.isdigit():
                slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
                again()
            else:
                print(f"└─[Output: {atbash(message)}]")
                again()

        elif (select == "2" or select == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            text = input("""
┌───(christopher)─[~/christopher/Classic/Caesar Cipher]
├─[Enter your message]"""+color_banner[1]+"""$ """+Color.End).lower()
            if len(text) == 0:
                slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
                again()
            elif text.isdigit():
                slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
                again()
            try:
                shift = int(input("├─[Enter your shift number]"""+color_banner[1]+"$ "+Color.End))
                if shift >= 1 and shift <= 25:
                    print(f"└─[Output: {caesar_cipher_encrypt(text,shift)}]")
                    again()
                else:
                    slowprint("├─["+Color.BRed+"Shift value must be a number Between 1 and 25 (Default: 3)"+Color.End+"]")
                    shift = 3
                    print(f"└─[Output: {caesar_cipher_encrypt(text,shift)}]")
                    again()
            except ValueError:
                slowprint("├─["+Color.BRed+"Shift value must be a number (Default: 3)"+Color.End+"]")
                shift = 3
                print(f"└─[Output: {caesar_cipher_encrypt(text,shift)}]")
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
    printf()
except KeyboardInterrupt:
    slowprint(Color.BRed+"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()