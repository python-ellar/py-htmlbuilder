import typing as t

from py_html.el.base import BaseHTML


class Form(BaseHTML):
    tag = "form"

    def __init__(
        self,
        accept_charset: t.Optional[t.Union[t.Literal["UTF-8", "ISO-8859-1"]]] = None,
        action: t.Optional[str] = None,
        autocomplete: t.Optional[t.Union[t.Literal["on", "off"]]] = None,
        enctype: t.Optional[
            t.Literal[
                "application/x-www-form-urlencoded",
                "multipart/form-data",
                "text/plain",
            ]
        ] = None,
        method: t.Optional[t.Union[t.Literal["get", "post"]]] = None,
        name: t.Optional[str] = None,
        novalidate: t.Optional[bool] = None,
        rel: t.Optional[
            t.Literal[
                "external",
                "help",
                "license",
                "next",
                "nofollow",
                "noopener",
                "noreferrer",
                "opener",
                "prev",
                "search",
            ]
        ] = None,
        target: t.Optional[
            t.Literal[
                "_blank",
                "_self",
                "_parent",
                "_top",
            ]
        ] = None,
        **attrs,
    ) -> None:
        super().__init__(
            acceptcharset=accept_charset,
            action=action,
            autocomplete=autocomplete,
            enctype=enctype,
            method=method,
            name=name,
            novalidate=novalidate,
            rel=rel,
            target=target,
            **attrs,
        )


class Input(BaseHTML):
    tag = "input"

    def __init__(
        self,
        type: t.Literal[
            "button",
            "checkbox",
            "color",
            "date",
            "datetime-local",
            "email",
            "file",
            "hidden",
            "image",
            "month",
            "number",
            "password",
            "radio",
            "range",
            "reset",
            "search",
            "submit",
            "tel",
            "text",
            "time",
            "url",
            "week",
        ] = "text",
        accept: t.Optional[
            t.Union[t.Literal["audio/*", "video/*", "image/*"], t.Any]
        ] = None,
        alt: t.Optional[str] = None,
        autocomplete: t.Optional[t.Union[t.Literal["on", "off"]]] = None,
        autofocus: t.Optional[t.Union[t.Literal["on", "off"]]] = None,
        checked: t.Optional[bool] = None,
        dirname: t.Optional[t.Any] = None,
        disabled: t.Optional[t.Literal["true"]] = None,
        form: t.Optional[t.Any] = None,
        form_action: t.Optional[str] = None,
        form_enctype: t.Optional[
            t.Literal[
                "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
            ]
        ] = None,
        form_method: t.Optional[t.Literal["get", "post"]] = None,
        form_novalidate: t.Optional[bool] = None,
        form_target: t.Optional[
            t.Literal[
                "_blank",
                "_self",
                "_parent",
                "_top",
            ]
        ] = None,
        height: t.Optional[t.Any] = None,
        list: t.Optional[t.Any] = None,
        max: t.Optional[t.Any] = None,
        maxlength: t.Optional[t.Any] = None,
        min: t.Optional[t.Any] = None,
        minlength: t.Optional[t.Any] = None,
        multiple: t.Optional[t.Any] = None,
        name: t.Optional[t.Any] = None,
        pattern: t.Optional[t.Any] = None,
        placeholder: t.Optional[t.Any] = None,
        popover_target: t.Optional[t.Any] = None,
        popover_target_action: t.Optional[t.Literal["hide", "show", "toggle"]] = None,
        readonly: t.Optional[bool] = None,
        required: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        src: t.Optional[int] = None,
        step: t.Optional[t.Union[int, t.Any]] = None,
        width: t.Optional[t.Any] = None,
        value: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            type=type,
            accept=accept,
            alt=alt,
            autocomplete=autocomplete,
            autofocus=autofocus,
            checked=checked,
            dirname=dirname,
            disabled=disabled,
            form=form,
            formaction=form_action,
            formenctype=form_enctype,
            formmethod=form_method,
            formnovalidate=form_novalidate,
            formtarget=form_target,
            height=height,
            list=list,
            name=name,
            max=max,
            maxlength=maxlength,
            min=min,
            minlength=minlength,
            multiple=multiple,
            pattern=pattern,
            placeholder=placeholder,
            popovertarget=popover_target,
            popovertargetaction=popover_target_action,
            readonly=readonly,
            required=required,
            size=size,
            src=src,
            step=step,
            width=width,
            value=value,
            **attrs,
        )


