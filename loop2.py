import random
import hashlib

# int.to_bytes(length, byteorder, *, signed=False)
# Return an array of bytes representing an integer.If byteorder is “big”, the most significant byte is at the beginning of the byte array. 
# If byteorder is “little”, the most significant byte is at the end of the byte array.
def hashed(d, n):
    d += n.to_bytes(4, 'little')
    return hashlib.sha256(d).hexdigest() # hash it and return the hex

# once you pass the below variables into the function, giv different names because they're no longer the same variable    
# bad form to reuse the name
# they're renamed in the function

data = b'real block info'
nonce = 1
count = 0
zeros_required = 5

# for i in range(100):
#     print(hashed(data, i))


while not hashed(data, nonce).startswith('0'*zeros_required):
    nonce +=1

print(nonce, hashed(data, nonce))

