import re
import textwrap
from block_to_block_type import BlockType
from htmlnode import HTMLNode, TagType
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from text_to_html_node import text_node_to_html_node


def block_to_html_node(block_type, block):
    if block_type == BlockType.HEADING:
        heading_dict = {
            1: TagType.H1,
            2: TagType.H2,
            3: TagType.H3,
            4: TagType.H4,
            5: TagType.H5,
            6: TagType.H6,
        }
        count = block.count("#")
        tag = heading_dict.get(count, None)
        content = block.lstrip("# ").strip()
        text_nodes = text_to_textnodes(content)
        children = [text_node_to_html_node(tn) for tn in text_nodes]
        return ParentNode(tag.value, children)
    
    elif block_type == BlockType.CODE:
        inner_code = block.strip()[3:-3]
        inner_code = textwrap.dedent(inner_code).lstrip("\n")
        code_node = LeafNode(TagType.CODE.value, inner_code)
        return ParentNode(TagType.PRE.value, [code_node])
    
    elif block_type == BlockType.QUOTE:
        lines = block.split('\n')
        cleaned_lines = [line.lstrip('> ').strip() for line in lines if line.strip()]
        text = "\n".join(cleaned_lines)
        text_nodes = text_to_textnodes(text)
        children = [text_node_to_html_node(tn) for tn in text_nodes]
        return ParentNode(TagType.QUOTE.value, children)
    
    elif block_type == BlockType.UL:
        lines = block.split('\n')
        children = []
        for  line in lines:
            if line.strip():
                item_text = line.lstrip("- ").strip()
                text_nodes = text_to_textnodes(item_text)
                item_children = [text_node_to_html_node(tn) for tn in text_nodes]
                children.append(ParentNode(TagType.LI.value, item_children))
        return ParentNode(TagType.UL.value, children)
    
    elif block_type == BlockType.OL:
        lines = block.split('\n')
        children = []
        for line in lines:
            if line.strip():
                item_text = re.sub(r'^\d+\.\s*', '', line).strip()
                text_nodes = text_to_textnodes(item_text)
                item_children = [text_node_to_html_node(tn) for tn in text_nodes]
                children.append(ParentNode(TagType.LI.value, item_children))
        return ParentNode(TagType.OL.value, children)
    else:
        no_spaces = " ".join(block.split())
        text_nodes = text_to_textnodes(no_spaces)
        children = [text_node_to_html_node(tn) for tn in text_nodes]
        return ParentNode(TagType.P.value, children)
