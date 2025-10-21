from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        from_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read()
    
    parent_node = markdown_to_html_node(from_content)
    title = extract_title(from_content)
        
    nodes = parent_node.to_html()
    
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", nodes)
    template_content = template_content.replace('href="/','href="{basepath}')
    template_content = template_content.replace('src="/','src="{basepath}')
    
    dest_dir =  os.path.dirname(dest_path)
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    with open(dest_path, "w") as f:
        f.write(template_content)
        
