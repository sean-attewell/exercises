# ##########################
# # first three halvenings #
# ##########################

# blocks_per_halvening = 210000
# subsidy = 50

# print(blocks_per_halvening * subsidy)

# # exercise: how many satoshis before the first halvening?

# # exercise: how many coins will be released before the 4th halvening?
# coins_released = 0

# coins_released += blocks_per_halvening * subsidy
# subsidy = subsidy / 2
# coins_released += blocks_per_halvening * subsidy
# subsidy = subsidy / 2
# coins_released += blocks_per_halvening * subsidy

# print(coins_released)

# #################
# # guessing game #
# #################

# # v1
# import random

# data = b'real block info'
# nonce = 0
# answer = random.randint(0, 1000)

# while not nonce != answer:
    # nonce += 1

# print(nonce)

# # v2

# import hashlib


# def hashed(d, n):
    # d += n.to_bytes(4, 'little')
    # return hashlib.sha256(d).hexdigest()


# data = b'real block info'
# nonce = 0
# zeros_required = 6

# while not hashed(data, nonce).startswith('0'*zeros_required):
    # nonce += 1

# print(nonce, hashed(data, nonce))


# ####################
# # count halvenings #
# ####################

blocks_per_halvening = 210_000
sat_per_coin = 100_000_000
subsidy = 50 * sat_per_coin
coins_issued = 0
halvenings = 0

while subsidy >= 1:
    coins_issued += blocks_per_halvening * subsidy
    subsidy = subsidy // 2
    halvenings += 1
    print(subsidy, coins_issued)

print(halvenings)
