import py_html.el as el
from py_html.contrib.bootstrap.breadcrumb import BBreadcrumb, BBreadcrumbItem
from py_html.contrib.bootstrap.layout_grid_system import BContainer


def breadcrumb_example():
    return BContainer(
        el.h1("Breadcrumb Examples"),
        el.div(
            BBreadcrumb(
                items=[
                    {"text": "Home", "href": "https://google.com"},
                    {"text": "Posts", "href": "#"},
                    {"text": "Another Story", "active": True},
                ],
            ),
            el.hr(),
            BBreadcrumb(
                BBreadcrumbItem("Foo", href="#foo"),
                BBreadcrumbItem("Bar", href="#bar"),
                BBreadcrumbItem("Baz", active=True),
            ),
        ),
        class_name="p-5 my-5 border",
    )
