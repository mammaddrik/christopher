import random
import string
import os

def passwordgenerate(length, quantity, lowercase, uppercase, number, symbol, excludesimilar, textfile):
    if (textfile.upper() == "Y" or textfile == ""):
        path = r"./passwordlist"
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir("./passwordlist")
        f = open("Password.txt","w")
        print("├─[Passwords file created on ./passwordlist]")

    #::::: Include Lowercase :::::
    if (lowercase.upper() == "Y" or lowercase == ""):
        lowercase = list(string.ascii_lowercase)
    else:
        lowercase = list()

    #::::: Include Uppercase :::::
    if (uppercase.upper() == "Y" or uppercase == ""):
        uppercase = list(string.ascii_uppercase)
    else:
        uppercase = list()

    #::::: Include Numbers :::::
    if (number.upper() == "Y" or number == ""):
        number = list(string.digits)
    else:
        number = list()

    #::::: Include Symbols :::::
    if (symbol.upper() == "Y" or symbol == ""):
        symbol = list(string.punctuation)
    else:
        symbol = list()

    characters = list(lowercase + uppercase + number + symbol)

    #::::: Exclude Similar Characters :::::
    if (excludesimilar.upper() == "Y" or excludesimilar == ""):
        for password_index in range(quantity):
            random.shuffle(characters)
            result = "".join(characters[:length])
            print(f"├─[ {result} ]")
            if (textfile.upper() == "Y" or textfile == ""):
                f.writelines(result + "\n")
        os.chdir("..")
        print("└─[Passwords are created]")
        try:
            f.close()
        except UnboundLocalError:
            pass
    else:
        for password_index in range(quantity):
            password = ""
            for index in range(length):
                password = password + random.choice(characters)
            result = (password)
            print(f"├─[ {result} ]")
            if (textfile.upper() == "Y" or textfile == ""):
                f.writelines(result + "\n")
        os.chdir("..")
        print("└─[Passwords are created]")
        try:
            f.close()
        except UnboundLocalError:
            pass