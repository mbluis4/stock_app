import csv

with open('../data/test.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        code = row[0]
        brand = row[1]
        print(code, brand)
