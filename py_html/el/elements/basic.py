import typing as t

from py_html.el.base import BaseElement, BaseHTML, Element


class Html(BaseElement):
    tag = "html"

    def __init__(
        self,
        *content: t.Any,
        lang: t.Optional[str] = None,
        xmlns: str = "http://www.w3.org/1999/xhtml",
        **attrs,
    ) -> None:
        super().__init__(*content, lang=lang, xmlns=xmlns, **attrs)

    def render_tag(self, attrs: str, inner_html: str):
        # html = ctx.render_content(self.content)
        return f"<!DOCTYPE html><{self.tag} {attrs}>{inner_html}</{self.tag}>"


class Head(BaseElement):
    tag = "head"


class Title(Element):
    def __init__(self, page_title: str = "") -> None:
        self.content = page_title

    def render_tag(self, attrs: str, inner_html: str):
        return f"<title>{inner_html}</title>"


class Body(BaseHTML):
    tag = "body"


class H1(BaseHTML):
    tag = "h1"


class H2(BaseHTML):
    tag = "h2"


class H3(BaseHTML):
    tag = "h3"


class H4(BaseHTML):
    tag = "h4"


class H5(BaseHTML):
    tag = "h5"


class H6(BaseHTML):
    tag = "h6"


class P(BaseHTML):
    tag = "p"


class Br(BaseHTML):
    tag = "br"

    def render_tag(self, attrs: str, inner_html: str):
        return f"<{self.tag} {attrs}>" if attrs else f"<{self.tag}>"


class Hr(Br):
    tag = "hr"


class Comment(Element):
    def __init__(self, comment: str = "") -> None:
        self.content = comment

    def render_tag(self, attrs: str, inner_html: str) -> str:
        return f"<!--{inner_html}-->"
