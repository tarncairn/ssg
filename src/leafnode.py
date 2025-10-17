from htmlnode import HTMLNode, TagType


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value and not self.tag == "img":
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return f"{self.value}"
        else:
            result = ""
            if self.tag:
                result += f"<{self.tag}"
                if self.props:
                    new = self.props_to_html()
                    result += f"{new}>"
                else:
                    result += f">"
            
            if self.value and self.value != "":
                result += f"{self.value}"
            if self.tag:
                result += f"</{self.tag}>"
            return result
        
        
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"