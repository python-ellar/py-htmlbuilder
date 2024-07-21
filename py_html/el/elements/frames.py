import typing as t

from py_html.el.base import BaseHTML


class IFrame(BaseHTML):
    tag = "iframe"

    def __init__(
        self,
        allow: t.Optional[bool] = None,
        allow_fullscreen: t.Optional[t.Literal["true", "false"]] = None,
        allow_payment_request: t.Optional[t.Literal["true", "false"]] = None,
        height: t.Optional[str] = None,
        loading: t.Optional[t.Literal["eager", "lazy"]] = None,
        name: t.Optional[str] = None,
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
        sandbox: t.Optional[
            t.Literal[
                "allow-forms",
                "allow-pointer-lock",
                "allow-popups",
                "allow-same-origin",
                "allow-scripts",
                "allow-top-navigation",
            ]
        ] = None,
        src: t.Optional[str] = None,
        srcdoc: t.Optional[str] = None,
        width: t.Optional[str] = None,
        **attrs,
    ) -> None:
        super().__init__(
            allow=allow,
            allowfullscreen=allow_fullscreen,
            allowpaymentrequest=allow_payment_request,
            height=height,
            loading=loading,
            name=name,
            referrerpolicy=referrer_policy,
            sandbox=sandbox,
            src=src,
            srcdoc=srcdoc,
            width=width,
            **attrs,
        )
