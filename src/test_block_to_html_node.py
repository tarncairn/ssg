import unittest
from block_to_html_node import block_to_html_node
from htmlnode import HTMLNode, TagType
from block_to_block_type import BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType

class TestBlockToHTMLNode(unittest.TestCase):
    def test_heading_default(self):
        block_type = BlockType.HEADING
        block = "# Chapter One"
        checker = "<h1>Chapter One</h1>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_heading_2(self):
        block_type = BlockType.HEADING
        block = "## The Beginning"
        checker = "<h2>The Beginning</h2>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)

    def test_heading_3(self):
        block_type = BlockType.HEADING
        block = "### The Situation"
        checker = "<h3>The Situation</h3>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_heading_4(self):
        block_type = BlockType.HEADING
        block = "#### The People Involved"
        checker = "<h4>The People Involved</h4>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_heading_5(self):
        block_type = BlockType.HEADING
        block = "##### What They Did"
        checker = "<h5>What They Did</h5>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
            
    def test_heading_6(self):
        block_type = BlockType.HEADING
        block = "###### Results"
        checker = "<h6>Results</h6>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_code_block(self):
        block_type = BlockType.CODE
        block = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""
        checker = "<pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_quote(self):
        block_type = BlockType.QUOTE
        block = "> This is a blockquote. It might contain its own `code example`\n> or a [link to further reading](https://www.docs.io)."
        checker ='<blockquote><p>This is a blockquote. It might contain its own <code>code example</code></p><p>or a <a href="https://www.docs.io">link to further reading</a>.</p></blockquote>'
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_ul(self):
        block_type = BlockType.UL
        block = "- Item one with `inline`.\n- Item two with **bold**.\n- Item three *italic*."
        checker = "<ul><li>Item one with <code>inline</code>.</li><li>Item two with <b>bold</b>.</li><li>Item three *italic*.</li></ul>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_ol(self):
        block_type = BlockType.OL
        block = "3. Third item\n4. Fourth item"
        checker = "<ol><li>Third item</li><li>Fourth item</li></ol>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
    def test_p(self):
        block_type = BlockType.PARAGRAPH
        block = "This introductory paragraph is **quite important**. It introduces the topic\nand includes a `key_term` and *some initial thoughts*."
        checker = "<p>This introductory paragraph is <b>quite important</b>. It introduces the topic and includes a <code>key_term</code> and *some initial thoughts*.</p>"
        self.assertEqual(block_to_html_node(block_type, block).to_html(), checker)
        
if __name__ == "__main__":
    unittest.main()
