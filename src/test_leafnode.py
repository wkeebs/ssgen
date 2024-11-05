import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_tag(self):
        value = "this is some text"
        node = LeafNode(value)
        self.assertEqual(value, node.to_html())
        
    def test_no_props(self):
        value = "this is some text"
        node = LeafNode(value, 'p')
        expected = "<p>this is some text</p>"
        self.assertEqual(expected, node.to_html())

    def test_with_props(self):
        value = "this is some text"
        props = {"href": "https://www.google.com", "alt": "alternate property"}
        node = LeafNode(value, 'a', props)
        expected = '<a href="https://www.google.com" alt="alternate property">this is some text</a>'
        self.assertEqual(expected, node.to_html())

if __name__ == "__main__":
    unittest.main()
