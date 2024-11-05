from enum import Enum
from typing import Self

from htmlnode import LeafNode


class TextType(Enum):
    """
    : @summary :
    Enumerator for @TextNode, specifically the type of node
    ___________________
    """
    TEXT = "text"
    PARAGRAPH = "paragraph"
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None) -> None:
        """
        : @summary :
        Represents a base text HTML node
        ___________________

        : @args :
            * text (str): the inner text
            * text_type (TextType): the type of node
            * url (str, optional): the url (if applicable). Defaults to None.
        ___________________
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: Self) -> bool:
        """
        : @summary :
        Textnodes are equal if all properties match
        ___________________

        : @args :
            * other (TextNode): the comparing node
        ___________________

        : @returns : 
            * bool: do they match?
        ___________________
        """
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        """
        : @summary :
        String representation generator
        ___________________

        : @returns : 
            * str: the repr
        ___________________
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """
    : @summary :
    Converts a given TextNode to a LeafNode, based on the node type
    ___________________

    : @args :
        * text_node (TextNode): the node itself
    ___________________

    : @raises :
        * Exception: when an invalid text type is given
    ___________________

    : @returns : 
        * LeafNode: the converted node
    ___________________
    """
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(value=text_node.text, tag="b")
        case TextType.ITALICS:
            return LeafNode(value=text_node.text, tag="i")
        case TextType.CODE:
            return LeafNode(value=text_node.text, tag="code")
        case TextType.LINK:
            return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Invalid text type: {text_node.text_type}")
