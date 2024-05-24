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
   [01]Classic Cipher         [02]Modern Cipher
   [03]Quantum Cipher         [04]Tools
   [05]Github                 [99]Exit""")

    #::::: Classic :::::
    classic_banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]Atbash Cipher        [02]Caesar Cipher
   [03]Affine Cipher        [04]Vigenère Cipher
   [05]Revers Text          [06]Playfire Cipher
   [07]Rail Fence Cipher    [08]Scytale Cipher
   [09]Polybius Square      [10]Columnar Cipher
   [11]Substitution Cipher  [12]
   [13]                     [14]
   [15]                     [16]
   [17]                     [18]
   [19]                     [20]
   [99]Back to Main Menu""")

    #::::: Modern :::::
    modern_banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]Hash Function             [02]Morse Code
   [03]Rot13 Cipher              [04]
   [05]                          [06]
   [07]                          [08]
   [09]                          [10]
   [11]                          [12]
   [13]                          [14]
   [15]                          [16]
   [17]                          [18]
   [19]                          [20]
   [99]Back to Main Menu""")

    #::::: Steganography :::::
    quantum_banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]                 [02]
   [03]Steganography    [99]Back to Main Menu""")

    #::::: Tools :::::
    tool_banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
   [01]Password List      [02]Password Manager
   [03]Password generator [04]Check Password
   [05]Frequency Analysis [99]Back to Main Menu""")

    #::::: Main Menu (Empty) :::::
    banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/""")