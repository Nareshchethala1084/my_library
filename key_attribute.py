#importing necessary libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
import os
import pandas as pd

# User input for Directory where the images will be saved
folder = input('Enter the path to save your images: ')

# Create a dataframe from the CSV and make a list of the names in the CSV
csv_path = input('Enter the path to your CSV file: ')
df = pd.read_csv(csv_path)
print(df)
col_name = input('Enter the column name with names: ')
nm_list = df[col_name].to_list()

# Get dimensions for the ellipse
x_center = 0.5  # Center of the ellipse (x coordinate)
y_center = 0.5  # Center of the ellipse (y coordinate)
width = float(input("Please enter the width of the ellipse: "))  # ideal width = 1.0
height = float(input("Please enter the height of the ellipse: "))  # ideal height = 0.5

# User input for vertical spacing between text and underline
vertical_spacing = float(input("Enter the vertical spacing between the text and the underline: "))

# Check if the directory exists, and if not, then create it
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Loop through each name in the list and create an ellipse image for each
for name in nm_list:
    fig, ax = plt.subplots()

    # Adding an ellipse with a black border
    ellipse = patches.Ellipse((x_center, y_center), width, height, linewidth=7, edgecolor='black', facecolor='none')
    ax.add_patch(ellipse)

    # Adding text within the ellipse
    text = ax.text(x_center, y_center, name, fontsize=20, ha='center', va='center')

    # Manually add an underline
    renderer = fig.canvas.get_renderer()
    text_extent = text.get_window_extent(renderer).transformed(ax.transData.inverted())
    text_width = text_extent.width  # Get text width in data coordinates
    text_height = text_extent.height  # Get text height to adjust the underline position

    line = Line2D([x_center - text_width / 2, x_center + text_width / 2],
                  [y_center - text_height / 2 - vertical_spacing, y_center - text_height / 2 - vertical_spacing],
                  color='black', linewidth=2)
    ax.add_line(line)

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
