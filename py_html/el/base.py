import typing as t
from abc import ABC, abstractmethod
from contextlib import contextmanager

from ellar.common.compatible import AttributeDict

from py_html.styles import StyleCSS
from py_html.styles.utils import snake_to_kebab


class NodeContext:
    def __init__(
        self, parent: t.Any, node_element: "Element", node_content: t.Any
    ) -> None:
        self.node_element = node_element
        self.parent_element = parent
        self.node_content = node_content

    def get_content(self, item: t.Any) -> str:
        if item is None or type(item) is bool:
            return ""

        if isinstance(item, NodeContext):
            return item.render()

        if isinstance(item, (list, tuple)):
            return "".join(self.get_content(child) for child in item)

        return str(item)

    def render(self) -> str:
        inner_html = self.node_element.render_content(self.node_content, self)
        attrs = self.node_element.render_attributes(self)

        return self.node_element.render_tag(attrs, inner_html)


class BuildContext:
    """
    TODO: Refactor Build Context More
    """

    def __init__(self, rendering_context: t.Dict, root_element: "Element") -> None:
        self.ctx = dict(rendering_context)
        self.root = root_element

    def get(self, key: t.Any, default=None) -> t.Optional[t.Any]:
        return self.ctx.get(key, default)

    def add_root_style(self, element: "Element") -> None:
        self.ctx.setdefault("root_styles", []).append(element)

    def add_bottom_scripts(self, element: "Element") -> None:
        self.ctx.setdefault("bottom_scripts", []).append(element)

    @classmethod
    def create_context(
        cls, rendering_context: t.Dict, root_element: "Element"
    ) -> "BuildContext":
        return cls(rendering_context, root_element)

    @contextmanager
    def render_with_context(
        self, element
    ) -> t.Generator["FactoryBuildContext", t.Any, None]:
        yield FactoryBuildContext(self.ctx, self.root, element)

    def child_node_context(
        self, element: t.Any, child: t.Any
    ) -> t.Union[NodeContext, t.List[NodeContext]]:
        if isinstance(child, Element):
            if isinstance(child, LazyComponent):
                child.set_context_data(self)

            if isinstance(child, Component):
                content = self.child_node_context(child, child.resolve_content())
                child.exports(self)
            else:
                content = self.child_node_context(child, child.content)
            return NodeContext(parent=element, node_element=child, node_content=content)

        if isinstance(child, (list, tuple, Fragment)):
            return [self.child_node_context(element, child=item) for item in child]

        if callable(child):
            with self.render_with_context(child) as factory_ctx:
                return factory_ctx.build_context(parent=element)

        return child

    def get_node_context(
        self, element: t.Union["Element", "Fragment"], parent: t.Any
    ) -> t.Union[t.List[NodeContext], NodeContext]:
        if isinstance(element, (list, tuple, Fragment)):
            return [self.child_node_context(parent, child=child) for child in element]

        content = self.child_node_context(parent, element.content)
        return NodeContext(parent, node_element=element, node_content=content)

    def build_context(self, parent=None) -> t.Union[NodeContext, t.List[NodeContext]]:
        return self.get_node_context(self.root, parent=parent)


class FactoryBuildContext(BuildContext):
    """
    Resolves Elements and Element Content that requires ctx object passed to it.
    It also ensures the scope of the ctx passed maintained and expires when down.
    """

    def __init__(
        self, rendering_context: t.Dict, root_element: "Element", element
    ) -> None:
        super().__init__({}, root_element)
        self.ctx = rendering_context
        self.element_factory = element

    @contextmanager
    def render_with_context(self, element):
        raise Exception("Context is already Available in Scope")

    def build_context(self, parent=None) -> t.Union[NodeContext, t.List[NodeContext]]:
        content = Fragment(self.element_factory(self))
        return self.get_node_context(content, parent=parent)


def render_component(element: t.Union["Element", t.Any], ctx: t.Dict) -> str:
    build_context = BuildContext.create_context(ctx, root_element=element)
    root_node = build_context.build_context()

    assert root_node
    content = root_node.render()

    return content
    # return element.render(build_context)


