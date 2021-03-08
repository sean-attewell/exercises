# import hashlib

# msg = input("Please enter a string for hashing: ")
# msg = msg.encode() # turn it into bytes

# hashed = hashlib.sha256(msg).hexdigest()

# print("The hash is: ", hashed)

import hashlib
import sys

filename = input("Please enter file name for hashing: ")

try:
    f = open(filename, 'rb') # 'w' cleared the file out! leave in read only. rb reads bytes.
except FileNotFoundError:
    print(filename + " not found!")
    sys.exit()

content = f.read()
f.close() # Good habit not to leave a bunch of open files on your system!

hashed = hashlib.sha256(content).hexdigest()

answer = '5146ac5310133fbb01439666131588006543ab5364435b748ddfc95a8cb8d63f'
if hashed == answer:
    print('File is legit')
else:
    print("File not legit")

    