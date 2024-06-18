import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

if __name__ == "__main__":
    unittest.main()