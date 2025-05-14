#import os
#
## Set the path to your directory
#directory = '../logos'
#
## Loop through all files in the directory
#for filename in os.listdir(directory):
#    # Only process files (not directories)
#    if os.path.isfile(os.path.join(directory, filename)):
#        name, ext = os.path.splitext(filename)
#
#        # Find the rightmost dash
#        if '-' in name:
#            new_name = name.rsplit('-', 1)[0].strip() + ext
#
#            # Full paths
#            old_path = os.path.join(directory, filename)
#            new_path = os.path.join(directory, new_name)
#
#            # Rename the file
#            os.rename(old_path, new_path)
#            print(f'Renamed: {filename} -> {new_name}')
#
import csv
import json

def parse_club_data(csv_filename):
    clubs = []

    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            club = {
                "club_name": row["Club Name"],
                "description": row["Club Description"],
                "logo_link": row["Club Logo (Please title the file the name of your club)"],
                "alt_text": row["Alt Text for Logo"]
            }
            clubs.append(club)

    return clubs

def save_to_json(data, json_filename):
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    csv_path = "descriptions.csv"
    json_path = "../clubs.json"

    clubs_data = parse_club_data(csv_path)
    save_to_json(clubs_data, json_path)
    print(f"✅ JSON file '{json_path}' created with {len(clubs_data)} clubs.")
