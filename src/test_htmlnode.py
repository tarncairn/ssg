import unittest
from htmlnode import TagType, HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_p(self):
        # Check that both nodes are equal
        node = HTMLNode(TagType.P, value="Even the smallest person can change the course of the future", children=None, props=None)
        node2 = '<p>Even the smallest person can change the course of the future</p>'
        self.assertEqual(node.__repr__(), node2)
    
    def test_raw_text(self):
        node = HTMLNode(value="Raw text")
        node2 = "Raw text"
        self.assertEqual(node.__repr__(), node2)
    
    def test_props(self):
        # Check that props function creates props as expected
        node = (HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",
}))
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),node2)
        
    def test_a(self):
        node = HTMLNode(TagType.LINK, children="Boot.dev", props={
    "href": "https://boot.dev",
    "target": "_blank",
})
        node2 = '<a href="https://boot.dev" target="_blank">Boot.dev</a>'
        self.assertEqual(node.__repr__(), node2)
    


if __name__ == "__main__":
    unittest.main()