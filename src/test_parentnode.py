import unittest

from htmlnode import ParentNode, LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_children(self):
        node = ParentNode(tag="p", children=[])
        error = None
        try:
            node.to_html()
        except ValueError as e:
            error = str(e)
        self.assertEqual(error, "All parent nodes must have children")

    def test_one_child(self):
        node = ParentNode(tag="p", children=[LeafNode(
            tag="p", value="This is a child node")])
        expected = "<p><p>This is a child node</p></p>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_child(self):
        node = ParentNode(tag="p", children=[ParentNode(tag="div", children=[
                          LeafNode(tag="p", value="This is a child node")])])
        expected = "<p><div><p>This is a child node</p></div></p>"
        self.assertEqual(node.to_html(), expected)
    
    def test_multiple_children(self):
        node = ParentNode("div", children=[
            LeafNode(tag="a", props={"href": "www.google.com"}, value="Google"),
            LeafNode(tag="p", value="Helloooo")
        ])
        expected = '<div><a href="www.google.com">Google</a><p>Helloooo</p></div>'
        self.assertEqual(node.to_html(), expected)
        
    def test_multiple_nested_children(self):
        node = ParentNode(tag="div", children=[
            LeafNode(tag="p", value="I am a child"),
            ParentNode(tag="div", children=[
                LeafNode(tag="p", value="I am a nested child")
            ]),
        ])
        expected = "<div><p>I am a child</p><div><p>I am a nested child</p></div></div>"
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
