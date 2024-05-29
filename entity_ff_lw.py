import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import pandas as pd
import gc  # Garbage collector for cleaning up memory

# Memory profiling import
from memory_profiler import profile

# Function to read font families from a CSV file
def read_font_families(csv_path, col_name):
    try:
        df = pd.read_csv(csv_path)
        return df[col_name].tolist()
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

@profile  # This decorator enables memory profiling for this function
def generate_images(folder, names, fonts):
    x = 0.1
    y = 0.1
    width = 1.0  # Default width
    height = 0.5  # Default height
    for name in names:
        # Ensure name is capitalized
        capitalized_name = name.upper()
        for font_family in fonts:
            for style in ['normal', 'italic', 'oblique']:
                for line_width in range(2, 8):
                    fig, ax = plt.subplots()
                    rect = patches.Rectangle((x, y), width, height, linewidth=line_width, edgecolor='black', facecolor='none')
                    ax.add_patch(rect)
                    center_x = x + width / 2
                    center_y = y + height / 2
                    ax.text(center_x, center_y, capitalized_name, fontsize=22, ha='center', va='center', family=font_family, style=style)
                    ax.set_xlim(x - 0.1, x + width + 0.1)
                    ax.set_ylim(y - 0.1, y + height + 0.1)
                    ax.set_aspect('equal', adjustable='box')
                    ax.axis('off')  # Hide axes
                    file_name = f"{capitalized_name}_{font_family.replace(' ', '_')}_{style}_{line_width}.png"
                    file_path = os.path.join(folder, file_name)
                    plt.savefig(file_path, dpi=300, bbox_inches='tight')
                    plt.close(fig)  # Close the figure to free up memory
                    gc.collect()  # Call garbage collector manually
                    print(f'Image saved: {file_path}')

# User inputs and setup
folder = input('Enter the path to save your images: ')
csv_path_names = input('Enter the path to your CSV file with names: ')
csv_path_fonts = input('Enter the path to your CSV file with font families: ')
col_name_names = input('Enter the column name with names: ')
col_name_fonts = input('Enter the column name with font families: ')

# Processing the data
try:
    df_names = pd.read_csv(csv_path_names)
    nm_list = df_names[col_name_names].str.upper().tolist()  # Ensuring names are capitalized right when reading
    font_families = read_font_families(csv_path_fonts, col_name_fonts)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    generate_images(folder, nm_list, font_families)
    print('All images have been generated.')
except Exception as e:
    print(f"Error: {e}")
