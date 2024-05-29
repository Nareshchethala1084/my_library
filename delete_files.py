#this code is used to delete files from the local repository if they are not present in the csv file
#Please be carefull while using this code as it might delete other files if you mistype the location

import os
import csv

def list_subfolders(main_folder):
    subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir() and not f.name.startswith('.')]
    return subfolders

def get_image_paths_from_csv(csv_file, column_name):
    image_paths = []
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            image_paths.append(row[column_name])
    return image_paths

def delete_files_not_in_csv(csv_image_paths, subfolders):
    for folder_path in subfolders:
        try:
            folder_files = os.listdir(folder_path)
        except PermissionError as e:
            print(f"PermissionError: {e} - Skipped folder: {folder_path}")
            continue
        
        for file_name in folder_files:
            file_path = os.path.join(folder_path, file_name)
            if file_path not in csv_image_paths:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    main_folder = input('Please input Your main folder with Data Files')  # Specify your main folder path here
    csv_file = input('Please input path to your csv_file')
    column_name = input('Please input your Column name that has file path')

    subfolders = list_subfolders(main_folder)
    csv_image_paths = get_image_paths_from_csv(csv_file, column_name)
    delete_files_not_in_csv(csv_image_paths, subfolders)
