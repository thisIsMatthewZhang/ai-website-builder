from typing import TypedDict, List, Optional


class ResponsiveConfig(TypedDict):
    menu: Optional[str]
    order: Optional[List[str]]
    columns: Optional[int]  # For "md+" and "lg+" responsive layout


class ResponsiveSettings(TypedDict):
    mobile: Optional[ResponsiveConfig]
    desktop: Optional[ResponsiveConfig]
    md_plus: Optional[ResponsiveConfig]  # Represents "md+"
    lg_plus: Optional[ResponsiveConfig]  # Represents "lg+"


class ContentBlock(TypedDict):
    _type: str
    headingLevel: Optional[int]
    content: Optional[List[str]]


class ContentItem(TypedDict):
    _type: str
    level: Optional[int]
    orientation: Optional[str]
    variant: Optional[str]
    label: Optional[str]
    subtype: Optional[str]


class Section(TypedDict):
    _id: str
    role: str
    position: Optional[str]
    maxWidth: Optional[str]
    variant: Optional[str]
    alignment: Optional[str]
    columns: Optional[int]
    content: Optional[List[ContentItem]]
    contentBlocks: Optional[List[ContentBlock]]
    responsive: Optional[ResponsiveSettings]


class Layout(TypedDict):
    _type: str  # e.g. "vertical"
    sections: List[Section]


class Page(TypedDict):
    path: str  # e.g. "/"
    layout: Layout


class PageLayout(TypedDict):
    page: Page
