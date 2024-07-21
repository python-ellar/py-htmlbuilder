from py_html.el.base import render_component
from starlette.responses import HTMLResponse

from ellar.common.responses.models import HTMLResponseModel

from ellar.common import ModuleRouter

from ellar.app import AppFactory
from ellar_cli.main import create_ellar_cli

from py_html.contrib.bootstrap.icon import BIcon

from py_html.contrib.bootstrap.avatar import BAvatar, BAvatarGroup

from py_html.contrib.bootstrap.layout_grid_system import BContainer, BRow, BCol

from py_html.styles import StyleCSS
import py_html.el as el

router = ModuleRouter("/example")

@router.get("/", response=HTMLResponse)
def template():
    content = el.Html(
        content=(
            el.Head(
                content=lambda ctx: el.Fragment(
                    el.Title(page_title="Bootstrap Example"),
                    el.Meta(charset="utf-8"),
                    el.Meta(name="viewport", content="width=device-width, initial-scale=1"),
                    # Latest compiled and minified CSS
                    el.Link(
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
                        rel="stylesheet"
                    ),
                    el.Link(
                        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
                        rel="stylesheet"
                    ),
                    # Latest compiled JavaScript
                    el.Script(
                        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
                    ),
                    *(ctx.get('root_styles', []))
                )
            ),
            el.Body(
                content=lambda ctx: el.Fragment(
                    """
                    <div class="container-fluid">
                      <h1>My First Bootstrap Page</h1>
                      <p>This is some text.</p>
                    </div>
                    """,
                    BContainer(
                        fluid=True,
                        content=(
                            el.H1(content="My First Bootstrap Page"),
                            el.P(content="This is some text."),
                        )
                    ),
                    BContainer(
                        class_name="p-5 my-5 border",
                        content=(
                            el.H1(content="My First Bootstrap Page"),
                            el.P(content="This is some text."),
                        )
                    ),
                    BContainer(
                        class_name="p-5 my-5 bg-dark text-white",
                        content=(
                            el.H1(content="My First Bootstrap Page"),
                            el.P(content="This is some text."),
                        )
                    ),
                    BContainer(
                        class_name="p-5 my-5 bg-primary text-white",
                        content=(
                            el.H1(content="My First Bootstrap Page"),
                            el.P(content="This is some text.")
                        )
                    ),
                    BContainer(
                        class_name=f"p-5 my-5 border",
                        content=(
                            el.H1(content="Avatars Examples"),
                            el.Div(class_name="mt-2", content=(
                                BAvatar(text="Foo", class_name="mx-2", size="72px"),
                                BAvatar(icon="people-fill", class_name="mx-2", size="72px"),
                                BAvatar(
                                    icon="people-fill",
                                    class_name="mx-2",
                                    size="45px",
                                    badge='100',
                                    variant="primary",
                                    badge_variant="dark"
                                ),
                                BAvatar(
                                    icon="people-fill",
                                    class_name="mx-2",
                                    size="45px",
                                    badge=BIcon(icon_name="exclamation-circle-fill",variant="warning"),
                                    variant="danger",
                                    badge_variant="danger",
                                    badge_position="bottom-left"
                                ),
                            )),
                            el.Hr(),
                            el.H1(content="Avatars Group Examples"),
                            el.Div(class_name="mt-2", content=(
                                BAvatarGroup(
                                    size="4rem",
                                    over_lap=0.2,
                                    content=(
                                        BAvatar(text="Foo", size="72px"),
                                        BAvatar(icon="people-fill", size="72px"),
                                        BAvatar(
                                            icon="people-fill",
                                            size="45px",
                                            badge='100',
                                            variant="primary",
                                            badge_variant="dark"
                                        ),
                                        BAvatar(
                                            icon="people-fill",
                                            size="45px",
                                            badge=BIcon(icon_name="exclamation-circle-fill", variant="warning"),
                                            variant="danger",
                                            badge_variant="danger",
                                            badge_position="bottom-left"
                                        ),
                                    )
                                )
                            )),

                        )
                    ),
                    BContainer(
                        class_name="p-5 my-5 border",
                        content=el.Div(
                            class_name="h2 mb-0",
                            content=(
                                BIcon(icon_name="exclamation-circle-fill",  class_name="mx-1", variant="success"),
                                BIcon(icon_name="exclamation-circle-fill", class_name="mx-1",variant="warning"),
                                BIcon(icon_name="exclamation-circle-fill", class_name="mx-1",variant="info"),
                                BIcon(icon_name="exclamation-circle-fill", class_name="mx-1",variant="danger"),
                                BIcon(icon_name="exclamation-circle-fill", class_name="mx-1",variant="primary"),
                                BIcon(icon_name="exclamation-circle-fill", class_name="mx-1",variant="secondary"),
                                BIcon(icon_name="exclamation-circle", class_name="mx-1 bg-info",variant="dark",),
                                BIcon(icon_name="bell-fill", class_name="border rounded p-2 mx-1", variant="dark"),
                            )
                        )
                    ),
                    el.Fragment(ctx.get('root_styles', [])),
                    BContainer(
                        class_name="p-5 my-5 bg-primary text-white",
                        content=el.Fragment(
                            BRow(
                                class_name="justify-content-md-center",
                                content=[
                                    BCol(col=True, lg=2, content="1 of 3", style=StyleCSS(background_color="red")),
                                    BCol(cols="12", md="auto", content="Variable width content",
                                         style=StyleCSS(background_color="yellow")),
                                    BCol(col=True, lg=2, content="Variable width content",
                                         style=StyleCSS(background_color="pink")),
                                ]
                            ),
                            BRow(
                                content=[
                                    BCol(content="1 of 3", style=StyleCSS(background_color="orange")),
                                    BCol(cols="12", md="auto", content="Variable width content",
                                         style=StyleCSS(background_color="gray")),
                                    BCol(col=True, lg=2, content="Variable width content",
                                         style=StyleCSS(background_color="smoke")),
                                ]
                            )
                        )
                    ),
                )
            )
        )
    )

    return render_component(content, {})

def bootstrap():
    application = AppFactory.create_app(routers=[router])
    return application


cli = create_ellar_cli("bootstrap_exercise:bootstrap")


if __name__ == "__main__":
    cli()