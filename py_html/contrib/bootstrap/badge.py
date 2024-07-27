import typing as t

import py_html.el as el
from py_html.contrib.bootstrap._types import BVariants
from py_html.contrib.bootstrap.util import apply_classes
from py_html.el.base import NodeContext


class BBadge(el.BaseHTML):
    class_name = "badge"

    def __init__(
        self,
        *content,
        tag: str = "span",
        variant: t.Optional[BVariants] = "secondary",
        pill: bool = False,
        **attrs,
    ):
        self.tag = tag
        self.variant = variant
        self.pill = pill

        super().__init__(*content, **attrs)

    def render_attributes(self, ctx: NodeContext) -> str:
        self.class_name += "" + apply_classes(bg=self.variant, badge_pill=self.pill)

        return super().render_attributes(ctx)
