import typing as t

from py_html.el.base import BaseElement, BaseHTML


class Script(BaseElement):
    tag = "script"

    def __init__(
        self,
        async_: t.Optional[bool] = None,
        cross_origin: t.Optional[t.Literal["anonymous", "use-credentials"]] = None,
        no_module: t.Optional[t.Literal["true", "false"]] = None,
        defer: t.Optional[bool] = None,
        integrity: t.Optional[str] = None,
        src: t.Optional[str] = None,
        type: t.Optional[str] = None,
        referrer_policy: t.Optional[
            t.Literal[
                "no-referrer",
                "no-referrer-when-downgrade",
                "origin",
                "origin-when-cross-origin",
                "same-origin",
                "strict-origin-when-cross-origin",
                "unsafe-url",
            ]
        ] = None,
        **attrs,
    ) -> None:
        attrs.update(
            {
                "async": async_,
            }
        )
        super().__init__(
            nomodule=no_module,
            crossorigin=cross_origin,
            defer=defer,
            integrity=integrity,
            src=src,
            referrerpolicy=referrer_policy,
            type=type,
            **attrs,
        )


class NoScript(BaseElement):
    tag = "noscript"


class Embed(BaseHTML):
    tag = "embed"

    def __init__(
        self,
        height: t.Optional[t.Any] = None,
        width: t.Optional[t.Any] = None,
        src: t.Optional[str] = None,
        type: t.Optional[str] = None,
        **attrs,
    ) -> None:
        super().__init__(height=height, width=width, src=src, type=type, **attrs)


class Object(BaseHTML):
    tag = "object"

    def __init__(
        self,
        height: t.Optional[t.Any] = None,
        width: t.Optional[t.Any] = None,
        src: t.Optional[str] = None,
        name: t.Optional[str] = None,
        form: t.Optional[str] = None,
        data: t.Optional[str] = None,
        type: t.Optional[str] = None,
        type_must_match: t.Optional[t.Literal["false", "true"]] = None,
        **attrs,
    ) -> None:
        super().__init__(
            height=height,
            width=width,
            src=src,
            type=type,
            name=name,
            form=form,
            data=data,
            typemustmatch=type_must_match,
            **attrs,
        )


class Param(BaseHTML):
    tag = "param"

    def __init__(
        self, name: t.Optional[str] = None, value: t.Optional[str] = None, **attrs
    ) -> None:
        super().__init__(name=name, value=value, **attrs)
