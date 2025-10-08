import unittest
from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_no_images(self):
        text = "This is text with no images"
        checker ="No matches were found."
        self.assertEqual(extract_markdown_images(text), checker)
        
    def test_missing_exclamation_mark(self):
        text = "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        checker ="No matches were found."
        self.assertEqual(extract_markdown_images(text), checker)
    
    def test_missing_square_bracket(self):
        text = "This is text with an !image](https://i.imgur.com/zjjcJKZ.png)"
        checker ="No matches were found."
        self.assertEqual(extract_markdown_images(text), checker)
    
    def test_missing_bracket(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png"
        checker ="No matches were found."
        self.assertEqual(extract_markdown_images(text), checker)
    
    
    