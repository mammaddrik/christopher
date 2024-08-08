import string
import sys

SYMBOL = string.printable
BLOCKSIZE = 16

def blockToString(blocks):
    output = ""
    for block in blocks:
        while block:
            index = block % len(SYMBOL)
            block = block // len(SYMBOL)
            output += SYMBOL[index]
    return output
def stringToBlock(plaintext):
    output = []
    while plaintext:
        block_number = 0
        block_string = None
        if len(plaintext) >= BLOCKSIZE:
            block_string = plaintext[0:BLOCKSIZE]
            plaintext = plaintext[BLOCKSIZE:]
        else:
            block_string = plaintext
            plaintext = ''
        for i in range(len(block_string)):
            index = SYMBOL.find(block_string[i])
            block_number += (index * (len(SYMBOL) ** i))
        output.append(block_number)
    return output

def publickey_encrypt(plaintext, publicKey, outputfile):
    plainblocks = stringToBlock(plaintext)
    cipherblocks = []
    for block in plainblocks:
        C = pow(block, publicKey[1], publicKey[0])
        cipherblocks.append(str(C))
    file = open(outputfile, 'w')
    file.write(",".join(cipherblocks))
    file.close()

def publickey_decrypt(encrypted_file, privateKey):
    file = open(encrypted_file, 'r')
    cipherblocks = file.read()
    file.close()
    cipherblocks = cipherblocks.split(',')
    plainblocks = []
    for block in cipherblocks:
        M = pow(int(block), privateKey[1], privateKey[0])
        plainblocks.append(M)
    return blockToString(plainblocks)

def readKeysFromFile(filename):
    try:
        publicFile = open(f"{filename}_public.key", "r")
        privateFile = open(f"{filename}_private.key", "r")
    except FileNotFoundError:
        print("└─[File not find]")
        sys.exit()
    publicKey = publicFile.read()
    privateKey = privateFile.read()
    try:
        publicKey = publicKey.split(",")
        publicKey = int(publicKey[1]), int(publicKey[2])
        privateKey = privateKey.split(",")
        privateKey = int(privateKey[1]), int(privateKey[2])
    except IndexError:
        print("└─[Public file or Private File is Empty]")
        sys.exit()
    publicFile.close()
    privateFile.close()
    return publicKey, privateKey