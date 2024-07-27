import typing as t

import py_html.el as el
from py_html.el.base import LazyComponent
from py_html.styles import StyleCSS

BOOTSTRAP_CSS = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
)
BOOTSTRAP_ICON = (
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
)
BOOTSTRAP_JS = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
)

_avatar_style = el.style(
    {
        ".b-avatar": StyleCSS(
            display="inline-flex",
            align_items="center",
            justify_content="center",
            vertical_align="middle",
            width="2.5rem",
            height="2.5rem",
            font_size="inherit",
            font_weight="400",
            max_width="100%",
            text_align="center",
            overflow="visible",
            position="relative",
            line_height=1,
            transition="color .15s ease-in-out background-color .15s ease-in-out, box-shadow .15s ease-in-out",
        ),
        ".b-avatar .b-avatar-text": StyleCSS(
            text_transform="uppercase", white_space="nowrap"
        ),
        ".b-avatar > .b-icon": StyleCSS(width="60%", height="auto", max_width="100%"),
        ".b-icon.bi": StyleCSS(
            display="inline-block", overflow="visible", vertical_align="-.15em"
        ),
        ".b-avatar .b-avatar-badge ": StyleCSS(
            position="absolute",
            min_height="1.5em",
            min_width="1.5em",
            padding="0.25em",
            line_height=1,
            border_radius="10em",
            font_size="70%",
            font_weight=700,
            z_index=1,
        ),
        ".b-avatar-group .b-avatar-group-inner": StyleCSS(
            display="flex", flex_wrap="wrap"
        ),
    }
)


class BootstrapHTML(el.html):
    def __init__(
        self,
        *content: t.Any,
        title: str = "Bootstrap Example",
        head_contents: t.Sequence[t.Union[str, el.Element]] = (),
        bootstrap_css_link: str = BOOTSTRAP_CSS,
        bootstrap_icon_link: str = BOOTSTRAP_ICON,
        bootstrap_js_link: str = BOOTSTRAP_JS,
        **attrs,
    ) -> None:
        page_content = el.fragment(
            el.head(
                el.fragment(
                    el.title(page_title=title),
                    el.meta(charset="utf-8"),
                    el.meta(
                        name="viewport",
                        content="width=device-width, initial-scale=1",
                    ),
                    # Latest compiled and minified CSS
                    el.link(href=bootstrap_css_link, rel="stylesheet"),
                    el.link(href=bootstrap_icon_link, rel="stylesheet"),
                    # Latest compiled JavaScript
                    el.script(src=bootstrap_js_link),
                    _avatar_style,
                    head_contents,
                    lambda ctx: LazyComponent(resolver=lambda: ctx.get("root_styles")),
                )
            ),
            *content,
            lambda ctx: LazyComponent(resolver=lambda: ctx.get("bottom_scripts")),
        )
        super().__init__(page_content, **attrs)
