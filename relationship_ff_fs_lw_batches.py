import matplotlib.pyplot as plt
import matplotlib.patches as patches  # For drawing shapes
import os  # For file and directory management
import pandas as pd  # For data manipulation and reading CSV files
import gc  # For garbage collection to free up memory

# Function to read names from a CSV file
def read_names(csv_path, col_name):
    try:
        df = pd.read_csv(csv_path)  # Reads the CSV file into a DataFrame
        return df[col_name].str.upper().tolist()  # Converts the specified column to uppercase and returns it as a list
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []  # Return an empty list if an error occurs

# Function to generate rhombus-shaped images with centered text in batches
def generate_rhombus_images_in_batches(folder, names, width, height, batch_size):
    x_offset = width / 2  # Half-width for positioning
    y_offset = height / 2  # Half-height for positioning

    # Loop through the names list in batches of 'batch_size'
    for i in range(0, len(names), batch_size):
        batch_names = names[i:i + batch_size]  # Get the current batch of names

        for name in batch_names:
            fig, ax = plt.subplots()  # Create a new figure and axes

            # Define the vertices for the rhombus shape
            vertices = [(0, -y_offset), (x_offset, 0), (0, y_offset), (-x_offset, 0)]
            rhombus = patches.Polygon(vertices, closed=True, linewidth=7, edgecolor='black', facecolor='none')
            ax.add_patch(rhombus)  # Add the rhombus to the axes

            # Add centered text to the rhombus
            ax.text(0, 0, name, fontsize=20, ha='center', va='center')

            # Set plot limits to include some padding
            padding = 0.1
            ax.set_xlim(-x_offset - padding, x_offset + padding)
            ax.set_ylim(-y_offset - padding, y_offset + padding)
            ax.set_aspect('equal', adjustable='box')  # Keep the aspect ratio equal
            ax.axis('off')  # Turn off the axes

            # Create the file name and save the file as .png
            file_name = name.replace(" ", "_") + ".png"
            file_path = os.path.join(folder, file_name)
            plt.savefig(file_path, dpi=300, bbox_inches='tight')  # Save the figure as a .png file
            plt.close(fig)  # Close the figure to free up memory
            gc.collect()  # Manually trigger garbage collection to free memory
            print(f'Image saved: {file_path}')  # Print confirmation of image saved

# User inputs and setup
folder = input('Enter the path to save your images: ')  # Directory to save the images
csv_path = input('Enter the path to your CSV file with names: ')  # Path to the CSV file containing names
col_name = input('Enter the column name with names: ')  # Column name with names
width = float(input("Please enter the width of the rhombus: "))  # Width of the rhombus
height = float(input("Please enter the height of the rhombus: "))  # Height of the rhombus
batch_size = int(input("Enter the batch size for processing names: "))  # Number of names to process in one batch

# Processing the data
try:
    names_list = read_names(csv_path, col_name)  # Read the names from the CSV file
    if not os.path.exists(folder):  # Check if the output folder exists
        os.makedirs(folder, exist_ok=True)  # Create the output folder if it doesn't exist
    generate_rhombus_images_in_batches(folder, names_list, width, height, batch_size)  # Generate images in batches
    print('All images have been generated.')  # Print confirmation of successful generation
except Exception as e:
    print(f"Error: {e}")  # Print any error that occurs during processing
