Multi-Agent Content Generation System
1. Problem Statement

The goal of this project is to design and implement a modular, agentic automation system that transforms a fixed product dataset into multiple structured, machine-readable content pages.

The system must:

Operate entirely via autonomous agents

Use a clear orchestration flow

Apply reusable content logic

Assemble content using templates

Output clean JSON artifacts

This challenge evaluates system design and automation engineering, not UI development or domain expertise.

2. Solution Overview

This project implements a LangGraph-based agentic pipeline that converts structured product input into three distinct content pages:

FAQ Page

Product Description Page

Comparison Page

Each step in the pipeline is handled by a single-responsibility agent, coordinated through a directed graph.
All content generation is deterministic, rule-driven, and traceable to the original input data.

The final outputs are written as JSON files to disk.

3. Scope & Assumptions
In Scope

Single fixed product dataset

Agent-based orchestration using LangGraph

Deterministic content generation

Template-driven page assembly

Machine-readable JSON output

Out of Scope

UI or frontend rendering

Databases or persistence layers

External APIs or integrations

Real-time user input

Model training or fine-tuning

Assumptions

Product data is trusted and complete

Content correctness is derived strictly from input data

Fictional comparison product is clearly marked and internally consistent

4. System Design (Most Important)
4.1 High-Level Architecture

The system is implemented as a directed acyclic graph (DAG) of agents:

START
  ↓
Product Parser Agent
  ↓
Question Generation Agent
  ↓
FAQ Page Agent
  ↓
Product Page Agent
  ↓
Comparison Page Agent
  ↓
Output Writer Agent
  ↓
END


Each agent:

Has a single responsibility

Accepts and returns structured state

Does not depend on hidden global context

4.2 Shared State Model

All agents operate on a shared GraphState object, which evolves as it passes through the graph.

Key fields include:

raw_product – initial input dataset

product – normalized product model

questions – categorized user questions

faq_page – assembled FAQ content

product_page – assembled product description

comparison_page – assembled comparison content

This state-based design ensures:

Clear data flow

Easy extensibility

Deterministic execution

4.3 Agent Responsibilities
Product Parser Agent

Converts raw input data into a validated internal product model

Performs no content generation

Question Generation Agent

Automatically generates categorized user questions

Categories include Usage, Safety, Informational, Purchase, and Comparison

FAQ Page Agent

Maps question categories to appropriate product attributes

Applies rule-based logic to generate answers

Produces structured FAQ JSON

Product Page Agent

Assembles a structured product description

Directly reflects normalized product data

Comparison Page Agent

Introduces a fictional Product B

Produces a structured comparison without external research

Output Writer Agent

Persists final JSON artifacts to disk

Creates output directories deterministically

4.4 Content Logic Blocks

Content generation is governed by explicit rule-based logic, not free-form prompting.

Examples include:

Mapping usage questions to usage instructions

Mapping safety questions to side effects

Mapping informational questions to ingredient lists

Structured comparison logic between two products

This separation ensures:

Reusability

Testability

Predictable outputs

4.5 Template-Based Assembly

Each content page follows a predefined template that specifies:

Required fields

Data dependencies

Output structure

Templates assemble content, but do not generate it themselves.
This enforces a clean separation between logic and presentation structure.

4.6 Output Artifacts

The system produces three machine-readable JSON files:

faq.json

product_page.json

comparison_page.json

These files represent the final deliverables of the pipeline.

5. Extensibility

The system is designed to be easily extended by:

Adding new page agents

Introducing new logic blocks

Supporting additional product schemas

Replacing deterministic logic with LLM-assisted blocks where appropriate

No changes to existing agents are required to extend functionality.

6. Conclusion

This project demonstrates a production-style agentic automation system with clear abstractions, deterministic behavior, and modular design.

The architecture emphasizes:

Clean agent boundaries

Explicit orchestration

Reusable content logic

Structured outputs

This approach mirrors real-world applied AI systems where automation, reliability, and design clarity are more critical than raw model complexity.

7. Setup & Execution Guide

This section describes how to run the project locally using LangGraph Dev with uv for dependency management.

7.1 Prerequisites

Ensure the following are installed:

Python 3.10+

Git

uv (Python package manager)

LangGraph CLI

Install uv (if not already installed):

pip install uv


uv is used instead of pip for faster and reproducible dependency management.

7.2 Project Setup

Clone the repository:

git clone https://github.com/<your-username>/kasparro-ai-agentic-content-generation-system-zuhair-ahmad.git
cd kasparro-ai-agentic-content-generation-system-zuhair-ahmad


Create and activate a virtual environment using uv:

uv venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate


Install dependencies:

uv pip install -r requirements.txt


(Ensure requirements.txt includes langgraph, pydantic, and langchain-core.)

7.3 Running the Agentic Pipeline

The project is executed using LangGraph Dev.

From the repository root, run:

langgraph dev


This command:

Loads the compiled LangGraph workflow

Initializes the agent orchestration graph

Enables local execution of the pipeline

7.4 Input State

The graph expects an initial state containing the raw product data.

Example input:

{
  "raw_product": {
    "name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "skin_type": ["Oily", "Combination"],
    "ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "how_to_use": "Apply 2–3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "price": "₹699"
  }
}

7.5 Output Artifacts

On successful execution, the system automatically creates an outputs/ directory and generates:

outputs/
├── faq.json
├── product_page.json
└── comparison_page.json


Each file is a machine-readable JSON representation of a generated content page.

7.6 Notes

No frontend or API server is required.

No external services or credentials are needed.

The system is fully self-contained and deterministic.

Re-running the pipeline overwrites existing output files.