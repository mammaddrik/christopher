import hashlib

def hashgenerator(password, hashvalue):
    setpass = bytes(password, 'utf-8')
    h = hashlib.new(hashvalue)
    h.update(setpass)
    Hash = h.hexdigest()
    print(f"└─[{hashvalue} Hash] {Hash}")