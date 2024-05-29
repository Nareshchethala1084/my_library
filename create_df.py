#Code to Create a Dataframe and csv file with file locatioon, name and series
import os
import pandas as pd

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

#create a empty column to add the type
df['Type']=''

#create a empty column for numeric representation
df['Numeric']=''

#create a empty column for test
df['test']=''

# Add a new column with a series of numbers prefixed by 'FL' starting from 1
df['FL Number'] = ['FL' + str(i) for i in range(1, len(df) + 1)]

# Print the DataFrame name
print("DataFrame Name: df")
# Display the DataFrame
print(df)

# Ask user for the location to save the CSV file
csv_path = input("Enter the path to save the CSV file: ")

# Save the DataFrame to CSV
df.to_csv(csv_path, index=False)

print(f"CSV file saved successfully at '{csv_path}'")
