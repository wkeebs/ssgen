import unittest
from text_node import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        exp_repr1 = "TextNode(\"This is a text node\", Type: bold, URL: None)"
        self.assertEqual(str(node1), exp_repr1)

        node2 = TextNode("This is a text node",
                         TextType.BOLD, "www.keeble.tech")
        exp_repr2 = "TextNode(\"This is a text node\", Type: bold, URL: www.keeble.tech)"
        self.assertEqual(str(node2), exp_repr2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node",
                         TextType.BOLD, "www.keeble.tech")
        self.assertNotEqual(node1, node2)

        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text nodE", TextType.BOLD)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.ITALICS)
        node6 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node5, node6)

        node7 = TextNode("This is a text node",
                         TextType.BOLD, "www.keeble.teck")
        node8 = TextNode("This is a text node",
                         TextType.BOLD, "www.keeble.tech")
        self.assertNotEqual(node7, node8)


class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        leaf_node = text_node_to_html_node(text_node)
        self.assertTrue(isinstance(leaf_node, LeafNode))
        self.assertEqual(leaf_node.to_html(), "This is a text node")

    def test_bold(self):
        text_node = TextNode("This is a bold node", TextType.BOLD)
        leaf_node = text_node_to_html_node(text_node)
        self.assertTrue(isinstance(leaf_node, LeafNode))
        self.assertEqual(leaf_node.to_html(), "<b>This is a bold node</b>")

    def test_italics(self):
        text_node = TextNode("This is a italic node", TextType.ITALICS)
        leaf_node = text_node_to_html_node(text_node)
        self.assertTrue(isinstance(leaf_node, LeafNode))
        self.assertEqual(leaf_node.to_html(), "<i>This is a italic node</i>")

    def test_code(self):
        text_node = TextNode("This is a code node", TextType.CODE)
        leaf_node = text_node_to_html_node(text_node)
        self.assertTrue(isinstance(leaf_node, LeafNode))
        self.assertEqual(leaf_node.to_html(),
                         "<code>This is a code node</code>")

    def test_link(self):
        url = "www.google.com"
        text_node = TextNode("This is a link", TextType.LINK, url)
        leaf_node = text_node_to_html_node(text_node)
        self.assertTrue(isinstance(leaf_node, LeafNode))
        self.assertEqual(leaf_node.to_html(), f'<a href="{
                         url}">This is a link</a>')

    def test_image(self):
        src = "/images/image.png"
        text = "This is an image"
        text_node = TextNode(text, TextType.IMAGE, url=src)
        leaf_node = text_node_to_html_node(text_node)
        self.assertTrue(isinstance(leaf_node, LeafNode))
        self.assertEqual(leaf_node.to_html(), f'<img src="{
                         src}" alt="{text}"></img>')


if __name__ == "__main__":
    unittest.main()
