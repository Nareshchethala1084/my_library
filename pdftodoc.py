from pdf2docx import Converter
import os

# Get user input for the file paths
pdf_file = input("Enter the full path to the PDF file: ")
output_filename = input("Enter the name for the DOCX file (without extension): ")
download_location = input("Enter the download location (directory path): ")

# Construct the output file path
docx_file = os.path.join(download_location, f"{output_filename}.docx")

# Create a converter object
cv = Converter(pdf_file)

# Convert the PDF to DOCX
cv.convert(docx_file, start=0, end=None)

# Close the converter
cv.close()

print(f"Conversion complete! The DOCX file is saved at {docx_file}")

