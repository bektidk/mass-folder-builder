import os

def create_folders(main_folder_path, folder_prefix, num_folders):
    """Creates a specified number of folders with a given prefix."""
    print("\n" + "-" * 40)
    print(f"Creating {num_folders} folders in: {main_folder_path}")
    print("-" * 40)

    # Ensure the main folder exists
    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)
        print(f"\n[Info] Main folder created at: {main_folder_path}")
    else:
        print(f"\n[Info] Main folder already exists at: {main_folder_path}")

    # Create the subfolders
    for i in range(1, num_folders + 1):
        folder_name = f"{folder_prefix}{i}"
        folder_path = os.path.join(main_folder_path, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"[Success] Folder '{folder_name}' created.")
        except FileExistsError:
            print(f"[Skip] Folder '{folder_name}' already exists.")

    print("\n" + "-" * 40)
    print("Process completed! Check your folders.")
    print("-" * 40)

if __name__ == "__main__":
    # Interactive user input
    print("-" * 40)
    print("Welcome to Mass Folder Builder!")
    print("-" * 40)

    main_folder_path = input("Enter the main folder path: ").strip()
    if not main_folder_path:
        print("[Error] Main folder path cannot be empty. Exiting...")
        exit()

    folder_prefix = input("Enter a prefix for the folders (leave blank for none): ").strip()
    if folder_prefix:
        folder_prefix += " "  # Add a space after the prefix if it's not empty

    try:
        num_folders = int(input("Enter the number of folders to create: ").strip())
        if num_folders <= 0:
            raise ValueError("The number of folders must be greater than 0.")
    except ValueError as e:
        print(f"[Error] Invalid input: {e}. Exiting...")
        exit()

    # Run the folder creation function only after all input is valid
    create_folders(main_folder_path, folder_prefix, num_folders)
