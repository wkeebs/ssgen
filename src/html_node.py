from typing import Self


class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list[Self] = None, props: dict[str, str] = None) -> None:
        """
        : @summary :
        Represents a general HTML node
        ___________________

        : @args :
            * tag (str, optional): the tag type of the node (e.g., "a" for <a>). Defaults to None.
            * value (str, optional): the value inside the node (e.g., <p>value here</p>). Defaults to None.
            * children (list[HTMLNode], optional): any nested child nodes. Defaults to None.
            * props (Dict[str, str]), optional): the properties of the node. Defaults to None.
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
        repr = f"{self.__class__.__name__}\n"
        if self.tag is not None:
            repr += f"Tag: {self.tag}\n"
        if self.value is not None:
            repr += f"Value:\n\"{self.value}\"\n"
        if self.children is not None:
            for node in self.children:
                node_str = str(node)
                lines = node_str.split("\n")
                for l in lines:
                    repr += f"    {l}\n"
        if self.props is not None:
            repr += "-- Props:\n"
            for key, val in self.props.items():
                repr += f"    {key}={val}\n"
        return repr
        

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
