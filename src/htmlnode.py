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
        return f"<{self.tag}>{self.props_to_html()}{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.children is None:
            raise ValueError("No children provided")
        if self.tag is None:
            raise ValueError("No tag provided")

        child_html = ""

        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}>{child_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children={self.children}, {self.props})"

class TextNode(HTMLNode):
    def __init__(self, tag, value, prop=None):
        super().__init__(tag, value, None, None)

    def text_node_to_html_node(text_node):
        text_type_text = "text"
        text_type_bold = "bold"
        text_type_italic = "italic"
        text_type_code = "code"
        text_type_link = "link"
        text_type_image = "image"
        
