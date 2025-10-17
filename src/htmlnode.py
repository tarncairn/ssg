from enum import Enum


class TagType(Enum):
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    P = "p"
    BOLD = "b"
    ITALIC = "i"
    OL = "ol"
    UL ="ul"
    LI = "li"
    HORIZONTAL_RULE = "hr"
    LINK = "a"
    IMAGE = "img"
    QUOTE = "blockquote"
    SPAN = "span"
    DIV ="div"
    CODE = "code"
    PRE = "pre"


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # new_variable = original_variable if original_variable is not None else default_value
        if isinstance(tag, TagType):
            self.tag = tag.value
        elif isinstance(tag, str):
            if TagType(tag):
                self.tag = tag
        else:
            self.tag = None
        self.value = value if value is not None else None
        self.children = children if children is not None else None
        self.props = props if props is not None else None
            
        
    def to_html(self):
        raise NotImplementedError("Not implemented yet")
    
    def props_to_html(self):
        result = []
        for key in self.props:
            if self.props[key] == "":
                raise ValueError("Key must refer to a value in props dictionary")
            else:
                result.append(f'{key}="{self.props[key]}"')
        return " " + " ".join(result)
    
    def __repr__(self):
        result = "HTMLNode("
        if self.tag:
            result += f'{TagType(self.tag)}, '
        else:
            result += "None, "
        if self.value:
            result += f"{self.value}, "
        else:
            result += "None, "
        if self.children:
            result += f"{self.children}, "
        else:
            result += "None, "
        if self.props:
            result += f"{self.props}"
        else:
            result += "None"
        result += ")"
        return result
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

