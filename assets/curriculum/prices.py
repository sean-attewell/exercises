from csv import DictReader

csv_file = open('assets/prices.csv')

reader = DictReader(csv_file)

csv_file.close()
