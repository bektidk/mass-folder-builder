```python
import os

def create_folders(main_folder_path, num_folders=1000):
    # Ensure the main folder exists
    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)
        print(f"Main folder created at {main_folder_path}")
    else:
        print(f"Main folder already exists at {main_folder_path}")

    # Create the subfolders
    for i in range(1, num_folders + 1):
        folder_path = os.path.join(main_folder_path, str(i))
        try:
            os.makedirs(folder_path)
            print(f"Folder '{i}' created.")
        except FileExistsError:
            print(f"Folder '{i}' already exists.")

# Specify the main folder path here
main_folder_path = "G:/My Folder"  # Change this path as needed

# Run the function
create_folders(main_folder_path)
