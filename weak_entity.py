#importing necessary packages
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import pandas as pd

# Path for the directory where images will be saved
folder = input('Enter path to save:')

# Create a DataFrame from the CSV and create a list the items
csv_path = input('Path to your file.csv:')
df = pd.read_csv(csv_path)
print(df)
col_name = input('Enter the column name with Names:')
nm_list = df[col_name].to_list()

# Get user dimensions for the outer rectangle
x = 0.1
y = 0.1
width = float(input("Please Enter width of the outer rectangle:"))
height = float(input("Please Enter height of the outer rectangle:"))

#Uniform padding between the outer and inner rectangles
uniform_padding = 0.1 * min(width, height)  # For example, 10% of the smaller dimension

# Dimensions for the inner rectangle (smaller and centered)
inner_width = width - 2 * uniform_padding
inner_height = height - 2 * uniform_padding
inner_x = x + uniform_padding
inner_y = y + uniform_padding

# Check if the directory exists, and if not, create it
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Create images for each name in the list
for name in nm_list:
    fig, ax = plt.subplots()

    # Add the outer rectangle
    outer_rect = patches.Rectangle((x, y), width, height, linewidth=6, edgecolor='black', facecolor='none')
    ax.add_patch(outer_rect)

    # Add the inner rectangle
    inner_rect = patches.Rectangle((inner_x, inner_y), inner_width, inner_height, linewidth=6, edgecolor='black', facecolor='none')
    ax.add_patch(inner_rect)

    # Calculate the center of the inner rectangle for text placement
    center_x = inner_x + inner_width / 2
    center_y = inner_y + inner_height / 2

    # Add centered text within the inner rectangle
    ax.text(center_x, center_y, name, fontsize=18, ha='center', va='center')

    # Set plot limits and aspect ratio
    padding = 0.1
    ax.set_xlim(x - padding, x + width + padding)
    ax.set_ylim(y - padding, y + height + padding)
    ax.set_aspect('equal')

    # Create the file name and save the image
    file_name = name.replace(" ", "_") + ".png"
    file_path = os.path.join(folder, file_name)

    plt.axis('off')  # Turn off the axis
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory

    print('Image saved under :', file_path)
