import typing as t

import py_html.el as el
from py_html.contrib.bootstrap._types import BTextVariant, BVariants
from py_html.contrib.bootstrap.util import apply_classes
from py_html.el.base import NodeContext


class BCard(el.BaseHTML):
    class_name = "card"

    def __init__(
        self,
        *content: t.Any,
        tag: str = "div",
        align: t.Literal["left", "center", "right"] = "left",
        text_variant: t.Optional[BTextVariant] = None,
        bg: t.Optional[BVariants] = None,
        overlay: bool = False,
        title: t.Optional[t.Union[str, "BCardTitle"]] = None,
        subtitle: t.Optional[t.Union[str, "BCardSubTitle"]] = None,
        header: t.Optional[t.Union[str, "BCardHeader"]] = None,
        footer: t.Optional[t.Union[str, "BCardFooter"]] = None,
        img: t.Optional[t.Union[str, "BCardImg"]] = None,
        **attrs,
    ) -> None:
        self.tag = tag
        self.align = align
        self.text_variant = text_variant
        self.overlay = overlay

        self.bg = bg

        self.class_name += apply_classes(text=self.text_variant, bg=self.bg)
        self.class_name += apply_classes(text=self.align)

        self.card_title = title
        self.subtitle = subtitle

        self.header = header
        self.footer = footer

        self.img = img

        super().__init__(*content, *attrs)

    def render_content(
        self, children: t.Optional[t.List[NodeContext]], parent: NodeContext
    ) -> t.Any:
        header_content = list(
            filter(lambda node: type(node.element) is BCardHeader, children or [])
        )
        footer_content = list(
            filter(lambda node: type(node.element) is BCardFooter, children or [])
        )
        body_content = list(
            filter(lambda node: type(node.element) is BCardBody, children or [])
        )

        if not header_content and self.header:
            header_content = self.header
            if isinstance(self.header, str):
                header_content = BCardHeader(self.header)

        if not footer_content and self.footer:
            footer_content = self.footer
            if isinstance(self.footer, str):
                footer_content = BCardFooter(self.footer)

        img_content = ()
        if self.img:
            img_content = self.img
            if isinstance(self.img, str):
                img_content = BCardImg(src=self.img)

        if body_content:
            if self.overlay:
                body_content = BCardImgOverlay(body_content)
            arranged_content = el.fragment(
                header_content,  #
                img_content,
                body_content,
                footer_content,
            )
        else:
            other_contents = list(
                filter(
                    lambda node: node
                    not in (header_content + footer_content + body_content),
                    children or [],
                )
            )
            body_content = BCardBody(
                title=self.card_title,
                subtitle=self.subtitle,
                *other_contents,
            )
            if self.overlay:
                body_content = BCardImgOverlay(body_content)

            arranged_content = el.fragment(
                header_content, img_content, body_content, footer_content
            )

        return parent.render_content(arranged_content)


class BCardHeader(el.BaseHTML):
    class_name = "card-header"

    def __init__(
        self,
        *content,
        tag: str = "div",
        text_variant: t.Optional[BTextVariant] = None,
        bg: t.Optional[BVariants] = None,
        border_variant: t.Optional[BVariants] = None,
        **attrs,
    ) -> None:
        self.tag = tag
        self.text_variant = text_variant
        self.border_variant = border_variant
        self.bg = bg

        self.class_name += apply_classes(text=self.text_variant, bg=self.bg)
        if self.border_variant:
            self.class_name += apply_classes(border=True)
            self.class_name += apply_classes(border=self.border_variant)

        super().__init__(*content, **attrs)


class BCardImgOverlay(el.div):
    class_name = "card-img-overlay"


class BCardImg(el.img):
    class_name = ""

    def __init__(
        self,
        position: t.Optional[t.Literal["top", "bottom", "left", "right"]] = None,
        **attrs,
    ) -> None:
        self.class_name += apply_classes(card_img=True if not position else position)
        attrs.setdefault("alt", "image")
        super().__init__(**attrs)


class BCardFooter(BCardHeader):
    class_name = "card-footer"


class BCardBody(el.div):
    class_name = "card-body"

    def __init__(
        self,
        *content,
        title: t.Optional[t.Union[str, "BCardTitle"]] = None,
        subtitle: t.Optional[t.Union[str, "BCardSubTitle"]] = None,
        **attrs,
    ) -> None:
        self.card_title = title
        self.subtitle = subtitle

        super().__init__(*content, **attrs)

    def render_content(
        self, children: t.Optional[t.List[NodeContext]], parent: NodeContext
    ) -> str:
        title_content = list(
            filter(lambda node: type(node.element) is BCardTitle, children or [])
        )
        subtitle_content = list(
            filter(lambda node: type(node.element) is BCardSubTitle, children or [])
        )

        if title_content or subtitle_content:
            return parent.render_content(children)

        title_content = self.card_title
        if isinstance(self.card_title, str):
            title_content = BCardTitle(self.card_title)

        subtitle_content = self.subtitle
        if isinstance(self.subtitle, str):
            subtitle_content = BCardSubTitle(self.subtitle)

        elm = el.fragment(title_content, subtitle_content, children)
        return parent.render_content(elm)


class BCardTitle(el.BaseHTML):
    class_name = "card-title"

    def __init__(self, *content, tag: str = "h4", **attrs) -> None:
        self.tag = tag
        super().__init__(*content, **attrs)


class BCardSubTitle(el.BaseHTML):
    class_name = "card-subtitle"

    def __init__(
        self, *content, tag: str = "h6", text_variant: BTextVariant = "muted", **attrs
    ) -> None:
        self.tag = tag
        self.text_variant = text_variant

        self.class_name += apply_classes(text=self.text_variant, mb=2)
        super().__init__(*content, **attrs)


class BCardText(el.BaseHTML):
    class_name = "card-text"

    def __init__(self, *content, tag: str = "p", **attrs) -> None:
        self.tag = tag
        super().__init__(*content, **attrs)


class BCardGroup(el.BaseHTML):
    class_name = "card-group"

    def __init__(self, *content, tag: str = "div", **attrs) -> None:
        self.tag = tag
        super().__init__(*content, **attrs)
