import os
import zipfile
from datetime import datetime

def backup_folder_to_zip(folder_path, backup_folder):
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"The folder {folder_path} does not exist")

    # Create the backup folder if it does not exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    # Create a unique backup file name based on the current date and time
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file_name = f"{os.path.basename(folder_path)}_backup_{timestamp}.zip"
    backup_file_path = os.path.join(backup_folder, backup_file_name)

    # Create a zip file and add the folder contents to it
    with zipfile.ZipFile(backup_file_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                backup_zip.write(file_path, os.path.relpath(file_path, folder_path))
    
    print(f"Backup completed successfully! Backup file created at: {backup_file_path}")

# Example usage
source_folder = "G:\civil"
backup_destination = "C:\Programming\Python\Backup"

backup_folder_to_zip(source_folder, backup_destination)
