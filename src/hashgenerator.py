import os
import hashlib
from passlib.hash import nthash
try:
    from Crypto.Hash import MD2, MD4
except ImportError:
    os.system("pip install -r requirements.txt")
import zlib

def hashgenerator(password, hashvalue):
    if hashvalue == "md2":
        setpass = bytes(password, 'utf-8')
        md2 = MD2.new()
        md2.update(setpass)
        print(f"└─[MD2 HASH] {md2.hexdigest()}")

    elif hashvalue == "md4":
        setpass = bytes(password, 'utf-8')
        md4_hash = MD4.new()
        md4_hash.update(setpass)
        print(f"└─[MD4 Hash] {md4_hash.hexdigest()}")

    elif hashvalue == "NTLM":
        hash_NTLM = nthash.hash(password)
        print(f"└─[NTLM HASH] {hash_NTLM}")

    elif hashvalue == "adler32":
        def adler32_hash(password):
            setpass = bytes(password, 'utf-8')
            adler32_checksum = zlib.adler32(setpass)
            return format(adler32_checksum & 0xFFFFFFFF, '08x')
        adler32_checksum = adler32_hash(password)
        print(f"└─[Adler-32 Checksum] {adler32_checksum}")

    elif hashvalue == "crc32":
        def crc32_hash(password):
            setpass = bytes(password, 'utf-8')
            crc32_checksum = zlib.crc32(setpass)
            return format(crc32_checksum & 0xFFFFFFFF, '08x')
        crc32_checksum = crc32_hash(password)
        print(f"└─[CRC32 checksum] {crc32_checksum}")

    elif hashvalue == "all":
        setpass = bytes(password, 'utf-8')
        md2 = MD2.new()
        md2.update(setpass)
        print(f"├─[    MD2   HASH    ] {md2.hexdigest()}")

        md4_hash = MD4.new()
        md4_hash.update(setpass)
        print(f"├─[    MD4   Hash    ] {md4_hash.hexdigest()}")

        hash_md5 = hashlib.md5(password.encode())
        print(f"├─[    MD5   HASH    ] {hash_md5.hexdigest()}")

        hash_sha1 = hashlib.sha1(password.encode())
        print(f"├─[    SHA1  HASH    ] {hash_sha1.hexdigest()}")

        hash_sha224 = hashlib.sha224(password.encode())
        print(f"├─[  SHA-224   HASH  ] {hash_sha224.hexdigest()}")

        hash_sha256 = hashlib.sha256(password.encode())
        print(f"├─[  SHA-256   HASH  ] {hash_sha256.hexdigest()}")

        hash_sha384 = hashlib.sha384(password.encode())
        print(f"├─[  SHA-384   HASH  ] {hash_sha384.hexdigest()}")

        hash_sha512 = hashlib.sha512(password.encode())
        print(f"├─[  SHA-512   HASH  ] {hash_sha512.hexdigest()}")

        hash_sha3_224 = hashlib.sha3_224(password.encode())
        print(f"├─[  sha3-224  HASH  ] {hash_sha3_224.hexdigest()}")

        hash_sha3_256 = hashlib.sha3_256(password.encode())
        print(f"├─[  SHA3-256  HASH  ] {hash_sha3_256.hexdigest()}")

        hash_sha3_384 = hashlib.sha3_384(password.encode())
        print(f"├─[  SHA3-384  HASH  ] {hash_sha3_384.hexdigest()}")

        hash_sha3_512 = hashlib.sha3_512(password.encode())
        print(f"├─[  SHA3-512  HASH  ] {hash_sha3_512.hexdigest()}")

        hash_shake_128 = hashlib.shake_128(password.encode())
        print(f"├─[  SHAKE-128 HASH  ] {hash_shake_128.hexdigest(16)}")

        hash_shake_256 = hashlib.shake_256(password.encode())
        print(f"├─[  SHAKE-256 HASH  ] {hash_shake_256.hexdigest(16)}")

        hash_blake2b = hashlib.blake2b(password.encode())
        print(f"├─[  blake2b   HASH  ] {hash_blake2b.hexdigest()}")

        hash_blake2s = hashlib.blake2s(password.encode())
        print(f"├─[  blake2s   HASH  ] {hash_blake2s.hexdigest()}")

        hash_NTLM = nthash.hash(password)
        print(f"├─[    NTLM  HASH    ] {hash_NTLM}")

        def adler32_hash(password):
            setpass = bytes(password, 'utf-8')
            adler32_checksum = zlib.adler32(setpass)
            return format(adler32_checksum & 0xFFFFFFFF, '08x')
        adler32_checksum = adler32_hash(password)
        print(f"├─[ Adler32 checksum ] {adler32_checksum}")

        def crc32_hash(password):
            setpass = bytes(password, 'utf-8')
            crc32_checksum = zlib.crc32(setpass)
            return format(crc32_checksum & 0xFFFFFFFF, '08x')
        crc32_checksum = crc32_hash(password)
        print(f"└─[ CRC-32  checksum ] {crc32_checksum}")

    else:
        setpass = bytes(password, 'utf-8')
        h = hashlib.new(hashvalue)
        h.update(setpass)
        Hash = h.hexdigest()
        print(f"└─[{hashvalue} Hash] {Hash}")



