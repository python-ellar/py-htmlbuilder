import typing as t

from py_html.el.base import BaseHTML, NodeContext
from py_html.styles import StyleCSS


class Style(BaseHTML):
    tag = "style"

    def __init__(
        self,
        *content: t.Union[t.Dict[str, StyleCSS], t.Any],
        type: str = "text/css",
        media: t.Optional[str] = None,
        **attrs,
    ) -> None:
        super().__init__(*content, type=type, media=media, **attrs)

    def render_content(
        self, children: t.Optional[t.List[NodeContext]], parent: NodeContext
    ) -> str:
        for item in children or []:
            if isinstance(item, (dict, StyleCSS)):
                ensure_style_css = StyleCSS(**item)

                inner_html = " ".join(
                    (
                        f"{k} " + "{" + f"{v.render()}" + "}"
                        for k, v in ensure_style_css.items()
                    )
                )

                return inner_html
        return parent.render_content(children)


class Div(BaseHTML):
    tag = "div"


class Span(BaseHTML):
    tag = "span"


class Header(BaseHTML):
    tag = "header"


class HGroup(BaseHTML):
    tag = "hgroup"


class Footer(BaseHTML):
    tag = "footer"


class Main(BaseHTML):
    tag = "main"


class Section(BaseHTML):
    tag = "section"


class Search(BaseHTML):
    tag = "search"


class Article(BaseHTML):
    tag = "article"


class Aside(BaseHTML):
    tag = "aside"


class Details(BaseHTML):
    tag = "details"

    def __init__(self, open: t.Optional[bool] = None, **attrs) -> None:
        super().__init__(open=open, **attrs)


class Dialog(Details):
    tag = "dialog"


class Summary(BaseHTML):
    tag = "summary"


class Data(BaseHTML):
    tag = "data"

    def __init__(self, value: t.Optional[t.Any] = None, **attrs) -> None:
        super().__init__(value=value, **attrs)
