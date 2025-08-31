import os

# Set the path to your directory (current directory where the script is located)
directory = '.'

print("Note: This script only changes file extensions to .png")
print("For actual image format conversion, you would need PIL/Pillow library")
print("-" * 60)

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Only process image files (not directories) and skip Python files and CSV files
    if (os.path.isfile(os.path.join(directory, filename)) and 
        not filename.endswith('.py') and 
        not filename.endswith('.csv') and
        not filename.endswith('.txt') and
        not filename.endswith('.md')):
        
        name, ext = os.path.splitext(filename)
        
        # Only process common image file extensions
        if ext.lower() not in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg']:
            print(f'Skipping non-image file: {filename}')
            continue

        # Find the rightmost dash and create new name
        if '-' in name:
            new_name = name.rsplit('-', 1)[0].strip().replace(' ', '').lower() + '.png'
        else:
            new_name = name.strip().replace(' ', '').lower() + '.png'

        # Full paths
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # Only rename if the new name is different
        if filename != new_name:
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_name}')
            except PermissionError as e:
                print(f'Permission denied: {filename} -> {new_name}')
            except FileExistsError as e:
                print(f'File already exists: {filename} -> {new_name}')
        else:
            print(f'No change needed: {filename}')

#import csv
#import json
#
#def parse_club_data(csv_filename):
#    clubs = []
#
#    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
#        reader = csv.DictReader(csvfile)
#        for row in reader:
#            club = {
#                "club_name": row["Club Name"],
#                "description": row["Club Description"],
#                "logo_link": row["Club Logo (Please title the file the name of your club)"],
#                "alt_text": row["Alt Text for Logo"]
#            }
#            clubs.append(club)
#
#    return clubs
#
#def save_to_json(data, json_filename):
#    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
#        json.dump(data, jsonfile, indent=4, ensure_ascii=False)
#
#if __name__ == "__main__":
#    csv_path = "descriptions.csv"
#    json_path = "../clubs.json"
#
#    clubs_data = parse_club_data(csv_path)
#    save_to_json(clubs_data, json_path)
#    print(f"✅ JSON file '{json_path}' created with {len(clubs_data)} clubs.")
#