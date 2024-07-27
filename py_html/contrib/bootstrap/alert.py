import py_html.el as el

from ._types import BVariants


class BAlert(el.BaseHTML):
    class_name = "alert"

    def __init__(
        self,
        *content,
        tag: str = "div",
        alert: BVariants = "primary",
        **attrs,
    ):
        attrs.setdefault("role", "alert")

        self.tag = tag
        self.class_name = f"alert alert-{alert}"

        super().__init__(*content, **attrs)


class BAlertLink(el.BaseHTML):
    class_name = "alert-link"

    def __init__(
        self,
        *content,
        tag: str = "a",
        **attrs,
    ):
        self.tag = tag
        super().__init__(*content, **attrs)
