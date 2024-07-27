import typing as t

from py_html.el.base import BaseHTML


class Table(BaseHTML):
    tag = "table"


class Caption(BaseHTML):
    tag = "caption"


class Th(BaseHTML):
    tag = "th"

    def __init__(
        self,
        *content,
        abbr: t.Optional[str] = None,
        colspan: t.Optional[int] = None,
        headers: t.Optional[str] = None,
        rowspan: t.Optional[int] = None,
        scope: t.Optional[t.Literal["col", "colgroup", "row", "rowgroup"]] = None,
        **attrs,
    ) -> None:
        super().__init__(
            *content,
            abbr=abbr,
            colspan=colspan,
            headers=headers,
            rowspan=rowspan,
            scope=scope,
            **attrs,
        )


class Tr(BaseHTML):
    tag = "tr"


class Td(BaseHTML):
    tag = "td"

    def __init__(
        self,
        *content,
        colspan: t.Optional[int] = None,
        headers: t.Optional[str] = None,
        rowspan: t.Optional[int] = None,
        **attrs,
    ) -> None:
        super().__init__(
            *content, colspan=colspan, headers=headers, rowspan=rowspan, **attrs
        )


class Thead(BaseHTML):
    tag = "thead"


class Tbody(BaseHTML):
    tag = "tbody"


class Tfoot(BaseHTML):
    tag = "tfoot"


class Col(BaseHTML):
    tag = "col"

    def __init__(self, *content, span: t.Optional[int] = None, **attrs) -> None:
        super().__init__(*content, span=span, **attrs)


class ColGroup(Col):
    tag = "colgroup"
