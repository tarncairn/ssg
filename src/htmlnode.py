from enum import Enum


class TagType(Enum):
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    P = "p"
    OL = "ol"
    UL ="ul"
    HORIZONTAL_RULE = "hr"
    LINK = "a"
    IMAGE = "img"
    QUOTE = "blockquote"


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None,props=None):
        if tag:
            self.tag = tag.value
        else:
            self.tag = None
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("Not implemented yet")
    
    def props_to_html(self):
        return " " + " ".join([f'{key}="{self.props[key]}"'for key in self.props])
    
    def __repr__(self):
        result = ""
        if self.tag:
            result += f"<{self.tag}"
            if self.props:
                new = self.props_to_html()
                result += f"{new}>"
            else:
                result += f">"
        if self.value:
            result += f"{self.value}"
        elif self.children:
            result += f"{self.children}"
        if self.tag:
            result += f"</{self.tag}>"
        return result