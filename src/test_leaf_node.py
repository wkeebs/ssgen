import unittest

from leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_tag(self):
        value = "this is some text"
        node = LeafNode(value=value)
        self.assertEqual(value, node.to_html())

    def test_no_props(self):
        value = "this is some text"
        node = LeafNode(tag='p', value=value)
        expected = "<p>this is some text</p>"
        self.assertEqual(expected, node.to_html())

    def test_with_props(self):
        value = "this is some text"
        props = {"href": "https://www.google.com", "alt": "alternate property"}
        node = LeafNode(tag='a', value=value, props=props)
        expected = '<a href="https://www.google.com" alt="alternate property">this is some text</a>'
        self.assertEqual(expected, node.to_html())


if __name__ == "__main__":
    unittest.main()
