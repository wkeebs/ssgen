from typing import List

from text_node import TextNode, TextType


def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    """
    : @summary :
    Splits text nodes by a delimiter based on the text node type
    ___________________

    : @args :
        * old_nodes (List[TextNode]): the nodes to be split
        * delimeter (str): the delimiter to split by
        * text_type (TextType): the type of text nodes to operate on
    ___________________

    : @returns : 
        * List[TextNode]: the new, split text nodes
    ___________________
    """
    new_nodes = []

    # split the nodes
    for old_node in old_nodes:
        split_text = old_node.text.split(delimiter)
        for idx, text in enumerate(split_text):
            if idx % 2 == 0:
                # the new nodes will have odd indices
                # because of how .split() works
                new_nodes.append(TextNode(text=text, text_type=old_node.text_type))
                continue
            new_node = TextNode(text=text, text_type=text_type)
            new_nodes.append(new_node)

    # filter out empty text nodes for brevity
    empty_node = TextNode("", TextType.TEXT)
    return list(filter(lambda n: n != empty_node, new_nodes))


if __name__ == "__main__":
    nodes = [
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text *with some* italics", TextType.TEXT),
            TextNode("This is **text with some bold**", TextType.TEXT),
            TextNode("This is normal text!", TextType.TEXT)
        ]
    bold_split = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split,"*",TextType.ITALICS)
    new_nodes = split_nodes_delimiter(italic_split, "`", TextType.CODE)
    print(new_nodes)
