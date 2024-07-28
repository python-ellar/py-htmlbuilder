import typing as t

from py_html.el.base import BaseElement, BaseHTML


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
        *content: t.Any,
        height: t.Optional[t.Any] = None,
        width: t.Optional[t.Any] = None,
        xmlns: str = "http://www.w3.org/2000/svg",
        viewBox: t.Optional[str] = None,
        role: str = "img",
        **attrs,
    ) -> None:
        super().__init__(
            *content,
            height=height,
            width=width,
            xmlns=xmlns,
            role=role,
            viewBox=viewBox,
            **attrs,
        )


class Use(BaseHTML):
    tag = "use"

    def __init__(
        self,
        *content,
        href: t.Optional[str] = None,
        xlink_href: t.Optional[t.Any] = None,
        x: t.Optional[t.Any] = None,
        y: t.Optional[t.Any] = None,
        height: t.Optional[t.Any] = None,
        width: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        attrs.update({"content": (), "xlink:href": xlink_href})
        super().__init__(
            *content,
            height=height,
            width=width,
            href=href,
            x=x,
            y=y,
            **attrs,
        )

    def render_tag(self, attrs: str, inner_html: str) -> str:
        return f"<{self.tag} {attrs}/>"


class Circle(BaseElement):
    tag = "circle"

    def __init__(
        self,
        *content: t.Any,
        cx: t.Optional[int] = None,
        cy: t.Optional[int] = None,
        r: t.Optional[int] = None,
        stroke: t.Optional[str] = None,
        stroke_width: t.Optional[str] = None,
        fill: t.Optional[str] = None,
        **attrs,
    ):
        super().__init__(
            *content,
            cx=cx,
            cy=cy,
            r=r,
            stroke=stroke,
            stroke_width=stroke_width,
            fill=fill,
            **attrs,
        )


class Rect(BaseElement):
    tag = "rect"

    def __init__(
        self,
        *content: t.Any,
        x: t.Optional[int] = None,
        y: t.Optional[int] = None,
        width: t.Optional[int] = None,
        height: t.Optional[int] = None,
        stroke: t.Optional[str] = None,
        stroke_width: t.Optional[str] = None,
        fill: t.Optional[str] = None,
        **attrs,
    ):
        super().__init__(
            *content,
            x=x,
            y=y,
            width=width,
            height=height,
            stroke=stroke,
            stroke_width=stroke_width,
            fill=fill,
            **attrs,
        )


class Polygon(BaseElement):
    tag = "polygon"

    def __init__(
        self,
        *content: t.Any,
        points: t.Optional[str] = None,
        stroke: t.Optional[str] = None,
        stroke_width: t.Optional[str] = None,
        fill: t.Optional[str] = None,
        **attrs,
    ):
        super().__init__(
            *content,
            points=points,
            stroke=stroke,
            stroke_width=stroke_width,
            fill=fill,
            **attrs,
        )


class Defs(BaseElement):
    tag = "defs"


class LinearGradient(BaseElement):
    tag = "linearGradient"


class Stop(BaseElement):
    tag = "stop"

    def __init__(self, *content: t.Any, stop_color: t.Optional[str] = None, **attrs):
        super().__init__(*content, stop_color=stop_color, **attrs)


class Ellipse(BaseElement):
    tag = "ellipse"

    def __init__(
        self,
        *content: t.Any,
        cx: t.Optional[int] = None,
        cy: t.Optional[int] = None,
        r: t.Optional[int] = None,
        rx: t.Optional[int] = None,
        ry: t.Optional[int] = None,
        stroke: t.Optional[str] = None,
        stroke_width: t.Optional[str] = None,
        fill: t.Optional[str] = None,
        **attrs,
    ):
        super().__init__(
            *content,
            cx=cx,
            cy=cy,
            r=r,
            rx=rx,
            ry=ry,
            stroke=stroke,
            stroke_width=stroke_width,
            fill=fill,
            **attrs,
        )


class Text(BaseElement):
    tag = "text"

    def __init__(
        self,
        *content: t.Any,
        font_size: t.Optional[int] = None,
        font_family: t.Optional[str] = None,
        x: t.Optional[str] = None,
        y: t.Optional[str] = None,
        fill: t.Optional[str] = None,
        **attrs,
    ):
        super().__init__(
            *content,
            font_size=font_size,
            font_family=font_family,
            x=x,
            y=y,
            fill=fill,
            **attrs,
        )


class Path(BaseElement):
    tag = "path"

    def __init__(
        self,
        *content: t.Any,
        d: t.Optional[str] = None,
        fill_rule: t.Optional[str] = None,
        clip_rule: t.Optional[str] = None,
        stroke: t.Optional[str] = None,
        fill: t.Optional[str] = None,
        **attrs,
    ):
        super().__init__(
            *content,
            d=d,
            fill_rule=fill_rule,
            clip_rule=clip_rule,
            stroke=stroke,
            fill=fill,
            **attrs,
        )
