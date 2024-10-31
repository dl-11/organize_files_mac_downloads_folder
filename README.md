# File Organizer for macOS

This Python script organizes files in your Downloads folder by sorting them into categorized subdirectories (e.g., Images, Documents, Videos). 
It automatically places each file into a corresponding folder based on its file type.

## Features
- Automatically categorizes and organizes files in the Downloads folder.
- Creates subdirectories for Images, Documents, Videos, Music, Archives, Applications, Scripts, and Others.
- Logs actions in a log file located in the Downloads folder (`organize_log.txt`).

## Requirements
- Python 3.x (should work with any recent version of Python)

## Installation
1. Clone the repository or download the `organizefiles_mac_downloads_folder.py` script.
2. Run the script using Python.

```bash
python organize_files_mac_downloads_folder.py
```

## Usage
- **Dry Run**: By default, the script performs a "dry run" (no files are moved). To execute, change the `dry_run` parameter to `False`.
- **Custom Downloads Path**: Modify the `downloads_path` variable if your Downloads folder is in a different location.

## Logging
A log file (`organize_log.txt`) is generated in the Downloads folder, detailing the organization actions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
This script was designed to streamline file management, keeping your Downloads folder organized and clutter-free.

