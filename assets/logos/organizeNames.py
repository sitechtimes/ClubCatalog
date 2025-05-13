import os

# Set the path to your directory
directory = '.logos'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Only process files (not directories)
    if os.path.isfile(os.path.join(directory, filename)):
        name, ext = os.path.splitext(filename)

        # Find the rightmost dash
        if '-' in name:
            new_name = name.rsplit('-', 1)[0].strip() + ext

            # Full paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_name}')
