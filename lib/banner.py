import os
#::::: Library :::::
from lib.color import Color, color_banner

#::::: Banner :::::
class Banner:
    "A Class to print different banner."

    #::::: Main Menu :::::
    christopher_banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]Cryptography          [02]Steganography
   [03]Tools                 [04]Github""")

    cipher_banner = (Color.End + r"""
\ \ """+color_banner[3]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[4]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[5]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]Atbash Cipher        [02]Caesar Cipher
   [03]Affine Cipher        [04]Vigenère Cipher
   [05]Reverse Text         [06]Playfire Cipher
   [07]Rail Fence Cipher    [08]Scytale Cipher
   [09]Polybius Square      [10]Columnar Cipher
   [11]Substitution Cipher  [12]Baconian Cipher
   [13]Morse Code           [14]Rot13 Cipher
   [15]One-Time Pad Cipher  [16]Hash Function
   [17]Enigma Machine       [18]AES(CBC)
   [19]Public Key Cipher    [20]RSA""")

    #::::: Steganography :::::
    steganography_banner = (Color.End + r"""
\ \ """+color_banner[5]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[4]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[3]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]Image             [02]Audio""")

    #::::: Tools :::::
    tool_banner = (Color.End + r"""
\ \ """+color_banner[2]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[0]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]Password List      [02]Password Manager
   [03]Password generator [04]Frequency Analysis""")

    #:::: Github ::::
    github_banner = (color_banner[1]+r"""╔══════════════════════════════════════════╗
║   """+Color.End+r"""["""+color_banner[2]+r"""+"""+Color.End+r"""]Christopher"""+color_banner[1]+r"""                         ║
║   """+Color.End+r"""["""+color_banner[3]+r"""+"""+Color.End+r"""]Tool for Encryption & Decryption"""+color_banner[1]+r"""    ║
║   """+Color.End+r"""["""+color_banner[4]+r"""+"""+Color.End+r"""]Version: 1.0"""+color_banner[1]+r"""                        ║
╚══════════════════════════════════════════╝"""+Color.End)
    #::::: Main Menu (Empty) :::::
    banner = (Color.End + r"""
\ \ """+color_banner[1]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[3]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[5]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/""")