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


class BBreadcrumb(el.ol):
    class_name = "breadcrumb"

    def __init__(
        self, *content: t.Any, items: t.Optional[t.List[BreadcrumbItem]] = None, **attrs
    ) -> None:
        super().__init__(*content, **attrs)
        self.items = items
        if self.items and self.content:
            raise Exception("Invalid Configuration. Use 'Items' or 'Content'")

    def render_content(
        self, children: t.Optional[t.List[NodeContext]], parent: NodeContext
    ) -> str:
        if self.items:
            return parent.render_content(self._get_breadcrumb_item_elements())
        return parent.render_content(children)

    def _get_breadcrumb_item_elements(self) -> el.fragment:
        assert self.items
        return el.fragment(
            *(
                BBreadcrumbItem(
                    item["text"],
                    href=item.get("href", "#"),
                    active=item.get("active", False),
                    target=item.get("target", "_self"),
                )
                for item in self.items
            )
        )


class BBreadcrumbItem(el.li):
    class_name = "breadcrumb-item"

    def __init__(
        self,
        *content: t.Any,
        target: aTarget = "_self",
        active: bool = False,
        href: str = "#",
        **attrs,
    ) -> None:
        attrs.setdefault("aria_current", "location")
        super().__init__(*content, **attrs)

        self.href = href
        self.target = target
        self.active = active

        self.class_name += apply_classes(active=active)

    def render_content(
        self, children: t.Optional[t.List[NodeContext]], parent: NodeContext
    ) -> str:
        if self.active:
            return parent.render_content(el.span(children))

        return parent.render_content(el.a(children, href=self.href, target=self.target))
