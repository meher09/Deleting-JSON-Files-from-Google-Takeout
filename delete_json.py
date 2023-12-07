import os
folder_path = "image"

for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(".json"):
            file_path = os.path.join(foldername, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {str(e)}")
