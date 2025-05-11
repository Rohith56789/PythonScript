import os
import logging
import shutil
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

try:
    # Folder to take a backup of (change this if needed)
    source_folder = r"D:\D\5-11\Files"  # Use raw string to avoid escape issues

    # Where to store the backup
    backup_folder = "backup"
    os.makedirs(backup_folder, exist_ok=True)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Construct the backup file name (without .zip extension — shutil adds it automatically)
    backup_filename = os.path.join(backup_folder, f"backup_{timestamp}")

    # Check if source folder exists before creating backup
    if not os.path.exists(source_folder):
        error_msg = f"Error: Source folder '{source_folder}' does not exist."
        print(error_msg)
        logging.error(error_msg)
        exit(1)

    # Create a zip archive of the source folder
    shutil.make_archive(backup_filename, 'zip', source_folder)

    success_msg = f"Backup created: {backup_filename}.zip"
    print(success_msg)
    logging.info(success_msg)

except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")
