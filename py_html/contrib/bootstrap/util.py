import typing as t

from py_html.styles.utils import snake_to_kebab


def apply_classes(**class_name_obj: t.Any) -> str:
    class_name = " "
    for k, v in class_name_obj.items():
        if v:
            k = snake_to_kebab(k)
            if type(v) == bool and v is True:
                class_name += f"{k} "
            else:
                class_name += f"{k}-{v} "
    return class_name
