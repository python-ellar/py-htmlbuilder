import typing as t

from .base import BaseElement, BaseHTML, Element, Fragment
from .elements.audio import Audio, Source, Track, Video
from .elements.basic import (
    DOCTYPE,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Body,
    Br,
    Comment,
    Head,
    Hr,
    Html,
    P,
    Title,
)
from .elements.formatting import (
    Abbr,
    Address,
    BlockQuote,
    Code,
    Del,
    I,
    Ins,
    Kbd,
    Mark,
    Meter,
    Pre,
    Progress,
    Q,
    Rp,
    Rt,
    Ruby,
    S,
    Samp,
    Small,
    Strong,
    Sub,
    Sup,
    Template,
    Time,
    U,
    Var,
    Wbr,
)
from .elements.forms import (
    Button,
    DataList,
    FieldSet,
    Form,
    Input,
    Label,
    Legend,
    OptGroup,
    Option,
    Output,
    Select,
    TextArea,
)
from .elements.frames import IFrame
from .elements.images import (
    Area,
    Canvas,
    FigCaption,
    Figure,
    Image,
    Map,
    Picture,
    Svg,
    Use,
)
from .elements.links import A, Link, Nav
from .elements.lists import Dd, Dl, Dt, Li, Menu, Ol, Ul
from .elements.meta_info import Base, Meta
from .elements.programming import Embed, NoScript, Object, Param, Script
from .elements.semantics import (
    Article,
    Aside,
    Data,
    Details,
    Dialog,
    Div,
    Footer,
    Header,
    HGroup,
    Main,
    Search,
    Section,
    Span,
    Style,
    Summary,
)
from .elements.tables import (
    Caption,
    Col,
    ColGroup,
    Table,
    Tbody,
    Td,
    Tfoot,
    Th,
    Thead,
    Tr,
)

__all__ = [
    "Td",
    "Th",
    "Tr",
    "Table",
    "Tbody",
    "Tfoot",
    "Thead",
    "Col",
    "ColGroup",
    "Caption",
    "Data",
    "Summary",
    "Dialog",
    "Details",
    "Aside",
    "Article",
    "Search",
    "Section",
    "Main",
    "Footer",
    "HGroup",
    "Header",
    "Span",
    "Div",
    "Style",
    "Param",
    "Object",
    "Embed",
    "NoScript",
    "Script",
    "Meta",
    "Base",
    "Menu",
    "Ul",
    "Ol",
    "Li",
    "Dl",
    "Dd",
    "Dt",
    "A",
    "Link",
    "Nav",
    "Image",
    "Map",
    "Area",
    "Canvas",
    "Figure",
    "FigCaption",
    "Picture",
    "Svg",
    "Use",
    "IFrame",
    "Output",
    "DataList",
    "Legend",
    "FieldSet",
    "Label",
    "Option",
    "OptGroup",
    "Select",
    "Button",
    "TextArea",
    "Input",
    "Form",
    "Var",
    "Wbr",
    "U",
    "Time",
    "Template",
    "Sup",
    "Sub",
    "Strong",
    "Small",
    "Samp",
    "S",
    "Ruby",
    "Rt",
    "Rp",
    "Progress",
    "Pre",
    "Meter",
    "Mark",
    "Kbd",
    "Ins",
    "I",
    "Del",
    "Code",
    "Q",
    "BlockQuote",
    "Address",
    "Abbr",
    "Fragment",
    "Comment",
    "Hr",
    "Br",
    "P",
    "H6",
    "H5",
    "H4",
    "H3",
    "H2",
    "H1",
    "Body",
    "Title",
    "Head",
    "Html",
    "DOCTYPE",
    "Audio",
    "Video",
    "Track",
    "Source",
    "BaseElement",
    "BaseHTML",
    "Element",
]


def __dir__() -> t.List[str]:
    return sorted(__all__)  # pragma: no cover
