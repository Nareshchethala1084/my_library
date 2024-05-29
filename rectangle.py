import matplotlib.pyplot as plt
import matplotlib.patches as patches #patches is a subplot of matplotlib to generate shapes
import os
import pandas as pd

# Define the directory and file name manually for demonstration purposes
folder = input('Enter/path/to/save:')

#creating a df and then list for the items in the csv
csv_path = input('Path/to/your/file.csv:')
df = pd.read_csv(csv_path)
print(df)
col_name = input('Enter the column name with Names:')
nm_list = df[col_name].to_list()

#getting rectangle dimensions
x = 0.1
y = 0.1
width = float(input("Please Enter width of the rectangle:"))
height = float(input("Please Enter Height of the rectangle:"))

# Check if the directory exists, and if not, create it
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Create a figure and a single Axes object
for name in nm_list:
    fig, ax = plt.subplots()

    # Add a rectangle with a black border and increased thickness
    rect = patches.Rectangle((x, y), width, height, linewidth=7, edgecolor='black', facecolor='none')
    ax.add_patch(rect)

    # Calculate the center of the rectangle
    center_x = x + width / 2
    center_y = y + height / 2

    # Add centered text
    ax.text(center_x, center_y, name, fontsize=24, ha='center', va='center')

    # Set dynamic plot limits based on the rectangle's position and dimensions
    padding = 0.1  # Adjust padding as needed
    ax.set_xlim(x - padding, x + width + padding)
    ax.set_ylim(y - padding, y + height + padding)
    ax.set_aspect('equal')

    #Create the file name and save the file as .png
    file_name = name.replace(" ", "_") + ".png"
    file_path = os.path.join(folder, file_name)

    # Save the figure
    plt.axis('off')  # Turn off the axis
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory

    # Returning the path for download
    file_path
