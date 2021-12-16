#!/usr/bin/env python3
import os, sys       # do not use any other imports/libraries

def bn(b):
    # b - bytes to encode as integer
    # your implementation here
    return int(str(b), 2)

def nb(i, length=None):
    # i - integer to encode as bytes
    # length - specifies in-how many bytes the number should be encoded
    # your implementation here
    # b = b''
    # while(i>0):
    #         x=(i&255) #take last 8 bits
    #         i=i>>8  #move bits to right
    #         b=bytes([x])+b
    
    # Implementation
    b = bin(i)
    
    # Removing first two elements
    b = b[2:]
    return b

def encrypt(pfile, kfile, cfile):
    # your implementation here
    # Read plain text
    
    # byte array -> int (use bn function)
    
    # plain text bit length and generate the same length key (os.urandom())
    
    # byte array -> int (use bn function)
    
    # ciphertext_int = plain_int ^ key_int
    
    # ciphertext_int -> byte array and write in file
    
    # key byte array write in file
    
    # ciphertext byte array write in file
    pass

def decrypt(cfile, kfile, pfile):
    # your implementation here 
    pass

def usage():
    print("Usage:")
    print("encrypt <plaintext file> <output key file> <ciphertext output file>")
    print("decrypt <ciphertext file> <key file> <plaintext output file>")
    sys.exit(1)

if len(sys.argv) != 5:
    usage()
elif sys.argv[1] == 'encrypt':
    encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == 'decrypt':
    decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    usage()