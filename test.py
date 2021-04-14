import csv
import random

with open('elements.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
print(random.sample(range(0, 16), 4))