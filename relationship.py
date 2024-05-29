import matplotlib.pyplot as plt
import matplotlib.patches as patches  # patches is a submodule of matplotlib to generate shapes
import os
import pandas as pd

# Define the directory and file name manually for demonstration purposes
folder = input('Enter/path/to/save:')

# Creating a DataFrame and then a list for the items in the CSV
csv_path = input('Path/to/your/file.csv:')
df = pd.read_csv(csv_path)
print(df)
col_name = input('Enter the column name with Names:')
nm_list = df[col_name].str.upper().to_list()

# Getting rhombus dimensions
width = float(input("Please Enter width of the rhombus:"))
height = float(input("Please Enter Height of the rhombus:"))
x_offset = width / 2
y_offset = height / 2

# Check if the directory exists, and if not, create it
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Create a figure and a single Axes object
for name in nm_list:
    fig, ax = plt.subplots()

    # Define vertices for a rhombus
    vertices = [(0, -y_offset), (x_offset, 0), (0, y_offset), (-x_offset, 0)]
    rhombus = patches.Polygon(vertices, closed=True, linewidth=7, edgecolor='black', facecolor='none')
    ax.add_patch(rhombus)

    # Calculate the center of the rhombus
    center_x = 0
    center_y = 0

    # Add centered text
    ax.text(center_x, center_y, name, fontsize=20, ha='center', va='center')

    # Set dynamic plot limits based on the rhombus's position and dimensions
    padding = 0.1  # Adjust padding as needed
    ax.set_xlim(-x_offset - padding, x_offset + padding)
    ax.set_ylim(-y_offset - padding, y_offset + padding)
    ax.set_aspect('equal', adjustable='box')

    # Create the file name and save the file as .png
    file_name = name.replace(" ", "_") + ".png"
    file_path = os.path.join(folder, file_name)

    # Save the figure
    plt.axis('off')  # Turn off the axis
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory

    # Returning the path for download
    print('Image saved at:', file_path)
