#using this code we can merge two seperate csv files
#make sure to change the column names as per your requirements

import pandas as pd

# Load the first CSV file into a DataFrame
file_path1 = input('Please Enter the First File path:')
df1 = pd.read_csv(file_path1)

# Load the second CSV file into a DataFrame
file_path2 = input('Please Enter the Second File path:')
df2 = pd.read_csv(file_path2)

# Define the common columns based on which you want to merge
common_columns = ['File Name', 'File Path', 'Numeric', 'FL Number', 'Description', 'Test']

# Concatenate the DataFrames along rows (axis=0)
merged_df = pd.concat([df1, df2], ignore_index=True)

# Reassign FL Number column to have continuous numbering
merged_df['FL Number'] = ['FL' + str(i) for i in range(1, len(merged_df) + 1)]

# Print the merged DataFrame
print(merged_df)

# Ask user for the desired saving path for the merged CSV file
save_path = input("Enter the path to save the merged CSV file: ")

# Save the merged DataFrame to the desired path
merged_df.to_csv(save_path, index=False)

print(f"Merged CSV file saved successfully at '{save_path}'")
