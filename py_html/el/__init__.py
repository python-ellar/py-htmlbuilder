import typing as t

from .base import BaseElement, BaseHTML, Element
from .base import Fragment as fragment
from .elements.audio import (
    Audio as audio,
)
from .elements.audio import (
    Source as source,
)
from .elements.audio import (
    Track as track,
)
from .elements.audio import (
    Video as video,
)
from .elements.basic import (
    H1 as h1,
)
from .elements.basic import (
    H2 as h2,
)
from .elements.basic import (
    H3 as h3,
)
from .elements.basic import (
    H4 as h4,
)
from .elements.basic import (
    H5 as h5,
)
from .elements.basic import (
    H6 as h6,
)
from .elements.basic import (
    Body as body,
)
from .elements.basic import (
    Br as br,
)
from .elements.basic import (
    Comment as comment,
)
from .elements.basic import (
    Head as head,
)
from .elements.basic import (
    Hr as hr,
)
from .elements.basic import (
    Html as html,
)
from .elements.basic import (
    P as p,
)
from .elements.basic import (
    Title as title,
)
from .elements.formatting import (
    Abbr as abbr,
)
from .elements.formatting import (
    Address as address,
)
from .elements.formatting import (
    BlockQuote as blockquote,
)
from .elements.formatting import (
    Code as code,
)
from .elements.formatting import (
    Del as del_,
)
from .elements.formatting import (
    Em as em,
)
from .elements.formatting import (
    I as i,
)
from .elements.formatting import (
    Ins as ins,
)
from .elements.formatting import (
    Kbd as kbd,
)
from .elements.formatting import (
    Mark as mark,
)
from .elements.formatting import (
    Meter as meter,
)
from .elements.formatting import (
    Pre as pre,
)
from .elements.formatting import (
    Progress as progress,
)
from .elements.formatting import (
    Q as q,
)
from .elements.formatting import (
    Rp as rp,
)
from .elements.formatting import (
    Rt as rt,
)
from .elements.formatting import (
    Ruby as ruby,
)
from .elements.formatting import (
    S as s,
)
from .elements.formatting import (
    Samp as samp,
)
from .elements.formatting import (
    Small as small,
)
from .elements.formatting import (
    Strong as strong,
)
from .elements.formatting import (
    Sub as sub,
)
from .elements.formatting import (
    Sup as sup,
)
from .elements.formatting import (
    Template as template,
)
from .elements.formatting import (
    Time as time,
)
from .elements.formatting import (
    U as u,
)
from .elements.formatting import (
    Var as var,
)
from .elements.formatting import (
    Wbr as wbr,
)
from .elements.forms import (
    Button as button,
)
from .elements.forms import (
    DataList as datalist,
)
from .elements.forms import (
    FieldSet as fieldset,
)
from .elements.forms import (
    Form as form,
)
from .elements.forms import (
    Input as input,
)
from .elements.forms import (
    Label as label,
)
from .elements.forms import (
    Legend as legend,
)
from .elements.forms import (
    OptGroup as optgroup,
)
from .elements.forms import (
    Option as option,
)
from .elements.forms import (
    Output as output,
)
from .elements.forms import (
    Select as select,
)
from .elements.forms import (
    TextArea as textarea,
)
from .elements.frames import IFrame as iframe
from .elements.images import (
    Area as area,
)
from .elements.images import (
    Canvas as canvas,
)
from .elements.images import (
    FigCaption as figcaption,
)
from .elements.images import (
    Figure as figure,
)
from .elements.images import (
    Image as img,
)
from .elements.images import (
    Map as map,
)
from .elements.images import (
    Picture as picture,
)
from .elements.images import (
    Svg as svg,
)
from .elements.images import (
    Use as use,
)
from .elements.links import A as a
from .elements.links import Link as link
from .elements.links import Nav as nav
from .elements.lists import (
    Dd as dd,
)
from .elements.lists import (
    Dl as dl,
)
from .elements.lists import (
    Dt as dt,
)
from .elements.lists import (
    Li as li,
)
from .elements.lists import (
    Menu as menu,
)
from .elements.lists import (
    Ol as ol,
)
from .elements.lists import (
    Ul as ul,
)
from .elements.meta_info import Base as base
from .elements.meta_info import Meta as meta
from .elements.programming import (
    Embed as embed,
)
from .elements.programming import (
    NoScript as noscript,
)
from .elements.programming import (
    Object as object,
)
from .elements.programming import (
    Param as param,
)
from .elements.programming import (
    Script as script,
)
from .elements.semantics import (
    Article as article,
)
from .elements.semantics import (
    Aside as aside,
)
from .elements.semantics import (
    Data as data,
)
from .elements.semantics import (
    Details as details,
)
from .elements.semantics import (
    Dialog as dialog,
)
from .elements.semantics import (
    Div as div,
)
from .elements.semantics import (
    Footer as footer,
)
from .elements.semantics import (
    Header as header,
)
from .elements.semantics import (
    HGroup as hgroup,
)
from .elements.semantics import (
    Main as main,
)
from .elements.semantics import (
    Search as search,
)
from .elements.semantics import (
    Section as section,
)
from .elements.semantics import (
    Span as span,
)
from .elements.semantics import (
    Style as style,
)
from .elements.semantics import (
    Summary as summary,
)
from .elements.tables import (
    Caption as caption,
)
from .elements.tables import (
    Col as col,
)
from .elements.tables import (
    ColGroup as colgroup,
)
from .elements.tables import (
    Table as table,
)
from .elements.tables import (
    Tbody as tbody,
)
from .elements.tables import (
    Td as td,
)
from .elements.tables import (
    Tfoot as tfoot,
)
from .elements.tables import (
    Th as th,
)
from .elements.tables import (
    Thead as thead,
)
from .elements.tables import (
    Tr as tr,
)

__all__ = [
    "td",
    "th",
    "tr",
    "table",
    "tbody",
    "tfoot",
    "thead",
    "col",
    "colgroup",
    "caption",
    "data",
    "summary",
    "dialog",
    "details",
    "aside",
    "article",
    "search",
    "section",
    "main",
    "footer",
    "hgroup",
    "header",
    "span",
    "div",
    "style",
    "param",
    "object",
    "embed",
    "noscript",
    "script",
    "meta",
    "base",
    "menu",
    "ul",
    "ol",
    "li",
    "dl",
    "dd",
    "dt",
    "a",
    "link",
    "nav",
    "img",
    "map",
    "area",
    "canvas",
    "figure",
    "figcaption",
    "picture",
    "svg",
    "use",
    "iframe",
    "output",
    "datalist",
    "legend",
    "fieldset",
    "label",
    "option",
    "optgroup",
    "select",
    "button",
    "textarea",
    "input",
    "form",
    "var",
    "wbr",
    "u",
    "time",
    "template",
    "sup",
    "sub",
    "strong",
    "small",
    "samp",
    "s",
    "ruby",
    "rt",
    "rp",
    "progress",
    "pre",
    "meter",
    "mark",
    "kbd",
    "ins",
    "i",
    "em",
    "del_",
    "code",
    "q",
    "blockquote",
    "address",
    "abbr",
    "fragment",
    "comment",
    "hr",
    "br",
    "p",
    "h6",
    "h5",
    "h4",
    "h3",
    "h2",
    "h1",
    "body",
    "title",
    "head",
    "html",
    "audio",
    "video",
    "track",
    "source",
    "BaseElement",
    "BaseHTML",
    "Element",
]


def __dir__() -> t.List[str]:
    return sorted(__all__)  # pragma: no cover
