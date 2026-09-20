# CSC Project Roadmap

Source of truth for the approved Computer Science Center (CSC) educational projects and their order of work. Maintainer: **Konstantinos Zitis**. Education website: [https://csc.gr](https://csc.gr).

Themes are ordered by strict priority: **1. AI, 2. Python, 3. Java, 4. JavaScript, 5. Flutter, 6. HTML / DOM**. Other languages and technologies are not part of the roadmap yet. Within a theme, projects are listed in priority order; the `#` column is the global order of work.

- **Planned**: approved, not yet released. **Available**: released and listed in the [catalogue](catalog/README.md). When a project becomes Available, update its status here and add it to the catalogue in the same change.
- A range in the Level column (for example Foundation / Intermediate) is guidance only. Fix one level (Foundation, Intermediate or Advanced) when the project starts and record it here.
- Create a new repository with [`tools/new-project.py`](tools/new-project.py), then follow the [project standard](docs/PROJECT_STANDARD.md), including **Efficient Project Generation**. Repository names follow [naming and versioning](docs/NAMING_AND_VERSIONING.md).

## 1. AI

| # | Repository | Title | Technology | Level | Status | Learning focus | Domain concept |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `csc-ai-multi-agent-operations-center` | Multi-Agent Operations Center | Python | Advanced | Planned | Agents, roles, tools, orchestration, multi-agent workflows | A team of specialised agents running an operations desk |
| 2 | `csc-ai-rag-knowledge-assistant` | RAG Knowledge Assistant | Python | Intermediate | Planned | Embeddings, retrieval, chunking, citations, RAG architecture | Answering questions from a document collection with sources |
| 3 | `csc-ai-agentic-business-assistant` | Agentic Business Assistant | Python | Intermediate | Planned | Tools, structured workflows, approvals, business automation | An assistant that carries out routine business tasks |
| 4 | `csc-ai-model-router` | Cost-Efficient AI Model Router | Python | Advanced | Planned | Model routing, fallback strategies, task classification, cost/performance trade-offs | Choosing the right model for each request |
| 5 | `csc-ai-n8n-agent-automation` | Agent Automation with n8n | JavaScript / workflow JSON (Python where appropriate) | Intermediate | Planned | Agents, automation, APIs, MCP-style workflows | Connecting agents to services through visual workflows |
| 6 | `csc-ai-vibe-coding-product-factory` | AI Product Factory | JavaScript / TypeScript + appropriate backend | Intermediate | Planned | AI-assisted product development, iterative building, deployment | Taking a product idea to a deployed application |
| 7 | `csc-ai-prompt-evaluation-lab` | Prompt Evaluation Lab | Python | Intermediate | Planned | Prompt design, structured outputs, comparison, evaluation | Testing prompts the way software is tested |
| 8 | `csc-ai-rag-evaluation-benchmark` | RAG Evaluation Benchmark | Python | Advanced | Planned | Relevance, groundedness, retrieval metrics, hallucination analysis | Measuring how trustworthy a RAG system is |
| 9 | `csc-ai-local-model-workbench` | Local AI Model Workbench | Python | Intermediate | Planned | Local models, privacy, inference, model comparison | Running and comparing models on the learner's own machine |
| 10 | `csc-ai-human-in-the-loop-agent` | Human-in-the-Loop Agent | Python | Advanced | Planned | Approvals, guardrails, escalation, audit trail | An agent that must ask a person before acting |

## 2. Python

| # | Repository | Title | Technology | Level | Status | Learning focus | Domain concept |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | `csc-python-energy-intelligence` | Greece Energy Intelligence Platform | Python | Intermediate | Planned | pandas, data analysis, statistics, visualisation, energy data | Understanding the Greek electricity system through data |
| 12 | `csc-python-climate-risk-lab` | Climate Risk Intelligence Lab | Python | Intermediate | Planned | Weather and extreme-event data, analysis, visualisation | Assessing climate and extreme-weather risk |
| 13 | `csc-python-automation-command-center` | Automation Command Center | Python | Intermediate | Planned | Files, APIs, reports, automation workflows | One place to run and monitor automation jobs |

## 3. Java

| # | Repository | Title | Technology | Level | Status | Learning focus | Domain concept |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 14 | [`csc-java-fire-response-system`](https://github.com/ConstantinSummer/csc-java-fire-response-system) | Greek Fire Response Coordination System | Java | Intermediate | Available | OOP with arrays: encapsulation, inheritance, polymorphism, enums, exceptions, state machine | Coordinating wildfire response resources |
| 15 | `csc-java-smart-city-mobility` | Smart City Mobility | Java (JavaFX where appropriate) | Intermediate / Advanced | Planned | EVs, charging, parking, traffic, JavaFX where appropriate | Managing electric-vehicle and parking demand in a city |
| 16 | `csc-java-space-mission-control` | Space Mission Control | Java | Advanced | Planned | Telemetry, events, concurrency, GUI | Monitoring a spacecraft from a control room |

## 4. JavaScript

Repository names use the technology identifier `javascript`, which is listed in [naming and versioning](docs/NAMING_AND_VERSIONING.md).

| # | Repository | Title | Technology | Level | Status | Learning focus | Domain concept |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | `csc-javascript-live-dashboard` | Live Dashboard | JavaScript | Intermediate | Planned | Async JavaScript, APIs, live data, DOM | A dashboard that updates as new data arrives |
| 18 | `csc-javascript-ai-workspace` | Browser AI Workspace | JavaScript | Intermediate | Planned | Browser AI workspace, structured workflows, local state | An AI-assisted workspace that runs in the browser |
| 19 | `csc-javascript-smart-travel-planner` | Smart Travel Planner | JavaScript | Intermediate | Planned | APIs, dynamic UI, map-style data, asynchronous programming | Planning a trip from live travel data |

## 5. Flutter

| # | Repository | Title | Technology | Level | Status | Learning focus | Domain concept |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | `csc-flutter-student-progress` | Student Progress App | Flutter / Dart | Intermediate | Planned | Navigation, state, forms, persistence, learning analytics | Tracking a learner's progress on a phone |
| 21 | `csc-flutter-smart-city-companion` | Smart City Companion | Flutter / Dart | Intermediate | Planned | APIs, modern mobile UI, state management | A mobile guide to city services |
| 22 | `csc-flutter-ai-productivity-hub` | AI Productivity Hub | Flutter / Dart | Advanced | Planned | AI-oriented productivity workflows | A personal productivity app built around AI features |

## 6. HTML / DOM

| # | Repository | Title | Technology | Level | Status | Learning focus | Domain concept |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 23 | `csc-web-interactive-newsroom` | Interactive Newsroom | HTML / CSS / JavaScript DOM | Foundation / Intermediate | Planned | Dynamic news dashboard, DOM manipulation, filters, accessibility | A newsroom front page that readers can filter and explore |
| 24 | `csc-web-smart-event-experience` | Smart Event Experience | HTML / CSS / JavaScript DOM | Intermediate | Planned | Interactive event platform, schedules, filtering, modal UI, dynamic state | A conference or festival programme visitors can browse |
| 25 | `csc-web-digital-museum-explorer` | Digital Museum Explorer | HTML / CSS / JavaScript DOM | Intermediate | Planned | Searchable exhibits, DOM rendering, categories, accessibility, responsive UI | Exploring a museum collection online |
