import csv
import json
import re
from pathlib import Path

def camel_to_snake(name):
    """Convert camelCase or PascalCase to snake_case"""
    # Insert an underscore before any uppercase letter that follows a lowercase letter
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert an underscore before any uppercase letter that follows a lowercase letter or digit
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def standardize_field_name(field_name):
    """Convert field names to standardized snake_case format"""
    
    # Handle specific field mappings for consistency first
    field_mappings = {
        'Timestamp': 'timestamp',
        'Club Name': 'club_name',
        'Club Logo (Please title the file the same as club name)': 'logo_link',
        'Club Description': 'description',
        'Email Address': 'email_address',
        'Alt Text for Logo': 'alt_text',
        'Social Media handle(s)/Google Classroom code (Optional)': 'social_media',
        'Club Categories (Select all that apply)': 'categories',
        'Club President(s)': 'club_presidents',
        'Does the club start after sing': 'start_after_sing',
        'Room Number': 'room_number',
        'Club Advisor': 'club_adviser',  # Standardize to adviser
        'Meeting Day': 'meeting_day',
        'Meeting Frequency': 'meeting_frequency',
    }
    
    # Return mapped field if it exists
    if field_name in field_mappings:
        return field_mappings[field_name]
    
    # Otherwise, convert to snake_case
    # Remove special characters and replace spaces with underscores
    field_name = re.sub(r'[^\w\s]', '', field_name)
    field_name = field_name.replace(' ', '_')
    field_name = field_name.replace('__', '_')  # Remove double underscores
    
    # Convert to snake_case
    field_name = camel_to_snake(field_name)
    
    return field_name

def convert_csv_to_json(csv_file_path, json_file_path):
    """
    Convert CSV file to JSON with standardized field names
    
    Category formatting recommendations:
    - Best: Use pipe separator (|) - e.g., "STEM|Arts & Crafts|Literary"
    - Alternative: Use semicolon (;) - e.g., "STEM;Arts & Crafts;Literary"  
    - Acceptable: Use comma (,) - e.g., "STEM, Arts & Crafts, Literary"
      (Note: Comma separation requires careful handling due to CSV format conflicts)
    """
    
    clubs_data = []
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            # Use comma as delimiter (standard CSV)
            reader = csv.DictReader(csvfile, delimiter=',')
            
            # Get original fieldnames and create mapping
            original_fieldnames = reader.fieldnames
            field_mapping = {}
            
            print("Field name mappings:")
            for original_field in original_fieldnames:
                standardized_field = standardize_field_name(original_field)
                field_mapping[original_field] = standardized_field
                print(f"  '{original_field}' -> '{standardized_field}'")
            
            # Process each row
            for row_num, row in enumerate(reader, 1):
                club_data = {}
                
                for original_field, value in row.items():
                    standardized_field = field_mapping[original_field]
                    
                    # Clean up the value
                    if value:
                        value = value.strip()
                        
                        # Handle categories field (convert to array if contains separators)
                        if standardized_field == 'categories':
                            if '|' in value:
                                # Handle pipe-separated categories (recommended format)
                                value = [cat.strip() for cat in value.split('|') if cat.strip()]
                            elif ';' in value:
                                # Handle semicolon-separated categories (alternative)
                                value = [cat.strip() for cat in value.split(';') if cat.strip()]
                            elif ',' in value:
                                # Handle comma-separated categories with special handling for "Arts & Crafts"
                                # This is more complex due to CSV comma conflicts
                                categories = []
                                parts = value.split(',')
                                i = 0
                                while i < len(parts):
                                    part = parts[i].strip()
                                    # Check if this part ends with " &" and there's a next part
                                    if part.endswith(' &') and i + 1 < len(parts):
                                        # Combine with next part (e.g., "Arts &" + "Crafts")
                                        next_part = parts[i + 1].strip()
                                        combined = f"{part} {next_part}"
                                        categories.append(combined)
                                        i += 2  # Skip next part since we combined it
                                    else:
                                        categories.append(part)
                                        i += 1
                                value = [cat for cat in categories if cat]
                            elif value:
                                value = [value]
                            else:
                                value = []
                        
                        # Convert boolean-like strings
                        elif value.lower() in ['yes', 'true', '1']:
                            value = True
                        elif value.lower() in ['no', 'false', '0']:
                            value = False
                        
                        # Handle empty strings
                        elif value == '':
                            value = ""
                    else:
                        value = ""
                    
                    club_data[standardized_field] = value
                
                # Only add if we have a club name
                if club_data.get('club_name'):
                    clubs_data.append(club_data)
                else:
                    print(f"Warning: Skipping row {row_num} - no club name found")
        
        # Write to JSON file
        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(clubs_data, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"\nSuccessfully converted {len(clubs_data)} clubs from CSV to JSON")
        print(f"Output file: {json_file_path}")
        
        # Show sample of the first club
        if clubs_data:
            print(f"\nSample club data:")
            sample_club = clubs_data[0]
            for key, value in sample_club.items():
                print(f"  {key}: {value}")
        
        return True
        
    except Exception as e:
        print(f"Error converting CSV to JSON: {str(e)}")
        return False

def main():
    # Define file paths
    csv_file = "public/clubs.csv"
    json_file = "public/clubs.json"
    
    # Check if CSV file exists
    if not Path(csv_file).exists():
        # Try the main CSV file
        csv_file = "public/24-25 Approved Clubs - Approved Clubs Alphabetically.csv"
        if not Path(csv_file).exists():
            print("Error: No CSV file found. Please ensure you have:")
            print("  - public/clubs.csv, or")
            print("  - public/24-25 Approved Clubs - Approved Clubs Alphabetically.csv")
            return
    
    print(f"Converting CSV to JSON with standardized field names...")
    print(f"Input:  {csv_file}")
    print(f"Output: {json_file}")
    print("-" * 50)
    
    success = convert_csv_to_json(csv_file, json_file)
    
    if success:
        print("\n✅ Conversion completed successfully!")
        print("\nAll field names have been standardized to snake_case format.")
        print("The JSON file is ready to use in your Vue.js application.")
    else:
        print("\n❌ Conversion failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
