import csv

with open('elements.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
for x in data:
    print(x)