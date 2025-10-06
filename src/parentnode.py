from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children, props=None):
        if not isinstance(tag,str):
            raise ValueError("Tag must be valid HTML tag, if tag is provided as an arg")
        super().__init__(tag=tag, children=children,props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        if not self.children:
            raise ValueError("All parent nodes must have children.")
        else:
            result = ""
            if self.tag:
                result += f"<{self.tag}"
                if self.props:
                    new = self.props_to_html()
                    result += f"{new}>"
                else:
                    result += f">"
            if self.children:
                children = "".join([child.to_html() for child in self.children])
                result += f"{children}"
            if self.tag:
                result += f"</{self.tag}>"
            return result