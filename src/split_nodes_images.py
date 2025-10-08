import re
from extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    result = []
    if not isinstance(old_nodes, list):
        raise ValueError("Must provide list of nodes.")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("Nodes must be text nodes.")
        images = extract_markdown_images(node.text)
        
        if len(images) == 0 or isinstance(images,str):
            result.append(node)
            continue
        
        parts = re.split(r"!(.*?)\)",node.text,maxsplit=2)
        for i in range(0,len(parts)+1):
            if parts[i] == "":
                break
            if i % 2 == 0:
                result.append(TextNode(text=parts[i], text_type=TextType.TEXT))
                continue
            else:
                result.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
                del images[0]
                continue
    if result == old_nodes:
        raise ValueError("No matches were found")
    return result
