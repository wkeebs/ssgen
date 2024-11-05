
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode | Tag: '{self.tag}', Value: '{self.value}', Children: '{self.children}', Props: '{self.props}'"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        out = ""
        for key, val in self.props.items():
            out += f" {key}=\"{val}\""
        return out


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        # if there is no tag, return just the value
        if self.tag is None:
            return self.value

        # otherwise render a HTML tag
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")

        if len(self.children) == 0:
            raise ValueError("All parent nodes must have children")

        # otherwise render a HTML tag
        children_string = ''.join(
            list(map(lambda child: child.to_html(), self.children)))
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
