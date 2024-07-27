import py_html.el as el
from py_html.contrib.bootstrap.button import BButton
from py_html.contrib.bootstrap.card import (
    BCard,
    BCardFooter,
    BCardGroup,
    BCardHeader,
    BCardImg,
    BCardText,
)
from py_html.contrib.bootstrap.layout_grid_system import BContainer


def _card_with_overlay():
    return (
        el.h3("Card Over example"),
        el.hr(),
        BCard(
            *(
                BCardText(
                    "Some quick example text to build on the card and make up the bulk of the card's content."
                ),
            ),
            overlay=True,
            img=BCardImg(
                src="https://picsum.photos/900/250/?image=3", alt="Card Image"
            ),
            text_variant="white",
            title="Image Overlay",
            subtitle="Subtitle",
        ),
    )


def _card_header_footer():
    return (
        el.h3("Card Header and footer", class_name="mt-3"),
        el.hr(),
        BCardGroup(
            *(
                BCard(
                    *(
                        BCardText("Header and footers using props"),
                        BButton("Go somewhere", variant="primary"),
                    ),
                    header="featured",
                    footer="Card Footer",
                    title="Title",
                ),
                BCard(
                    title="Title",
                    *(
                        BCardHeader(
                            tag="header", *(el.h6("Header Slot", class_name="mb-0"),)
                        ),
                        BCardText("Header and footers using props"),
                        BButton("Go somewhere", variant="primary"),
                        BCardFooter(tag="footer", *(el.em("Footer Slot"),)),
                    ),
                ),
            )
        ),
    )


def card_examples():
    return BContainer(*_card_with_overlay(), *_card_header_footer())
