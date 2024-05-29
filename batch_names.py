import pandas as pd
import os

# Function to split and save CSV in batches
def save_batches(csv_path, col_name, output_folder, batch_size):
    try:
        df = pd.read_csv(csv_path)  # Read the entire CSV file into a DataFrame
        num_rows = len(df)  # Total number of rows
        batch_num = 1  # Initialize batch counter

        # Loop through DataFrame in increments of batch_size
        for i in range(0, num_rows, batch_size):
            batch_df = df[i:i + batch_size]  # Create a DataFrame slice for the current batch
            batch_file = os.path.join(output_folder, f'batch_{batch_num}.csv')  # Name the file for the batch
            batch_df.to_csv(batch_file, index=False)  # Save the batch DataFrame to a CSV file
            print(f'Saved {batch_file}')
            batch_num += 1  # Increment the batch counter

    except Exception as e:
        print(f"Error: {e}")

# User Inputs
csv_path = input('Enter the path to your input CSV file: ')  # Input CSV file path
output_folder = input('Enter the path to save batch files: ')  # Folder to save the batch CSV files
batch_size = int(input("Enter the batch size (number of rows per file): "))  # Batch size

# Check if the output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder, exist_ok=True)

# Process the CSV in batches
save_batches(csv_path, None, output_folder, batch_size)
