# project 2
# program to generate hashes of string data using sha1,sha256 and sha512 hashlib

#generate hash using hashlib sha1

import hashlib
mystring = input('Enter string to hash: ')
hash_object = hashlib.sha1(mystring.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

#generate hash using hashlib sha256

import hashlib
mystring = input('Enter string to hash: ')
hash_object = hashlib.sha256(mystring.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

#generate hash using hashlib sha512

import hashlib
mystring = input('Enter string to hash: ')
hash_object = hashlib.sha512(mystring.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)