class Element(ABC):
    content = None
    attrs: t.Dict = {}

    @abstractmethod
    def render_tag(self, attrs: str, inner_html: str) -> str:
        """Render element"""

    def render_content(self, content: t.Any, ctx: NodeContext) -> t.Any:
        """Dynamic set or modify Element Properties before render"""
        return ctx.get_content(content)

    def render_attributes(self, ctx: NodeContext) -> str:
        rendered_attrs = []

        for key, value in ((k, v) for k, v in self.attrs.items() if v):
            key = snake_to_kebab(key)
            if isinstance(value, StyleCSS):
                rendered_attrs.append(f'{key}="{value.render()}"')
            else:
                if isinstance(value, bool):
                    rendered_attrs.append(f"{key}")
                else:
                    rendered_attrs.append(f'{key}="{value}"')
        return " ".join(rendered_attrs)


class BaseElement(Element):
    tag: str

    id: t.Optional[t.Any]
    title: t.Optional[t.Any]
    class_name: t.Optional[t.Any]
    style: t.Optional[StyleCSS]
    lang: t.Optional[t.Any]
    dir: t.Optional[t.Any]
    accesskey: t.Optional[t.Any]
    contenteditable: t.Optional[t.Any]
    draggable: t.Optional[t.Any]
    enterkeyhint: t.Optional[t.Any]
    hidden: t.Optional[t.Any]
    inert: t.Optional[t.Any]
    inputmode: t.Optional[t.Any]
    popover: t.Optional[t.Any]
    spellcheck: t.Optional[t.Any]
    tabindex: t.Optional[t.Any]
    translate: t.Optional[t.Any]
    autofocus: t.Optional[bool]

    def __init__(
        self,
        content: t.Optional[t.Any] = None,
        id: t.Optional[t.Any] = None,
        title: t.Optional[t.Any] = None,
        class_name: t.Optional[t.Any] = None,
        style: t.Optional[StyleCSS] = None,
        lang: t.Optional[t.Any] = None,
        dir: t.Optional[t.Any] = None,
        accesskey: t.Optional[t.Any] = None,
        contenteditable: t.Optional[t.Any] = None,
        draggable: t.Optional[t.Any] = None,
        enterkeyhint: t.Optional[t.Any] = None,
        hidden: t.Optional[t.Any] = None,
        inert: t.Optional[t.Any] = None,
        inputmode: t.Optional[t.Any] = None,
        popover: t.Optional[t.Any] = None,
        spellcheck: t.Optional[t.Any] = None,
        tabindex: t.Optional[t.Any] = None,
        translate: t.Optional[t.Any] = None,
        autofocus: t.Optional[bool] = None,
        **attrs: t.Any,
    ):
        assert self.tag

        block_style = getattr(self, "style", StyleCSS())
        block_class_name = getattr(self, "class_name", "")

        self.style = StyleCSS(**(style or {}))
        self.style.update(**block_style)
        class_name = (
            f"{block_class_name} {class_name or ''}" if block_class_name else class_name
        )

        self.attrs = AttributeDict(
            attrs,
            id=id,
            title=title,
            lang=lang,
            dir=dir,
            autofocus=autofocus,
            accesskey=accesskey,
            contenteditable=contenteditable,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            hidden=hidden,
            inert=inert,
            inputmode=inputmode,
            popover=popover,
            spellcheck=spellcheck,
            tabindex=tabindex,
            translate=translate,
        )
        # remove all nullable values
        for key, value in self.attrs.copy().items():
            if value is None and not hasattr(self, key):
                self.attrs.pop(key)
            else:
                self.attrs[key] = getattr(self, key, value)

        self.content = content
        self.id = id
        self.title = title
        self.lang = lang
        self.dir = dir
        self.class_name = class_name

    def render_attributes(self, ctx: NodeContext) -> str:
        self.attrs.update(
            {
                "class": self.class_name,
                "id": self.id,
                "lang": self.lang,
                "dir": self.dir,
                "title": self.title,
                "style": self.style,
            }
        )
        return super().render_attributes(ctx)

    def render_tag(self, attrs: str, inner_html: str) -> str:
        opening_tag = f"<{self.tag} {attrs}>" if attrs else f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{inner_html}{closing_tag}"


