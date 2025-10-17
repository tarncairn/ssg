import re
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from block_to_html_node import block_to_html_node
from htmlnode import HTMLNode, TagType
from textnode import TextNode,TextType
from text_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block_type, block)
        html_nodes.append(html_node)
    final = ParentNode(TagType.DIV.value, html_nodes)
    return final
