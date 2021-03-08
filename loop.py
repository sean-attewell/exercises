from collections import Counter

msg = 'cypherpunks write code'

vowels = 'aeiou'

# two ways to iterate

# for i in range(10):
#     print(i)

# for i in range(len(msg)):
#     char = msg[i]
#     if char not in vowels:
#         print(char)

# for char in msg:
#     if char not in vowels:
#         print(char)

#----------------
# result = ''

# for char in msg:
#     if char not in vowels:
#         result += char

# print(result)

#----------------

# result = []

# for char in msg:
#     if char not in vowels:
#         result.append(char)

# print(result)

#----------------

# result = 0

# for char in msg:
#     if char == 'e':
#         result += 1

# print(result)

#----------------

# result = {}

# for char in msg:
#     if char not in result:
#         result[char] = 1
#     else:
#         result[char] += 1

# print(result)

#----------------

result = Counter()

for char in msg:
    result[char] += 1

print(result.most_common(5))