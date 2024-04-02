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
        if select == "99":
            christopher()
        again()

    #::::: Modern :::::
    if (choice == "2" or choice == "02"):
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
    if (choice == "3" or choice == "03"):
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
except KeyboardInterrupt:
    slowprint(Color.BRed+"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()