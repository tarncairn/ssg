import unittest
from split_nodes_images import split_nodes_image
from textnode import TextType, TextNode

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_no_images(self):
        node = TextNode(
        "This is text with no images",
        TextType.TEXT,
    )
        self.assertRaises(ValueError, split_nodes_image, [node])
        
    def test_missing_exclamation_mark(self):
        node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT,
    )
        self.assertRaises(ValueError, split_nodes_image, [node])
    
    def test_missing_square_bracket(self):
        node = TextNode(
        "This is text with an !image](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT,
    )
        self.assertRaises(ValueError, split_nodes_image, [node])
            
    def test_missing_bracket(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png",
        TextType.TEXT,
    )
        self.assertRaises(ValueError, split_nodes_image, [node])
    
    def test_non_node_arg(self):
        node = "This is just a string"
        self.assertRaises(ValueError, split_nodes_image, node)
        
    def test_non_textnode_arg(self):
        node = "This is just a string"
        self.assertRaises(ValueError, split_nodes_image, [node])