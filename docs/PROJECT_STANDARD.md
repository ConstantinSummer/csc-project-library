# CSC Educational Project Standard

Every Computer Science Center (CSC) educational project must be a complete, runnable application that supports source-code study, lesson discussion and extension work. A focused scope is welcome; disconnected exercises do not constitute a library project.

Use the [README template](../templates/PROJECT_README_TEMPLATE.md) and the [naming and versioning conventions](NAMING_AND_VERSIONING.md). Documentation must be in English and identify CSC, [https://csc.gr](https://csc.gr), and maintainer **Konstantinos Zitis**.

## Mandatory documentation

Every project must have a root `README.md` containing the following sections. Longer explanations may live in linked documents, but the README must remain the entry point and contain all essential setup and execution steps.

### 1. Project overview

Describe the application's purpose, intended users, principal features and scope. Declare its primary catalogue area, learning level (Foundation, Intermediate or Advanced), and the release covered by the instructions. Distinguish implemented features from extension ideas.

### 2. Learning objectives

List observable outcomes: what learners should be able to explain, trace, implement or evaluate after completing the project. Relate objectives to actual application features and source files.

### 3. Prerequisites

State required programming knowledge, subject concepts, tools and environment assumptions. Identify any required account, service, hardware or dataset, including access or cost constraints where applicable.

### 4. Technologies used

List languages, runtimes, frameworks, libraries and storage systems, with supported versions and a short explanation of their roles. Keep dependency manifests consistent with the documentation.

### 5. Setup instructions

Provide ordered steps from downloading or cloning a named release through installing dependencies and configuring the application. Include working directories, supported platforms, configuration variables and any database or sample-data preparation. Provide safe example configuration where needed; never include real credentials. Explain how learners can verify that setup succeeded.

### 6. Execution instructions

Give exact commands or platform-specific actions to start the application, a representative input or workflow, and expected output or behaviour. Document how to stop it and any common startup problems. Include test commands or a reproducible manual validation procedure, as appropriate to the application.

### 7. Architecture / project structure

Show the relevant directory tree and explain component responsibilities, the entry point, data flow and external dependencies. Explain significant design choices and their trade-offs, at a depth appropriate to the learning level.

### 8. Concepts to identify and discuss

Identify the concepts demonstrated by the implementation and point to concrete source files, symbols or execution paths. Ask learners to connect the code to its behaviour and discuss reasonable alternatives.

### 9. Guided review questions

Provide project-specific questions that progress from comprehension and execution tracing to design reasoning and evaluation. Questions must be answerable through the implementation, application behaviour and lesson discussion.

### 10. Extension challenges

Provide meaningful extensions to the working application, ordered by difficulty. For each challenge, state the objective, constraints, relevant starting points and observable acceptance criteria. Keep the baseline application usable without completing challenges; avoid presenting unimplemented extensions as existing features.

### 11. Versioning / releases

Use Semantic Versioning with `v`-prefixed Git tags, starting at `v1.0.0` for the first complete teaching baseline. Link the documented release and its release notes. Describe changes to features, setup, prerequisites and educational material, including migration steps when necessary. Keep lessons tied to an explicit release so learners can reproduce the same baseline.

## Release and catalogue readiness

Before a project is listed as **Available**:

- Verify setup and execution from a clean checkout of the intended release on the documented environment.
- Check the supplied example workflow and automated tests or documented manual checks.
- Review all mandatory sections for accuracy and replace template placeholders.
- Verify that review questions and extension challenges refer to the released implementation.
- Publish a tagged release with concise release notes and working links.
- Add the project to the appropriate catalogue area with its repository, primary learning level, focus and release.

Planned entries must remain clearly labelled **Planned** and must not imply that runnable applications or releases already exist.
