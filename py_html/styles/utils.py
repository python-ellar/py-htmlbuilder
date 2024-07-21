import re


def camel_to_kebab(style_property: str) -> str:
    # Use regular expression to find camelCase patterns and replace them with kebab-case
    kebab_case_property = re.sub(r"([a-z])([A-Z])", r"\1-\2", style_property).lower()
    return kebab_case_property


def snake_to_kebab(style_property: str) -> str:
    return style_property.replace("_", "-")
