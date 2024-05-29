import os
import pandas as pd
from IPython.display import display, HTML

# Function to list all files recursively in a directory
def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# Ask user for the folder path
directory_path = input("Enter the path to the folder containing files: ")

# Check if the entered path exists
if not os.path.isdir(directory_path):
    print(f"Error: '{directory_path}' is not a valid directory path.")
    exit()

# List all files (including files in subdirectories)
files_list = list_files(directory_path)

# Filter only image files (you can adjust this based on your file extensions)
image_files = [file for file in files_list if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Extract filenames without the ".pdf_page_1" part
file_names = [os.path.splitext(os.path.basename(file))[0].replace('.pdf_page_1', '') for file in image_files]

# Create a DataFrame with file names and locations
df = pd.DataFrame({'File Name': file_names, 'File Path': image_files})

# Function to create clickable links
def create_link(row):
    return f'<a href="file://{row["File Path"]}">{row["File Name"]}</a>'

# Apply the create_link function to create clickable links in a new 'Link' column
df['Link'] = df.apply(create_link, axis=1)

# Display the HTML with clickable links
display(HTML(df[['Link']].to_html(escape=False)))

