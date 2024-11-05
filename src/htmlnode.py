from typing import List, Self, Dict


class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: List[Self] = None, props: str = None) -> None:
        """
        : @summary :
        Represents a general HTML node
        ___________________

        : @args :
            * tag (str, optional): the tag type of the node (e.g., "a" for <a>). Defaults to None.
            * value (str, optional): the value inside the node (e.g., <p>value here</p>). Defaults to None.
            * children (HTMLNode[], optional): any nested child nodes. Defaults to None.
            * props {str: str}, optional): the properties of the node. Defaults to None.
        ___________________
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        """
        : @summary :
        String representation of the node
        ___________________

        : @returns : 
            * str: the repr
        ___________________
        """
        return f"HTMLNode | Tag: '{self.tag}', Value: '{self.value}', Children: '{self.children}', Props: '{self.props}'"

    def to_html(self) -> NotImplementedError:
        """
        : @summary :
        To be overridden by children
        ___________________

        : @raises :
            * NotImplementedError: when called directly
        ___________________
        """
        raise NotImplementedError

    def props_to_html(self) -> str:
        """
        : @summary :
        Converts the properties of the HTML node to string format
        ___________________

        : @returns : 
            * str: the formatted properties
        ___________________
        """
        if self.props is None:
            return ""

        out = ""
        for key, val in self.props.items():
            out += f" {key}=\"{val}\""
        return out


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: Dict[str][str] = None) -> None:
        """
        : @summary :
        Represents a leaf node, i.e., a HTML node with no children
        ___________________

        : @args :
            * tag (str, optional): the HTML tag. Defaults to None.
            * value (str, optional): the value inside the leaf. Defaults to None.
            * props ({str: str}, optional): any properties the node has. Defaults to None.
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


class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: List[HTMLNode] = [], props: Dict[str][str] = None) -> None:
        """
        : @summary :
        Represents a "Parent" HTML node - one that has some nested children
        ___________________

        : @args :
            * tag (str, optional): the HTML tag. Defaults to None.
            * children (HTMLNode[], optional): any child nodes. Defaults to [].
            * props ({str: str}, optional): the HTML properties. Defaults to None.
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
