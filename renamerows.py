#Code to Rename the file names from the column File Name
#Please check the name of the column and make changes accordingly

#importing pandas
import pandas as pd

#create a dataframe for the existing csv file
#Asking for the user path
file_path = input('File path:')

#creating a dataframe
df = pd.read_csv(file_path)

# Function to convert underscore-separated words to capitalized words
def convert_to_capitalized(word):
    words = word.split('_')
    capitalized_words = [w.capitalize() for w in words]
    return ' '.join(capitalized_words)

# Apply the conversion function to the column 'File Name' and create a new column 'Name'
#check your dataframe columns and make appropriate changes
df['Name'] = df['File Name'].apply(convert_to_capitalized)

# Ask user for the path to save the updated CSV file
updated_csv_path = input("Enter the path to save the updated CSV file: ")

# Save updated DataFrame to CSV
df.to_csv(updated_csv_path, index=False)

print(f"Updated CSV file saved successfully at '{updated_csv_path}'")
