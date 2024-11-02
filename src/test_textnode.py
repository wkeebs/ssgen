import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        exp_repr1 = "TextNode(This is a text node, bold, None)"
        self.assertEqual(str(node1), exp_repr1)

        node2 = TextNode("This is a text node",
                         TextType.BOLD, "www.keeble.tech")
        exp_repr2 = "TextNode(This is a text node, bold, www.keeble.tech)"
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


if __name__ == "__main__":
    unittest.main()
