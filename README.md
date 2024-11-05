# Mass Folder Builder

The **Mass Folder Builder** repository contains a Python script to automatically create 1000 subfolders within a specified main folder. This is useful for quickly generating large sets of folders for organizing files or testing purposes.

## Features

- Creates a specified number of subfolders (default: 1000).
- Allows customization of the main folder path where subfolders will be generated.
- Numbered folder names (e.g., "1", "2", ..., "1000").

## Requirements

- Python 3.x installed on your system.

## Usage

### Step 1: Clone the Repository

To begin, clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/mass-folder-builder.git
cd mass-folder-builder
```

### Step 2: Modify the Main Folder Path (Optional)

Open the `create_folders.py` file. Update the `main_folder_path` variable if you wish to specify a different directory for the folders. For example:

```python
main_folder_path = "G:/My Folder"
```

If left as is, this will create the folders in the current working directory.

### Step 3: Run the Script

In your terminal or command prompt, navigate to the project directory and run the script:

```bash
python create_folders.py
```

### Step 4: Check the Result

After the script completes, you will find 1000 subfolders numbered sequentially from "1" to "1000" in the specified main folder.

## Example

For example, setting `main_folder_path = "G:/My Folder"` and running the script will result in 1000 folders created inside `G:/My Folder`, named `1`, `2`, `3`, ..., `1000`.

## Notes

- Ensure that the specified directory exists before running the script, as the script will not create the main folder if it does not already exist.
- Running the script multiple times will not overwrite existing folders but will notify you if they already exist.
