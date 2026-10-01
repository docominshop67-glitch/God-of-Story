import shutil
import os

source_dir = r"c:\Users\ACER\Desktop\docomin"
dest_dir = r"c:\Users\ACER\Desktop\Docomin_Upload_To_GitHub"

exclude_dirs = {'.git', 'node_modules', '__pycache__'}
exclude_exts = {'.exe', '.db', '.sqlite3', '.log', '.zip'}

if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)

os.makedirs(dest_dir)

for root, dirs, files in os.walk(source_dir):
    # Exclude directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    # Create corresponding directory structure in dest
    rel_path = os.path.relpath(root, source_dir)
    target_dir = os.path.join(dest_dir, rel_path)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    for file in files:
        if any(file.endswith(ext) for ext in exclude_exts):
            continue
        source_file = os.path.join(root, file)
        target_file = os.path.join(target_dir, file)
        shutil.copy2(source_file, target_file)

print("Files successfully copied to:", dest_dir)
