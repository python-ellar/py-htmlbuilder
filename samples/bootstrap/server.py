from ellar.app import AppFactory
from ellar.common import ModuleRouter
from ellar_cli.main import create_ellar_cli
from examples.avatar import avatar_example
from examples.breadcrumb import breadcrumb_example
from examples.buttons import button_example
from examples.card import card_examples
from examples.icons import icon_example
from examples.layout import columns_example, container_example
from starlette.responses import HTMLResponse

import py_html.el as el
from py_html.contrib.bootstrap.main import BootstrapHTML
from py_html.el.base import render_component

router = ModuleRouter("/example")


@router.get("/", response=HTMLResponse)
def template():
    content = BootstrapHTML(
        el.body(
            container_example(),
            columns_example(),
            icon_example(),
            avatar_example(),
            breadcrumb_example(),
            button_example(),
            card_examples(),
        )
    )

    return render_component(content, {})


def bootstrap_app():
    application = AppFactory.create_app(routers=[router])
    return application


cli = create_ellar_cli("server:bootstrap_app")

if __name__ == "__main__":
    cli()
