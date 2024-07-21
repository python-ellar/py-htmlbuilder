import typing as t

if t.TYPE_CHECKING:
    from .base import FontFace, KeyFrames, MediaQuery


class CSSAttributesSpec(t.TypedDict, total=False):
    accent_color: t.Any
    align_content: t.Literal[
        "stretch",
        "center",
        "flex-start",
        "flex-end",
        "space-between",
        "space-around",
        "space-evenly",
        "initial",
        "inherit",
    ]
    align_items: t.Literal[
        "normal",
        "stretch",
        "center",
        "flex-start",
        "flex-end",
        "start",
        "end",
        "baseline",
        "initial",
        "inherit",
    ]
    align_self: t.Literal[
        "auto",
        "stretch",
        "center",
        "flex-start",
        "flex-end",
        "baseline",
        "initial",
        "inherit",
    ]
    all: t.Literal["initial", "inherit", "unset"]
    animation: t.Optional[t.Any]
    animation_delay: t.Optional[t.Any]
    animation_direction: t.Literal[
        "normal", "reverse", "alternate", "alternate-reverse", "initial", "inherit"
    ]
    animation_duration: t.Optional[t.Any]
    animation_fill_mode: t.Literal[
        "none", "forwards", "backwards", "both", "initial", "inherit"
    ]
    animation_iteration_count: t.Union[int, t.Literal["infinite", "initial", "inherit"]]
    animation_name: t.Union[t.Any, t.Literal["initial", "inherit"]]
    animation_play_state: t.Literal["paused", "running", "initial", "inherit"]
    animation_timing_function: t.Union[
        t.Any,
        t.Literal[
            "linear",
            "ease",
            "ease-in",
            "ease-out",
            "ease-in-out",
            "step-start",
            "step-end",
            "initial",
            "inherit",
        ],
    ]
    aspect_ratio: t.Union[t.Any, t.Literal["initial", "inherit"]]
    backdrop_filter: t.Union[t.Any, t.Literal["filter", "initial", "inherit"]]
    backface_visibility: t.Union[
        t.Any, t.Literal["visible", "hidden", "initial", "inherit"]
    ]
    background: t.Optional[t.Any]
    background_attachment: t.Union[
        t.Any, t.Literal["scroll", "fixed", "local", "initial", "inherit"]
    ]
    background_blend_mode: t.Literal[
        "normal",
        "multiply",
        "screen",
        "overlay",
        "darken",
        "lighten",
        "color-dodge",
        "saturation",
        "color",
        "luminosity",
    ]
    background_clip: t.Union[
        t.Any,
        t.Literal["border-box", "padding-box", "content-box", "initial", "inherit"],
    ]
    background_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]
    background_image: t.Union[t.Any, t.Literal["url", "none", "initial", "inherit"]]
    background_origin: t.Union[
        t.Any,
        t.Literal["padding-box", "border-box", "content-box", "initial", "inherit"],
    ]

    background_position: t.Union[
        t.Any,
        t.Literal[
            "left top",
            "left center",
            "left bottom",
            "right top",
            "right center",
            "right bottom",
            "center top",
            "center center",
            "center bottom",
        ],
    ]

    background_position_x: t.Union[
        t.Any, t.Literal["left", "right", "center", "initial", "inherit"]
    ]
    background_position_y: t.Union[
        t.Any, t.Literal["top", "bottom", "center", "initial", "inherit"]
    ]
    background_repeat: t.Union[
        t.Any,
        t.Literal["repeat", "repeat-x", "repeat-y", "no-repeat", "initial", "inherit"],
    ]
    background_size: t.Union[
        t.Any, t.Literal["auto", "cover", "contain", "initial", "inherit"]
    ]

    block_size: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]

    border: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_block: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_block_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]

    border_block_end: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_block_end_color: t.Union[
        t.Any, t.Literal["transparent", "initial", "inherit"]
    ]
    border_block_end_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_block_end_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    border_block_start: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_block_start_color: t.Union[
        t.Any, t.Literal["transparent", "initial", "inherit"]
    ]
    border_block_start_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_block_start_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]
    border_block_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_block_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    border_bottom: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_bottom_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]
    border_bottom_left_radius: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_bottom_right_radius: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_bottom_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_bottom_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    border_collapse: t.Union[
        t.Any, t.Literal["separate", "collapse", "initial", "inherit"]
    ]
    border_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]
    border_end_end_radius: t.Union[t.Any, t.Literal["0", "initial", "inherit"]]
    border_end_start_radius: t.Union[t.Any, t.Literal["0", "initial", "inherit"]]

    border_image: t.Union[t.Any, t.Literal["initial", "inherit"]]

    border_image_outset: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_image_repeat: t.Union[
        t.Any, t.Literal["stretch", "repeat", "round", "space", "initial", "inherit"]
    ]
    border_image_slice: t.Union[t.Any, t.Literal["fill", "initial", "inherit"]]

    border_image_source: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    border_image_width: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]

    border_inline: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_inline_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]

    border_inline_end: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_inline_end_color: t.Union[
        t.Any, t.Literal["transparent", "initial", "inherit"]
    ]
    border_inline_end_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_inline_end_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    border_inline_start: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_inline_start_color: t.Union[
        t.Any, t.Literal["transparent", "initial", "inherit"]
    ]
    border_inline_start_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_inline_start_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]
    border_inline_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_inline_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    border_left: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_left_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]
    border_left_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_left_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    border_radius: t.Union[t.Any, t.Literal["initial", "inherit"]]

    border_right: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_right_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]
    border_right_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_right_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    border_spacing: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_start_end_radius: t.Union[t.Any, t.Literal["0", "initial", "inherit"]]
    border_start_start_radius: t.Union[t.Any, t.Literal["0", "initial", "inherit"]]
    border_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]

    border_top: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_top_color: t.Union[t.Any, t.Literal["transparent", "initial", "inherit"]]
    border_top_left_radius: t.Union[t.Any, t.Literal["initial", "inherit"]]
    border_top_right_radius: t.Union[t.Any, t.Literal["initial", "inherit"]]

    border_top_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    border_top_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]
    border_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    bottom: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]

    box_decoration_break: t.Union[
        t.Any, t.Literal["slice", "clone", "initial", "inherit", "unset"]
    ]
    box_reflect: t.Union[
        t.Any,
        t.Literal["none", "below", "above", "left", "right", "initial", "inherit"],
    ]
    box_shadow: t.Union[t.Any, t.Literal["none", "inset", "initial", "inherit"]]
    box_sizing: t.Union[
        t.Any, t.Literal["content-box", "border-box", "initial", "inherit"]
    ]

    break_after: t.Union[
        t.Any,
        t.Literal[
            "auto",
            "all",
            "always",
            "avoid",
            "avoid-column",
            "avoid-page",
            "avoid-region",
            "column",
            "left",
            "page",
            "recto",
            "region",
            "right",
            "verso",
            "initial",
            "inherit",
        ],
    ]
    break_before: t.Union[
        t.Any,
        t.Literal[
            "auto",
            "all",
            "always",
            "avoid",
            "avoid-column",
            "avoid-page",
            "avoid-region",
            "column",
            "left",
            "page",
            "recto",
            "region",
            "right",
            "verso",
            "initial",
            "inherit",
        ],
    ]
    break_inside: t.Union[
        t.Any,
        t.Literal[
            "auto",
            "all",
            "always",
            "avoid",
            "avoid-column",
            "avoid-page",
            "avoid-region",
            "column",
            "left",
            "page",
            "recto",
            "region",
            "right",
            "verso",
            "initial",
            "inherit",
        ],
    ]
    caption_side: t.Union[t.Any, t.Literal["top", "bottom", "initial", "inherit"]]
    caret_color: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]

    charset: t.Optional[t.Literal["charset"]]

    clear: t.Union[
        t.Any, t.Literal["none", "left", "right", "both", "initial", "inherit"]
    ]
    clip: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    clip_path: t.Union[
        t.Any,
        t.Literal[
            "margin-box",
            "border-box",
            "padding-box",
            "content-box",
            "fill-box",
            "stroke-box",
            "view-box",
            "none",
            "initial",
            "inherit",
        ],
    ]
    color: t.Union[t.Any, t.Literal["initial", "inherit"]]
    color_scheme: t.Union[t.Any, t.Literal["normal", "light", "dark", "only"]]
    column_count: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    column_fill: t.Union[t.Any, t.Literal["balance", "auto", "initial", "inherit"]]
    column_gap: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    column_rule: t.Union[t.Any, t.Literal["initial", "inherit"]]
    column_rule_color: t.Union[t.Any, t.Literal["initial", "inherit"]]
    column_rule_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    column_rule_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]
    column_span: t.Union[t.Any, t.Literal["none", "all", "initial", "inherit"]]
    column_width: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    columns: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    content: t.Union[
        t.Any,
        t.Literal[
            "normal",
            "none",
            "counter",
            "attr",
            "string",
            "open-quote",
            "close-quote",
            "no-open-quote",
            "no-close-quote",
            "initial",
            "inherit",
        ],
    ]
    counter_increment: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    counter_reset: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    counter_set: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    cursor: t.Union[
        t.Any,
        t.Literal[
            "alias",
            "all-scroll",
            "auto",
            "cell",
            "col-resize",
            "context-menu",
            "copy",
            "crosshair",
            "default",
            "e-resize",
            "ew-resize",
            "grab",
            "grabbing",
            "help",
            "move",
            "n-resize",
            "ne-resize",
            "nesw-resize",
            "ns-resize",
            "nw-resize",
            "nwse-resize",
            "no-drop",
            "none",
            "not-allowed",
            "pointer",
            "progress",
            "row-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "text",
            "vertical-text",
            "w-resize",
            "wait",
            "zoom-in",
            "zoom-out",
            "initial",
            "inherit",
        ],
    ]
    direction: t.Union[t.Any, t.Literal["ltr", "rtl", "initial", "inherit"]]
    display: t.Union[
        t.Literal[
            "inline",
            "block",
            "contents",
            "flex",
            "grid",
            "inline-block",
            "inline-flex",
            "inline-grid",
            "inline-table",
            "list-item",
            "table-caption",
            "table-column-group",
            "table-header-group",
            "table-footer-group",
            "table-row-group",
            "table-cell",
            "table-column",
            "table-row",
            "none",
            "initial",
            "inherit",
        ],
        t.Any,
    ]
    empty_cells: t.Union[t.Any, t.Literal["show", "hide", "initial", "inherit"]]

    filter: t.Union[
        t.Any,
        t.Literal[
            "none",
            "blur()",
            " brightness()",
            "contrast() ",
            "drop-shadow()",
            "grayscale()",
            "hue-rotate()",
            "invert()",
            "opacity()",
            "saturate()",
            "sepia()",
            "url()",
        ],
    ]
    flex: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    flex_basis: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    flex_direction: t.Union[
        t.Any,
        t.Literal[
            "row", "row-reverse", "column", "column-reverse", "initial", "inherit"
        ],
    ]
    flex_flow: t.Union[t.Any, t.Literal["initial", "inherit"]]
    flex_grow: t.Union[t.Any, t.Literal["initial", "inherit"]]
    flex_shrink: t.Union[t.Any, t.Literal["initial", "inherit"]]
    flex_wrap: t.Union[
        t.Any, t.Literal["nowrap", "wrap", "wrap-reverse", "initial", "inherit"]
    ]
    float: t.Union[t.Any, t.Literal["none", "left", "right", "initial", "inherit"]]
    font: t.Any

    font_face: "FontFace"

    font_family: t.Union[t.Any, t.Literal["initial", "inherit"]]
    font_feature_settings: t.Union[t.Any, t.Literal["normal"]]
    font_kerning: t.Union[t.Any, t.Literal["auto", "normal", "none"]]
    font_size: t.Union[
        t.Any,
        t.Literal[
            "medium",
            "xx-small",
            "x-small",
            "small",
            "large",
            "x-large",
            "xx-large",
            "smaller",
            "larger",
            "initial",
            "inherit",
        ],
    ]
    font_size_adjust: t.Union[int, t.Literal["none", "initial", "inherit"]]
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
    ]
    font_style: t.Literal["normal", "italic", "oblique"]
    font_variant: t.Union[
        t.Any, t.Literal["normal", "small-caps", "initial", "inherit"]
    ]
    font_variant_caps: t.Union[
        t.Any,
        t.Literal[
            "normal",
            "small-caps",
            "all-small-caps",
            "petite-caps",
            "all-petite-caps",
            "unicase",
            "titling-caps",
            "initial",
            "inherit",
            "unset",
        ],
    ]
    font_weight: t.Literal[
        "normal", "bold", "100", "200", "300", "400", "500", "600", "700", "800", "900"
    ]

    gap: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    grid: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    grid_area: t.Any
    grid_auto_columns: t.Union[t.Any, t.Literal["auto", "max-content", "min-content"]]
    grid_auto_flow: t.Union[
        t.Any, t.Literal["row", "column", "dense", "row dense", "column dense"]
    ]
    grid_auto_rows: t.Union[t.Any, t.Literal["auto", "max-content", "min-content"]]
    grid_column: t.Any
    grid_column_end: t.Union[t.Any, t.Literal["auto", "span"]]
    grid_column_gap: t.Any
    grid_column_start: t.Union[t.Any, t.Literal["auto", "span"]]
    grid_gap: t.Any
    grid_row: t.Any
    grid_row_end: t.Union[t.Any, t.Literal["auto", "span"]]
    grid_row_gap: t.Any
    grid_row_start: t.Union[t.Any, t.Literal["auto"]]
    grid_template: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    grid_template_areas: t.Union[t.Any, t.Literal["none"]]
    grid_template_columns: t.Union[
        t.Any,
        t.Literal["none", "auto", "max-content", "min-content", "initial", "inherit"],
    ]
    grid_template_rows: t.Union[
        t.Any,
        t.Literal["none", "auto", "max-content", "min-content", "initial", "inherit"],
    ]
    hanging_punctuation: t.Union[
        t.Any,
        t.Literal[
            "none", "first", "last", "allow-end", "force-end", "initial", "inherit"
        ],
    ]
    height: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    hyphens: t.Union[t.Any, t.Literal["none", "manual", "auto", "initial", "inherit"]]
    hyphenate_character: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    image_rendering: t.Union[
        t.Any,
        t.Literal[
            "auto",
            "smooth",
            "high-quality",
            "crisp-edges",
            "pixelated",
            "initial",
            "inherit",
        ],
    ]

    import_: t.Any

    inline_size: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    inset: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    inset_block: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    inset_block_end: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    inset_block_start: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    inset_inline: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    inset_inline_end: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    inset_inline_start: t.Union[
        t.Any, t.Literal["auto", "isolate", "initial", "inherit"]
    ]

    isolation: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    justify_content: t.Union[
        t.Any,
        t.Literal[
            "flex-start",
            "flex-end",
            "center",
            "space-between",
            "space-around",
            "space-evenly",
            "initial",
            "inherit",
        ],
    ]
    justify_items: t.Union[
        t.Any,
        t.Literal[
            "legacy",
            "auto",
            "normal",
            "left",
            "right",
            "center",
            "start",
            "end",
            "stretch",
            "flex-start",
            "flex-end",
            "baseline",
            "initial",
            "inherit",
        ],
    ]
    justify_self: t.Union[
        t.Any,
        t.Literal[
            "auto",
            "normal",
            "left",
            "right",
            "center",
            "start",
            "end",
            "stretch",
            "flex-start",
            "flex-end",
            "baseline",
            "initial",
            "inherit",
        ],
    ]

    keyframes: "KeyFrames"

    left: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    letter_spacing: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    line_height: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    list_style: t.Union[t.Any, t.Literal["initial", "inherit"]]
    list_style_image: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    list_style_position: t.Union[
        t.Any, t.Literal["inside", "outside", "initial", "inherit"]
    ]
    list_style_type: t.Union[
        t.Any,
        t.Literal[
            "disc",
            "armenian",
            "circle",
            "cjk-ideographic",
            "decimal",
            "decimal-leading-zero",
            "georgian",
            "bering",
            "hebrew",
            "ring",
            "hiragana",
            "hiragana-iroha",
            "ring",
            "katakana",
            "katakana-iroha",
            "lower-alpha",
            "lower-greek",
            "lower-latin",
            "lower-roman",
            "none",
            "square",
            "upper-alpha",
            "upper-greek",
            "upper-latin",
            "upper-roman",
            "initial",
            "inherit",
        ],
    ]

    margin: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_block: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_block_end: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_block_start: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_bottom: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_inline: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_inline_end: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_inline_start: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_left: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_right: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    margin_top: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    mask_image: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    mask_mode: t.Union[
        t.Any, t.Literal["match-source", "luminance", "alpha", "initial", "inherit"]
    ]
    mask_origin: t.Union[
        t.Any,
        t.Literal[
            "border-box",
            "content-box",
            "padding-box",
            "margin-box",
            "fill-box",
            "stroke-box",
            "view-box",
            "initial",
            "inherit",
        ],
    ]
    mask_position: t.Union[
        t.Any,
        t.Literal[
            "left top",
            "left center",
            "left bottom",
            "right top",
            "right center",
            "right bottom",
            "center top",
            "center center",
            "center bottom",
        ],
    ]
    mask_repeat: t.Union[
        t.Any,
        t.Literal[
            "repeat",
            "repeat-x",
            "repeat-y",
            "space",
            "round",
            "no-repeat",
            "initial",
            "inherit",
        ],
    ]
    mask_size: t.Union[
        t.Any, t.Literal["auto", "contain", "cover", "initial", "inherit"]
    ]
    max_block_size: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    max_height: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    max_inline_size: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    max_width: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]

    media: t.Optional["MediaQuery"]

    min_block_size: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    min_inline_size: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    min_height: t.Union[t.Any, t.Literal["initial", "inherit"]]
    min_width: t.Union[t.Any, t.Literal["initial", "inherit"]]
    mix_blend_mode: t.Union[
        t.Any,
        t.Literal[
            "normal",
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "difference",
            "exclusion",
            "hue",
            "saturation",
            "color",
            "luminosity",
        ],
    ]

    object_fit: t.Union[
        t.Any,
        t.Literal[
            "fill", "contain", "cover", "scale-down", "none", "initial", "inherit"
        ],
    ]
    object_position: t.Union[t.Any, t.Literal["initial", "inherit"]]

    offset: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    offset_anchor: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    offset_distance: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    offset_path: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    offset_rotate: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]

    opacity: t.Union[t.Any, t.Literal["initial", "inherit"]]

    order: t.Union[t.Any, t.Literal["initial", "inherit"]]

    orphans: t.Union[t.Any, t.Literal["initial", "inherit"]]

    outline: t.Union[t.Any, t.Literal["initial", "inherit"]]
    outline_color: t.Union[t.Any, t.Literal["initial", "inherit"]]
    outline_offset: t.Union[t.Any, t.Literal["initial", "inherit"]]
    outline_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
        ],
    ]
    outline_width: t.Union[
        t.Any, t.Literal["medium", "thin", "thick", "initial", "inherit"]
    ]

    overflow: t.Union[
        t.Any, t.Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
    ]
    overflow_anchor: t.Union[t.Any, t.Literal["auto", "none", "initial", "inherit"]]
    overflow_wrap: t.Union[
        t.Any, t.Literal["normal", "anywhere", "break-word", "initial", "inherit"]
    ]
    overflow_x: t.Union[
        t.Any, t.Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
    ]
    overflow_y: t.Union[
        t.Any, t.Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
    ]

    overscroll_behavior: t.Union[
        t.Any, t.Literal["auto", "contain", "none", "initial", "inherit"]
    ]
    overscroll_behavior_block: t.Union[
        t.Any, t.Literal["auto", "contain", "none", "initial", "inherit"]
    ]
    overscroll_behavior_inline: t.Union[
        t.Any, t.Literal["auto", "contain", "none", "initial", "inherit"]
    ]
    overscroll_behavior_x: t.Union[
        t.Any, t.Literal["auto", "contain", "none", "initial", "inherit"]
    ]
    overscroll_behavior_y: t.Union[
        t.Any, t.Literal["auto", "contain", "none", "initial", "inherit"]
    ]

    padding: t.Union[t.Any, t.Literal["initial", "inherit"]]
    padding_block: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    padding_block_end: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    padding_block_start: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    padding_bottom: t.Union[t.Any, t.Literal["initial", "inherit"]]
    padding_inline: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    padding_inline_end: t.Union[t.Any, t.Literal["initial", "inherit"]]
    padding_inline_start: t.Union[t.Any, t.Literal["initial", "inherit"]]
    padding_left: t.Union[t.Any, t.Literal["initial", "inherit"]]
    padding_right: t.Union[t.Any, t.Literal["initial", "inherit"]]
    padding_top: t.Union[t.Any, t.Literal["initial", "inherit"]]
    page_break_after: t.Union[
        t.Any,
        t.Literal["auto", "always", "avoid", "left", "right", "initial", "inherit"],
    ]
    page_break_before: t.Union[
        t.Any,
        t.Literal["auto", "always", "avoid", "left", "right", "initial", "inherit"],
    ]
    page_break_inside: t.Union[t.Any, t.Literal["auto", "avoid", "initial", "inherit"]]
    paint_order: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    perspective: t.Union[t.Any, t.Literal["none"]]
    perspective_origin: t.Union[t.Any, t.Literal["initial", "inherit"]]
    place_content: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    place_items: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    place_self: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    pointer_events: t.Union[t.Any, t.Literal["auto", "none"]]
    position: t.Union[
        t.Literal[
            "static", "absolute", "fixed", "relative", "sticky", "initial", "inherit"
        ],
        t.Any,
    ]
    quotes: t.Union[t.Any, t.Literal["initial", "inherit"]]
    resize: t.Union[
        t.Any, t.Literal["none", "both", "horizontal", "vertical", "initial", "inherit"]
    ]
    right: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    rotate: t.Union[t.Any, t.Literal["initial", "inherit"]]
    row_gap: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    scale: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_behavior: t.Union[t.Any, t.Literal["auto", "smooth", "initial", "inherit"]]
    scroll_margin: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_block: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_block_end: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_block_start: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_bottom: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_inline: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_inline_end: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_inline_start: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_left: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_right: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_margin_top: t.Union[t.Any, t.Literal["initial", "inherit"]]
    scroll_padding: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_block: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_block_end: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_block_start: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_bottom: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_inline: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_inline_end: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_inline_start: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_left: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_right: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_padding_top: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    scroll_snap_align: t.Union[
        t.Any, t.Literal["none", "start", "end", "center", "initial", "inherit"]
    ]
    scroll_snap_stop: t.Union[
        t.Any, t.Literal["normal", "always", "initial", "inherit"]
    ]
    scroll_snap_type: t.Union[
        t.Any,
        t.Literal[
            "none",
            "x",
            "y",
            "block",
            "inline",
            "both",
            "mandatory",
            "proximity",
            "initial",
            "inherit",
        ],
    ]
    scrollbar_color: t.Union[t.Any, t.Literal["auto"]]
    tab_size: t.Union[t.Any, t.Literal["initial", "inherit"]]
    table_layout: t.Union[t.Any, t.Literal["auto", "fixed", "initial", "inherit"]]
    text_align: t.Union[
        t.Any, t.Literal["left", "right", "center", "justify", "initial", "inherit"]
    ]
    text_align_last: t.Union[
        t.Any,
        t.Literal[
            "auto",
            "left",
            "right",
            "center",
            "justify",
            "start",
            "end",
            "initial",
            "inherit",
        ],
    ]
    text_decoration: t.Union[t.Any, t.Literal["initial", "inherit"]]
    text_decoration_color: t.Union[t.Any, t.Literal["initial", "inherit"]]
    text_decoration_line: t.Union[
        t.Any,
        t.Literal[
            "none", "underline", "overline", "line-through", "initial", "inherit"
        ],
    ]
    text_decoration_style: t.Union[
        t.Any,
        t.Literal["solid", "double", "dotted", "dashed", "wavy", "initial", "inherit"],
    ]
    text_decoration_thickness: t.Union[
        t.Any, t.Literal["auto", "from-font", "initial", "inherit"]
    ]

    text_emphasis: t.Union[
        t.Any,
        t.Literal[
            "none",
            "filled",
            "open",
            "dot",
            "circle",
            "double-circle",
            "triangle",
            "sesame",
            "initial",
            "inherit",
        ],
    ]
    text_emphasis_color: t.Union[t.Any, t.Literal["initial", "inherit"]]
    text_emphasis_position: t.Union[
        t.Any, t.Literal["over", "under", "left", "right", "initial", "inherit"]
    ]
    text_emphasis_style: t.Union[
        t.Any,
        t.Literal[
            "none",
            "filled",
            "open",
            "dot",
            "circle",
            "double-circle",
            "triangle",
            "sesame",
            "string",
            "initial",
            "inherit",
        ],
    ]
    text_indent: t.Union[t.Any, t.Literal["initial", "inherit"]]
    text_justify: t.Union[
        t.Any,
        t.Literal[
            "auto", "inter-word", "inter-character", "none", "initial", "inherit"
        ],
    ]
    text_orientation: t.Union[
        t.Any,
        t.Literal[
            "mixed",
            "upright",
            "sideways",
            "sideways-right",
            "use-glyph-orientation",
            "initial",
            "inherit",
        ],
    ]
    text_overflow: t.Union[t.Any, t.Literal["clip", "ellipsis", "initial", "inherit"]]
    text_shadow: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    text_transform: t.Union[
        t.Any,
        t.Literal["none", "capitalize", "uppercase", "lowercase", "initial", "inherit"],
    ]
    text_underline_offset: t.Union[
        t.Any, t.Literal["auto", "length", "percentage", "initial", "inherit"]
    ]
    text_underline_position: t.Union[
        t.Any,
        t.Literal["auto", "under", "from-font", "left", "right", "initial", "inherit"],
    ]
    top: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    transform: t.Union[t.Any, t.Literal["none", "initial", "inherit"]]
    transform_origin: t.Union[t.Any, t.Literal["initial", "inherit"]]
    transform_style: t.Union[
        t.Any, t.Literal["flat", "preserve-3d", "initial", "inherit"]
    ]
    transition: t.Union[t.Any, t.Literal["initial", "inherit"]]
    transition_delay: t.Union[t.Any, t.Literal["initial", "inherit"]]
    transition_duration: t.Union[t.Any, t.Literal["none", "all", "initial", "inherit"]]
    transition_property: t.Union[t.Any, t.Literal["none", "all", "initial", "inherit"]]
    transition_timing_function: t.Union[
        t.Any,
        t.Literal[
            "linear",
            "ease",
            "ease-in",
            "ease-out",
            "ease-in-out",
            "step-start",
            "step-end",
            "steps",
            "cubic-bezier",
            "initial",
            "inherit",
        ],
    ]
    translate: t.Union[t.Any, t.Literal["initial", "inherit"]]
    unicode_bidi: t.Union[
        t.Any, t.Literal["normal", "embed", "bidi-override", "initial", "inherit"]
    ]
    user_select: t.Union[t.Any, t.Literal["auto", "none", "text", "all"]]
    vertical_align: t.Union[
        int,
        t.Literal[
            "baseline",
            "sub",
            "super",
            "top",
            "text-top",
            "middle",
            "bottom",
            "text-bottom",
            "initial",
            "inherit",
        ],
    ]
    visibility: t.Union[
        t.Any, t.Literal["visible", "hidden", "collapse", "initial", "inherit"]
    ]
    white_space: t.Union[
        t.Any,
        t.Literal[
            "normal", "nowrap", "pre", "pre-line", "pre-wrap", "initial", "inherit"
        ],
    ]
    widows: t.Union[int, t.Literal["initial", "inherit"]]
    width: t.Union[t.Any, t.Literal["auto", "initial", "inherit"]]
    word_break: t.Union[
        t.Any,
        t.Literal[
            "normal", "break-all", "keep-all", "break-word", "initial", "inherit"
        ],
    ]
    word_spacing: t.Union[t.Any, t.Literal["normal", "initial", "inherit"]]
    word_wrap: t.Union[t.Any, t.Literal["normal", "break-word", "initial", "inherit"]]
    writing_mode: t.Union[
        t.Any, t.Literal["horizontal-tb", "vertical-rl", "vertical-lr"]
    ]
    z_index: t.Union[int, t.Literal["auto", "initial", "inherit"]]
