from typing import List, Dict, TypedDict, Union

class ColorVariants(TypedDict):
    DEFAULT: str
    light: str
    dark: str

class Colors(TypedDict):
    primary: ColorVariants
    secondary: ColorVariants
    neutral: Dict[str, str]
    feedback: Dict[str, str]

class FontSizeMap(TypedDict):
    xs: str
    sm: str
    base: str
    lg: str
    xl: str
    _2xl: str

class Theme(TypedDict):
    colors: Colors
    fontFamily: Dict[str, List[str]]
    fontSize: FontSizeMap
    fontWeight: Dict[str, int]
    lineHeight: Dict[str, str]
    spacing: Dict[str, str]
    borderRadius: Dict[str, str]
    screens: Dict[str, str]
    container: Dict[str, Union[bool, str]]
    boxShadow: Dict[str, str]

class ComponentStyle(TypedDict):
    base: str
    primary: str
    secondary: str
    disabled: str

class Components(TypedDict):
    button: Dict[ComponentStyle, str]
    card: Dict[ComponentStyle, str]
    _input: Dict[ComponentStyle, str]

class Accessibility(TypedDict):
    focusOutline: str
    contrast: str

class StyleGuide(TypedDict):
    theme: Theme
    components: Components
    accessibility: Accessibility
