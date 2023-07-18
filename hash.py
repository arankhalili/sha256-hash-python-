import hashlib

#This program is a sha256 hash that when you add a 4-digit number to it,it gives you a 16-digit phrase that has encrypted your number.

def hashing(number):
    number_str = str(number).encode('utf-8')
    hash = hashlib.sha256(number_str)
    hash_hex = hash.hexdigest()
    return hash_hex
#In this part, it asks you for a 4-digit password:

hash1234 = hashing(input('give me a 4-digit number!'))
print(hash1234)

#you can copy this code and paste it in your python IDE to use it.
