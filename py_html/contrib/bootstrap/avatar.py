import typing as t

import py_html.el as el
from py_html.contrib.bootstrap._types import BVariants
from py_html.contrib.bootstrap.icon import BIcon
from py_html.contrib.bootstrap.util import apply_classes
from py_html.el import Fragment
from py_html.el.base import NodeContext
from py_html.styles import StyleCSS

avatar_style = el.Style(
    {
        ".b-avatar-testing": StyleCSS(
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
    }
)


class BAvatar(el.BaseElement):
    class_name = "b-avatar"

    def __init__(
        self,
        tag: str = "span",
        size: t.Optional[str] = None,
        badge: t.Optional[t.Any] = None,
        variant: t.Optional[BVariants] = "secondary",
        badge_variant: t.Optional[BVariants] = "secondary",
        badge_position: t.Literal[
            "top-right", "top-left", "bottom-left", "bottom-right"
        ] = "bottom-right",
        rounded: t.Literal["circle", "square"] = "circle",
        icon: t.Optional[str] = None,
        text: t.Optional[str] = None,
        **attrs,
    ):
        self.tag = tag
        self.badge = badge
        self.variant = variant
        self.icon = icon
        self.text = text
        self.badge_position = badge_position
        self.badge_variant = badge_variant
        self.rounded = rounded
        self.size = size

        if not self.icon and not self.text:
            self.icon = "people-fill"

        super().__init__(**attrs)

    def render_content(self, content: t.Any, ctx: NodeContext) -> str:
        self.class_name = (
            self.class_name
            + " "
            + apply_classes(bg=self.variant, rounded=self.rounded, badge=True)
        )

        if self.size:
            self.style.update_style(width=self.size, height=self.size)

        element = el.Fragment(
            BAvatarText(
                content=self.text,
                style=StyleCSS(font_size=f"calc({self.size} * 0.4)")
                if self.size
                else None,
            )
            if self.text
            else None,
            el.Span(
                content=BIcon(
                    icon_name=self.icon,
                    variant=None,
                ),
                style=StyleCSS(font_size=f"calc({self.size} * 0.6)")
                if self.size
                else None,
            )
            if self.icon
            else None,
            BAvatarBadge(
                content=self.badge,
                variant=self.badge_variant,
                position=self.badge_position,
                style=StyleCSS(font_size=f"calc({self.size} * 0.28)"),
            )
            if self.badge
            else el.Comment(),
            content,
        )
        return ctx.render_content(element)


class BAvatarText(el.Span):
    class_name = "b-avatar-text"


class BAvatarBadge(el.Span):
    class_name = "b-avatar-badge"

    def __init__(
        self,
        variant: t.Optional[BVariants] = "secondary",
        position: t.Literal[
            "top-right", "top-left", "bottom-left", "bottom-right"
        ] = "bottom-right",
        class_name: t.Optional[str] = "",
        style: t.Optional[StyleCSS] = None,
        **attrs,
    ):
        self.variant = variant
        self.position = position

        super().__init__(class_name=class_name, style=style, **attrs)

    def render_attributes(self, ctx: NodeContext) -> str:
        position_style = {}

        if self.position == "bottom-right":
            position_style = StyleCSS(bottom="0px", right="0px")
        elif self.position == "bottom-left":
            position_style = StyleCSS(bottom="0px", left="0px")
        elif self.position == "top-left":
            position_style = StyleCSS(top="0px", left="0px")
        elif self.position == "top-right":
            position_style = StyleCSS(top="0px", right="0px")

        self.style = StyleCSS(**(self.style or {}), **position_style)
        self.class_name = self.class_name + apply_classes(badge=True, bg=self.variant)

        return super().render_attributes(ctx)


class BAvatarGroup(el.BaseElement):
    class_name = "b-avatar-group"

    def __init__(
        self,
        tag: str = "div",
        over_lap: t.Optional[float] = 0.3,
        size: t.Optional[str] = None,
        rounded: t.Optional[t.Literal["circle", "square"]] = None,
        variant: t.Optional[BVariants] = None,
        content: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        self.tag = tag
        attrs.setdefault("role", "group")

        super().__init__(
            content=_BAvatarGroupInner(
                content=content,
                size=size,
                over_lap=over_lap,
                rounded=rounded,
                variant=variant,
            ),
            **attrs,
        )


class _BAvatarGroupInner(el.Div):
    class_name = "b-avatar-group-inner"

    def __init__(
        self,
        size: t.Optional[str] = None,
        over_lap: t.Optional[float] = 0.3,
        rounded: t.Optional[t.Literal["circle", "square"]] = None,
        variant: t.Optional[BVariants] = None,
        **attrs,
    ) -> None:
        self.size = size
        self.rounded = rounded
        self.variant = variant
        self.overlap = 1 if abs(over_lap) > 1 else abs(over_lap)

        super().__init__(**attrs)

    def get_parent_style(self) -> StyleCSS:
        if self.size:
            formular = f"calc({self.size} * {self.overlap * 0.5})"
            return StyleCSS(padding_left=formular, padding_right=formular)
        return StyleCSS()

    def render_content(self, content: Fragment, ctx: NodeContext) -> str:
        for node in content or []:
            if isinstance(node.element, BAvatar):
                if self.size:
                    node.element.size = self.size

                    formular = f"calc((-{self.size}) * {self.overlap * 0.5})"
                    node.element.style.update_style(
                        margin_left=formular, margin_right=formular
                    )

                if self.rounded:
                    node.element.rounded = self.rounded

                if self.variant:
                    node.element.variant = self.variant

        return ctx.render_content(content)

    def render_attributes(self, ctx: NodeContext) -> str:
        self.style = StyleCSS(**(self.style or {}), **self.get_parent_style())
        return super().render_attributes(ctx)
