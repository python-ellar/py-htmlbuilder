import typing as t

import py_html.el as el
from py_html.contrib.bootstrap.util import apply_classes
from py_html.el.base import NodeContext

aTarget = t.Literal[
    "_blank",
    "_self",
    "_parent",
    "_top",
]


class BreadcrumbItem(t.TypedDict, total=False):
    text: str
    href: t.Optional[str]
    active: bool
    target: aTarget


class BBreadcrumb(el.Ol):
    class_name = "breadcrumb"

    def __init__(self, *items: BreadcrumbItem, **attrs) -> None:
        super().__init__(**attrs)
        self.items = items
        if self.items and self.content:
            raise Exception("Invalid Configuration. Use 'Items' or 'Content'")

    def render_content(self, content: t.Any, ctx: NodeContext) -> t.Any:
        if self.items:
            return ctx.render_content(self._get_breadcrumb_item_elements())
        return ctx.render_content(content)

    def _get_breadcrumb_item_elements(self) -> el.Fragment:
        return el.Fragment(
            *(
                BBreadcrumbItem(
                    href=item.get("href", "#"),
                    active=item.get("active", False),
                    target=item.get("target", "_self"),
                    content=item["text"],
                )
                for item in self.items
            )
        )


class BBreadcrumbItem(el.Li):
    class_name = "breadcrumb-item"

    def __init__(
        self, target: aTarget = "_self", active: bool = False, href: str = "#", **attrs
    ) -> None:
        attrs.setdefault("aria_current", "location")
        super().__init__(**attrs)

        self.href = href
        self.target = target
        self.active = active

        self.class_name += apply_classes(active=active)

    def render_content(self, content: t.Any, ctx: NodeContext) -> t.Any:
        if self.active:
            return ctx.render_content(el.Span(content=content))

        return ctx.render_content(
            el.A(href=self.href, content=content, target=self.target)
        )
