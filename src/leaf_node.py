from typing import Dict
from html_node import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: Dict[str, str] = None) -> None:
        """
        : @summary :
        Represents a leaf node, i.e., a HTML node with no children
        ___________________

        : @args :
            * tag (str, optional): the HTML tag. Defaults to None.
            * value (str, optional): the value inside the leaf. Defaults to None.
            * props (Dict[str, str], optional): any properties the node has. Defaults to None.
        ___________________
        """
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        """
        : @summary :
        Converts the leaf node to HTML format
        ___________________

        : @raises :
            * ValueError: when the leaf has no value
        ___________________

        : @returns : 
            * str: the formatted node (i.e., the repr)
        ___________________
        """
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        # if there is no tag, return just the value
        if self.tag is None:
            return self.value

        # otherwise render a HTML tag
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
