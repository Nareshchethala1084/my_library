#importing necessary libraries
import matplotlib.pyplot as plt #For plotting
import matplotlib.patches as patches  # For drawing shapes
import os  # For file and directory management
import pandas as pd  # For data manipulation and reading CSV files
import gc  # For garbage collection to free up memory

# Function to read font families from a CSV file
def read_font_families(csv_path, col_name):
    try:
        df = pd.read_csv(csv_path) #reads the csv and creates a dataframe
        return df[col_name].tolist() #returrns the created dataframe into a list
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return [] #if any errors then the code will give us the empty list

# Function to read names from a CSV file
def read_names(csv_path, col_name): 
    #using the user input for csv_path and csv_name this function generates the list of the names
    try:
        df = pd.read_csv(csv_path)  # Reads the CSV file into a DataFrame
        return df[col_name].tolist()  # Converts the specified column to a list
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []  # Return an empty list if an error occurs

# Function to generate rhombus-shaped images with centered text in batches
def generate_rhombus_images_in_batches(folder, names, fonts, width, height):
    #using the user input variables this function creates rhombus shape by trying each combination possible with the variables
    x_offset = width / 2  # Half-width for positioning
    y_offset = height / 2  # Half-height for positioning
    for name in names:  #For each name in the list of names
        for font_family in fonts: #For each name in the list of names combine with the font_family in fonts list
            for style in ['normal', 'italic', 'oblique']: #from the above line combination each combination further makes combination with style in the given list
                for line_width in range(2, 8): #from the above combination it further combines with line width of range 2-7(8 is excluded)
                    fig, ax = plt.subplots()  # Create a new figure and axes
                    # Define the vertices for the rhombus shape
                    vertices = [(0, -y_offset), (x_offset, 0), (0, y_offset), (-x_offset, 0)]
                    rhombus = patches.Polygon(vertices, closed=True, linewidth=line_width, edgecolor='black', facecolor='none')
                    ax.add_patch(rhombus)  # Add the rhombus to the axes

                    # Add centered text to the rhombus
                    ax.text(0, 0, name, fontsize=20, ha='center', va='center', fontfamily=font_family, fontstyle=style)

                    # Set plot limits to include some padding
                    padding = 0.1
                    ax.set_xlim(-x_offset - padding, x_offset + padding)
                    ax.set_ylim(-y_offset - padding, y_offset + padding)
                    ax.set_aspect('equal', adjustable='box')  # Keep the aspect ratio equal
                    ax.axis('off')  # Turn off the axes

                    # Create the file name and save the file as .png
                    file_name = f"{name}_{font_family.replace(' ', '_')}_{style}_{line_width}.png"
                    file_path = os.path.join(folder, file_name)
                    plt.savefig(file_path, dpi=300, bbox_inches='tight')  # Save the figure as a .png file
                    plt.close(fig)  # Close the figure to free up memory
                    gc.collect()  # Manually trigger garbage collection to free memory
                    print(f'Image saved: {file_path}')  # Print confirmation of image saved

# User inputs and setup
folder = input('Enter the path to save your images: ')  # Directory to save the images
names_csv_path = input('Enter the path to your CSV file with names: ')  # Path to the CSV file containing names
names_col_name = input('Enter the column name with names: ')  # Column name with names
font_csv_path = input('Enter the path to your CSV file with fonts: ')  # Path to the CSV file containing font families
font_col_name = input('Enter the column name with fonts: ')  # Column name with fonts
width = float(input("Please enter the width of the rhombus: "))  # Width of the rhombus
height = float(input("Please enter the height of the rhombus: "))  # Height of the rhombus

# Processing the data
try:
    names_list = read_names(names_csv_path, names_col_name)  # Read the names from the CSV file
    fonts_list = read_font_families(font_csv_path, font_col_name)  # Read the font families from the CSV file

    if not os.path.exists(folder):  # Check if the output folder exists
        os.makedirs(folder, exist_ok=True)  # Create the output folder if it doesn't exist

    generate_rhombus_images_in_batches(folder, names_list, fonts_list, width, height)  # Generate images in batches

    print('All images have been generated.')  # Print confirmation of successful generation
except Exception as e:
    print(f"Error: {e}")  # Print any error that occurs during processing
