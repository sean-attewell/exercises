# introduce the repl in this section

# you can print them
print(2)

# decimals work, too
print(2.1)

# negative numbers work, too
print(-2.1)

# math operations
print(1 + 2)
print(1 - 5)
print(3 * 4)
print(35 / 7)

# exponentials
print(3**2)

# order of operations
print(3 + 4 - 5)
print((3 + 4) - 5)

# equality vs assignment
print(1 == 1)
print(1 = 1)
print(a == 1)
print(a = 1)
print(a == 1)

# exercise: get this to evaluate True w/o typing "1"
print(1 == 'FIXME')

# some other operators (this one very important in bitcoin)
print(10 % 3)

# bitcoin uses this number as the modulus to keep signatures from getting too big
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
big_number = 105936749493397165751943248390023977685888340619776708311600296471039819517671

print(big_number ** 10)
print(big_number ** 10 > N)
print(big_number ** 10 % N)
print(big_number ** 10 % N < N)

# strings and numbers are different types
print(type('10'))
print(type(10))

# we can convert types
# but they look the same when printed. does it do anything?
print(10)
print(str(10))

# useful formatting sentence like we did earlier
print(2009 + ' is the year bitcoin launched')       # causes error
print(str(2009) + ' is the year bitcoin launched')  # doesn't cause error

print(1 + '2')                                      # causes error
print(1 + int(2))                                   # doesn't cause error

print(10)
print(int(10))

# more operations
number = -10
print(abs(number))
print(pow(3, 2))

# max / min
print(max(18000, 5900))
print(min(18000, 5900))

# round
print(round(3.2))
print(round(3.8))

# i want to show you other functions that are available yet
print(floor(3.2))

# let's grab more functions
from math import *
print(floor(3.2))
print(ceil(3.2))
print(sqrt(9))
print(log(16))
print(e)
print(pow(e, log(16)))
print(log(16, 2))
print(pow(2, log(16, 2)))

# what will this be: log(100, 2)
