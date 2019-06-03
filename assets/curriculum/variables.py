# contains repeating information
print('Satoshi sent Hal Finney the first ever bitcoin transaction. Some think Hal Finney was Satoshi')

# reapeating information can be abstracted into "variables"
satoshi = 'Satoshi'
print(satoshi + ' sent Hal Finney the first ever bitcoin transaction. Some think Hal Finney was ' + satoshi)

# exercise: make a "hal" variable
hal = 'Hal Finney'
print(satoshi + ' sent ' + hal + ' the first ever bitcoin transaction. Some think ' + hal +' was ' + satoshi)

# indexing
print(hal[0])

# exercise: get the 'F'
print(hal[4])

# reverse indexing
print(hal[-1])

# exercise: get the 'F' with reverse indexing
print(hal[-6])

# what's the 'index' of 'e'?
print(hal.index('e'))

# where does the last hal start?
print(hal.index('Finney'))

# what about happens if we don't give it a variable
print(hal.index())

# we can mutate the 'hal' variable
hal.replace('Hal', 'Harold')
print(hal)

# separate the different parts of the string (a list)
print(hal.split())

# introduce the REPL
