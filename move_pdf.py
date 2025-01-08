import os
import shutil

# Source directory (nested folder structure)
source_dir = "3 Machine Learning"

# Destination directory (where PDFs will be copied)
destination_dir = "all_ml_notes"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Walk through the directory structure
for root, _, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".pdf"):
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_dir, file)

            # Copy the file
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied: {source_file_path} to {destination_file_path}")
