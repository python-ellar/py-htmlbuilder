import py_html.el as el
from py_html.contrib.bootstrap.icon import BIcon
from py_html.contrib.bootstrap.layout_grid_system import BContainer


def icon_example():
    return BContainer(
        *(
            el.div(
                class_name="h2 mb-0",
                *(
                    BIcon(
                        icon_name="exclamation-circle-fill",
                        class_name="mx-1",
                        variant="success",
                    ),
                    BIcon(
                        icon_name="exclamation-circle-fill",
                        class_name="mx-1",
                        variant="warning",
                    ),
                    BIcon(
                        icon_name="exclamation-circle-fill",
                        class_name="mx-1",
                        variant="info",
                    ),
                    BIcon(
                        icon_name="exclamation-circle-fill",
                        class_name="mx-1",
                        variant="danger",
                    ),
                    BIcon(
                        icon_name="exclamation-circle-fill",
                        class_name="mx-1",
                        variant="primary",
                    ),
                    BIcon(
                        icon_name="exclamation-circle-fill",
                        class_name="mx-1",
                        variant="secondary",
                    ),
                    BIcon(
                        icon_name="exclamation-circle",
                        class_name="mx-1 bg-info",
                        variant="dark",
                    ),
                    BIcon(
                        icon_name="bell-fill",
                        class_name="border rounded p-2 mx-1",
                        variant="dark",
                    ),
                ),
            ),
        ),
        class_name="p-5 my-5 border",
    )
