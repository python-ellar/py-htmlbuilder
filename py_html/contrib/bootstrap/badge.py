from py_html.contrib.bootstrap.util import apply_classes

from py_html.contrib.bootstrap._types import BVariants
import py_html.el as el
import typing as t


class BBadge(el.BaseHTML):
    class_name = "badge"

    def __init__(
            self,
            tag: str = 'span',
            variant: t.Optional[BVariants] = "secondary",
            pill: bool = False,
            class_name: t.Optional[str] = "",
            **attrs
    ):
        self.tag = tag
        self.variant = variant

        class_name = class_name or "" + apply_classes(bg=variant, badge_pill=pill)
        super().__init__(class_name=class_name, **attrs)