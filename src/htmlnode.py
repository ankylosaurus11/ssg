class HTMLNode:
    __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = ""
        for key, value in props.items():
            attributes += f' {key}="{value}"'
        return attributes

    def __repr__(self):
        print(tag, value, children, props)