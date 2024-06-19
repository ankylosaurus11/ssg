import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

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

if __name__ == "__main__":
    unittest.main()