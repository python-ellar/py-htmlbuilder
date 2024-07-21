import typing as t
from abc import ABC, abstractmethod
from contextlib import contextmanager

from py_html.styles.utils import snake_to_kebab

from ellar.common.compatible import AttributeDict

from py_html.styles import StyleCSS


class NodeContext:
    def __init__(self, element, content) -> None:
        self.element = element
        self.content = content

    def render(self) -> str:
        pass


class BuildContext:
    def __init__(self, rendering_context: t.Dict, root_element: 'Element') -> None:
        self.ctx = dict(rendering_context)
        self.root = root_element

    @classmethod
    def create_context(cls, rendering_context: t.Dict, root_element: 'Element') -> 'BuildContext':
        return cls(rendering_context, root_element)

    @contextmanager
    def render_with_context(self, element) ->  t.Generator['FactoryBuildContext', t.Any, None]:
        yield FactoryBuildContext(self.ctx, element)

    def render_with_props(self, props: t.Any, owner: t.Any) -> t.Any:
        pass

    def render_content(self, content: t.Union['Element', t.Any]) -> str:
        def _gen_content(item: t.Any) -> str:
            if item is None or type(item) is bool:
                return ""

            if isinstance(item, Element):
                return item.render(self)

            if isinstance(item, (list, tuple)):
                return "".join(
                    _gen_content(item=child)
                    for child in item
                )

            if callable(item):
                with self.render_with_context() as factory_ctx:
                    return factory_ctx.render_content(item)

            return str(item)

        return _gen_content(content)

    def get_node_context(self, element: t.Union['Element', t.Any]) -> t.List[NodeContext]:
        def _gen_content(item: t.Any):
            if item is None or type(item) is bool:
                return ""

            if isinstance(item, Element):
                return NodeContext(item, content=_gen_content(item.content))

            if isinstance(item, (list, tuple)):
                return [
                    _gen_content(item=child)
                    for child in item
                ]

            if callable(item):
                with self.render_with_context(item) as factory_ctx:
                    return factory_ctx.build_context()

            return item

        return NodeContext(element, content=_gen_content(element.content))

    def build_context(self) -> t.Union[NodeContext, t.List[NodeContext]]:
        return self.get_node_context(self.root)


class FactoryBuildContext(BuildContext):
    def __init__(self, rendering_context: t.Dict, root_element: 'Element', element) -> None:
        super().__init__(rendering_context, root_element)
        self.element_factory = element

    @contextmanager
    def render_with_context(self, element):
        raise Exception("Context is already Available in Scope")

    def render_with_props(self, props: t.Any, owner: t.Any) -> t.Any:
        pass

    def render_content(self, content: t.Union['Element', t.Any]) -> str:
        return super().render_content(content(self))

    def build_context(self) -> t.Union[NodeContext, t.List[NodeContext]]:
        content = self.element_factory(self)
        return self.get_node_context(content)


def render_component(element: t.Union['Element', t.Any], ctx: t.Dict) -> str:
    build_context = BuildContext.create_context(ctx, root_element=element)
    root_node = build_context.build_context()
    assert root_node
    # return element.render(build_context)


class Element(ABC):
    content = ""
    # def _render_content(self, content: t.Any, ctx: t.Dict) -> str:
    #     ensure_content = content
    #     if callable(content):
    #         ensure_content = content(ctx)
    #
    #     def _gen_content(item: t.Any) -> str:
    #         if item is None or type(item) is bool:
    #             return ""
    #
    #         if isinstance(item, Element):
    #             return item.render(ctx)
    #
    #         if callable(content):
    #             raise Exception(f"Invalid Setup. Cant render => {content}")
    #
    #         return str(item)
    #
    #     if isinstance(ensure_content, (list, tuple)):
    #         return "".join(
    #             _gen_content(item=child)
    #             for child in ensure_content
    #         )
    #
    #     return _gen_content(ensure_content)

    @abstractmethod
    def render(self, ctx: BuildContext) -> str:
        """Render element"""


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

    def _render_attributes(self, ctx: BuildContext) -> str:
        rendered_attrs = []

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

    def _tag_output(self, attrs: str, inner_html: str) -> str:
        opening_tag = f"<{self.tag} {attrs}>" if attrs else f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{inner_html}{closing_tag}"

    def render(self, ctx: BuildContext):
        attrs = self._render_attributes(ctx)
        inner_html = ctx.render_content(self.content)
        return self._tag_output(attrs, inner_html)


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
