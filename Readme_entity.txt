Image Generation Script for Business Names
==========================================

Description:
------------
This Python script automates the creation of images of entities. The text for each rectangle is collected from a specified column in the CSV file.
You can generate the nouns using chatgpt or if any other sources.
Each rectangle is saved as a separate image file in a user-defined directory.

Features:
---------
- Dynamically reads names from a CSV file.
- Generates images with a rectangle for each name, with the name centered within the rectangle.
- Allows customization of rectangle dimensions.
- Supports setting a specific save directory for images.

How to Use:
-----------
1. Run the script.
2. Input the path where the images should be saved when prompted.
3. Input the full path to your CSV file containing the names.
4. Specify the column name in the CSV that contains the names.
5. Enter the desired width and height for the rectangles.(width = 1.0 and height = 0.6 are the ideal parameters to use)

Output:
-------
The script will save each generated image in the specified directory. Each image will feature a rectangle with a name centered inside. The image files are named after the respective names in the CSV file, with spaces replaced by underscores.

Requirements:
-------------
- Python
- matplotlib for plotting
- pandas for reading CSV files
