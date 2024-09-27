import csv
import json

# Load CSV file
csv_file_path = 'clubs.csv'  # Replace with your CSV file path
json_file_path = 'clubsdata.json'  # Output JSON file path

# Initialize a list to hold the club data
clubs_list = []

# Read the CSV file
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert the 'Category' field from a string to a list
        if 'Category' in row and row['Category']:
            row['Category'] = [category.strip() for category in row['Category'].split(',')]
        else:
            row['Category'] = []
        
        # Add the row to the clubs list
        clubs_list.append(row)

# Write the list to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(clubs_list, jsonfile, indent=4)