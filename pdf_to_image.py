import os
from pdf2image import convert_from_path

# Ask user for the path to the folder containing PDF files
pdf_folder = input("Enter the path to the folder containing PDF files: ")

# Check if the entered path exists
if not os.path.isdir(pdf_folder):
    print(f"Error: '{pdf_folder}' is not a valid directory path.")
    exit()

# List all PDF files in the folder
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

if not pdf_files:
    print(f"No PDF files found in '{pdf_folder}'.")
else:
    # Convert each PDF file to images
    for pdf_file in pdf_files:
        # Full path to the PDF file
        pdf_path = os.path.join(pdf_folder, pdf_file)
        
        # Convert PDF to list of PIL Image objects
        images = convert_from_path(pdf_path)
        
        print(f"Detected {len(images)} pages in '{pdf_file}'.")  # Debugging
        
        # Save each page as a separate image file
        for i, image in enumerate(images):
            image.save(f'{pdf_file}_page_{i+1}.png', 'PNG')

    print("Conversion completed successfully.")

