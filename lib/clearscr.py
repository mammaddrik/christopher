#::::: Default Library :::::
import os

#::::: Clear Screen :::::
def clearScr():
    "A Function to clean up the command prompt or terminal."
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")