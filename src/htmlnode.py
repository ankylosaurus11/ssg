class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        attributes = ""
        for key, value in self.props.items():
            attributes += f' {key}="{value}"'
        return attributes

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if value == "":
            raise ValueError("No value provided")
        self.value = value

    def to_html(self):
        if not self.tag:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if children == "":
            raise ValueError("No children provided")
        if tag == "":
            raise ValueError("No tag provided")
        
    def to_html(self):
        
