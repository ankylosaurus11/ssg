import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

class TestLeafNode(unittest.TestCase):
    def test_leaf(self):
        leaf = LeafNode(tag="p", value="This is a paragraph")
        expected_leaf = '<p>This is a paragraph</p>'
        self.assertEqual(leaf.to_html(), expected_leaf)

    def test_leaf_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value="")

class TestParentNode(unittest.TestCase):
    def test_parent(self):
        leaf1 = LeafNode("b", "Bold text")
        leaf2 = LeafNode(None, "Normal text")
        leaf3 = LeafNode("i", "italic text")
        leaf4 = LeafNode(None, "Another normal text")
        parent = ParentNode("p", [leaf1, leaf2, leaf3, leaf4])
        expected_parent = '<p><b>Bold text</b>Normal text<i>italic text</i>Another normal text</p>'
        self.assertEqual(parent.to_html(), expected_parent)

if __name__ == "__main__":
    unittest.main()