import csv
from decimal import Decimal

# f = open('assets/prices.csv')
f = open('assets/prices-extended.csv')

# DictReader turns csv file you pass it into a dictionary
reader = csv.DictReader(f)

# % move in a day
# for row in reader:
#     date = row['date']
#     high = Decimal(row['high'])
#     low = Decimal(row['low'])
#     absolute_change = high - low
#     proportion_change = absolute_change / low
#     percent_change = proportion_change * 100
#     print(date, percent_change)


# find maximum value for absolute change in a day
# craziest_date = None
# craziest_change = 0 # % high above low


# for row in reversed(list(reader)):
#     date = row['date']
#     high = Decimal(row['high'])
#     low = Decimal(row['low'])
#     absolute_change = high - low
#     proportion_change = absolute_change / low
#     percent_change = proportion_change * 100
#     # update if now record set
#     # TODO: consider negative moves
#     if percent_change > craziest_change:
#         craziest_date = date
#         craziest_change = percent_change
#         print('New Record! ', craziest_date, craziest_change, high, low) # starts at the top of file, which is 2019

# print(craziest_date, craziest_change)


# high_prices = {} # year -> high price in year

# for row in reader:
#     year = row['date'][-4:]
#     high = Decimal(row['high'])
#     # either we've seen the year before or we haven't
#     if year not in high_prices:
#         high_prices[year] = high  # initialise
#     else:
#         high_prices[year] = max(high_prices[year], high)

# print(high_prices)


high_prices = {} # year -> high price in year

for row in reader:
    year = row['date'][-4:]
    day_high = Decimal(row['high'])

    # look up the year in the dictionary. If it exists it will be just set to itself. Otherwise make new year and set to day high.
    high_prices[year] = high_prices.get(year, day_high)
    
    # if day high is bigger than currently stored high price for year, set to day high
    high_prices[year] = max(high_prices[year], day_high)

print(high_prices)