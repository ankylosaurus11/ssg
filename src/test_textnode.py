import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
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

if __name__ == "__main__":
    unittest.main()