import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        checker = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), checker)
        
    def test_link_first(self):
        text = "This is a [link to youtube](https://youtube.com) and a **bolded** text"
        checker = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link to youtube", TextType.LINK, "https://youtube.com"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), checker)
        
    
    def test_broken_link(self):
        text = "This is a link to youtube](https://youtube.com) and a **bolded** text"
        checker = [
            TextNode("This is a link to youtube](https://youtube.com) and a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), checker)
    
    def test_broken_image(self):
        text = "This is **text** with an _italic_ word and a `code block` and an !obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        checker = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an !obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), checker)
    
    def test_broken_bolded_text(self):
        text = "This is **text with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertRaises(ValueError, text_to_textnodes, text)
        
    def test_broken_italicised_text(self):
        text = "This is **text** with an italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertRaises(ValueError, text_to_textnodes, text)
        
    
    def test_broken_code_text(self):
        text = "This is **text** with an _italic_ word and a `code block and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertRaises(ValueError, text_to_textnodes, text)
    