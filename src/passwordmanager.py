import pandas as pd
import os
from pwinput import pwinput
import string
from lib.color import Color, color_banner

ALPHABET = string.ascii_letters + string.digits
path = os.getcwd()
def get_master_password():
    master_pass = pwinput(prompt = "\n┌───(christopher)─[~/christopher/Tools/Password Manager]\n└─[Enter master password]"+color_banner[1]+"$ "+Color.End, mask="*")
    processed_password = ""
    for char in master_pass:
        if char.isalpha():
            processed_password += str(ord(char.lower()) - 96)
        else:
            processed_password += char
    master_pass = int(processed_password.replace("-", ""))
    return master_pass

def encrypt(password, master_pass):
    encrypted_password = ""
    for char in password:
        if char in ALPHABET:
            new_pos = (ALPHABET.find(char) + master_pass) % len(ALPHABET)
            encrypted_password += ALPHABET[new_pos]
        else:
            encrypted_password += char
    return encrypted_password

def decrypt(encrypted_password, master_pass):
    decrypted_password = ""
    for char in encrypted_password:
        if char in ALPHABET:
            new_pos = (ALPHABET.find(char) - master_pass) % len(ALPHABET)
            decrypted_password += ALPHABET[new_pos]
        else:
            decrypted_password += char
    return decrypted_password

def create_csv():
    data = {'Url/App name': [], 'Username': [], 'Password': []}
    df = pd.DataFrame(data)
    try:
        df.to_csv(path+'/storage/password.csv', index=False)
    except PermissionError:
        print("Close the password.csv file.")

def add(name, encrypted_pass, url):
    user_data = {'Url/App name': [url], 'Username': [name], 'Password': [encrypted_pass]}
    df = pd.DataFrame(user_data)
    df.to_csv(path+'/storage/password.csv', mode='a', header=False, index=False)
    print('└─[Added  Successfully]')

def edit(index, new_name, new_password):
    df = pd.read_csv("password.csv")
    df.loc[index, ['Username', 'Password']] = [new_name, new_password]
    try:
        df.to_csv(path+'/storage/password.csv', index=False)
    except PermissionError:
        print("Close the password.csv file.")
    print('\nEDITED SUCCESSFULLY')

def delete(index):
    df = pd.read_csv("password.csv")
    df.drop([index], axis=0, inplace=True)
    try:
        df.to_csv(path+'/storage/password.csv', index=False)
    except PermissionError:
        print("Close the password.csv file.")
    print('\nDELETED SUCCESSFULLY')

data_file = os.path.isfile(path+'/storage/password.csv')
if not data_file:
    create_csv()