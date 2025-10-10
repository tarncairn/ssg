import unittest
from block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlock(unittest.TestCase):
    def test_header(self):
        block = "# Chapter One"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_code(self):
        block = "```python\n def print_self(self):\n\tprint(self)\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
    def test_quote(self):
        block = "> This is a blockquote. It might contain its own `code example`\n> or a [link to further reading](https://www.docs.io)."
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_ol(self):
        block = "3. A numbered item\n4. Another one"
        self.assertEqual(block_to_block_type(block), BlockType.OL)
        
    def test_ul(self):
        block = "- Item one with `inline`.\n- Item two with **bold**.\n- Item three *italic*."
        self.assertEqual(block_to_block_type(block), BlockType.UL)
        
    def test_paragraph(self):
        block = "The concluding paragraph for this section. It brings everything\ntogether and might reference a `final_function` or a [summary article](https://www.summary.org)."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_non_string_block(self):
        block = [
            "# Chapter One",
            "This introductory paragraph is **quite important**. It introduces the topic\nand includes a `key_term` and *some initial thoughts*.",
            "> This is a blockquote. It might contain its own `code example`\n> or a [link to further reading](https://www.docs.io).",
            "## Section 1.1",
            "```python\n def print_self(self):\n\tprint(self)\n```",
            "A paragraph following a subheading. It might talk about\n![illustration](https://via.placeholder.com/150) and other **visuals**.\nThere's also a link: [See More](http://learn.net).",
            "- Item one with `inline`.\n- Item two with **bold**.\n- Item three *italic*.",
            "3. A numbered item\n4. Another one",
            "The concluding paragraph for this section. It brings everything\ntogether and might reference a `final_function` or a [summary article](https://www.summary.org)."
        ]
        self.assertRaises(ValueError, block_to_block_type, block)