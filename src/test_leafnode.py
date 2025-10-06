import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_props(self):
        node = (LeafNode(tag="a",value=None,props={
    "href": "https://www.google.com",
    "target": "_blank",
}))
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),node2)
    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a",value="Boot.dev",props={"href": "https://boot.dev","target": "_blank"})
        checker ='<a href="https://boot.dev" target="_blank">Boot.dev</a>'
        self.assertEqual(node.to_html(), checker)
    def test_raw(self):
        node = LeafNode(tag=None,value="Raw text")
        checker = "Raw text"
        self.assertEqual(node.to_html(), checker)
    def test_empty_tag(self):
        self.assertRaises(ValueError, LeafNode, "", value="Text")

if __name__ == "__main__":
    unittest.main()
