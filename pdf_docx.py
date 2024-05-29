from pdf2docx import Converter

# Get the PDF file path and output DOCX file path from the user
pdf_file = input("Enter the path to the PDF file: ")
docx_file = input("Enter the path to save the DOCX file: ")

# Create a Converter object
cv = Converter(pdf_file)

# Convert and save to a DOCX file
cv.convert(docx_file)
cv.close()

print(f"Conversion completed successfully. The DOCX file has been saved to: {docx_file}")

