import pandas as pd
import os
import os.path
from pwinput import pwinput
import string
import tabulate

ALPHABET = string.ascii_letters + string.digits

def get_master_password():
    master_pass = pwinput(prompt ="\n Enter master password: ", mask="*")
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
    df.to_csv('password.csv', index=False)

def add(name, encrypted_pass, url):
    user_data = {'Url/App name': [url], 'Username': [name], 'Password': [encrypted_pass]}
    df = pd.DataFrame(user_data)
    df.to_csv('data.csv', mode='a', header=False, index=False)
    print('\n' * 2 + ' ADDED SUCCESSFULLY')

def search(url=''):
    df = pd.read_csv('data.csv')
    dfS = df[df['Url/App name'].str.contains(url, na=False, case=False)]
    index_d = dfS.index.values
    password = []
    dfS = dfS.reset_index()
    for index, row in dfS.iterrows():
        find_password = dfS.loc[index, 'Password']
        dec_password = decrypt(find_password, master_password)
        password.append(dec_password)
    dfS = dfS.set_index(index_d)
    dfS['Password'] = password
    return dfS

def edit(index, new_name, new_password):
    df = pd.read_csv("data.csv")
    df.loc[index, ['Username', 'Password']] = [new_name, new_password]
    df.to_csv('data.csv', index=False)
    print('\nEDITED SUCCESSFULLY')

def delete(index):
    df = pd.read_csv("data.csv")
    df.drop([index], axis=0, inplace=True)
    df.to_csv('data.csv', index=False)
    print('\nDELETED SUCCESSFULLY')

data_file = os.path.isfile('data.csv')
if not data_file:
    create_csv()