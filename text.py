import loremipsum
from dataclasses import dataclass
from py_html.el.elements.meta_info import Meta

from py_html.el.elements.forms import TextArea

from py_html.el.elements.programming import Script

from py_html.el.elements.links import Link

from py_html.el.elements.basic import Html, Body, Head, Title, H3, Fragment

from py_html.styles import StyleCSS

from py_html.el.elements.semantics import Div, Span, Style, Section


class BlockContainer(Div):
    style = StyleCSS(display="block", backgroundColor="#f9f9f9", padding="20px")
    class_name = "container"


block_container = BlockContainer


@dataclass
class Post:
    title: str
    content: str


def head_component(page_title: str, **attrs):
    return Head(
        **attrs,
        content=[
            Title(page_title=page_title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Style(
                content=lambda ctx: {
                    'a': StyleCSS(),
                    '#block-display': StyleCSS(backgroundColor="#add8e6", padding="10px")
                }
            ),
            # Latest compiled and minified CSS
            Link(
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
                rel="stylesheet"
            ),
            # Latest compiled JavaScript
            Script(
                src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            )
        ]
    )


def body(content):
    if not isinstance(content, (list, tuple)):
        content = [content]

    return Body(
        content=Fragment(
            BlockContainer(
                content=lambda ctx: [
                    Div(
                        id="block-display",
                        style=StyleCSS(display="block"),
                        content="Block Display",
                    ),
                    Span(
                        id="inline-display",
                        style=StyleCSS(display="inline", backgroundColor="#90ee90", padding="10px"),
                        content="Inline Display",
                    ),
                    lambda ctx: Div(
                        id="inline-block-display",
                        style=StyleCSS(
                            display="inline-block",
                            backgroundColor="#ffb6c1",
                            padding="10px"
                        ),
                        content=lambda ctx: [
                            "Inline-Block Display"
                        ],
                    ),
                ]
            ),
            *content
        )
    )


if __name__ == "__main__":
    display_demo = Html(
        content=Fragment(
            head_component(page_title="Bootstrap Example"),
            body(content=Fragment(
                Section(
                    id="flex-display",
                    style=StyleCSS(
                        display="flex",
                        backgroundColor="#ffe4b5",
                        padding="10px",
                        justifyContent="space-around",
                    ),
                    content=(
                        Div(
                            id="flex-item-1",
                            style=StyleCSS(backgroundColor="#ff6347", padding="10px"),
                            content="Flex Item 1",
                        ),
                        Div(
                            id="flex-item-2",
                            style=StyleCSS(backgroundColor="#4682b4", padding="10px"),
                            content="Flex Item 2",
                        ),
                        Div(
                            id="flex-item-3",
                            style=StyleCSS(backgroundColor="#dda0dd", padding="10px"),
                            content="Flex Item 3",
                        ),
                    ),
                ),
                Section(
                    id="grid-display",
                    style=StyleCSS(
                        display="grid",
                        backgroundColor="#e6e6fa",
                        padding="10px",
                        gridTemplateColumns="1fr 1fr",
                        gap="10px",
                    ),
                    content=lambda ctx: [
                        Div(
                            style=StyleCSS(backgroundColor="#7fffd4", padding="10px"),
                            content=(
                                H3(content=item.title),
                                TextArea(content=item.content, rows=4)
                            ),
                        )
                        for item in ctx['posts']
                        # Div(
                        #     id="grid-item-1",
                        #     style=StyleCSS(backgroundColor="#7fffd4", padding="10px"),
                        #     text="Grid Item 1",
                        # ),
                        # Div(
                        #     id="grid-item-2",
                        #     style=StyleCSS(backgroundColor="#fa8072", padding="10px"),
                        #     text="Grid Item 2",
                        # ),
                        # Div(
                        #     id="grid-item-3",
                        #     style=StyleCSS(backgroundColor="#ffefd5", padding="10px"),
                        #     text="Grid Item 3",
                        # ),
                        # Div(
                        #     id="grid-item-4",
                        #     style=StyleCSS(backgroundColor="#afeeee", padding="10px"),
                        #     text="Grid Item 4",
                        # ),
                    ],
                ),
                Section(
                    id="none-display",
                    style=StyleCSS(
                        display="none",
                        backgroundColor="#d3d3d3",
                        padding="10px",
                    ),
                    content="None Display (Shouldn't be visible)",
                )
            ))
        )
    )
    dvcdsv = display_demo.render(ctx={
        'posts': [Post(title=f"Post {i + 1}", content=loremipsum.get_paragraph(True)) for i in range(50)]
    })
    print(dvcdsv, sep="")
