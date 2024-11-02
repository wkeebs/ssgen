
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
        out = ""
        for key, val in self.props.items():
            out += f" {key}=\"{val}\""
        return out