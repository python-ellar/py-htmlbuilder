from dataclasses import dataclass, field, asdict
from typing import List, Union, Optional, Dict

class Style:
    def __init__(self, **styles):
        self.styles = styles

    def set_style(self, property, value):
        self.styles[property] = value

    def render(self):
        return '; '.join(f'{prop}: {val}' for prop, val in self.styles.items() if val is not None)

@dataclass
class Element:
    id: Optional[str] = None
    class_: Optional[str] = None
    style: Union[Style, Dict[str, str], None] = None
    title: Optional[str] = None
    lang: Optional[str] = None
    dir: Optional[str] = None
    attrs: Dict[str, Union[str, Style]] = field(default_factory=dict)

    def __post_init__(self):
        if self.id:
            self.attrs['id'] = self.id
        if self.class_:
            self.attrs['class'] = self.class_
        if self.title:
            self.attrs['title'] = self.title
        if self.lang:
            self.attrs['lang'] = self.lang
        if self.dir:
            self.attrs['dir'] = self.dir
        if isinstance(self.style, dict):
            self.attrs['style'] = Style(**self.style)
        elif isinstance(self.style, Style):
            self.attrs['style'] = self.style

    def set_attribute(self, key, value):
        self.attrs[key] = value

    def get_attribute(self, key):
        return self.attrs.get(key)

    def render_attributes(self):
        rendered_attrs = []
        for key, value in self.attrs.items():
            if value is None:
                continue
            if isinstance(value, Style):
                rendered_attrs.append(f'{key}="{value.render()}"')
            else:
                rendered_attrs.append(f'{key}="{value}"')
        return ' '.join(rendered_attrs)

@dataclass
class HTMLElement(Element):
    tag: str = ""
    text: Optional[str] = None
    children: List[Union['HTMLElement', str]] = field(default_factory=list)

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        opening_tag = f'<{self.tag} {self.render_attributes()}>' if self.attrs else f'<{self.tag}>'
        inner_html = self.text if self.text else ''.join(child.render() if isinstance(child, HTMLElement) else str(child) for child in self.children)
        closing_tag = f'</{self.tag}>'
        return f'{opening_tag}{inner_html}{closing_tag}'

    def __str__(self):
        return self.render()

# Specific HTML element classes
@dataclass
class Div(HTMLElement):
    def __init__(self, text=None, children=None, **attrs):
        super().__init__('div', text, children or [], **attrs)

@dataclass
class Span(HTMLElement):
    def __init__(self, text=None, children=None, **attrs):
        super().__init__('span', text, children or [], **attrs)

@dataclass
class P(HTMLElement):
    def __init__(self, text=None, children=None, **attrs):
        super().__init__('p', text, children or [], **attrs)

@dataclass
class Script(HTMLElement):
    def __init__(self, src=None, text=None, **attrs):
        if src:
            attrs['src'] = src
        super().__init__('script', text, [], **attrs)

@dataclass
class Button(HTMLElement):
    def __init__(self, text=None, onclick=None, **attrs):
        if onclick:
            attrs['onclick'] = onclick
        super().__init__('button', text, [], **attrs)

# Main Block
if __name__ == "__main__":
    display_demo = Div(
        id="main-container",
        class_="container",
        style={"display": "block", "padding": "20px", "background-color": "#f9f9f9"},
        children=[
            Div(
                id="block-display",
                style={"display": "block", "background-color": "#add8e6", "padding": "10px"},
                text="Block Display"
            ),
            Span(
                id="inline-display",
                style={"display": "inline", "background-color": "#90ee90", "padding": "10px"},
                text="Inline Display"
            ),
            Div(
                id="inline-block-display",
                style={"display": "inline-block", "background-color": "#ffb6c1", "padding": "10px"},
                text="Inline-Block Display"
            ),
            Div(
                id="flex-display",
                style={
                    "display": "flex",
                    "background-color": "#ffe4b5",
                    "padding": "10px",
                    "justify-content": "space-around"
                },
                children=[
                    Div(id="flex-item-1", style={"background-color": "#ff6347", "padding": "10px"}, text="Flex Item 1"),
                    Div(id="flex-item-2", style={"background-color": "#4682b4", "padding": "10px"}, text="Flex Item 2"),
                    Div(id="flex-item-3", style={"background-color": "#dda0dd", "padding": "10px"}, text="Flex Item 3")
                ]
            ),
            Div(
                id="grid-display",
                style={
                    "display": "grid",
                    "background-color": "#e6e6fa",
                    "padding": "10px",
                    "grid-template-columns": "1fr 1fr",
                    "gap": "10px"
                },
                children=[
                    Div(id="grid-item-1", style={"background-color": "#7fffd4", "padding": "10px"}, text="Grid Item 1"),
                    Div(id="grid-item-2", style={"background-color": "#fa8072", "padding": "10px"}, text="Grid Item 2"),
                    Div(id="grid-item-3", style={"background-color": "#ffefd5", "padding": "10px"}, text="Grid Item 3"),
                    Div(id="grid-item-4", style={"background-color": "#afeeee", "padding": "10px"}, text="Grid Item 4")
                ]
            ),
            Div(
                id="none-display",
                style={"display": "none", "background-color": "#d3d3d3", "padding": "10px"},
                text="None Display (Shouldn't be visible)"
            )
        ]
    )

    print(display_demo.render())
