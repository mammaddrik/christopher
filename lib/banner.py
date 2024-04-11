#::::: Library :::::
from lib.color import Color, color_banner

#::::: Banner :::::
class Banner:
    "A Class to print different banner."

    #::::: Main Menu :::::
    christopher_banner = (Color.End + """
\ \ """+color_banner[0]+"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+"""     abcd efgh ijkl m-n opqr stuv wxyz     """+Color.End+"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+"""\ 
   \__________________________________________/
    [01]Classic           [02]Modern
    [03]Quantum           [04]Password Manager
    [05]Github            [99]Exit""")

    #::::: Classic :::::
    classic_banner = (Color.End + """
\ \ """+color_banner[0]+"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+"""\ 
   \__________________________________________/
    [01]Atbash Cipher    [02]Caesar Cipher      
    [03]Affine Cipher    [99]Back to Main Menu""")

    #::::: Modern :::::
    modern_banner = (Color.End + """
\ \ """+color_banner[0]+"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+"""\ 
   \__________________________________________/
    [01]                 [02]Modern
    [03]                 [99]Back to Main Menu""")

    #::::: Quantum :::::
    quantum_banner = (Color.End + """
\ \ """+color_banner[0]+"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+"""\ 
   \__________________________________________/
    [01]                 [02]      
    [03]Quantum          [99]Back to Main Menu""")

    #::::: Main Menu (Empty) :::::
    banner = (Color.End + """
\ \ """+color_banner[0]+"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+"""\ 
   \__________________________________________/""")
