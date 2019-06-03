##########################
# first three halvenings #
##########################

blocks_per_halvening = 210000
initial_subsidy = 50

print(blocks_per_halvening * initial_subsidy)

# exercise: how many satoshis before the first halvening?

# exercise: how many coins will be released before the 4th halvening?
coins_released = 0

coins_released += blocks_per_halvening * initial_subsidy
coins_released += blocks_per_halvening * (initial_subsidy / 2)
coins_released += blocks_per_halvening * (initial_subsidy / 4)

print(coins_released)

#################
# guessing game #
#################

from random import randint

number = randint(1, 11)
guess = None

while number != guess:
    guess = input('I am thinking of a number 1-10: ')
    guess = int(guess)

print('you got it!')

####################
# count halvenings #
####################

blocks_per_halvening = 210_000
sat_per_coin = 100_000_000
initial_subsidy = 50 * sat_per_coin
subsidy = initial_subsidy
coins_issued = 0
halvenings = 0

while subsidy >= 1:
    coins_issued += blocks_per_halvening * subsidy
    subsidy = subsidy / 2
    halvenings += 1
    print(coins_issued)

print(halvenings)
