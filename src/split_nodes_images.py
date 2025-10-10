import re
from extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    result = []
    if not isinstance(old_nodes, list):
        raise ValueError("Must provide list of nodes.")
    
    for node in old_nodes:
        if not isinstance(node,TextNode):
            raise ValueError("Nodes must be valid")
            continue
        if node.text_type != "text":
            result.append(node)
            continue
        text = node.text
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue
        
        for alt, url in images:
            marker = f"![{alt}]({url})"
            before, found, text = text.partition(marker)
            if before:
                result.append(TextNode(before,TextType.TEXT))
            result.append(TextNode(alt,TextType.IMAGE, url))
        if text:
                result.append(TextNode(text, TextType.TEXT))
    return result
