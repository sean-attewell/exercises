sat_per_coin = 100_000_000
initial_subsidy = 50 * sat_per_coin
blocks_per_halvening = 210_000
coins_released = 0

# print(initial_subsidy * blocks_per_halvening) # 10.5 million bitcoins given out in the first 4 years!
# print((initial_subsidy / 2) * blocks_per_halvening) # 5.25 million bitcoins given out in the next 4 years!
# print((initial_subsidy / 4) * blocks_per_halvening) # 2.625 million bitcoins given out in the next 4 years!

# add coins released in first era
coins_released += (initial_subsidy * blocks_per_halvening)

# add coins released in second era
coins_released += ((initial_subsidy / 2) * blocks_per_halvening)

# add coins released in third era
coins_released += ((initial_subsidy / 4) * blocks_per_halvening)


# 75% after 2 eras


print(coins_released)