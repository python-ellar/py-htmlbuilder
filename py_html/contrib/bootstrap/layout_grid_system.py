import typing as t

import py_html.el as el
from py_html.contrib.bootstrap.util import apply_classes


class BContainer(el.BaseHTML):
    class_name = "container"

    def __init__(self, tag: str = "div", fluid: bool = False, **attrs):
        self.tag = tag
        self.class_name = "container-fluid" if fluid else "container"

        super().__init__(**attrs)


class BRow(el.BaseHTML):
    class_name = "row"

    def __init__(
        self,
        tag: str = "div",
        justify_content: t.Optional[
            t.Literal["start", "center", "end", "around", "between"]
        ] = None,
        align_items: t.Optional[
            t.Literal["start", "center", "end", "baseline", "stretch"]
        ] = None,
        cols: t.Optional[t.Union[str, int]] = None,
        cols_lg: t.Optional[t.Union[str, int]] = None,
        cols_md: t.Optional[t.Union[str, int]] = None,
        cols_sm: t.Optional[t.Union[str, int]] = None,
        cols_xl: t.Optional[t.Union[str, int]] = None,
        g: t.Optional[t.Union[str, int]] = None,
        g_lg: t.Optional[t.Union[str, int]] = None,
        g_md: t.Optional[t.Union[str, int]] = None,
        g_sm: t.Optional[t.Union[str, int]] = None,
        g_xl: t.Optional[t.Union[str, int]] = None,
        **attrs,
    ):
        self.tag = tag
        super().__init__(**attrs)

        self.class_name += apply_classes(
            justify_content=justify_content,
            align_items=align_items,
            row_cols=cols,
            row_cols_lg=cols_lg,
            row_cols_md=cols_md,
            row_cols_sm=cols_sm,
            row_cols_xl=cols_xl,
            g=g,
            g_lg=g_lg,
            g_md=g_md,
            g_sm=g_sm,
            g_xl=g_xl,
        )


class BCol(el.BaseHTML):
    def __init__(
        self,
        tag: str = "div",
        cols: t.Optional[t.Union[str, int]] = None,
        col: bool = False,
        sm: t.Optional[t.Union[str, int]] = None,
        md: t.Optional[t.Union[str, int]] = None,
        lg: t.Optional[t.Union[str, int]] = None,
        xl: t.Optional[t.Union[str, int]] = None,
        xxl: t.Optional[t.Union[str, int]] = None,
        offset: t.Optional[t.Union[str, int]] = None,
        offset_lg: t.Optional[t.Union[str, int]] = None,
        offset_md: t.Optional[t.Union[str, int]] = None,
        offset_sm: t.Optional[t.Union[str, int]] = None,
        offset_xl: t.Optional[t.Union[str, int]] = None,
        order: t.Optional[t.Union[str, int]] = None,
        order_lg: t.Optional[t.Union[str, int]] = None,
        order_md: t.Optional[t.Union[str, int]] = None,
        order_sm: t.Optional[t.Union[str, int]] = None,
        order_xl: t.Optional[t.Union[str, int]] = None,
        align_self: t.Optional[
            t.Literal["start", "center", "end", "baseline", "stretch"]
        ] = None,
        **attrs,
    ):
        self.tag = tag
        super().__init__(**attrs)

        self.class_name = self.class_name or "" + apply_classes(
            col=cols if cols else col or True,
            col_sm=sm,
            col_md=md,
            col_xxl=xxl,
            col_xl=xl,
            col_lg=lg,
            offset=offset,
            offset_sm=offset_sm,
            offset_lg=offset_lg,
            offset_md=offset_md,
            offset_xl=offset_xl,
            align_self=align_self,
            order=order,
            order_lg=order_lg,
            order_md=order_md,
            order_sm=order_sm,
            order_xl=order_xl,
        )
