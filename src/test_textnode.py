import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "test.com")
        node2 = TextNode("This is a text node", "bold", "test.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "test.com")
        self.__repr__(node)

if __name__ == "__main__":
    unittest.main()