import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import pandas as pd

# Define the directory where the images will be saved
folder = input('Enter the path to save your images: ')

# Read data from the CSV file
csv_path = input('Enter the path to your CSV file: ')
df = pd.read_csv(csv_path)
print(df)
col_name = input('Enter the column name with names: ')
nm_list = df[col_name].to_list()

# Get dimensions for the ellipse
x_center = 0.5  # Center of the ellipse (x coordinate)
y_center = 0.5  # Center of the ellipse (y coordinate)
width = float(input("Please enter the width of the ellipse: "))
height = float(input("Please enter the height of the ellipse: "))

# Check if the directory exists, and if not, create it
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Create an ellipse image for each name in the list
for name in nm_list:
    fig, ax = plt.subplots()

    # Add an ellipse with a black border
    ellipse = patches.Ellipse((x_center, y_center), width, height, linewidth=7, edgecolor='black', facecolor='none')
    ax.add_patch(ellipse)

    # Add centered text within the ellipse
    ax.text(x_center, y_center, name, fontsize=20, ha='center', va='center')

    # Set plot limits to ensure the entire ellipse is visible
    ax.set_xlim(x_center - width / 2 - 0.1, x_center + width / 2 + 0.1)
    ax.set_ylim(y_center - height / 2 - 0.1, y_center + height / 2 + 0.1)
    ax.set_aspect('equal')  # This ensures the ellipse isn't distorted

    # Construct the file path and save the image
    file_name = name.replace(" ", "_") + ".png"
    file_path = os.path.join(folder, file_name)
    plt.axis('off')  # Turn off the axis
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory

    # Print the saved file path
    print(f'Image saved under: {file_path}')
