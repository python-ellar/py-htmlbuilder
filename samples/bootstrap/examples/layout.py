import py_html.el as el
from py_html.contrib.bootstrap.layout_grid_system import BCol, BContainer, BRow
from py_html.styles import StyleCSS


def columns_example():
    return el.fragment(
        BContainer(
            *(
                BRow(
                    *(
                        BCol(
                            "1 of 3",
                            col=True,
                            lg=2,
                            style=StyleCSS(background_color="red"),
                        ),
                        BCol(
                            "Variable width content",
                            cols="12",
                            md="auto",
                            style=StyleCSS(background_color="yellow"),
                        ),
                        BCol(
                            "Variable width content",
                            col=True,
                            lg=2,
                            style=StyleCSS(background_color="pink"),
                        ),
                    ),
                    class_name="justify-content-md-center",
                ),
                BRow(
                    BCol("1 of 3", style=StyleCSS(background_color="orange")),
                    BCol(
                        "Variable width content",
                        cols="12",
                        md="auto",
                        style=StyleCSS(background_color="gray"),
                    ),
                    BCol(
                        "Variable width content",
                        col=True,
                        lg=2,
                        style=StyleCSS(background_color="smoke"),
                    ),
                ),
            ),
            class_name="p-5 my-5 bg-primary text-white",
        ),
    )


def container_example():
    return el.fragment(
        BContainer(
            *(
                el.h1("Container Fluid"),
                el.p("This is some text."),
            ),
            fluid=True,
        ),
        BContainer(
            *(
                el.h1("Container"),
                el.p("This is some text."),
            ),
            class_name="p-5 my-5 border",
        ),
        BContainer(
            *(
                el.h1("Container with Dark Color"),
                el.p("This is some text."),
            ),
            class_name="p-5 my-5 bg-dark text-white",
        ),
        BContainer(
            *(
                el.h1("Container with Primary Color"),
                el.p("This is some text."),
            ),
            class_name="p-5 my-5 bg-primary text-white",
        ),
    )
