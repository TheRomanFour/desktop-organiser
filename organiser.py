import os
import shutil

def organize_desktop(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = os.listdir(source_folder)

    for file in files:
        file_path = os.path.join(source_folder, file)
        if os.path.isdir(file_path) or file == os.path.basename(__file__):
            continue

        if file.lower().endswith(".lnk"):
            continue

        _, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()  

        type_folder = os.path.join(destination_folder, file_extension[1:])
        if not os.path.exists(type_folder):
            os.makedirs(type_folder)

        shutil.move(os.path.join(source_folder, file), os.path.join(type_folder, file))

    print("Desktop organized successfully!")

if __name__ == "__main__":
    source_folder = os.path.expanduser("~/Desktop")  
    destination_folder = os.path.expanduser("~/Desktop/OrganizedDesktop") 

    organize_desktop(source_folder, destination_folder)
