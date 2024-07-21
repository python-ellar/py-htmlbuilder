import typing as t

from py_html.el.base import BaseElement, BaseHTML


class Meta(BaseElement):
    tag = "meta"

    def __init__(
        self,
        charset: t.Optional[t.Union[t.Literal["utf-8"], t.Any]] = None,
        content: t.Optional[str] = None,
        http_equiv: t.Optional[
            t.Literal[
                "content-security-policy", "content-type", "default-style", "refresh"
            ]
        ] = None,
        name: t.Optional[
            t.Literal[
                "application-name",
                "author",
                "description",
                "generator",
                "keywords",
                "viewport",
            ]
        ] = None,
        **attrs,
    ) -> None:
        attrs.update({"http-equiv": http_equiv})
        super().__init__(charset=charset, name=name, **attrs)
        self.attrs.update(content=content)

    def _tag_output(self, attrs: str, inner_html: str) -> str:
        return f"<{self.tag} {attrs} {inner_html}>"


class Base(BaseHTML):
    tag = "base"

    def __init__(
        self,
        href: t.Optional[t.Any] = None,
        target: t.Optional[t.Literal["_blank", "_parent", "_self", "_top"]] = None,
        **attrs,
    ) -> None:
        super().__init__(href=href, target=target, **attrs)
