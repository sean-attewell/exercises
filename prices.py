import csv
from decimal import Decimal
from pprint import pprint

# f = open('assets/prices.csv')
f = open('assets/prices-extended.csv') # 'r' by default

# DictReader turns csv file you pass it into a dictionary
# Each row of the csv is now an OrderedDict, with the heading as the key
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
#         print('New Record! ', craziest_date, craziest_change, high, low) # starts at the top of file by defaul, which is 2019, so we reversed it

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


# high_prices = {} # year -> high price in year

# for row in reader:
#     year = row['date'][-4:]
#     day_high = Decimal(row['high'])

#     # look up the year in the dictionary. If it exists, the value at that year will just be set to where it already is. Otherwise make new year and set to day high.
#     high_prices[year] = high_prices.get(year, day_high)
    
#     # if day high is bigger than currently stored high price for year, set to day high
#     high_prices[year] = max(high_prices[year], day_high)

# print(high_prices)



data = {} # dict with years with values of a dict containing high and low values for the year, and total volume

for row in reader:
    year = row['date'][-4:]
    high = Decimal(row['high'])
    low = Decimal(row['low'])
    volume = Decimal(row['volume'])
    # either we've seen the year before or we haven't
    if year not in data:
        data[year] = {'year': year, 'high': high, 'low': low, 'volume': volume}  # initialise inc year redundancy
    else:
        data[year]['high'] = max(data[year]['high'], high)
        data[year]['low'] = min(data[year]['low'], low)
        data[year]['volume'] += volume

# pprint(data)

# Now want to write this dictionary of the summary to it's own csv file

f.close() # closing prices-extended.csv we used to make the dict

f = open('prices-yearly.csv', 'w') # don't forget write permission to make a file!
writer = csv.DictWriter(f, ['year', 'high', 'low', 'volume'])
writer.writeheader()

# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# year is the key, summary is the value (which is a dictionary)
# if we were using items() we could skip over first by saying for _, summary in data.items():

for summary in data.values(): # got headings on csv so just need to populate rows with values
    writer.writerow(summary)

f.close()


# for summary in data.values(): # got headings on csv so just need to populate rows with values
#     print(summary.values())