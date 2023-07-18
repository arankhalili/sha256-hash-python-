import hashlib

def hashing(number):
    number_str = str(number).encode('utf-8')
    hash = hashlib.sha256(number_str)
    hash_hex = hash.hexdigest()
    return hash_hex

hash1234 = hashing(input('give me a 4-digit number!'))
print(hash1234)