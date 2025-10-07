import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        node = TextNode("This is text with no inner blocks", TextType.TEXT)
        new_nodes = [TextNode("This is text with no inner blocks", TextType.TEXT)]
        self.assertRaises(TypeError, split_nodes_delimiter,[node],TextType.CODE)
        
    def test_no_text_type(self):
        node = TextNode("This is text with no inner blocks", TextType.TEXT)
        new_nodes = [TextNode("This is text with no inner blocks", TextType.TEXT)]
        self.assertRaises(TypeError, split_nodes_delimiter,[node],"")
        
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code block",  TextType.CODE, None), TextNode(" word",  TextType.TEXT, None)]
        self.assertEqual(split_nodes_delimiter([node],"`",TextType.CODE), new_nodes)
    
    def test_code_no_closing_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node],"`",TextType.CODE)
       
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("bold",  TextType.BOLD, None), TextNode(" word",  TextType.TEXT, None)]
        self.assertEqual(split_nodes_delimiter([node],"**",TextType.BOLD), new_nodes)
        
    def test_bold_no_closing_delimiter(self):
        node = TextNode("This is text with a **bold word", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node],"**",TextType.BOLD)
        
    def test_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = [TextNode("This is text with an ", TextType.TEXT, None), TextNode("italic",  TextType.ITALIC, None), TextNode(" word",  TextType.TEXT, None)]
        self.assertEqual(split_nodes_delimiter([node],"_",TextType.ITALIC), new_nodes)
        
    def test_italic_no_closing_delimiter(self):
        node = TextNode("This is text with a _italic word", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node],"_",TextType.ITALIC)
    
    
    
    