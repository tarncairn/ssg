import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_raises_no_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        self.assertRaises(ValueError,ParentNode,tag=None,children=[child_node] )

    def test_to_html_raises_no_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("p",children=None)
        self.assertRaises(ValueError,parent_node.to_html)

    def test_value_arg_included(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        self.assertRaises(TypeError,ParentNode, "p",[child_node], value="Value added")
    
    def test_empty_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        self.assertRaises(ValueError,ParentNode, "", [child_node])

    def test_tag_is_invalid(self):
        child_node = LeafNode("b", "grandchild")
        self.assertRaises(ValueError, ParentNode, tag=123, children=[child_node])

if __name__ == "__main__":
    unittest.main()