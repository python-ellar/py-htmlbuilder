import typing as t

from py_html.el.base import BaseHTML


class Menu(BaseHTML):
    tag = "menu"


class Ul(BaseHTML):
    tag = "ul"


class Ol(BaseHTML):
    tag = "ol"

    def __init__(
        self,
        *content,
        reversed: t.Optional[bool] = None,
        start: t.Optional[int] = None,
        type: t.Optional[t.Literal["1", "A", "a", "I", "i"]] = None,
        **attrs,
    ) -> None:
        super().__init__(*content, reversed=reversed, start=start, type=type, **attrs)


class Li(BaseHTML):
    tag = "li"

    def __init__(self, *content, value: t.Optional[int] = None, **attrs) -> None:
        super().__init__(*content, value=value, **attrs)


class Dl(BaseHTML):
    tag = "dl"


class Dt(BaseHTML):
    tag = "dt"


class Dd(BaseHTML):
    tag = "dd"
