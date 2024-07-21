import typing as t

import py_html.el as el
from py_html.contrib.bootstrap._types import BVariants
from py_html.styles import StyleCSS


class BIcon(el.I):
    def __init__(
        self,
        icon_name: str,
        variant: t.Optional[BVariants] = "secondary",
        style: t.Optional[StyleCSS] = None,
        font_scale: float = 1,
        **attrs,
    ) -> None:
        style = StyleCSS(**(style or {}))
        style.update_style(font_size=f"{100*font_scale}%")

        if not icon_name.startswith("bi-"):
            icon_name = f"bi-{icon_name}"

        self._icon_name = icon_name

        attrs.update(
            class_name=f"bi {icon_name} b-icon {f'text-{variant}' if variant else ''} "
            + attrs.get("class_name", "")
        )
        super().__init__(style=style, **attrs)
