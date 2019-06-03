from utils import sha256

# hash a string
hashed = sha256('funds not safu')
print(hashed)

def hash_text():
    # hash user input
    string = input('Enter a string for hashing: ')
    hashed = sha256(string)
    print('The hash of "' + string + '" is ' + hashed)

def hash_file():
    filename = input('Enter a filename for hashing: ')

    # do first w/o exception handling and demonstrate crash
    # then introduce exception handling here
    try:
        binary = open(filename, 'rb')
    except FileNotFoundError:
        print("File not found")
        return

    print(sha256(binary.read()))

hash_file()
