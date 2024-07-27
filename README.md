# py-HTML
Building Static HTML and CSS in Python

## Introduction
PyHTML is a library that compiles HTML syntax based on how py-HTML elements are combined. The compiled HTML is still static not JS interactions or Virtual DOM thingy.
It simply provides components that make it easier to build the HTML template faster. 

Although there are Jinja and Mako in this space, I don't intend to make this library a substitute for such a package.

**This is just an experiment.**

## Quick Bootstrap Example

```python
from py_html.el.base import render_component
import py_html.el as el

from starlette.responses import HTMLResponse

from ellar.common import ModuleRouter

from ellar.app import AppFactory
from ellar_cli.main import create_ellar_cli


router = ModuleRouter("/example")


@router.get("/", response=HTMLResponse)
def template():
    content = el.html(
        el.head(
            el.title("Example HTML"),
            lambda ctx: el.link(href=ctx.get("bootstrap_css", ""))
        ),
        el.body(class_name="container py-4", *(
            el.header(
                class_name="pb-3 mb-4 border-bottom",
                *(
                    el.a(href="/", class_name="d-flex align-items-center text-dark text-decoration-none"),
                    el.span("Jumbotron example", class_name="fs-4")
                )
            ),
            el.div(class_name="p-5 mb-4 bg-light rounded-3", *(
                el.div(class_name="container-fluid py-5", *(
                    el.h1("Custom jumbotron", class_name="display-5 fw-bold"),
                    el.p("""
                        Using a series of utilities, you can create this jumbotron, just like the one in previous versions of Bootstrap.
                         Check out the examples below for how you can remix and restyle it to your liking.
                        """, class_name="col-md-8 fs-4"
                    ),
                    el.button("Example button", class_name="btn btn-primary btn-lg", type="button")
                )),
            )),
            el.footer("© 2024", class_name="pt-3 mt-4 text-muted border-top")
        ))
    )

    return render_component(content, {
        "bootstrap_css":  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    })


def app_bootstrap():
    application = AppFactory.create_app(routers=[router])
    return application


cli = create_ellar_cli("readme:app_bootstrap")

if __name__ == "__main__":
    cli()
```
Start up command
```shell
python readme.py runserver --reload
```

Visit [http://127.0.0.1:8000/example/](http://127.0.0.1:8000/example/)

![Swagger UI](docs/images/readme.png)
