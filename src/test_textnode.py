import unittest

from textnode import (
    TextNode,
    LeafNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "hi")
        node2 = TextNode("This is a text node", "bold", "hi")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "test.com")
        node2 = TextNode("This is a text node", "bold", "test.com")
        expected_repr = "TextNode(This is a text node, bold, test.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_text_eq(self):
        text_node = TextNode("hello this is text", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node, LeafNode(None, "hello this is text"))

    def test_url_eq(self):
        node = TextNode("this is a text node", text_type_text, "whocares.com")
        node2 = TextNode("this is a text node", text_type_text, "whocares.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()