
string = 'cypherpunks write code'

# in operator
print('i' in string)
print('z' in string)

# introduce for loops
vowels = 'aeiou'

for character in string:
    if character in vowels:
        print(character)

# iterate over a range

for i in range(len(string)):
    if string[i] in vowels:
        print(string[i])

# build up a result as we go
result = ''
for character in string:
    if character in vowels:
        result += character
print(result)

# introduce lists
l = [2, 1, 3]
print(l)
print(l[0])
print(l[2])
print(len(l))
print(sorted(l))
l.append(5)
print(l)

result = []
for character in string:
    if character in vowels:
        result.append(character)

# what if we don't want to count duplicates
result = []
for character in string:
    if character in vowels and character not in result:
        result.append(character)

# how to count the occurrence of various letters?
e_count = 0
for character in string:
    if character == 'e':
        e_count += 1
print(e_count)

# but how to count everything? introduce dictionaries

d = {'first': 'Justin', 'last': 'Moon'}
print(d)
print(d['first'])
print(d['last'])
print('age' in d)
d['age'] = 30
print(d)
print(d['age'])
print('age' in d)

# count letter occurrences
counts = {}
for character in string:
    if character in counts:
        counts[character] += 1
    else:
        counts[character] = 1
print(counts)

# there's also a magical collections.Counter object that will handle that if statement for us
# we'll use this shortly
from collections import Counter

counts = Counter()
for character in string:
    counts[character] += 1
print(counts)
