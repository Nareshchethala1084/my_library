import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# User input for the directory to save the images
folder = input('Enter the path to save your image: ')

# User input for the name to display in the image
name = input('Enter the name to display: ')

# Get dimensions for the ellipse
x_center = 0.5  # Center of the ellipse (x coordinate)
y_center = 0.5  # Center of the ellipse (y coordinate)
width = float(input("Please enter the width of the ellipse: "))  # ideal width = 1.0
height = float(input("Please enter the height of the ellipse: "))  # ideal height = 0.5

# Font styles to iterate over
font_styles = ['normal', 'italic', 'oblique', 'serif', 'sans-serif']

# Line widths to iterate over
line_widths = range(2, 8)  # From 2 to 7 inclusive

# Check if the directory exists, and if not, create it
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Loop over each combination of font style and line width
for font_style in font_styles:
    for line_width in line_widths:
        fig, ax = plt.subplots()

        # Adding an ellipse with specified line width and black border
        ellipse = patches.Ellipse((x_center, y_center), width, height, linewidth=line_width, edgecolor='black', facecolor='none')
        ax.add_patch(ellipse)

        # Adding text within the ellipse, with specified font style
        ax.text(x_center, y_center, name, fontsize=20, ha='center', va='center', style=font_style)

        # Set plot limits to ensure the entire ellipse is visible
        ax.set_xlim(x_center - width / 2 - 0.1, x_center + width / 2 + 0.1)
        ax.set_ylim(y_center - height / 2 - 0.1, y_center + height / 2 + 0.1)
        ax.set_aspect('equal')  # Ensures the ellipse isn't distorted

        # Construct the file path and save the image
        file_name = f'{name.replace(" ", "_")}_{line_width}_{font_style}.png'
        file_path = os.path.join(folder, file_name)
        plt.axis('off')  # Turn off the axis
        plt.savefig(file_path, dpi=300, bbox_inches='tight')
        plt.close(fig)  # Close the figure to free memory

        # Print the saved file path
        print(f'Image saved under: {file_path}')

