import typing as t

from py_html.el.base import BaseHTML


class Image(BaseHTML):
    tag = "image"

    def __init__(
        self,
        alt: t.Optional[str] = None,
        cross_origin: t.Optional[t.Literal["anonymous", "use-credentials"]] = None,
        is_map: t.Optional[bool] = None,
        height: t.Optional[str] = None,
        loading: t.Optional[t.Literal["eager", "lazy"]] = None,
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
        long_desc: t.Optional[t.Any] = None,
        src: t.Optional[str] = None,
        sizes: t.Optional[t.Any] = None,
        src_set: t.Optional[t.List[str]] = None,
        width: t.Optional[str] = None,
        use_map: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            alt=alt,
            cross_origin=cross_origin,
            ismap=is_map,
            height=height,
            loading=loading,
            referrerpolicy=referrer_policy,
            longdesc=long_desc,
            src=src,
            sizes=sizes,
            width=width,
            srcset=src_set,
            usemap=use_map,
            **attrs,
        )


class Map(BaseHTML):
    tag = "map"

    def __init__(
        self,
        name: str,
        **attrs,
    ) -> None:
        super().__init__(
            name=name,
            **attrs,
        )


class Area(BaseHTML):
    tag = "area"

    def __init__(
        self,
        alt: t.Optional[str] = None,
        coords: t.Optional[t.Any] = None,
        download: t.Optional[str] = None,
        href: t.Optional[str] = None,
        href_lang: t.Optional[str] = None,
        media: t.Optional[t.Any] = None,
        rel: t.Optional[
            t.Literal[
                "alternate",
                "author",
                "bookmark",
                "help",
                "license",
                "next",
                "nofollow",
                "noreferrer",
                "prefetch",
                "prev",
                "search",
                "tag",
            ]
        ] = None,
        shape: t.Optional[t.Literal["default", "rect", "circle", "poly"]] = None,
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
            alt=alt,
            coords=coords,
            download=download,
            href=href,
            hreflang=href_lang,
            media=media,
            referrerpolicy=referrer_policy,
            rel=rel,
            shape=shape,
            target=target,
            type=type,
            **attrs,
        )


class Canvas(BaseHTML):
    tag = "canvas"

    def __init__(
        self,
        height: t.Optional[t.Any] = None,
        width: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            height=height,
            width=width,
            **attrs,
        )


class FigCaption(BaseHTML):
    tag = "figcaption"


class Figure(BaseHTML):
    tag = "figure"


class Picture(BaseHTML):
    tag = "picture"


class Svg(BaseHTML):
    tag = "svg"

    def __init__(
        self,
        height: t.Optional[t.Any] = None,
        width: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            height=height,
            width=width,
            **attrs,
        )


class Use(BaseHTML):
    tag = "use"

    def __init__(
        self,
        href: t.Optional[str] = None,
        xlink_href: t.Optional[t.Any] = None,
        x: t.Optional[t.Any] = None,
        y: t.Optional[t.Any] = None,
        height: t.Optional[t.Any] = None,
        width: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        attrs.update({"content": None, "xlink:href": xlink_href})
        super().__init__(
            height=height,
            width=width,
            href=href,
            x=x,
            y=y,
            **attrs,
        )

    def render_tag(self, attrs: str, inner_html: str) -> str:
        return f"<{self.tag} {attrs}/>"
