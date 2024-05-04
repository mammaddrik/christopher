import itertools
import os

def interactive(combinations):
    password_list = []
    counter = 0
    path = r"./passwordlist"
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir("./passwordlist")
    for i in range(1, len(combinations)):
        for subset in itertools.permutations(combinations, i):
            password = "".join(subset)
            password_list.append(password)
    with open(combinations[0]+".txt", "w") as file:
        for password in password_list:
            if not len(password) <=2:
                file.write(password + "\n")
                counter += 1
    print(f"└─[Output: wordlist of {counter} passwords created on ./passwordlist]")
    os.chdir("..")