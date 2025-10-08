import unittest
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        checker = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertListEqual(extract_markdown_links(text), checker)
    
    def test_no_links(self):
        text = "This is text with no links"
        checker ="No matches were found."
        self.assertEqual(extract_markdown_links(text), checker)
    
    def test_missing_square_bracket(self):
        text = "This is text with a link [to boot dev(https://www.boot.dev) and to youtube](https://www.youtube.com/@bootdotdev)"
        checker ="No matches were found."
        self.assertEqual(extract_markdown_links(text), checker)
    
    def test_missing_bracket(self):
        text = "This is text with an ![image]https://i.imgur.com/zjjcJKZ.png"
        checker ="No matches were found."
        self.assertEqual(extract_markdown_links(text), checker)
    
    
    