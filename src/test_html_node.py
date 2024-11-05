import unittest

from html_node import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')

    def test_blank_props_to_html(self):
        props = {}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), '')

    def test_single_prop_to_html(self):
        props = {
            "href": "https://www.google.com",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com"')


if __name__ == "__main__":
    unittest.main()
