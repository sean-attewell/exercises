##################
### calculator ###
##################

num1 = input('Enter a number: ')
num2 = input('Enter a another number: ')

result = int(num1) + int(num2)
print(result)

# allow decimals

result = float(num1) + float(num2)
print(result)

# exercse: change this calculator so that it does multiplication
# exercise: change this calculator so that it inputs 3 numbers

###################
### even or odd ###
###################

# have them comment out calculator

# introducing "if" statements
if True:
    print('true')
else:
    print('false')

# other conditions:
# ""
# "a"
# 1 == 2
# 1 < 2

# in repl
bool('')
bool('a')
bool(1 == 2)
bool(1 < 2)

# review modulus operator
print(5 % 2)
print(4 % 2)

# given a number, how would we determine if it is even or odd?
number = 5
if number % 2 == 0:
    print(number + ' is even')
else:
    print(number + 'is odd')

# say whether user input is even or odd
number = input('Enter a number: ')
if number % 2 == 0:
    print(number + ' is even')
else:
    print(number + 'is odd')

# print(), pow(), round() are called "functions"
# let's create one of our own

def hello():
    print('hello, world')

# turn it into a function
def even_or_odd(number):
    if number % 2 == 0:
        print(number + ' is even')
    else:
        print(number + 'is odd')

number = int(input('Enter a number: '))
even_or_odd(number)

# functions can do more than just print, they can "return"
# maybe do this first one in repl???

def hello():
    return 'hello, world'

hello()  # this would be confusing in REPL
print(hello())
x = hello()
print(x)

# turn it into a function
def even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input('Enter a number: '))
print(even_or_odd(number))

# we can write it even simpler
def is_even(number):
    return number % 2 == 0

number = int(input('Enter a number: '))
if is_even(number):
    print(number + ' is even')
else:
    print(number + 'is odd')

# exercise: positive or negative? 
