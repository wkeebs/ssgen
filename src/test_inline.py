import unittest
from inline_markdown import *
from text_node import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALICS),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(nodes, expected)


class TestInlineMarkdownSplitting(unittest.TestCase):
    def test_no_split(self):
        node = TextNode("This is a text node with no code", TextType.TEXT)
        new_nodes = split_nodes_delimiter("`", TextType.CODE)([node])
        self.assertEqual(new_nodes, [node])

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter("`", TextType.CODE)([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_into_multiple(self):
        node = TextNode(
            "**This** is a text **node** with multiple **bold words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter("**", TextType.BOLD)([node])
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
        bold_split = split_nodes_delimiter("**", TextType.BOLD)
        italic_split = split_nodes_delimiter("*", TextType.ITALICS)
        code_split = split_nodes_delimiter("`", TextType.CODE)

        splitters = [bold_split, italic_split, code_split]
        for splitter in splitters:
            nodes = splitter(nodes)

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
        self.assertEqual(nodes, expected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(expected, matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        expected = [
            ("link", "https://boot.dev"),
            ("another link", "https://blog.boot.dev"),
        ]
        self.assertListEqual(expected, matches)


class TestSplitInlineMarkdown(unittest.TestCase):
    def test_split_one_image(self):
        node = TextNode(
            "This is text with an image ![of boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("of boot dev", TextType.IMAGE, "https://www.boot.dev"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_two_images(self):
        node = TextNode(
            "This is text with an image ![of boot dev](https://www.boot.dev) and ![of me](https://www.image.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("of boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("of me", TextType.IMAGE, "https://www.image.com"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_no_images(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [node]
        self.assertListEqual(new_nodes, expected)

    def test_split_empty_alt_text(self):
        node = TextNode(
            "Empty alt text ![](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Empty alt text ", TextType.TEXT),
            TextNode("", TextType.IMAGE, "https://www.boot.dev"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_duplicate_image(self):
        node = TextNode(
            "This is text with the same image ![here](https://www.boot.dev) and ![here](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with the same image ", TextType.TEXT),
            TextNode("here", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("here", TextType.IMAGE, "https://www.boot.dev"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_triple_duplicate_image(self):
        node = TextNode(
            "This is text with the same image ![here](https://www.boot.dev) and ![here](https://www.boot.dev) and ![here](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with the same image ", TextType.TEXT),
            TextNode("here", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("here", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("here", TextType.IMAGE, "https://www.boot.dev"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_multiple_duplicate_images(self):
        node = TextNode(
            "This is text with the same image ![here](https://www.boot.dev) and ![here](https://www.boot.dev) and this is ![also here](www.keeble) and ![also here](www.keeble)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with the same image ", TextType.TEXT),
            TextNode("here", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("here", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("also here", TextType.IMAGE, "www.keeble"),
            TextNode(" and ", TextType.TEXT),
            TextNode("also here", TextType.IMAGE, "www.keeble"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_one_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_two_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to me](https://www.image.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to me", TextType.LINK, "https://www.image.com"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_no_images(self):
        node = TextNode("This is text with no links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [node]
        self.assertListEqual(new_nodes, expected)

    def test_split_multiple_duplicate_links(self):
        node = TextNode(
            "This is text with the same link [here](https://www.boot.dev) and [here](https://www.boot.dev) and this is [also here](www.keeble) and [also here](www.keeble)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with the same link ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("also here", TextType.LINK, "www.keeble"),
            TextNode(" and ", TextType.TEXT),
            TextNode("also here", TextType.LINK, "www.keeble"),
        ]
        self.assertListEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
