"""
Remove jpg files less than 2kb in a given folder recursively
"""

import os

folder = r"C:\little pics"

for current_folder, subfolder, file_names in os.walk(folder):
    for file_name in file_names:
        if file_name.lower().endswith(".jpg"):
            full_path = os.path.join(current_folder, file_name)
            if os.path.getsize(full_path) < 2048:
                os.remove(full_path)
    

