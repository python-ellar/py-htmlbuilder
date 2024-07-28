import typing as t

from typing_extensions import Unpack

from .spec import CSSAttributesSpec
from .utils import snake_to_kebab


class StyleCSS(dict):
    def __init__(self, **styles: Unpack[CSSAttributesSpec]) -> None:
        super().__init__(**styles)

    def update_style(self, **styles: Unpack[CSSAttributesSpec]) -> None:
        self.update(styles)

    def render(self) -> str:
        def _gen() -> t.Generator[str, t.Any, None]:
            for prop, val in ((k, v) for k, v in self.items() if v):
                if isinstance(val, (MediaQuery, KeyFrames, FontFace)):
                    yield val.render()
                    continue

                yield f"{snake_to_kebab(prop)}: {val}"

        return "; ".join(_gen())


class MediaQuery:
    def __init__(self, conditions: t.Any, **style: StyleCSS) -> None:
        self.conditions = conditions
        self.styles = StyleCSS(**style)

    def render(self, ctx: t.Dict):
        styles = (
            f"{k} " + "{" + f"{v.render(ctx)}" + "}" for k, v in self.styles.items()
        )
        return f"@media {self.conditions}" "{" + f"{' '.join(styles)}" + "}"


class FontFace:
    def __init__(
        self,
        *,
        font_family: t.Any,
        src: t.Optional[t.Any] = None,
        font_stretch: t.Literal[
            "normal",
            "condensed",
            "ultra-condensed",
            "extra-condensed",
            "semi-condensed",
            "expanded",
            "semi-expanded",
            "extra-expanded",
            "ultra-expanded",
        ] = "normal",
        font_style: t.Literal["normal", "italic", "oblique"] = "normal",
        font_weight: t.Literal[
            "normal",
            "bold",
            "100",
            "200",
            "300",
            "400",
            "500",
            "600",
            "700",
            "800",
            "900",
        ] = "normal",
        unicore_range: t.Any = "U+0-10FFFF",
    ) -> None:
        self.style = StyleCSS(
            font_family=font_family,
            src=src,
            font_stretch=font_stretch,
            font_style=font_style,
            font_weight=font_weight,
            unicore_range=unicore_range,
        )

    def render(self):
        return "@font-face {" + f"{self.style.render()}" + "}"


class KeyFrames:
    def __init__(self, animation_name: t.Any, **keyframes: StyleCSS) -> None:
        self.animation_name = animation_name
        self.keyframes = keyframes

    def render(self):
        keyframes = (
            f"{k} " + "{" + f"{v.render()}" + "}" for k, v in self.keyframes.items()
        )
        return (
            f"@keyframes {self.animation_name}" + "{" + f"{' '.join(keyframes)}" + "}"
        )
