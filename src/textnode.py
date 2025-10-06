from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"
    

class TextNode:
    def __init__(self,text, text_type,url=None):
        self.text = text #text content of the node
        if isinstance(text_type, TextType):
            self.text_type = text_type.value
        elif isinstance(text_type, str):
            raise AttributeError("Text type must be a valid text type")
        else:
            self.tag = None
         #type of text this node contains, which is a member of the TextType enum
        self.url = url # url of the link or image if the text is a link
    
    def __eq__(self, other):
        text_is_equal = (self.text == other.text)
        text_type_is_equal = (self.text_type == other.text_type)
        url_is_equal = (self.url == other.url)
        return text_is_equal and text_type_is_equal and url_is_equal
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"