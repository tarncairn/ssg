import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_alone(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")
        
    def test_with_p(self):
        md = """# Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)
        """
        self.assertEqual(extract_title(md), "Tolkien Fan Club")
        
    def test_double_title(self):
        md =  """# Tolkien Fan Club
        
        
        # Second Title

        ![JRR Tolkien sitting](/images/tolkien.png)
        """
        self.assertEqual(extract_title(md), "Tolkien Fan Club")
        
    def test_no_title(self):
        md = """## Not a title"""
        self.assertRaises(Exception, extract_title, md)