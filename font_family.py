import csv
import os
import matplotlib.font_manager

# Fetching the list of font names
fonts = sorted(set(f.name for f in matplotlib.font_manager.fontManager.ttflist))

# Asking user for the path to save the file
filepath = input('Please input the directory path to save your file: ')
filename = input('Please enter the filename (e.g., available_fonts.csv): ')

if not filename:
    filename = 'available_fonts.csv'  # Default filename if user does not provide one

# Full path combining both filepath and filename
full_path = os.path.join(filepath, filename)

# Check if the directory exists, and if not, create it
if not os.path.exists(filepath):
    os.makedirs(filepath)  # Create the directory if it does not exist

# Writing to a CSV file
with open(full_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Font Name'])  # Writing header
    for font in fonts:
        writer.writerow([font])  # Writing each font name as a row

print(f'Saved the list of fonts into {full_path}')
