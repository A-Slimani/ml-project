import csv

with open('FuelConsumption.csv', newline='') as file:
  reader = csv.reader(file)
  headers = next(reader)
  print(headers)