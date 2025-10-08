import unittest
from split_nodes_links import split_nodes_link
from textnode import TextType, TextNode

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
    
    def test_no_images(self):
        node = TextNode(
        "This is text with no images",
        TextType.TEXT,
    )
        self.assertRaises(ValueError, split_nodes_link, [node])
        

    
    def test_missing_square_bracket(self):
        node = TextNode(
        "This is text with an !image](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT,
    )
        self.assertRaises(ValueError, split_nodes_link, [node])
            
    def test_missing_bracket(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png",
        TextType.TEXT,
    )
        self.assertRaises(ValueError, split_nodes_link, [node])
    
    def test_non_node_arg(self):
        node = "This is just a string"
        self.assertRaises(ValueError, split_nodes_link, node)
        
    def test_non_textnode_arg(self):
        node = "This is just a string"
        self.assertRaises(ValueError, split_nodes_link, [node])