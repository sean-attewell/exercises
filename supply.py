sat_per_coin = 100_000_000
subsidy = 50 * sat_per_coin
blocks_per_halvening = 210_000
coins_released = 0
halvenings = 0

while subsidy >= 1: # can't give out less than 1 satoshi! I'll give satoshis until I can't give them any more!
    coins_released += subsidy * blocks_per_halvening
    subsidy = subsidy // 2 # division which throws out remainders, because you can't have less than a sat
    halvenings += 1
    print(halvenings, subsidy)

print('halvenings: ', halvenings, 'coins_released: ', coins_released)

# The glory of deflation
