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

        if len(split_text) % 2 == 0:
            raise ValueError("Invalid markdown: formatted section not closed")

        for idx, text in enumerate(split_text):
            if text == "":
                # .split() generates empty strings if nothing exists
                # before or after the delimiter
                continue

            # the formatted nodes have odd indices
            if idx % 2 == 0:
                new_nodes.append(
                    TextNode(text=text, text_type=old_node.text_type))
            else:
                new_nodes.append(TextNode(text=text, text_type=text_type))

    return new_nodes
