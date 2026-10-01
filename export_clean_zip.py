import zipfile
import os

source_dir = r"c:\Users\ACER\Desktop\docomin"
zip_path = r"c:\Users\ACER\Desktop\Docomin_ReadyForManus.zip"

exclude_dirs = {'.git', 'node_modules', '__pycache__'}
exclude_exts = {'.exe', '.db', '.sqlite3', '.log'}

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_dir):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if any(file.endswith(ext) for ext in exclude_exts):
                continue
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, source_dir)
            zipf.write(file_path, arcname)

print("ZIP created at:", zip_path)
