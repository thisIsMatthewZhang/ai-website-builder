# DSPy AI Website Builder
An intelligent, multi-stage website generator that transforms a simple natural language query into a complete website structure. Using DSPy for programmatic LLM control, this tool automates the planning, layout design, and coding of professional websites using Astro and TailwindCSS.

## Tech Stack
Core Logic: DSPy (Declarative Self-improving Language Programs)

LLM: Claude 3.5 Sonnet (via DSPy LM)

Frontend Framework: Astro

Styling: TailwindCSS

Data Handling: Pydantic-style TypedDicts & JSON Adapters

## Features
Structured Planning: Automatically breaks down a user query (e.g., "Build a plumbing site") into a logical sitemap with page descriptions.

Layout Orchestration: Generates detailed, plain-English layout guides for every section of every page.

Chain of Thought (CoT): Utilizes dspy.ChainOfThought for complex reasoning during layout and task generation.

Sequential Task Execution: Converts layout designs into a sequence of actionable coding tasks.

Automated Code Generation: Produces production-ready .astro components, package.json configurations, and Tailwind utility classes.

## Architecture & Workflow
The system follows a modular pipeline defined in the WebsiteBuilder class:

Page Generation: Identifies required routes (e.g., /contact, /services).

Layout Description: Creates a visual blueprint for each page based on a style_guide.json.

JSON Layout Mapping: Maps descriptions to a formal PageLayout schema.

Task Synthesis: Creates a sequential roadmap of coding requirements.

Code Production: Generates the final source code for the entire site.