class BaseHTML(BaseElement):
    tag: str

    def __init__(
        self,
        onclick: t.Optional[t.Any] = None,
        ondblclick: t.Optional[t.Any] = None,
        onmousedown: t.Optional[t.Any] = None,
        onmouseup: t.Optional[t.Any] = None,
        onmouseover: t.Optional[t.Any] = None,
        onmousemove: t.Optional[t.Any] = None,
        onmouseout: t.Optional[t.Any] = None,
        onkeypress: t.Optional[t.Any] = None,
        onkeydown: t.Optional[t.Any] = None,
        onkeyup: t.Optional[t.Any] = None,
        onafterprint: t.Optional[t.Any] = None,
        onbeforeprint: t.Optional[t.Any] = None,
        onbeforeunload: t.Optional[t.Any] = None,
        onerror: t.Optional[t.Any] = None,
        onhashchange: t.Optional[t.Any] = None,
        onload: t.Optional[t.Any] = None,
        onmessage: t.Optional[t.Any] = None,
        onoffline: t.Optional[t.Any] = None,
        ononline: t.Optional[t.Any] = None,
        onpagehide: t.Optional[t.Any] = None,
        onpageshow: t.Optional[t.Any] = None,
        onpopstate: t.Optional[t.Any] = None,
        onresize: t.Optional[t.Any] = None,
        onstorage: t.Optional[t.Any] = None,
        onunload: t.Optional[t.Any] = None,
        **attrs,
    ) -> None:
        super().__init__(
            onclick=onclick,
            ondblclick=ondblclick,
            onmousedown=onmousedown,
            onmouseup=onmouseup,
            onmouseover=onmouseover,
            onmousemove=onmousemove,
            onmouseout=onmouseout,
            onkeypress=onkeypress,
            onkeydown=onkeydown,
            onkeyup=onkeyup,
            onafterprint=onafterprint,
            onbeforeprint=onbeforeprint,
            onbeforeunload=onbeforeunload,
            onerror=onerror,
            onhashchange=onhashchange,
            onload=onload,
            onmessage=onmessage,
            onoffline=onoffline,
            ononline=ononline,
            onpagehide=onpagehide,
            onpageshow=onpageshow,
            onpopstate=onpopstate,
            onresize=onresize,
            onstorage=onstorage,
            onunload=onunload,
            **attrs,
        )


class Fragment:
    def __init__(self, *contents: t.Union[Element, t.Any]) -> None:
        self.content = list(contents)

    def __iter__(self):
        for item in self.content:
            if isinstance(item, (Fragment, list, tuple)):
                for y in item:
                    yield y
                continue
            yield item


class LazyComponent(BaseElement):
    """
    Defers NodeContext computation till during rendering
    """

    content: t.Any = None

    def __init__(self, resolver: t.Callable, **attrs) -> None:
        self.tag = "lazy-component"

        super(LazyComponent, self).__init__(**attrs)

        self._resolver = resolver
        self._ctx: t.Optional[BuildContext] = None

    def set_context_data(self, ctx: BuildContext) -> None:
        self._ctx = ctx

    def resolve_lazy_element(
        self, parent: t.Optional["Element"] = None
    ) -> t.Union[NodeContext, t.List[NodeContext]]:
        assert (
            self._ctx is not None
        ), "please set_context_data() before resolving element."

        element = self._resolver()
        return self._ctx.child_node_context(parent, element)

    def render_tag(self, attrs: str, inner_html: str) -> str:
        if attrs:
            return f"<div {attrs}>{inner_html}</div>"
        return inner_html

    def render_content(self, content: t.Any, ctx: NodeContext) -> t.Any:
        resolved_content = self.resolve_lazy_element(ctx.parent_element)
        return ctx.get_content(resolved_content)


class Component:
    """
    Provide dynamic content through `resolve_content` method.
    """

    @abstractmethod
    def resolve_content(self) -> t.Union[Fragment, Element]:
        pass

    @abstractmethod
    def exports(self, ctx: BuildContext) -> None:
        """Exports CSS of Scripts to HTML"""
