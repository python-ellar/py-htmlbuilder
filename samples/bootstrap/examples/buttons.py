import py_html.el as el
from py_html.contrib.bootstrap.button import BButton, BButtonGroup
from py_html.contrib.bootstrap.layout_grid_system import BContainer


def button_example():
    return BContainer(
        *(
            el.h1("Button Example"),
            el.div(
                *(
                    (
                        BButton(i, pill=True, variant=i, class_name="mx-2")
                        for i in [
                            "primary",
                            "outline-secondary",
                            "success",
                            "outline-danger",
                            "info",
                        ]
                    ),
                    el.hr(),
                    (
                        BButton(i, squared=True, variant=i, class_name="mx-2")
                        for i in [
                            "primary",
                            "outline-secondary",
                            "success",
                            "outline-danger",
                            "info",
                        ]
                    ),
                    el.hr(),
                    (
                        BButton(i, variant=i, class_name="mx-2")
                        for i in [
                            "primary",
                            "secondary",
                            "success",
                            "danger",
                            "warning",
                            "info",
                            "light",
                            "dark",
                        ]
                    ),
                    el.hr(),
                    (
                        BButton(
                            f"outline-{i}",
                            variant=f"outline-{i}",
                            class_name="mx-2",
                        )
                        for i in [
                            "primary",
                            "secondary",
                            "success",
                            "danger",
                            "warning",
                            "info",
                            "light",
                            "dark",
                        ]
                    ),
                    el.hr(),
                    BButton("Link", variant="link", class_name="mx-2"),
                    el.hr(),
                    (
                        BButton(c, size=i, class_name="mx-2")
                        for i, c in [
                            ("sm", "Small"),
                            ("md", "Medium"),
                            ("lg", "Large"),
                        ]
                    ),
                    el.hr(),
                    BButtonGroup(
                        size="md",
                        squared=True,
                        *(
                            BButton("Button 1", variant="outline-primary"),
                            BButton("Button 2", variant="outline-primary"),
                            BButton("Button 3", variant="outline-primary"),
                        ),
                    ),
                )
            ),
        ),
        class_name="p-5 my-5 border",
    )
