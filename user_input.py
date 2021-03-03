# x = input('Enter a number: ')
# y = input('Enter a second number: ')

# product = float(x) * float(y)

# print(product)

# ---------------------

# x = input('Enter a number to find out if it\'s even or odd: ')

# is_even = float(x) % 2 == 0

# if is_even:
#     print('Even')
# else:
#     print('Odd')

# ---------------------

# def is_even(x):

#     even = x % 2 == 0

#     if even:
#         print('Even')
#     else:
#         print('Odd')

# x = input('Enter a number to find out if it\'s even or odd: ')
# x = float(x)

# is_even(x)

# ---------------------

def is_pos_or_neg(x):


    if x > 0:
        print('Positive')
    elif x < 0:
        print('Negative')
    else:
        print('zero')

x = input('Enter a number to find out if it\'s positive or negative: ')
x = float(x)

is_pos_or_neg(x)