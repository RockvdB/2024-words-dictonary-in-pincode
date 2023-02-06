#!/usr/bin/env python3
################################################################################
# Description: genereer een md5 hash van file:  crypto_key_words.txt.
#                     ########################################
#                     ###         SHA256 Hash  test        ###
#                     ########################################
# Purpose:     make sha256 from file.
# Author:      Rick van den Berg
# Version:     1
################################################################################
#0123456789012345678901234567890123456789012345678901234567890123456789012345678
################################################################################
# Parameters:
#
################################################################################
# Python program to make SHA256 hash value of a file
import hmac
import hashlib 
import binascii

# filename = input("Enter the file name: ")
# with open(filename,"rb") as f:
#     bytes = f.read() # read file as bytes
#     # readable_hash = hashlib.md5(bytes).hexdigest()
#     # print(readable_hash)
#     hashed_string = hashlib.sha256(bytes).hexdigest()
#     print(hashed_string)
 
def signature(key, msg):
    key = binascii.unhexlify(key)
    msg = msg.encode()
    return hmac.new(key, msg, hashlib.sha256).hexdigest()
    #.upper()
 
 
print(signature("012345678901234567890123456789", "2048"))