import os
import hashlib
try:
    from passlib.hash import nthash
    from Crypto.Hash import MD2, MD4
except ImportError:
    os.system("pip install -r requirements.txt")
import zlib

def bytes_to_str(password:str) -> bytes:
    """
    Converts the provided password from a string to bytes using UTF-8 encoding.

    Parameters:
    password (str): The password string to be converted.

    Returns:
    bytes: The UTF-8 encoded byte representation of the password.
    """
    return bytes(password, 'utf-8')

def print_hash(label: str, hash_value: str):
    """
    Prints the hash label and its corresponding hash value.

    Parameters:
    label (str): The label for the hash type (e.g., 'MD5 HASH').
    hash_value (str): The hexadecimal hash value to be printed.
    """
    print(f"{label}\t: {hash_value}")

def adler32_hash(password: str)-> str:
    """
    Computes the Adler-32 hash of the given password and returns it as a hexadecimal string.

    Parameters:
    password (str): The password to hash.

    Returns:
    str: The Adler-32 hash of the password in hexadecimal format.
    """
    return format(zlib.adler32(bytes_to_str(password)) & 0xFFFFFFFF, '08x')

def crc32_hash(password: str)-> str:
    """
    Computes the CRC32 hash of the given password and returns it as a hexadecimal string.

    Parameters:
    password (str): The password to hash.

    Returns:
    str: The CRC32 hash of the password in hexadecimal format.
    """
    return format(zlib.crc32(bytes_to_str(password)) & 0xFFFFFFFF, '08x')

def generate_hashes(password: str, hash_methods: str):
    """
    Computes and prints hashes for the given password using the specified hash methods.

    Parameters:
    password (str): The password to hash.
    hash_methods (list of str): A list of hash methods to use (e.g., ['md5', 'sha256']).

    For each hash method:
        - MD2 and MD4 hashes are computed using `pycryptodome`.
        - NTLM hash is computed using `passlib`.
        - Adler-32 and CRC32 hashes are computed using `zlib`.
        - For other hash methods, the `hashlib` library is used.
    """
    for method in hash_methods:
        if method == 'md2':
            h = MD2.new()
        elif method == 'md4':
            h = MD4.new()
        elif method == 'ntlm':
            print_hash('NTLM HASH', nthash.hash(password))
            continue
        elif method == 'adler32':
            print_hash('Adler-32', adler32_hash(password))
            continue
        elif method == 'crc32':
            print_hash('CRC32     ', crc32_hash(password))
            continue
        else:
            try:
                h = hashlib.new(method)
            except ValueError:
                print(f"Unsupported hash method: {method}")
                continue
        h.update(bytes_to_str(password))
        if method in ['shake_128', 'shake_256']:
            hash_value = h.hexdigest(16)
        else:
            hash_value = h.hexdigest()
        print_hash(f'{method.upper()} HASH', hash_value)

def hashgenerator(password: str, hashvalue: str):
    """
    Determines which hash methods to use based on the `hashvalue` argument and generates the corresponding hashes.

    Args:
    password (str): The password to hash.
    hashvalue (str): Specifies which hash methods to use. If "all", hashes for all supported methods are generated.

    If `hashvalue` is "all", the function generates hashes using all supported methods. Otherwise, it generates hashes using the specified method.
    """
    if hashvalue == "all":
        hash_methods = [
            'md2', 'md4', 'md5', 'sha1', 'sha224', 'sha256',
            'sha384', 'sha512', 'sha3_224', 'sha3_256',
            'sha3_384', 'sha3_512', 'shake_128', 'shake_256',
            'blake2b', 'blake2s', 'ntlm', 'adler32', 'crc32'
        ]
    else:
        hash_methods = [hashvalue]
    generate_hashes(password, hash_methods)