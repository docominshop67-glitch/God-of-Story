import zipfile
import os

def create_project_zip(output_filename="docomin_project.zip"):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_path = os.path.join(base_dir, output_filename)
    
    exclude_dirs = {'.git', '__pycache__', '.venv', 'venv'}
    exclude_extensions = {'.pyc', '.zip'}

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in exclude_extensions:
                    continue
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, rel_path)
    
    print("Project zip archive created successfully at:", zip_path)
    return zip_path

if __name__ == '__main__':
    create_project_zip()
