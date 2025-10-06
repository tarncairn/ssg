from textnode import TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type and TextType(text_node.text_type):
        # TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
        if TextType(text_node.text_type) == TextType.TEXT:
            return LeafNode(tag=None,value=text_node.text)
        # TextType.BOLD: This should return a LeafNode with a "b" tag and the text
        elif TextType(text_node.text_type) == TextType.BOLD:
            return LeafNode(tag=text_node.text_type, value=text_node.text)
        # TextType.ITALIC: "i" tag, text
        elif TextType(text_node.text_type) == TextType.ITALIC:
            return LeafNode(tag=text_node.text_type, value=text_node.text)
        # TextType.CODE: "code" tag, text
        elif TextType(text_node.text_type) == TextType.CODE:
            return LeafNode(tag=text_node.text_type, value=text_node.text)
        # TextType.LINK: "a" tag, anchor text, and "href" prop
        elif TextType(text_node.text_type) == TextType.LINK:
            return LeafNode(tag=text_node.text_type, value=text_node.text, props={"href":text_node.url})
        # TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
        elif TextType(text_node.text_type) == TextType.IMAGE:
            return LeafNode(tag=text_node.text_type, value="", props={"src":text_node.url,"alt":text_node.text})
    else:
        raise ValueError("Text type is invalid")