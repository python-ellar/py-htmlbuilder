import typing as t

from py_html.el.base import BaseHTML


class A(BaseHTML):
    tag = "a"

    def __init__(
        self,
        ping: t.Optional[t.Any] = None,
        download: t.Optional[str] = None,
        href: t.Optional[str] = None,
        href_lang: t.Optional[str] = None,
        media: t.Optional[t.Any] = None,
        rel: t.Optional[
            t.Literal[
                "alternate",
                "author",
                "bookmark",
                "external",
                "help",
                "license",
                "next",
                "nofollow",
                "noreferrer",
                "noopener",
                "prev",
                "search",
                "tag",
            ]
        ] = None,
        target: t.Optional[
            t.Literal[
                "_blank",
                "_self",
                "_parent",
                "_top",
            ]
        ] = None,
        type: t.Optional[t.Any] = None,
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
        super().__init__(
            ping=ping,
            download=download,
            href=href,
            hreflang=href_lang,
            media=media,
            referrerpolicy=referrer_policy,
            rel=rel,
            target=target,
            type=type,
            **attrs,
        )


class Link(BaseHTML):
    tag = "link"

    def __init__(
        self,
        cross_origin: t.Optional[t.Literal["anonymous", "use-credentials"]] = None,
        sizes: t.Optional[t.Any] = None,
        href: t.Optional[str] = None,
        href_lang: t.Optional[str] = None,
        media: t.Optional[t.Any] = None,
        rel: t.Optional[
            t.Literal[
                "alternate",
                "author",
                "dns-prefetch",
                "help",
                "icon",
                "license",
                "next",
                "pingback",
                "preconnect",
                "prefetch",
                "preload",
                "prerender",
                "prev",
                "search",
                "stylesheet",
            ]
        ] = None,
        type: t.Optional[t.Any] = None,
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
        super().__init__(
            crossorigin=cross_origin,
            sizes=sizes,
            href=href,
            hreflang=href_lang,
            media=media,
            referrerpolicy=referrer_policy,
            rel=rel,
            type=type,
            **attrs,
        )

    def render_tag(self, attrs: str, inner_html: str) -> str:
        tag_output = f"<{self.tag} {attrs}/>" if attrs else f"<{self.tag}/>"
        return tag_output


class Nav(BaseHTML):
    tag = "nav"
