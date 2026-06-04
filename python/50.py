import shutil
import os

src_folder = "data_src"
dest_folder = "data_backup"

if not os.path.exists(src_folder):
    os.makedirs(src_folder)
    with open(os.path.join(src_folder, "test.txt"), "w") as f:
        f.write("backup test")
        
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)
    
copied = set()
try:
    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        dest_file = os.path.join(dest_folder, filename)
        if os.path.isfile(src_file) and filename not in copied:
            shutil.copy2(src_file, dest_file)
            copied.add(filename)
            with open("backup.log", "a") as log:
                log.write(f"Copied {filename} to backup\n")
    print("Backup complete")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
