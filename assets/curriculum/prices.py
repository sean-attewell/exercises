from csv import DictReader, DictWriter
import csv
from decimal import Decimal
from pprint import pprint

csv_file = open('assets/prices.csv')

reader = DictReader(csv_file)

csv_file.close()

def spreads():
    csv_file = open('assets/prices.csv')
    reader = DictReader(csv_file)
    for line in reader:
        spread = Decimal(line['high']) - Decimal(line['low'])
        print(line['date'], spread)
    csv_file.close()

# exercise: change in last years closing price
# first solution uses if / else
# second solution uses next()


def percentage_increases():
    csv_file = open('assets/prices.csv')
    reader = DictReader(csv_file)
    reader = reversed(list(reader))
    last = next(reader)
    for current in reader:
        last_close = Decimal(last['close'])
        current_close = Decimal(current['close'])
        percent_change = ((current_close - last_close) / last_close) * 100
        print(percent_change)
        last = current
    csv_file.close()

# average close for each year
# exercise: average volume and mkt_cap over year
# generate a new csv representing values for the whole year ...

def high_price_every_year():
    csv_file = open('assets/prices.csv')
    reader = DictReader(csv_file)
    # import pdb; pdb.set_trace()
    print(next(reader))

def yearly_highs():
    # for each year: high, low, volume
    csv_file = open('assets/prices-extended.csv')
    reader = DictReader(csv_file)
    result = {}
    for line in reader:
        year_str = line['date'][-4:]
        high = Decimal(line['high'])

        # if we've already seen year, update result
        if year_str in result:
            result[year_str] = max(result[year_str], high)

        # else, initialize year values
        else:
            result[year_str] = high
    return result

def yearly_highs_lows():
    # for each year: high, low, volume
    csv_file = open('assets/prices-extended.csv')
    reader = DictReader(csv_file)
    result = {}
    for line in reader:
        year_str = line['date'][-4:]
        high = Decimal(line['high'])
        low = Decimal(line['low'])

        # if we've already seen year, update result
        if year_str in result:
            year = result[year_str]
            year['high'] = max(year['high'], high)
            year['low'] = min(year['low'], low)

        # else, initialize year values
        else:
            result[year_str] = {
                'high': high,
                'low': low,
            }

    return result

# exercise: give them the "else" case below

def yearly_summary():
    # for each year: high, low, volume
    csv_file = open('assets/prices-extended.csv')
    reader = DictReader(csv_file)
    result = {}
    for line in reader:
        year_str = line['date'][-4:]
        high = Decimal(line['high'])
        low = Decimal(line['low'])
        volume = int(line['volume'])

        # if we've already seen year, update result
        if year_str in result:
            year = result[year_str]
            year['high'] = max(year['high'], high)
            year['low'] = min(year['low'], low)
            year['volume'] += volume

        # else, initialize year values
        else:
            result[year_str] = {
                'high': high,
                'low': low,
                'volume': volume,
            }
    pprint(result)
    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['year', 'high', 'low', 'volume'])
        for year, values in result.items():
            writer.writerow([year, values['high'], 
                values['low'], values['volume']])


pprint(high_for_year())
