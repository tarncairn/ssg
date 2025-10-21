import os
import shutil
import sys
from pathlib import Path
from generate_pages_recursive import generate_pages_recursive


def copy_static(base_path):
    
        
    static_path = Path("./static")
    public_path = Path("./docs")
    content_path = Path("./content")
    template_path = Path("./template.html")
    destination_path = Path("./docs")
    
    static_exists = os.path.exists(static_path)
    public_exists = os.path.exists(public_path)
    
        
    if public_exists:
        shutil.rmtree(public_path)
    
    os.mkdir(public_path)
    print(f"Contents successfully deleted from {public_path}")
    copier(static_path, public_path)
    generate_pages_recursive(content_path, template_path, destination_path,base_path)
    
    
def copier(src_dir, destination_dir):
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        destination_path = os.path.join(destination_dir, item)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, destination_path)
            print(f"{src_path} file successfully copied to public folder")
        else:
            os.mkdir(destination_path)
            print(f"{destination_path} folder successfully copied to public folder")
            copier(src_path, destination_path)
    
   
    



def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static(base_path)
    
    
        
if __name__ == "__main__":
    main()