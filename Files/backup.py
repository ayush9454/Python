import os
import sys
import pathlib
import zipfile

dirName = input("Enter the directory name that you want to backup: ")

if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exist")
    sys.exit(1)

curDirectory = pathlib.Path(os.path.abspath(dirName))

try:
    with zipfile.ZipFile("myZip.zip", mode="w") as archive:
        for file_path in curDirectory.rglob("*"):
            archive.write(file_path, arcname=file_path.relative_to(curDirectory))
    if os.path.isfile("myZip.zip"):
        print("Archive", "myZip.zip", "created successfully")
    else:
        print("Error in creating zip archive")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
