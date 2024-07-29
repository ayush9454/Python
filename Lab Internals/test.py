import os
import pathlib
import sys
import zipfile

dirName=input("Enter the name of the directory you want to bakckup ")
if not os.path.isdir(dirName):
    print("directory does not exist ")
    sys.exit(0)

curDirectory=pathlib.Path(dirName)
with zipfile.ZipFile("myZip.zip",mode='w') as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curDirectory))

if os.path.isfile("myZip.zip"):
    print("Backup created successfully")
else:
    print("An error occured ")