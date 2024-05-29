import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Path for the directory where the image will be saved
folder = input('Path/to/save/image:')

# Direct user input for the name to be displayed in the image
name = input('Enter the name to display:')
name = name.upper()  # Convert the name to uppercase

# Get user dimensions for the outer rhombus
x_center = 0.5  # Center of the rhombus
y_center = 0.5
outer_width = float(input("Please Enter width of the outer rhombus:"))
outer_height = float(input("Please Enter height of the outer rhombus:"))

# Uniform padding between the outer and inner rhombuses
uniform_padding = 0.1 * min(outer_width, outer_height)

# Dimensions for the inner rhombus
inner_width = outer_width - 2 * uniform_padding
inner_height = outer_height - 2 * uniform_padding

# Check if the directory exists, and if not, create it
if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)

# Creating a single image
fig, ax = plt.subplots()

# Define vertices for the outer rhombus
outer_vertices = [(x_center, y_center - outer_height / 2), (x_center + outer_width / 2, y_center),
                  (x_center, y_center + outer_height / 2), (x_center - outer_width / 2, y_center)]
outer_rhombus = patches.Polygon(outer_vertices, closed=True, linewidth=6, edgecolor='black', facecolor='none')
ax.add_patch(outer_rhombus)

# Define vertices for the inner rhombus
inner_vertices = [(x_center, y_center - inner_height / 2), (x_center + inner_width / 2, y_center),
                  (x_center, y_center + inner_height / 2), (x_center - inner_width / 2, y_center)]
inner_rhombus = patches.Polygon(inner_vertices, closed=True, linewidth=4, edgecolor='black', facecolor='none')
ax.add_patch(inner_rhombus)

# Add centered text within the inner rhombus
ax.text(x_center, y_center, name, fontsize=20, ha='center', va='center')

# Set plot limits and aspect ratio
ax.set_xlim(x_center - outer_width / 2 - 0.1, x_center + outer_width / 2 + 0.1)
ax.set_ylim(y_center - outer_height / 2 - 0.1, y_center + outer_height / 2 + 0.1)
ax.set_aspect('equal')

# Create the file name and save the image
file_name = name.replace(" ", "_") + ".png"
file_path = os.path.join(folder, file_name)

# Save the image in the filepath
plt.axis('off')  # Turn off the axis
plt.savefig(file_path, dpi=300, bbox_inches='tight')
plt.close(fig)  # Close the figure to free memory

# Print the location of saved image
print('Image saved under:', file_path)
