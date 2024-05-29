#importing necessary libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import pandas as pd

# Path for the directory where images will be saved
folder = input('Path/to/save/images:')

# Create a DataFrame from the CSV and create a list of the items
csv_path = input('Path/to/your/file.csv:')
df = pd.read_csv(csv_path)
print(df)
col_name = input('Enter the column name with Names:')
nm_list = df[col_name].str.upper().to_list()

# Get user dimensions for the outer ellipse
x_center = 0.5  # Center of the ellipse (x coordinate)
y_center = 0.5  # Center of the ellipse (y coordinate)
width = float(input("Please Enter width of the outer ellipse:"))  # ideal width = 1.0
height = float(input("Please Enter height of the outer ellipse:"))  # ideal height = 0.5

# Uniform padding between the outer and inner ellipses
uniform_padding = 0.1 * min(width, height)  # 10% of the minimum dimension

# Dimensions for the inner ellipse
inner_width = width - 2 * uniform_padding
inner_height = height - 2 * uniform_padding

# Checking for the directory, and if not, then we will create it to save the images
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Creating images for each name in the list from the dataframe
for name in nm_list:
    fig, ax = plt.subplots()

    # Add the outer ellipse
    outer_ellipse = patches.Ellipse((x_center, y_center), width, height, linewidth=6, edgecolor='black', facecolor='none')
    ax.add_patch(outer_ellipse)

    # Add the inner ellipse
    inner_ellipse = patches.Ellipse((x_center, y_center), inner_width, inner_height, linewidth=4, edgecolor='black', facecolor='none')
    ax.add_patch(inner_ellipse)

    # Add centered text within the inner ellipse
    ax.text(x_center, y_center, name, fontsize=20, ha='center', va='center')

    # Set plot limits and aspect ratio
    ax.set_xlim(x_center - width / 2 - 0.1, x_center + width / 2 + 0.1)
    ax.set_ylim(y_center - height / 2 - 0.1, y_center + height / 2 + 0.1)
    ax.set_aspect('equal')

    # Create the file name and replace spaces with underscores and save the image
    file_name = name.replace(" ", "_") + ".png"
    file_path = os.path.join(folder, file_name)

    # Save the image in the filepath
    plt.axis('off')  # Turn off the axis
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory

    # Print the location of saved image
    print('Image saved under :', file_path)
