# project 3
# program to generate hashes of string data using salting with sha1,sha256 and sha512 hashlib

#generate hash using hashlib sha1 with salt
import hashlib, uuid
mystring = input('Enter string to hash: ')
salt = uuid.uuid4().hex
hashed_object = hashlib.sha1((mystring + salt).encode())
hex_dig = hashed_object.hexdigest()
print(hex_dig)

#generate hash using hashlib sha256 with salt

import hashlib, uuid
mystring = input('Enter string to hash: ')
salt = uuid.uuid4().hex
hashed_object = hashlib.sha256((mystring + salt).encode())
hex_dig = hashed_object.hexdigest()
print(hex_dig)

#generate hash using hashlib sha512 with salt

import hashlib, uuid
mystring = input('Enter string to hash: ')
salt = uuid.uuid4().hex
hashed_object = hashlib.sha512((mystring + salt).encode())
hex_dig = hashed_object.hexdigest()
print(hex_dig)

