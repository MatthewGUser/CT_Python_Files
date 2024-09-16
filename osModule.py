# [ Task 1 ]

import os

def list_directory_contents(path):
    # Check if the provided path is valid
    if not os.path.exists(path):
        print(f"The directory '{path}' does not exist.")
        return

    if not os.path.isdir(path):
        print(f"The path '{path}' is not a directory.")
        return

    # List all files and subdirectories
    try:
        print(f"Contents of '{path}':")
        for root, dirs, files in os.walk(path):
            print(f"\nDirectory: {root}")
            if dirs:
                print("Subdirectories:")
                for d in dirs:
                    print(f"  {d}")
            if files:
                print("Files:")
                for f in files:
                    print(f"  {f}")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    user_path = input("Enter the directory path: ")
    list_directory_contents(user_path)
