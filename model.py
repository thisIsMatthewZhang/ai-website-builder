import dspy
from dotenv import load_dotenv
from typing import List, TypedDict, Dict
from style_guide import StyleGuide
from page_layout import PageLayout
from task import Task

load_dotenv()

lm = dspy.LM("claude-sonnet-4-5-20250929", model_type="responses")

dspy.configure(lm=lm, adapter=dspy.JSONAdapter())

class Page(TypedDict):
    """
    Represents each page of a website
    ex: {page: "/contact/", description: "..."}
    """
    page: str
    description: str

class GenerateWebsitePages(dspy.Signature):
    """Generate website pages using Astro and TailwindCSS"""
    query: str = dspy.InputField()
    pages: List[Page] = dspy.OutputField()

class GenerateLayoutGuide(dspy.Signature):
    """
    Give detailed descriptions of the layout guide of each section of a website page in plain English given the style guide and page description.
    Refrain from including any direct coding syntax.
    Example:
            Hero Section:
               - Takes up full width of page
               - On the left side has text that reads ... with a CTA button
               - On right side has an image of ...
    """
    page: str = dspy.InputField()
    page_description: str = dspy.InputField()
    style_guide: StyleGuide = dspy.InputField()
    layout_guide: str = dspy.OutputField(desc="text describing the layout guide for a web page")


class GeneratePageLayout(dspy.Signature):
    """
    Generate a page layout for any webpage given a generic JSON that represents a page layout, the style guide, and page description.
    """
    generic_layout: PageLayout = dspy.InputField()
    style_guide: StyleGuide = dspy.InputField()
    page_description: str = dspy.InputField()
    page_layout: PageLayout = dspy.OutputField()

class GenerateTasks(dspy.Signature):
    """
    Generate a sequential list of coding-related tasks to build out the website in one go.
    """
    page_layouts: List[PageLayout] = dspy.InputField()
    style_guide: StyleGuide = dspy.InputField()
    page_descriptions: List[str] = dspy.InputField()
    tasks: List[Task] = dspy.OutputField()

class GenerateTaskCode(dspy.Signature):
    """
    Generate .astro, package.json, and necessary TailwindCSS code for given each task description.
    Use the provided list of pages and page descriptions to understand the pages the site needs,
    then generate the necessary code.
    """
    style_guide: StyleGuide = dspy.InputField()
    task_description: str = dspy.InputField()
    pages: List[str] = dspy.InputField()
    page_descriptions: List[str] = dspy.InputField()
    task_code: str = dspy.OutputField(desc="code that is generated as specified by the task description")


class WebsiteBuilder(dspy.Module):
    """Build website using Astro and TailwindCSS"""
    def __init__(self):
        self.generate_pages = dspy.ChainOfThought(GenerateWebsitePages)
        self.generate_layout_guide = dspy.ChainOfThought(GenerateLayoutGuide)
        self.generate_page_layout = dspy.ChainOfThought(GeneratePageLayout)
        self.generate_tasks = dspy.ChainOfThought(GenerateTasks)
        self.generate_task_code = dspy.ChainOfThought(GenerateTaskCode)


    def forward(self, query: str):
        pages = self.generate_pages(query=query)
        print(pages)
        page_descriptions = [pg['description'] for pg in pages.completions.pages[-1]]
        page_names = [pg['page'] for pg in pages.completions.pages[-1]]
        print("Pages generated")

        layout_guides: List[str] = []
        with open('./style_guide.json') as f:
            style_guide: StyleGuide = f
        for pg in pages.completions.pages[-1]:
            response = self.generate_layout_guide(page=pg['page'], page_description=pg['description'], style_guide=style_guide)
            layout_guides.append(response.layout_guide)
        print("Layout guides generated")

        page_layouts: List[PageLayout] = []
        with open('./site_page_layout.json') as f:
            generic_layout: PageLayout = f
        for pg in pages.completions.pages[-1]:
            response = self.generate_page_layout(generic_layout=generic_layout, style_guide=style_guide, page_description=pg['description'])
            page_layouts.append(response.page_layout)
            print(response)
        print("Page layouts generated")
        
        tasks = self.generate_tasks(page_layouts=page_layouts, style_guide=style_guide, page_descriptions=page_descriptions)
        code_for_tasks: List[str] = []
        for task in tasks.completions.tasks[-1]:
            code = self.generate_task_code(style_guide=style_guide, task_description=task['task_description'], pages=page_names, page_descriptions=page_descriptions)
            code_for_tasks.append(code)
            # print(code)
        return code_for_tasks

website_builder = WebsiteBuilder()
query = "Generate me a plumbing site"
print(website_builder(query=query))
