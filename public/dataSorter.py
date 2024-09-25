import csv
import json

with open('daaa.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

with open('yes.json', 'w') as f:
    json.dump(data, f, indent=4)
