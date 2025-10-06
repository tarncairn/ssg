from htmlnode import HTMLNode, TagType


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
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
            
            if self.value:
                result += f"{self.value}"
            if self.tag:
                result += f"</{self.tag}>"
            return result