class TextArea(BaseHTML):
    tag = "textarea"

    def __init__(
        self,
        auto_focus: t.Optional[bool] = None,
        cols: t.Optional[int] = None,
        disabled: t.Optional[bool] = None,
        form: t.Optional[t.Any] = None,
        maxlength: t.Optional[int] = None,
        name: t.Optional[str] = None,
        placeholder: t.Optional[str] = None,
        readonly: t.Optional[bool] = None,
        required: t.Optional[bool] = None,
        rows: t.Optional[int] = None,
        wrap: t.Optional[t.Literal["hard", "soft"]] = None,
        **attrs,
    ) -> None:
        super().__init__(
            autofocus=auto_focus,
            cols=cols,
            disabled=disabled,
            form=form,
            maxlength=maxlength,
            name=name,
            placeholder=placeholder,
            rows=rows,
            wrap=wrap,
            readonly=readonly,
            required=required,
            **attrs,
        )


class Button(BaseHTML):
    tag = "button"

    def __init__(
        self,
        auto_focus: t.Optional[bool] = None,
        disabled: t.Optional[bool] = None,
        form: t.Optional[t.Any] = None,
        form_action: t.Optional[str] = None,
        form_enctype: t.Optional[
            t.Literal[
                "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
            ]
        ] = None,
        form_method: t.Optional[t.Literal["get", "post"]] = None,
        form_novalidate: t.Optional[bool] = None,
        form_target: t.Optional[
            t.Literal[
                "_blank",
                "_self",
                "_parent",
                "_top",
            ]
        ] = None,
        popover_target: t.Optional[t.Any] = None,
        popover_target_action: t.Optional[t.Literal["hide", "show", "toggle"]] = None,
        type: t.Literal["button", "reset", "submit"] = "button",
        name: t.Optional[str] = None,
        value: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            autofocus=auto_focus,
            name=name,
            disabled=disabled,
            form=form,
            formaction=form_action,
            formenctype=form_enctype,
            formmethod=form_method,
            formnovalidate=form_novalidate,
            formtarget=form_target,
            popovertarget=popover_target,
            popovertargetaction=popover_target_action,
            type=type,
            value=value,
            **attrs,
        )


class Select(BaseHTML):
    tag = "select"

    def __init__(
        self,
        auto_focus: t.Optional[bool] = None,
        disabled: t.Optional[bool] = None,
        form: t.Optional[t.Any] = None,
        multiple: t.Optional[bool] = None,
        required: t.Optional[bool] = None,
        name: t.Optional[str] = None,
        size: t.Optional[int] = None,
        **attrs,
    ) -> None:
        super().__init__(
            autofocus=auto_focus,
            name=name,
            disabled=disabled,
            form=form,
            multiple=multiple,
            required=required,
            size=size,
            **attrs,
        )


class OptGroup(BaseHTML):
    tag = "optgroup"

    def __init__(
        self,
        label: t.Optional[str] = None,
        disabled: t.Optional[bool] = None,
        **attrs,
    ) -> None:
        super().__init__(
            label=label,
            disabled=disabled,
            **attrs,
        )


class Option(BaseHTML):
    tag = "option"

    def __init__(
        self,
        label: t.Optional[str] = None,
        disabled: t.Optional[bool] = None,
        selected: t.Optional[bool] = None,
        value: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            label=label,
            disabled=disabled,
            selected=selected,
            value=value,
            **attrs,
        )


class Label(BaseHTML):
    tag = "label"

    def __init__(
        self,
        for_: t.Optional[str] = None,
        form: t.Optional[str] = None,
        **attrs,
    ) -> None:
        attrs.update({"for": for_, "form": form})
        super().__init__(**attrs)


class FieldSet(BaseHTML):
    tag = "fieldset"

    def __init__(
        self,
        name: t.Optional[str] = None,
        disabled: t.Optional[bool] = None,
        form: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(name=name, disabled=disabled, form=form, **attrs)


class Legend(BaseHTML):
    tag = "legend"


class DataList(BaseHTML):
    tag = "datalist"


class Output(Label):
    tag = "output"

    def __init__(
        self,
        name: t.Optional[str] = None,
        **attrs,
    ) -> None:
        super().__init__(name=name, **attrs)
