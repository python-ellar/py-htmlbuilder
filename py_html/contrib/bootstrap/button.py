import typing as t

import py_html.el as el
from py_html.contrib.bootstrap.util import apply_classes
from py_html.el.base import NodeContext

button_variant = t.Literal[
    "link",
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
    "outline-primary",
    "outline-secondary",
    "outline-success",
    "outline-danger",
    "outline-warning",
    "outline-info",
    "outline-light",
    "outline-dark",
]


class BButton(el.BaseHTML):
    class_name = "btn"

    def __init__(
        self,
        *content: t.Any,
        tag: str = "button",
        disabled: bool = False,
        pill: bool = False,
        squared: bool = False,
        pressed: bool = False,
        size: t.Literal["sm", "md", "lg"] = "sm",
        type: t.Literal["button", "submit", "reset"] = "button",
        variant: button_variant = "primary",
        href: t.Optional[str] = None,
        **attrs,
    ) -> None:
        self.tag = tag
        self.href = href
        self.pill = pill
        self.squared = squared
        self.size = size
        self.variant = variant
        self.type = type
        self.disabled = disabled
        self.pressed = pressed

        super().__init__(*content, **attrs)

    def render_attributes(self, ctx: NodeContext) -> str:
        self.class_name += apply_classes(
            pill=self.pill,
            rounded="0" if self.squared else None,
            btn=self.variant,
            disabled=self.disabled,
            active=self.pressed,
        )
        self.class_name += apply_classes(
            btn=self.size,
        )
        if self.pressed:
            self.attrs.setdefault("aria_pressed", self.pressed)

        self.attrs.update(disabled=self.disabled, type=self.type)
        return super().render_attributes(ctx)


class BButtonGroup(el.BaseHTML):
    class_name = "btn-group"

    def __init__(
        self,
        *content: t.Any,
        tag: str = "div",
        squared: bool = False,
        size: t.Literal["sm", "md", "lg"] = "sm",
        vertical: bool = False,
        **attrs,
    ) -> None:
        attrs.setdefault("role", "group")

        self.tag = tag
        self.vertical = vertical
        self.size = size
        self.squared = squared

        super().__init__(*content, **attrs)

        if self.vertical:
            self.class_name.replace(self.__class__.class_name, "btn-group-vertical")

    def render_content(
        self, children: t.Optional[t.List[NodeContext]], parent: NodeContext
    ) -> str:
        for node in children or []:
            if isinstance(node.element, BButton):
                if self.size:
                    node.element.size = self.size

                if self.squared:
                    node.element.squared = self.squared

        return parent.render_content(children)


class BButtonToolbar(el.BaseHTML):
    class_name = "btn-toolbar"
    role = "toolbar"

    def __init__(self, *content: t.Any, tag: str = "div", **attrs) -> None:
        self.tag = tag
        super().__init__(*content, **attrs)
