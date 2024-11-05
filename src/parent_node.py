from typing import Dict, List
from html_node import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: List[HTMLNode] = [], props: Dict[str, str] = None) -> None:
        """
        : @summary :
        Represents a "Parent" HTML node - one that has some (>=1) nested children
        ___________________

        : @args :
            * tag (str, optional): the HTML tag. Defaults to None.
            * children (List[HTMLNode], optional): any child nodes. Defaults to [].
            * props (Dict[str, str], optional): the HTML properties. Defaults to None.
        ___________________
        """
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        """
        : @summary :
        Converts the parent node to its html format, recursively converting
        its children in the process.
        ___________________

        : @raises :
            * ValueError: when the parent has no tag
            * ValueError: when the parents has no children
        ___________________

        : @returns : 
            * str: the HTML formatted node
        ___________________
        """
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")

        if len(self.children) == 0:
            raise ValueError("All parent nodes must have children")

        # otherwise render a HTML tag
        children_string = ''.join(
            list(map(lambda child: child.to_html(), self.children)))
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
