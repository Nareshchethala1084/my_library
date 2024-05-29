import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import pandas as pd

# Function to read font families from a CSV file
def read_font_families(csv_path, col_name):
    try:
        df = pd.read_csv(csv_path)
        return df[col_name].tolist()
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# User input for Directory where the images will be saved
folder = input('Enter the path to save your images: ')

# User input for CSV file paths and column names
csv_path_names = input('Enter the path to your CSV file with names: ')
csv_path_fonts = input('Enter the path to your CSV file with font families: ')
col_name_names = input('Enter the column name with names: ')
col_name_fonts = input('Enter the column name with font families: ')

# Create a dataframe from the names CSV and make a list of the names
try:
    df_names = pd.read_csv(csv_path_names)
    nm_list = df_names[col_name_names].tolist()
except Exception as e:
    print(f"Error reading names CSV file: {e}")
    nm_list = []

# Read font families from the CSV
font_families = read_font_families(csv_path_fonts, col_name_fonts)

# Get dimensions for the ellipse
x_center = 0.5  # Center of the ellipse (x coordinate)
y_center = 0.5  # Center of the ellipse (y coordinate)
try:
    width = float(input("Please enter the width of the ellipse: ")) # ideal width = 1.0
    height = float(input("Please enter the height of the ellipse: ")) # ideal height = 0.5
except ValueError:
    print("Invalid input for width or height. Using default values.")
    width = 1.0
    height = 0.5

# Check if the directory exists, and if not, then create it
try:
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
except Exception as e:
    print(f"Error creating directory: {e}")

# Initialize count for total images
total_images = 0

# Looping through each name and each font family, and create an attribute image for each combination
for name in nm_list:
    for font_family in font_families:
        for style in ['normal', 'italic', 'oblique']:
            for line_width in range(2, 8):  # Use a different variable name for line width iterator
                try:
                    fig, ax = plt.subplots()

                    # Adding an ellipse with a black border
                    ellipse = patches.Ellipse((x_center, y_center), width, height, linewidth=line_width, edgecolor='black', facecolor='none')
                    ax.add_patch(ellipse)

                    # Adding text within the ellipse with the current font family
                    ax.text(x_center, y_center, name, fontsize=20, family=font_family, style=style, ha='center', va='center')

                    # Set plot limits to ensure the entire ellipse is visible
                    ax.set_xlim(x_center - width / 2 - 0.1, x_center + width / 2 + 0.1)
                    ax.set_ylim(y_center - height / 2 - 0.1, y_center + height / 2 + 0.1)
                    ax.set_aspect('equal')  # This ensures the ellipse isn't distorted

                    # Construct the file path and save the image
                    file_name = f'{name}_{font_family.replace(" ", "_")}_{style}_{line_width}.png'
                    file_path = os.path.join(folder, file_name)
                    plt.axis('off')  # Turn off the axis
                    plt.savefig(file_path, dpi=300, bbox_inches='tight')
                    plt.close(fig)  # Close the figure to free memory

                    # Increment count for total images
                    total_images += 1

                    # Print the saved file path
                    print(f'Image saved under: {file_path}')
                except Exception as e:
                    print(f"Error generating image: {e}")
        else:
            print(f'Skipping unavailable font: {font_family}')

# Print total number of images generated
print(f'Total images generated: {total_images}')
