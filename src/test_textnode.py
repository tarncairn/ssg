import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Check that both nodes are equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_text(self):
        # Check that different text property are not equal
        node = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_text_type(self):
        # Check when text type property are not equal
        node = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a text", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_url(self):
        # Check when urls are different
        node = TextNode("This is a text", TextType.BOLD,'https://boot.dev')
        node2 = TextNode("This is a text", TextType.BOLD,'https://github.com')
        self.assertNotEqual(node, node2)
        
    def test_rep(self):
        # Check string representation of object is accurate
        text = "This is text"
        type = TextType.BOLD
        url = "https://boot.dev"
        node = TextNode(text,type,url)
        str_eq = f"TextNode({text}, {type.value}, {url})"
        self.assertEqual(node.__repr__(), str_eq)
        
    def test_url_is_none(self):
        text = "This is text"
        type = TextType.BOLD
        node = TextNode(text,type)
        str_eq = f"TextNode({text}, {type.value}, {None})"
        self.assertEqual(node.__repr__(), str_eq)

    def test_to_html_text(self):
        text = "This is text"
        type = TextType.TEXT
        node = TextNode(text,type)
        str_eq = f"{text}"
        self.assertEqual(node.to_html(), str_eq)

    def test_to_html_bold(self):
        text = "This is text"
        type = TextType.BOLD
        node = TextNode(text,type)
        str_eq = f"<b>{text}</b>"
        self.assertEqual(node.to_html(), str_eq)

    def test_to_html_italic(self):
        text = "This is text"
        type = TextType.ITALIC
        node = TextNode(text,type)
        str_eq = f"<i>{text}</i>"
        self.assertEqual(node.to_html(), str_eq)

    def test_to_html_code(self):
        text = "This is text"
        type = TextType.CODE
        node = TextNode(text,type)
        str_eq = f"<code>{text}</code>"
        self.assertEqual(node.to_html(), str_eq)

    def test_to_html_link_no_url(self):
        text = "This is text"
        type = TextType.LINK
        node = TextNode(text,type)
        str_eq = f"<a>{text}</a>"
        self.assertEqual(node.to_html(), str_eq)
        
    def test_to_html_link_with_url(self):
        text = "This is text"
        url = "https://boot.dev"
        type = TextType.LINK
        node = TextNode(text,type,url)
        str_eq = f"<a href={url}>{text}</a>"
        self.assertEqual(node.to_html(), str_eq)
        
    def test_to_html_img_with_src(self):
        text = "This is text"
        src = "https://boot.dev"
        type = TextType.IMAGE
        node = TextNode(text,type,src)
        str_eq = f"<img src={src}>{text}</img>"
        self.assertEqual(node.to_html(), str_eq)
        
    def test_to_html_img_no_src(self):
        text = "This is text"
        type = TextType.IMAGE
        node = TextNode(text,type)
        str_eq = f"<img>{text}</img>"
        self.assertEqual(node.to_html(), str_eq)
        


if __name__ == "__main__":
    unittest.main()