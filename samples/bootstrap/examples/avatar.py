import py_html.el as el
from py_html.contrib.bootstrap.avatar import BAvatar, BAvatarGroup
from py_html.contrib.bootstrap.icon import BIcon
from py_html.contrib.bootstrap.layout_grid_system import BContainer


def avatar_example():
    return BContainer(
        class_name="p-5 my-5 border",
        *(
            el.h1("Avatars Examples"),
            el.div(
                *(
                    lambda ctx: BAvatar(text="Foo", class_name="mx-2", size="72px"),
                    BAvatar(icon="people-fill", class_name="mx-2", size="72px"),
                    BAvatar(
                        icon="people-fill",
                        class_name="mx-2",
                        size="45px",
                        badge="100",
                        variant="primary",
                        badge_variant="dark",
                    ),
                    lambda ctx: BAvatar(
                        icon="people-fill",
                        class_name="mx-2",
                        size="45px",
                        badge=BIcon(
                            icon_name="exclamation-circle-fill", variant="warning"
                        ),
                        variant="danger",
                        badge_variant="danger",
                        badge_position="bottom-left",
                    ),
                )
            ),
            el.hr(),
            el.h1("Avatars Group Examples"),
            el.div(
                class_name="mt-2",
                *(
                    BAvatarGroup(
                        BAvatar(text="Foo", size="72px"),
                        BAvatar(icon="people-fill", size="72px"),
                        BAvatar(
                            icon="people-fill",
                            size="45px",
                            badge="100",
                            variant="primary",
                            badge_variant="dark",
                        ),
                        lambda ctx: BAvatar(
                            icon="people-fill",
                            size="45px",
                            badge=BIcon(
                                icon_name="exclamation-circle-fill",
                                variant="warning",
                            ),
                            variant="danger",
                            badge_variant="danger",
                            badge_position="bottom-right",
                        ),
                        size=f"{i + 1 * 2}rem",
                        over_lap=0.2,
                    )
                    for i in range(5)
                ),
            ),
        ),
    )
