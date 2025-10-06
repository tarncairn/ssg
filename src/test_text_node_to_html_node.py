import unittest
from leafnode import LeafNode
from textnode import TextType, TextNode
from text_to_html_node import text_node_to_html_node


class TestTextToHTMLNode(unittest.TestCase):
    def test_text(self):
        #Text
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        #Bold
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        leaf_node = LeafNode(tag="b",value="This is a bold node" )
        self.assertEqual(html_node.to_html(), leaf_node.to_html())

    def test_italic(self):
        #Italic
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        leaf_node = LeafNode(tag="i",value="This is an italic node" )
        self.assertEqual(html_node.to_html(), leaf_node.to_html())

    def test_code(self):
        #Code
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        leaf_node = LeafNode(tag="code",value="This is a code node" )
        self.assertEqual(html_node.to_html(), leaf_node.to_html())

    def test_link(self):
        #Link
        node = TextNode("This is a link node", TextType.LINK,"https://boot.dev")
        html_node = text_node_to_html_node(node)
        leaf_node = LeafNode(tag="a",value="This is a link node", props={"href":"https://boot.dev"})
        self.assertEqual(html_node.to_html(), leaf_node.to_html())

    def test_image(self):
        #Image
        node = TextNode("This is the image alt text", TextType.IMAGE,"https://boot.dev")
        html_node = text_node_to_html_node(node)
        leaf_node = LeafNode(tag="img",value="", props={"src":"https://boot.dev", "alt": "This is the image alt text"})
        self.assertEqual(html_node.to_html(), leaf_node.to_html())

    def test_invalid(self):
        #Invalid
        with self.assertRaises(AttributeError):
            text_node_to_html_node(TextNode("This should be invalid", "invalid"))
if __name__ == "__main__":
    unittest.main()
