# import hashlib

# msg = input("Please enter a string for hashing: ")
# msg = msg.encode() # turn it into bytes

# hashed = hashlib.sha256(msg).hexdigest()

# print("The hash is: ", hashed)

import hashlib
import sys

filename = input("Please enter file name for hashing: ")

try:
    f = open(filename, 'r') # 'w' cleared the file out! leave in read only. 
except FileNotFoundError:
    print(filename + " not found!")
    sys.exit()

content = f.read()
f.close() # Good habit not to leave a bunch of open files on your system!

msg = content.encode() # Turn into bytes
hashed = hashlib.sha256(msg).hexdigest()

print("The hash is: ", hashed)