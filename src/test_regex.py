import unittest

from textnode import (
    extract_markdown_images, 
    extract_markdown_links
)

class RegexUnitTest(unittest.TestCase):
    def test_image_extract(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected_text = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(extract_markdown_images(text), expected_text)

    def test_link_extract(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected_text = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(extract_markdown_links(text), expected_text)

if __name__ == "__main__":
    unittest.main()