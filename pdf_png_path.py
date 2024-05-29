#Code to convert pdf to png and also asks the specific folder to save the file
import os
from pdf2image import convert_from_path

# Ask user for the path to the folder containing PDF files
pdf_folder = input("Enter the path to the folder containing PDF files: ")

# Check if the entered path exists
if not os.path.isdir(pdf_folder):
    print(f"Error: '{pdf_folder}' is not a valid directory path.")
    exit()

# Extract the folder name
folder_name = os.path.basename(pdf_folder)

# Create a new folder to save converted images
output_folder = os.path.join(pdf_folder, f"{folder_name}_converted_images")
os.makedirs(output_folder, exist_ok=True)

# Ask user for the path to save converted image files
save_path = input("Enter the path to save the converted image files: ")

# Check if the save_path exists, if not create the folder
os.makedirs(save_path, exist_ok=True)

# List all PDF files in the folder
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

if not pdf_files:
    print(f"No PDF files found in '{pdf_folder}'.")
else:
    # Convert each PDF file to images
    for pdf_file in pdf_files:
        # Full path to the PDF file
        pdf_path = os.path.join(pdf_folder, pdf_file)
        
        # Convert PDF to list of PIL Image objects with a crop box
        images = convert_from_path(pdf_path, use_cropbox=True)
        
        print(f"Detected {len(images)} pages in '{pdf_file}'.")  # Debugging
        
        # Save each page as a separate image file in the specified folder
        for i, image in enumerate(images):
            image.save(os.path.join(save_path, f'{pdf_file}_page_{i+1}.png'), 'PNG')

    print(f"Conversion completed successfully. Images saved in the '{save_path}' folder.")
