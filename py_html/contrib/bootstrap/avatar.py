import typing as t

import py_html.el as el
from py_html.contrib.bootstrap._types import BVariants
from py_html.contrib.bootstrap.icon import BIcon
from py_html.contrib.bootstrap.util import apply_classes
from py_html.styles import StyleCSS

avatar_style = el.Style(
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
            position='absolute',
            min_height='1.5em',
            min_width='1.5em',
            padding='0.25em',
            line_height=1,
            border_radius="10em",
            font_size="70%",
            font_weight=700,
            z_index=1
        ),
        '.b-avatar-group .b-avatar-group-inner': StyleCSS(
            display="flex",
            flex_wrap="wrap"
        )
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
        badge_position: t.Literal["top-right", "top-left", "bottom-left", "bottom-right"] = "bottom-right",
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


    def render(self, ctx: t.Dict) -> str:
        slot = self.content
        if not isinstance(self.content, (list, tuple)):
            slot = [self.content]

        class_name = self.class_name + " " + apply_classes(
            bg=self.variant, rounded=self.rounded, badge=True
        )

        if self.size:
            self.style.update_style(width=self.size, height=self.size)

        element = _ElementTag(
            tag=self.tag,
            style=self.style,
            class_name=class_name,
            content=el.Fragment(
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
                BAvatarBadge(content=self.badge, variant=self.badge_variant, position=self.badge_position)
                if self.badge else el.Comment(),
                *slot,
            ),
            **self.attrs,
        )

        ctx.setdefault("root_styles", []).append(avatar_style)
        return element.render(ctx)


class _ElementTag(el.BaseHTML):
    def __init__(
        self,
        tag: str = "span",
        **attrs,
    ):
        self.tag = tag
        super().__init__(**attrs)


class BAvatarText(el.Span):
    class_name = "b-avatar-text"


class BAvatarBadge(el.Span):
    class_name = "b-avatar-badge"

    def __init__(
            self,
            variant: t.Optional[BVariants] = "secondary",
            position: t.Literal["top-right", "top-left", "bottom-left", "bottom-right"] = "bottom-right",
            class_name: t.Optional[str] = "",
            style: t.Optional[StyleCSS] = None,
            **attrs
    ):
        self.variant = variant
        self.position = position

        super().__init__(class_name=class_name, style=style, **attrs)

    def render(self, ctx: t.Dict) -> str:
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

        return super().render(ctx)


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
            **attrs
    ) -> None:
        self.tag = tag
        attrs.setdefault('role', 'group')

        super().__init__(
            content=_BAvatarGroupInner(
                content=content,
                size=size,
                over_lap=over_lap,
                rounded=rounded,
                variant=variant
            ),
            **attrs
        )


class _BAvatarGroupInner(el.Div):
    class_name = "b-avatar-group-inner"

    def __init__(
            self,
            size: t.Optional[str] = None,
            over_lap: t.Optional[float] = 0.3,
            rounded: t.Optional[t.Literal["circle", "square"]] = None,
            variant: t.Optional[BVariants] = None,
            **attrs
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

    def _set_child_props(self, ctx: t.Dict) -> str:
        content = self.content
        if callable(content):
            content = self.content(ctx)
        elif isinstance(content, el.Fragment):
            content = content.contents

        _gen = []

        for avatar in (item for item in (content if isinstance(content, (list, tuple)) else [content])):
            if callable(avatar):
                avatar = avatar(ctx)

            if isinstance(avatar, BAvatar):
                if self.size:
                    avatar.size = self.size

                    formular = f"calc((-{self.size}) * {self.overlap * 0.5})"
                    avatar.style.update_style(margin_left=formular, margin_right=formular)

                if self.rounded:
                    avatar.rounded = self.rounded

                if self.variant:
                    avatar.variant = self.variant

            _gen.append(super()._render_content(avatar, ctx))

        return " ".join(_gen)

    def render(self, ctx: t.Dict) -> str:
        self.style = StyleCSS(**(self.style or {}), **self.get_parent_style())

        attrs = self._render_attributes(ctx)
        inner_html = self._set_child_props(ctx)

        return self._tag_output(attrs, inner_html)