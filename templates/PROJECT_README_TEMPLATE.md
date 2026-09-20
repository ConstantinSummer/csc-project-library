<!-- Copy this file to the root README.en.md of a future CSC application repository.
Create README.md as a complete Greek translation with the same structure and released-project information.
Keep both files synchronized, retain the language switch at the top of each, replace every <...>
placeholder, choose one learning level and remove authoring comments.
Also create RELEASE_NOTES.md (complete English release notes, canonical for GitHub) and
RELEASE_NOTES.el.md (complete equivalent Greek version) in the repository root and update them
together. README.en.md links to RELEASE_NOTES.md; README.md links to RELEASE_NOTES.el.md.
The GitHub Release body uses the English RELEASE_NOTES.md content plus a short pointer to the Greek file.
Follow https://github.com/ConstantinSummer/csc-project-library/blob/main/docs/PROJECT_STANDARD.md.
Do not present extension ideas as implemented features. -->

# CSC — <Project Title>

[Ελληνικά](README.md) | **English**

A complete educational application from **Computer Science Center (CSC)**.

Education website: [https://csc.gr](https://csc.gr)

Maintainer: **Konstantinos Zitis**

| Project information | Value |
| --- | --- |
| Repository | `csc-<technology>-<project-name>` |
| Primary area | <Catalogue area> |
| Learning level | <Foundation / Intermediate / Advanced — choose one> |
| Documented release | <Version and link to the matching release> |

## Project overview

<Describe the application, its intended users and the problem it solves.>

Implemented features:

- <Feature learners can run and observe>

Scope and limitations: <Explain what the baseline application covers.>

### Learning workflow

1. Download or clone the documented release and complete setup.
2. Run the application and try the example workflow.
3. Study the source code using the architecture and concept references below.
4. Discuss design decisions and guided review questions during lessons.
5. Complete extension challenges and demonstrate that their acceptance criteria are met.

## Learning objectives

After studying and extending this application, learners should be able to:

- <Observable outcome connected to a real feature or source component>
- <Observable design or implementation outcome>

## Prerequisites

- Knowledge: <Required programming and subject concepts>
- Environment: <Supported operating systems, tools and hardware>
- External resources: <Accounts, services, datasets and costs, or explicitly None>

## Technologies used

| Technology | Supported version | Role |
| --- | --- | --- |
| <Language/runtime/framework/library/database> | <Version> | <Purpose> |

## Setup instructions

1. <Give the actual repository download/clone command and select the documented release tag.>
2. <Specify the working directory and prerequisite installation steps.>
3. <Provide exact dependency installation commands.>
4. <Explain example configuration, required variables and safe local values; never supply secrets.>
5. <Describe database/sample-data initialization, or state that none is needed.>
6. <Give a setup verification command or action and its expected result.>

<!-- Replace these instructions with commands and steps tested on the documented environment. -->

## Execution instructions

### Start and stop

<Give exact commands/actions, their working directory and any URL or interface to open. Explain how to stop the application.>

### Example workflow

<Provide representative input or user actions and the observable expected result.>

### Verify behaviour

<Provide test commands with expected results, or reproducible manual validation steps covering the main workflow.>

### Troubleshooting

| Symptom | Likely cause | Resolution |
| --- | --- | --- |
| <Common startup issue> | <Cause> | <Concrete fix> |

## Architecture / project structure

<Insert a directory tree reflecting the actual released repository.>

| Component / source path | Responsibility |
| --- | --- |
| <Actual path> | <Role and relationship to other components> |

Entry point and data flow: <Trace a representative operation through the application.>

Design decisions: <Explain important choices, alternatives and trade-offs.>

## Concepts to identify and discuss

| Concept | Source reference | Discussion prompt |
| --- | --- | --- |
| <Concept> | <Relative link to actual source file or symbol> | <Connect implementation to behaviour or an alternative design> |

## Guided review questions

1. <Comprehension question about a concrete application feature>
2. <Question tracing input, state changes and output through actual components>
3. <Question about an implemented design choice and its trade-offs>
4. <Question evaluating an edge case or alternative approach>

## Extension challenges

The documented release is the working baseline. The following features are learner extensions.

### Challenge 1: <Title>

- Difficulty: <Relative difficulty and expected prior knowledge>
- Objective: <New or improved behaviour>
- Starting points: <Relevant files or components>
- Constraints: <Required boundaries or preserved behaviour>
- Acceptance criteria: <Observable outcomes and how to verify them>

### Challenge 2: <Title — greater difficulty>

- Difficulty: <Relative difficulty and expected prior knowledge>
- Objective: <New or improved behaviour>
- Starting points: <Relevant files or components>
- Constraints: <Required boundaries or preserved behaviour>
- Acceptance criteria: <Observable outcomes and how to verify them>

## Versioning / releases

This project follows [CSC naming and versioning conventions](https://github.com/ConstantinSummer/csc-project-library/blob/main/docs/NAMING_AND_VERSIONING.md), using Semantic Versioning and `v`-prefixed tags.

- Teaching baseline: <Explicit stable version and release link>
- Release notes: [RELEASE_NOTES.md](RELEASE_NOTES.md) — <features, fixes, setup impacts and educational changes; in README.md link to RELEASE_NOTES.el.md instead>
- Compatibility and migration: <Setup, environment, data or lesson changes; state None for the initial baseline if applicable>

Use the documented release for lessons so that code, review questions and instructions match.


## About CSC

Computer Science Center provides structured education in programming, software development, AI and related computing subjects. CSC educational projects are designed to be run, studied, discussed and extended by learners. Learn more at [https://csc.gr](https://csc.gr).

## Author

**Konstantinos Zitis**<br>
Computer Science Educator & Software Developer<br>
Computer Science Center (CSC)<br>
[https://csc.gr](https://csc.gr)

## License

This project is source-available educational material published under the **CSC Educational Use License**, not an OSI-approved open-source license. See the repository's root `LICENSE` file. The license permits personal learning, educational experiments and attributed learner portfolio work; commercial resale, paid redistribution, rebranding and use in third-party educational products require prior written permission from CSC.
