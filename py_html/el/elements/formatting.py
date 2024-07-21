import typing

from py_html.el.base import BaseHTML


class Abbr(BaseHTML):
    tag = "abbr"


class Address(BaseHTML):
    tag = "address"


class BlockQuote(BaseHTML):
    tag = "blockquote"

    def __init__(self, cite: typing.Optional[str] = None, **attrs) -> None:
        super().__init__(cite=cite, **attrs)


class Q(BlockQuote):
    tag = "q"


class Code(BaseHTML):
    tag = "code"


class Del(BaseHTML):
    tag = "del"

    def __init__(
        self,
        cite: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        **attrs,
    ) -> None:
        super().__init__(cite=cite, datetime=datetime, **attrs)


class Dfn(BaseHTML):
    tag = "dfn"


class Em(BaseHTML):
    tag = "em"


class I(BaseHTML):
    tag = "i"


class Ins(Del):
    tag = "ins"


class Kbd(BaseHTML):
    tag = "kbd"


class Mark(BaseHTML):
    tag = "mark"


class Meter(BaseHTML):
    tag = "meter"

    def __init__(
        self,
        form: typing.Optional[str] = None,
        high: typing.Optional[int] = None,
        low: typing.Optional[int] = None,
        max: typing.Optional[int] = None,
        min: typing.Optional[int] = None,
        optimum: typing.Optional[int] = None,
        value: typing.Optional[int] = None,
        **attrs,
    ) -> None:
        super().__init__(
            form=form,
            high=high,
            low=low,
            max=max,
            min=min,
            optimum=optimum,
            value=value,
            **attrs,
        )


class Pre(BaseHTML):
    tag = "pre"


class Progress(BaseHTML):
    tag = "progress"

    def __init__(
        self,
        max: typing.Optional[int] = None,
        value: typing.Optional[int] = None,
        **attrs,
    ) -> None:
        super().__init__(max=max, value=value, **attrs)


class Rp(BaseHTML):
    tag = "rp"


class Rt(BaseHTML):
    tag = "rt"


class Ruby(BaseHTML):
    tag = "ruby"


class S(BaseHTML):
    tag = "s"


class Samp(BaseHTML):
    tag = "samp"


class Small(BaseHTML):
    tag = "small"


class Strong(BaseHTML):
    tag = "strong"


class Sub(BaseHTML):
    tag = "sub"


class Sup(BaseHTML):
    tag = "sup"


class Template(BaseHTML):
    tag = "template"


class Time(BaseHTML):
    tag = "time"


class U(BaseHTML):
    tag = "u"


class Wbr(BaseHTML):
    tag = "wbr"


class Var(BaseHTML):
    tag = "var"
