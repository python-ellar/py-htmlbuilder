from ellar.app import AppFactory
from ellar.common import ModuleRouter
from ellar_cli.main import create_ellar_cli
from starlette.responses import HTMLResponse

import py_html.el as el
from py_html.el.base import render_component

router = ModuleRouter("/example")


@router.get("/", response=HTMLResponse)
def template():
    content = el.html(
        el.head(
            el.title("Example HTML"),
            lambda ctx: el.link(href=ctx.get("bootstrap_css", "")),
        ),
        el.body(
            class_name="container py-4",
            *(
                el.header(
                    class_name="pb-3 mb-4 border-bottom",
                    *(
                        el.a(
                            href="/",
                            class_name="d-flex align-items-center text-dark text-decoration-none",
                        ),
                        el.span("Jumbotron example", class_name="fs-4"),
                    ),
                ),
                el.div(
                    class_name="p-5 mb-4 bg-light rounded-3",
                    *(
                        el.div(
                            class_name="container-fluid py-5",
                            *(
                                el.h1(
                                    "Custom jumbotron", class_name="display-5 fw-bold"
                                ),
                                el.p(
                                    """
                        Using a series of utilities, you can create this jumbotron, just like the one in previous versions of Bootstrap.
                         Check out the examples below for how you can remix and restyle it to your liking.
                        """,
                                    class_name="col-md-8 fs-4",
                                ),
                                el.button(
                                    "Example button",
                                    class_name="btn btn-primary btn-lg",
                                    type="button",
                                ),
                            ),
                        ),
                    ),
                ),
                el.footer("© 2024", class_name="pt-3 mt-4 text-muted border-top"),
            ),
        ),
    )

    return render_component(
        content,
        {
            "bootstrap_css": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
        },
    )


def app_bootstrap():
    application = AppFactory.create_app(routers=[router])
    return application


cli = create_ellar_cli("readme:app_bootstrap")

if __name__ == "__main__":
    cli()
