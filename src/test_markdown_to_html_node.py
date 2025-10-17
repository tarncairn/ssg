import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
        
    def test_header(self):
        md = """
        # Heading One
        
        
        ## Heading Two
        
        
        ### Heading Three
        
        
        #### Heading Four
        
        
        ##### Heading Five
        
        
        ###### Heading Six
        
        
        """
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading One</h1><h2>Heading Two</h2><h3>Heading Three</h3><h4>Heading Four</h4><h5>Heading Five</h5><h6>Heading Six</h6></div>",
        )
    
    def test_p(self):
        md = """
        Come show me how ye bury yer treasure, lad! Even pirates, before they attack another ship, hoist a black flag. Merchant and pirate were for a long period one and the same person. Even today mercantile morality is really nothing but a refinement of piratical morality. It’s not everyday you get to do a pirate movie, you might as well go for it. Well actualy piracy is a democracy with captains voted for by the crew.
        
        Brwaack! Polly want a cracker? … Oh, wait. That’s for Talk Like a PARROT Day. Is that a belayin’ pin in yer britches, or are ye … Take what you can, give nothing back Even pirates, before they attack another ship, hoist a black flag. The Code is more like guidelines, really. Pirate’s code: First freedom and the captain. Second the loot, third woman and the rum and at the end no mercy if they not immediately surrender! A pirate is a man that is weak to achieve but too strong to steal from even the greatest achiever. Right from the Voyage og Noah, surviving was by sailing. Avast ye! and sail against the tides. Whats a pirate’s favorite fast food restaurant? Arrrrbys!
        
        They don’t call me Long John because my head is so big. I’ve crushed seventeen men’s skulls between me thighs! Take what you can, give nothing back Give me freedom or give me the rope. For I shall not take the shackles that subjugate the poor to uphold the rich. Where there is a sea there are pirates. How much does the pirate pay for an ear piercing? … A buccaneer! (buck- in- ear…) Whats a pirate’s favorite fast food restaurant? Arrrrbys!
        """
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Come show me how ye bury yer treasure, lad! Even pirates, before they attack another ship, hoist a black flag. Merchant and pirate were for a long period one and the same person. Even today mercantile morality is really nothing but a refinement of piratical morality. It’s not everyday you get to do a pirate movie, you might as well go for it. Well actualy piracy is a democracy with captains voted for by the crew.</p><p>Brwaack! Polly want a cracker? … Oh, wait. That’s for Talk Like a PARROT Day. Is that a belayin’ pin in yer britches, or are ye … Take what you can, give nothing back Even pirates, before they attack another ship, hoist a black flag. The Code is more like guidelines, really. Pirate’s code: First freedom and the captain. Second the loot, third woman and the rum and at the end no mercy if they not immediately surrender! A pirate is a man that is weak to achieve but too strong to steal from even the greatest achiever. Right from the Voyage og Noah, surviving was by sailing. Avast ye! and sail against the tides. Whats a pirate’s favorite fast food restaurant? Arrrrbys!</p><p>They don’t call me Long John because my head is so big. I’ve crushed seventeen men’s skulls between me thighs! Take what you can, give nothing back Give me freedom or give me the rope. For I shall not take the shackles that subjugate the poor to uphold the rich. Where there is a sea there are pirates. How much does the pirate pay for an ear piercing? … A buccaneer! (buck- in- ear…) Whats a pirate’s favorite fast food restaurant? Arrrrbys!</p></div>",
        )
    
    def test_ul(self):
        md = """
        - As a noun:
        - A written or printed record of items, often in a meaningful grouping or sequence, such as a guest list, shopping list, or list of members. 
        - In computing, a series of records in a file or an ordered collection of data. 
        - A ship or other object leaning to one side. 
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,"<div><ul><li>As a noun:</li><li>A written or printed record of items, often in a meaningful grouping or sequence, such as a guest list, shopping list, or list of members.</li><li>In computing, a series of records in a file or an ordered collection of data.</li><li>A ship or other object leaning to one side.</li></ul></div>")
        
    def test_link(self):
        md = """
        This is how you can go to [boot.dev](https://boot.dev)
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,'<div><p>This is how you can go to <a href="https://boot.dev">boot.dev</a></p></div>')
        
    def test_image(self):
        md = """
        This is a ![pretty image](https://i.pinimg.com/1200x/ae/69/61/ae6961d438f056efb35d7e829f432af7.jpg)
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,'<div><p>This is a <img src="https://i.pinimg.com/1200x/ae/69/61/ae6961d438f056efb35d7e829f432af7.jpg" alt="pretty image"></img></p></div>')
        
    def test_p_with_italics_and_bold(self):
        md = """
        So _that's_ what it's **like**? I can't believe that I could've been getting this this whole time!
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,"<div><p>So <i>that's</i> what it's <b>like</b>? I can't believe that I could've been getting this this whole time!</p></div>")
        