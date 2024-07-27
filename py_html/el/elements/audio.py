import typing as t

from py_html.el.base import BaseHTML


class Audio(BaseHTML):
    tag = "audio"

    def __init__(
        self,
        *content,
        auto_play: t.Optional[bool] = None,
        controls: t.Optional[bool] = None,
        loop: t.Optional[bool] = None,
        muted: t.Optional[bool] = None,
        preload: t.Optional[t.Literal["auto", "metadata", "none"]] = None,
        src: t.Optional[str] = None,
        **attrs,
    ) -> None:
        super().__init__(
            *content,
            autoplay=auto_play,
            controls=controls,
            loop=loop,
            muted=muted,
            preload=preload,
            src=src,
            **attrs,
        )


class Source(BaseHTML):
    tag = "source"

    def __init__(
        self,
        *content,
        media: t.Optional[t.Any] = None,
        sizes: t.Optional[t.Any] = None,
        type: t.Optional[
            t.Union[
                t.Any,
                t.Literal[
                    "video/ogg", "video/mp4", "video/webm", "audio/ogg", "audio/mpeg"
                ],
            ]
        ] = None,
        src: t.Optional[str] = None,
        src_set: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            *content,
            media=media,
            sizes=sizes,
            type=type,
            src=src,
            srcset=src_set,
            **attrs,
        )


class Track(BaseHTML):
    tag = "track"

    def __init__(
        self,
        *content,
        default: t.Optional[bool] = None,
        kind: t.Optional[
            t.Literal[
                "captions",
                "chapters",
                "descriptions",
                "metadata",
                "subtitles",
            ]
        ] = None,
        label: t.Optional[str] = None,
        src: t.Optional[t.Any] = None,
        src_lang: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            *content,
            default=default,
            kind=kind,
            label=label,
            src=src,
            srclang=src_lang,
            **attrs,
        )


class Video(Audio):
    tag = "video"

    def __init__(
        self,
        *content,
        poster: t.Optional[str] = None,
        height: t.Optional[str] = None,
        width: t.Optional[str] = None,
        **attrs,
    ) -> None:
        super().__init__(
            *content,
            poster=poster,
            height=height,
            width=width,
            **attrs,
        )
