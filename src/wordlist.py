from itertools import product
import string
import os

def wordlist(min_len, max_len):
    counter = 0
    character = string.digits+string.ascii_letters
    path = r"./passwordlist"
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir("./passwordlist")
    with open("wordlist.txt", "w") as f:
        for i in range(min_len, max_len+1):
            for j in product(character, repeat=i):
                word = "".join(j)
                f.write(word+"\n")
                counter+=1
    print(f"└─[Output: wordlist of {counter} passwords created on ./passwordlist]")
    os.chdir("..")
