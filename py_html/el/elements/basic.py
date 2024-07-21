import typing as t

from py_html.el.base import BaseElement, BaseHTML, Element, BuildContext


class DOCTYPE(Element):
    def __init__(self, page_content: t.Any) -> None:
        self.content = page_content

    def render(self, ctx: BuildContext):
        html = ctx.render_content(self.content)
        return f"<!DOCTYPE html>{html}"


class Html(BaseElement):
    tag = "html"

    def __init__(
        self,
        lang: t.Optional[str] = None,
        xmlns: str = "http://www.w3.org/1999/xhtml",
        **attrs,
    ) -> None:
        super().__init__(lang=lang, xmlns=xmlns, **attrs)


class Head(BaseElement):
    tag = "head"


class Title(Element):
    def __init__(self, page_title: str = "") -> None:
        self.page_title = page_title

    def render(self, ctx: t.Dict):
        return f"<title>{self.page_title}</title>"


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

    def _tag_output(self, attrs: str, inner_html: str):
        return f"<{self.tag} {attrs}>" if attrs else f"<{self.tag}>"


class Hr(Br):
    tag = "hr"


class Comment(Element):
    def __init__(self, comment: str = "") -> None:
        self.comment = comment

    def render(self, ctx: t.Dict):
        return f"<!--{self.comment}-->"


class Fragment(Element):
    def __init__(self, *contents: t.Union[Element, t.Any]) -> None:
        self.content = contents

    def render(self, ctx: BuildContext):
        _gen = (ctx.render_content(content) for content in self.content)
        return " ".join(_gen)
