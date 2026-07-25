from pathlib import Path

def create_folder():
    name = input("Enter folder name: ")
    path = Path(name)

    if not path.exists():
        path.mkdir()
        print("Folder created successfully.")
    else:
        print("Folder already exists.")

def read_folder():
    name = input("Enter folder name: ")
    path = Path(name)

    if path.exists() and path.is_dir():
        files = list(path.glob("*"))
        if files:
            print("\nFiles/Folders:")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file.name}")
        else:
            print("Folder is empty.")
    else:
        print("Folder not found.")

def rename_folder():
    old = input("Enter current folder name: ")
    new = input("Enter new folder name: ")

    old_path = Path(old)
    new_path = Path(new)

    if old_path.exists():
        old_path.rename(new_path)
        print("Folder renamed successfully.")
    else:
        print("Folder not found.")

def delete_folder():
    name = input("Enter folder name: ")
    path = Path(name)

    if path.exists() and path.is_dir():
        path.rmdir()
        print("Folder deleted successfully.")
    else:
        print("Folder not found or folder is not empty.")

def create_file():
    name = input("Enter file name (with extension): ")

    if not Path(name).exists():
        with open(name, "w") as file:
            data = input("Enter file content:\n")
            file.write(data)
        print("File created successfully.")
    else:
        print("File already exists.")

def read_file():
    name = input("Enter file name: ")

    if Path(name).exists():
        with open(name, "r") as file:
            print("\nFile Content:\n")
            print(file.read())
    else:
        print("File not found.")

def update_file():
    name = input("Enter file name: ")

    if Path(name).exists():

        print("\n1. Rename File")
        print("2. Append Data")
        print("3. Overwrite Data")

        choice = int(input("Enter choice: "))

        if choice == 1:
            new_name = input("Enter new file name: ")
            Path(name).rename(new_name)
            print("File renamed successfully.")

        elif choice == 2:
            with open(name, "a") as file:
                data = input("Enter data to append:\n")
                file.write("\n" + data)
            print("Data appended successfully.")

        elif choice == 3:
            with open(name, "w") as file:
                data = input("Enter new data:\n")
                file.write(data)
            print("File updated successfully.")

        else:
            print("Invalid choice.")

    else:
        print("File not found.")

def delete_file():
    name = input("Enter file name: ")
    path = Path(name)

    if path.exists():
        path.unlink()
        print("File deleted successfully.")
    else:
        print("File not found.")

while True:

    print("\n========== FILE MANAGEMENT SYSTEM ==========")
    print("1. Create Folder")
    print("2. Read Folder")
    print("3. Rename Folder")
    print("4. Delete Folder")
    print("5. Create File")
    print("6. Read File")
    print("7. Update File")
    print("8. Delete File")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_folder()

    elif choice == 2:
        read_folder()

    elif choice == 3:
        rename_folder()

    elif choice == 4:
        delete_folder()

    elif choice == 5:
        create_file()

    elif choice == 6:
        read_file()

    elif choice == 7:
        update_file()

    elif choice == 8:
        delete_file()

    elif choice == 0:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")