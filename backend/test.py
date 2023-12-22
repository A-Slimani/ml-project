import csv

with open('./static/Australian Vehicle Prices.csv', 'r') as f:
    reader = csv.reader(f)
    print(next(reader))
    # for row in reader:
    #     print(row)