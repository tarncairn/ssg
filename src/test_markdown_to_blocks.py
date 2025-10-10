import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_heading_and_blockquote(self):
        md="""
# Heading 1


> A block-quote
> spanning two lines


## Heading 2
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "> A block-quote\n> spanning two lines",
                "## Heading 2",
            ],
        )
        
    def test_all(self):
        md = """This is the first paragraph. It contains some `inline code`,
*italicized words*, and **bold text**. You can also find a [helpful link](https://www.example.com) here.

The second paragraph continues the theme with an ![image icon](https://img.icons8.com/ios/452/info.png)
and more `code` and _emphasis_. This paragraph also spans multiple lines to test internal newlines.

Finally, a short third paragraph with just **bold** and a `code snippet`."""
        self.assertEqual(markdown_to_blocks(md),[
    "This is the first paragraph. It contains some `inline code`,\n*italicized words*, and **bold text**. You can also find a [helpful link](https://www.example.com) here.",
    "The second paragraph continues the theme with an ![image icon](https://img.icons8.com/ios/452/info.png)\nand more `code` and _emphasis_. This paragraph also spans multiple lines to test internal newlines.",
    "Finally, a short third paragraph with just **bold** and a `code snippet`."
])
    
    
    def test_chapter(self):
        md = """# Chapter One

This introductory paragraph is **quite important**. It introduces the topic
and includes a `key_term` and *some initial thoughts*.

> This is a blockquote. It might contain its own `code example`
> or a [link to further reading](https://www.docs.io).

## Section 1.1

A paragraph following a subheading. It might talk about
![illustration](https://via.placeholder.com/150) and other **visuals**.
There's also a link: [See More](http://learn.net).

- Item one with `inline`.
- Item two with **bold**.
- Item three *italic*.

The concluding paragraph for this section. It brings everything
together and might reference a `final_function` or a [summary article](https://www.summary.org)."""
        self.assertEqual(markdown_to_blocks(md),[
        "# Chapter One",
        "This introductory paragraph is **quite important**. It introduces the topic\nand includes a `key_term` and *some initial thoughts*.",
        "> This is a blockquote. It might contain its own `code example`\n> or a [link to further reading](https://www.docs.io).",
        "## Section 1.1",
        "A paragraph following a subheading. It might talk about\n![illustration](https://via.placeholder.com/150) and other **visuals**.\nThere's also a link: [See More](http://learn.net).",
        "- Item one with `inline`.\n- Item two with **bold**.\n- Item three *italic*.",
        "The concluding paragraph for this section. It brings everything\ntogether and might reference a `final_function` or a [summary article](https://www.summary.org)."
    ])
        
    def test_empty_lines(self)  :
        md = """First content block.
It has `inline code`.


Second content block.
This one has *italics* and a [link](https://broken.link).


    
Third content block. It's **bold**.
And an ![image](https://picsum.photos/id/237/50/50).

"""
        self.assertEqual(markdown_to_blocks(md),[
    "First content block.\nIt has `inline code`.",
    "Second content block.\nThis one has *italics* and a [link](https://broken.link).",
    "Third content block. It's **bold**.\nAnd an ![image](https://picsum.photos/id/237/50/50)."
])