<div id="top"></div>
<h1 align="center">
    <br>
    <a href="https://github.com/mammaddrik/christopher"><img src="https://i.postimg.cc/7h9CxC2V/christopher.png" alt="Garns logo" width="200" height="200"></a>
    <br>
    Christopher
    <br>
</h1>

<h3 align="center">Tool for Encryption & Decryption.</h3>

<p align="center">
    <a href="https://github.com/mammaddrik/christopher/releases">
    <img src="https://img.shields.io/github/release/mammaddrik/christopher.svg">
</p>

<p align="center">
    <img src="https://i.postimg.cc/Kjb1t7bF/christopher.png">
</p>

<details>
<summary>Contents</summary>

[Including](#Including)<br>
[Installation](#installation)<br>
[Usage](#usage)<br>
[License](#license)

</details>

<br>
This is a python script for cryptography and steganography that is compiled from ciphers. Each algorithm includes Encryption and Decryption.
<br>

What is Cryptography? [Here](https://en.wikipedia.org/wiki/Cryptography)<br>
What is Steganography? [Here](https://en.wikipedia.org/wiki/Steganography)

## Including
<details>

1. **Cryptography**
    - Atbash Cipher
    - Caesar Cipher
      - Encryption
      - Decryption
      - Crack
    - Affine Cipher
      - Encryption
      - Decryption
      - Crack
    - Vigenère Cipher
      - Encryption
      - Decryption
      - Crack
    - Revers Text
    - Play Fire Cipher
      - Encryption
      - Decryption
    - Rail Fence Cipher
      - Encryption
      - Decryption
      - Crack
    - Scytale Cipher
      - Encryption
      - Decryption
    - Polybius Square
      - Encryption
      - Decryption
    - Columnar Cipher
      - Encryption
      - Decryption
      - Crack
    - Simple Substitution Cipher
      - Encryption
      - Decryption
      - Crack
    - Baconian Cipher
    - Morse Code
    - Rot13 Cipher
    - One-Time Pad Cipher
      - Encryption
      - Decryption
    - Hash Function
      - Hash Generator
        - MD2
        - MD4
        - MD5
        - SHA1
        - SHA224
        - SHA256
        - SHA384
        - SHA512
        - sha3-224
        - sha3-256
        - sha3-384
        - sha3-512
        - shake-128
        - shake-256
        - blake2b
        - blake2s
        - NTLM
        - adler32
        - crc32
      - Hash Cracker
        - md5
        - sha1
        - sha256
        - sha384
        - sha512
      - Hash Identifier
    - Enigma Machine
    - AES(CBC)
      - Encryption
      - Decryption
    - Public Key Cipher
      - Encryption
      - Decryption
    - RSA
      - Encryption
      - Decryption
2. **Steganography**
    - Image
      - Encryption
      - Decryption
    - Audio
      - Encryption
      - Decryption
3. **Tools**
    - Password List
      - All Situations
      - Custom
    - Password Manager
      - Encryption
      - Decryption
      - Create CSV file
      - Add
      - Edit
      - Delete
    - Password generator
    - Frequency Analysis
</details>

## Installation
> **Note:** Christopher isn't compatible with python2, run it with python3 instead.<br>
> I suggest you definitely use [cmder](https://cmder.app/).
```
git clone https://github.com/mammaddrik/christopher.git
cd christopher
python pip install -r requirements.txt
python christopher.py
```
### requirements
| **requirements**  | **Command**  |
| ------------- | ------------- |
| pandas  | `python pip install pandas`  |
| pwinput  | `python pip install pwinput`  |
| pycryptodome  | `python pip install pycryptodome`  |
| passlib  | `python pip install passlib`  |
| rsa  | `python pip install rsa`  |
| stepic  | `python pip install stepic`  |
| eyed3  | `python pip install eyed3`  |

> **Note:** You may encounter an error while installing this requirements. If an error occurs, use the following command:
```
python -m pip install --upgrade pip
python pip install -r requirements.txt
```