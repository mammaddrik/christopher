#::::: Library :::::
from lib.color import Color, color_banner

#::::: Banner :::::
class Banner:
    "A Class to print different banner."

    #::::: Main Menu :::::
    christopher_banner = (Color.End + """
\ \ """+color_banner[0]+"""p  u  e  v  f  g  b  c  u  r  e"""+Color.End+""" / /
 \ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ /
  \ """+color_banner[1]+"""  abcdefghijklm-nopqrstuvwxyz"""+Color.End+"""   /
   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
   /"""+color_banner[2]+"""c  h  r  i  s  t  o  p  h  e  r"""+Color.End+"""\ 
   \_______________________________/
    [01]Classic          [02]Modern
    [03]Quantum          [99]Exit""")

    #::::: Classic :::::
    classic_banner = (Color.End + """
\ \ """+color_banner[0]+"""p  u  e  v  f  g  b  c  u  r  e"""+Color.End+""" / /
 \ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ /
  \ """+color_banner[1]+"""  abcdefghijklm-nopqrstuvwxyz"""+Color.End+"""   /
   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
   /"""+color_banner[2]+"""c  h  r  i  s  t  o  p  h  e  r"""+Color.End+"""\ 
   \_______________________________/
 [01]Atbash Cipher   [02]Caesar Cipher
 [03]Affine Cipher   [99]Go Back to Main Menu""")

    #::::: Modern :::::
    modern_banner = (Color.End + """
\ \ """+color_banner[0]+"""p  u  e  v  f  g  b  c  u  r  e"""+Color.End+""" / /
 \ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ /
  \ """+color_banner[1]+"""  abcdefghijklm-nopqrstuvwxyz"""+Color.End+"""   /
   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
   /"""+color_banner[2]+"""c  h  r  i  s  t  o  p  h  e  r"""+Color.End+"""\ 
   \_______________________________/
    [01]                 [02]Modern
    [03]                 [99]Go Back to Main Menu""")

    #::::: Quantum :::::
    quantum_banner = (Color.End + """
\ \ """+color_banner[0]+"""p  u  e  v  f  g  b  c  u  r  e"""+Color.End+""" / /
 \ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ /
  \ """+color_banner[1]+"""  abcdefghijklm-nopqrstuvwxyz"""+Color.End+"""   /
   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
   /"""+color_banner[2]+"""c  h  r  i  s  t  o  p  h  e  r"""+Color.End+"""\ 
   \_______________________________/
    [01]                 [02]      
    [03]Quantum          [99]Go Back to Main Menu""")

    #::::: Main Menu (Empty) :::::
    banner = (Color.End + """
\ \ """+color_banner[0]+"""p  u  e  v  f  g  b  c  u  r  e"""+Color.End+""" / /
 \ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ /
  \ """+color_banner[1]+"""  abcdefghijklm-nopqrstuvwxyz"""+Color.End+"""   /
   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
   /"""+color_banner[2]+"""c  h  r  i  s  t  o  p  h  e  r"""+Color.End+"""\ 
   \_______________________________/""")
