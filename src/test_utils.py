import unittest

from utils import split_nodes_delimiter
from text_node import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_split(self):
        node = TextNode("This is a text node with no code", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_into_multiple(self):
        node = TextNode(
            "**This** is a text **node** with multiple **bold words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This", TextType.BOLD),
            TextNode(" is a text ", TextType.TEXT),
            TextNode("node", TextType.BOLD),
            TextNode(" with multiple ", TextType.TEXT),
            TextNode("bold words", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_nodes(self):
        self.maxDiff = None
        nodes = [
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text *with some* italics", TextType.TEXT),
            TextNode("This is **text with some bold**", TextType.TEXT),
            TextNode("This is normal text!", TextType.TEXT)
        ]
        bold_split = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        italic_split = split_nodes_delimiter(bold_split, "*", TextType.ITALICS)
        new_nodes = split_nodes_delimiter(italic_split, "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text ", TextType.TEXT),
            TextNode("with some", TextType.ITALICS),
            TextNode(" italics", TextType.TEXT),
            TextNode("This is ", TextType.TEXT),
            TextNode("text with some bold", TextType.BOLD),
            TextNode("This is normal text!", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
