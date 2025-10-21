import os
from pathlib import Path
from generate_page import generate_page
from extract_title import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    folders = []
    if os.path.exists(dir_path_content):
        folders.extend(os.listdir(dir_path_content))
    
    for item in folders:
        item_path = Path(dir_path_content) / item
        
        if os.path.isfile(item_path):
            print(f"Page is being generated for {item_path}")
            correct_file_name = item.replace(".md", ".html")
            item_destination_path = dest_dir_path / correct_file_name
            generate_page(str(item_path), template_path, item_destination_path, base_path)
        else:
            print(f"Going deeper into {item_path}")
            item_destination_path = dest_dir_path / item
            generate_pages_recursive(str(item_path), template_path, item_destination_path, base_path)