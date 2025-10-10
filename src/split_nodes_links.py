import re
from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_link(old_nodes):
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
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue
        
        for alt, url in links:
            marker = f"[{alt}]({url})"
            before, found, text = text.partition(marker)
            if before:
                result.append(TextNode(before,TextType.TEXT))
            result.append(TextNode(alt,TextType.LINK, url))
        if text:
                result.append(TextNode(text, TextType.TEXT))
    return result
