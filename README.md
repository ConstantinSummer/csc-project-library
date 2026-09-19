# CSC Educational Project Library

The official educational project library of **Computer Science Center (CSC)**, connected to [https://csc.gr](https://csc.gr).

This repository is the central catalogue and standards repository for complete educational software projects used with advanced learners. Projects are runnable applications with a coherent purpose, documented design and extension opportunities, rather than isolated exercises. Each application will live in its own repository; this repository contains the catalogue, shared standards and reusable documentation template.

## How learners use the library

1. Download or clone a project at its documented release and follow the setup instructions.
2. Run the application and explore its expected behaviour with the supplied examples.
3. Study the source code, tracing how the application implements its features.
4. Discuss architecture, concepts, trade-offs and guided review questions during lessons.
5. Complete extension challenges, verify the resulting behaviour and explain the design decisions made.

## Planned areas

All areas are currently **Planned**; no application is published in this catalogue yet.

- Java
- Python
- Data Structures & Algorithms
- Dart
- Flutter
- Web
- Databases
- AI

See the [project catalogue](catalog/README.md) for project status, learning levels and release links as projects become available.

## Learning levels

Levels describe the demands of a project within its subject area, not a learner's overall ability. Even Foundation projects are complete applications.

| Level | Expected starting point | Learning emphasis |
| --- | --- | --- |
| Foundation | Basic syntax, control flow and simple functions in the relevant language | Follow a small application, understand its structure and make guided changes. |
| Intermediate | Confidence reading and modifying small applications | Connect multiple components, apply abstractions and validate behaviour. |
| Advanced | Experience with modular applications and the stated subject prerequisites | Evaluate architecture and trade-offs, investigate constraints and implement substantial extensions independently. |

Each project must declare one primary level and concrete prerequisites.

## Repository naming

Application repositories use `csc-<technology>-<project-name>`, with lowercase words separated by hyphens. The technology identifies the primary area; the project name describes the application. This central repository retains the name `csc-project-library`.

See [naming and versioning](docs/NAMING_AND_VERSIONING.md) for technology identifiers, folder and branch names, release rules and commit conventions.

## Documentation and standards

- [Project standard](docs/PROJECT_STANDARD.md): mandatory educational content and readiness criteria.
- [Naming and versioning](docs/NAMING_AND_VERSIONING.md): consistent repository and development conventions.
- [Project README template](templates/PROJECT_README_TEMPLATE.md): starting point for future project documentation.

Before adding an application to the catalogue as Available, verify that its documentation follows the standard and that its linked release can be set up and run using the documented instructions.

## Maintainer

**Konstantinos Zitis** — Computer Science Center (CSC)

Education website: [https://csc.gr](https://csc.gr)
