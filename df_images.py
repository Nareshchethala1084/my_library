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

# Create a DataFrame with file names and locations
df = pd.DataFrame({'File Path': image_files})

# Function to create clickable links
def create_link(filepath):
    return f'<a href="file://{filepath}">{filepath}</a>'

# Apply the create_link function to the 'File Path' column
df['File Path'] = df['File Path'].apply(create_link)

# Display the HTML with clickable links
display(HTML(df.to_html(escape=False)))
