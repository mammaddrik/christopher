<div id="top"></div>
<h1 align="center">
    <br>
    <a href="https://github.com/mammaddrik/christopher"><img src="https://i.postimg.cc/7h9CxC2V/christopher.png" alt="christopher logo" width="200" height="200"></a>
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
    <img src="https://i.postimg.cc/VkJkrZtn/christopher.png">
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
    - Reverse Text
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
        - MD5
        - SHA1
        - SHA256
        - SHA384
        - SHA512
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
### <img src="https://i.postimg.cc/nLp4jWx0/Windows.png" width="15" height="15" alt="docker"/> Windows
> **Note:** Christopher isn't compatible with python2, run it with python3 instead.<br>
> I suggest you definitely use [cmder](https://cmder.app/).
```
git clone https://github.com/mammaddrik/christopher.git
cd christopher
python pip install -r requirements.txt
python christopher.py
```
Or you can download that exe file.
<p align="center">
    <img src="https://i.postimg.cc/R0t7NnNQ/christopher-Windows.png">
</p>

### <img src="https://cdn.simpleicons.org/docker/2496ED" width="15" height="15" alt="docker"/> Docker
install docker on your system. [docker](https://www.docker.com/)
```
docker build -t christopher .
docker run -ti christopher
```
<p align="center">
    <img src="https://i.postimg.cc/Y0vqCQSt/christopher-docker.png">
</p>

### <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/linux-colored.svg" width="15" height="15" alt="docker"/> Linux
> **Note:** Christopher isn't compatible with python2, run it with python3 instead.<br>
```
git clone https://github.com/mammaddrik/christopher.git
cd christopher
python pip install -r requirements.txt
python christopher.py
```
Or you can install it
```
git clone https://github.com/mammaddrik/christopher.git
cd christopher
python pip install -r requirements.txt
sudo chmod +x setup.sh
sudo bash setup.sh
christopher
```
> **Note:** If you get a permission denied error, use this comment: `bash christopher`<br>

<p align="center">
    <img src="https://i.postimg.cc/BQNM0DKj/christopher-Linux.png">
</p>

### requirements
| **Requirements**  | **Command**  | **Link**  | **Version**  |
| ------------- | ------------- | ------------- | ------------- |
| pandas  | `python pip install pandas`  | [pypi](https://pypi.org/project/pandas/)  | 2.2.2  |
| pwinput  | `python pip install pwinput`  | [pypi](https://pypi.org/project/pwinput/)  | 1.0.3  |
| pycryptodome  | `python pip install pycryptodome`  | [pypi](https://pypi.org/project/pycryptodome/)  | 3.20.0|
| passlib  | `python pip install passlib`  | [pypi](https://pypi.org/project/passlib/)  | 1.7.4  |
| rsa  | `python pip install rsa`  | [pypi](https://pypi.org/project/rsa/)  | 4.9  |
| stepic  | `python pip install stepic`  | [pypi](https://pypi.org/project/stepic/)  | 0.5.0  |
| eyed3  | `python pip install eyed3`  | [pypi](https://pypi.org/project/eyed3/)  | 0.9.7  |
> **Note:** You may encounter an error while installing this requirements. If an error occurs, use the following command.
```
python -m pip install --upgrade pip
python pip install -r requirements.txt
```

## Usage
After installing the script, you can choose options from the script.<br>


## License
Christopher is licensed under [MIT License](https://github.com/mammaddrik/christopher/blob/main/LICENSE).

<p align="right"><a href="#top">back to top</a></p>