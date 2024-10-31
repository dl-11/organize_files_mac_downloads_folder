
import os
import shutil
import logging
from datetime import datetime

# Define the path to the Downloads folder
downloads_path = os.path.expanduser("~/Downloads")

# File type categories and corresponding extensions for organized folder structure
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".heic"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Applications": [".dmg", ".pkg", ".app", ".exe"],
    "Scripts": [".py", ".sh", ".js", ".bat"],
    "Others": []  # Default folder for any other file types
}

# Set up logging to record file movements in a log file within the Downloads directory
log_file = os.path.join(downloads_path, "organize_log.txt")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def organize_files(dry_run=True):
    """Organizes files in the Downloads folder by moving them into categorized subdirectories.

    Args:
        dry_run (bool): If True, no files are moved. Used to preview actions.
    """
    
    # Iterate through files in the Downloads folder
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Determine the file's extension and identify the target folder
        _, file_extension = os.path.splitext(filename)
        destination_folder = "Others"  # Default category for uncategorized files

        for folder, extensions in file_types.items():
            if file_extension.lower() in extensions:
                destination_folder = folder
                break

        # Create the target folder if it doesn't exist
        target_folder_path = os.path.join(downloads_path, destination_folder)
        os.makedirs(target_folder_path, exist_ok=True)

        # Define the target path for the file in the new folder
        target_path = os.path.join(target_folder_path, filename)

        # Log and move the file if not in dry run mode
        if dry_run:
            logging.info(f"Dry Run: Would move {filename} to {destination_folder}")
        else:
            shutil.move(file_path, target_path)
            logging.info(f"Moved {filename} to {destination_folder}")

if __name__ == "__main__":
    # Execute the organize_files function
    organize_files(dry_run=True)  # Set to False to enable actual file movement
