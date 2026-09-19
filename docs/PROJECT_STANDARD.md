# CSC Educational Project Standard

Every Computer Science Center (CSC) educational project must be a complete, runnable application that supports source-code study, lesson discussion and extension work. A focused scope is welcome; disconnected exercises do not constitute a library project.

Use the [README template](../templates/PROJECT_README_TEMPLATE.md) and the [naming and versioning conventions](NAMING_AND_VERSIONING.md). Every project must provide complete Greek and English README documentation and identify CSC, [https://csc.gr](https://csc.gr), and maintainer **Konstantinos Zitis** in both versions.

## Bilingual documentation and technical language

Every CSC educational project repository must contain two complete, equivalent entry-point documents:

- `README.md` is the primary Greek version for CSC learners.
- `README.en.md` is the complete English version for international readers.

Both files must contain a prominent language switch at the top linking directly to the other version. They must document the same released application, features, learning objectives, prerequisites, setup, execution workflow, architecture, review questions, extension challenges, versioning, attribution, licensing and CSC information. When either version changes, review and update the other in the same change so that neither becomes incomplete or stale.

Translate explanatory prose for its target audience, but keep source-code identifiers, filenames, paths, package names, commands, configuration keys, APIs and established technical conventions in English. Architecture diagrams may use English technical terms in both versions when this improves precision and consistency with the code. Both READMEs must retain the required branding and attribution for **Konstantinos Zitis**, **Computer Science Center (CSC)** and [https://csc.gr](https://csc.gr).

## Ownership, licensing and attribution

Every CSC educational repository must contain a root `LICENSE` file titled **CSC Educational Use License**. CSC projects are source-available educational material, not OSI-approved open-source software. Do not substitute MIT, Apache, GPL or another standard open-source license unless CSC explicitly changes the policy for that repository.

The license must permit viewing, downloading, executing and modifying the source for personal learning and educational study, including personal derivative work for study and portfolio use. It must require retained attribution to **Konstantinos Zitis**, **Computer Science Center (CSC)** and [https://csc.gr](https://csc.gr), reserve copyright to Konstantinos Zitis / CSC, prohibit commercial resale, paid redistribution, rebranding, republication as another training product or course, and incorporation into a commercial educational product without prior written permission, include a no-warranty statement, and direct commercial or institutional licensing enquiries to [https://csc.gr](https://csc.gr).

Both project READMEs must contain dedicated `Author`, `License` and `About CSC` sections, translated appropriately for their target language. The restrained author attribution must identify:

- **Konstantinos Zitis**
- **Computer Science Educator / Software Developer**
- **Computer Science Center (CSC)**
- [https://csc.gr](https://csc.gr)

The `License` section must link to the repository's root `LICENSE`. The `About CSC` section must use two or three sentences explaining that CSC provides structured education in programming, software development, AI and related computing subjects, with a link to [https://csc.gr](https://csc.gr). Branding must remain professional and informative rather than repetitive or promotional, and every repository must retain a clear educational character.

## Project presentation standard

Treat every CSC project as both educational material and a technically credible public portfolio. Where relevant to the application, each repository should provide:

- a polished README that explains what the application does, what learners can learn, who created it, its CSC ownership and where to find related learning material;
- examples captured from real executions;
- real application screenshots when they add explanatory value;
- an architecture diagram, preferably Mermaid so it renders natively in GitHub;
- accurate GitHub topics;
- tagged stable releases with release notes; and
- a link to the corresponding lesson or subject area on [https://csc.gr](https://csc.gr).

Never create fake or mock screenshots and present them as real application output. For web applications, automated browser or headless tooling may capture real screenshots when technically practical. For console applications, prefer clean terminal transcripts and add a screenshot only when it provides genuine value. Use SVG or PNG for architecture diagrams only when Mermaid is unsuitable.

## Discoverability and repository metadata

Repository titles, descriptions and README introductions must make sense to learners and developers who have not previously visited CSC. A visitor should quickly understand what the application does, what it teaches, who created it, that it belongs to CSC, and where to find more lessons. GitHub repository descriptions must be concise and optimized for international discoverability, using clear internationally understood technical language; add Greek context only when the platform limit permits it without reducing clarity. Public application repositories should use accurate, English-language GitHub topics such as `education`, `computer-science`, `programming`, `learning`, `csc`, the primary technology, and a small number of project-specific concepts. Technical quality and educational value always take precedence over marketing; do not add irrelevant or promotional topics merely to increase reach.

## Mandatory documentation

Every project must have a root `README.md` in Greek and a root `README.en.md` in English, each containing the following sections and a prominent link to the other language at the top. Longer explanations may live in linked documents, but both READMEs must remain complete entry points and contain all essential setup and execution steps.

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

### 12. Author, License and About CSC

Include the required author attribution, summarize the CSC Educational Use License with a link to the root `LICENSE`, and include the standard `About CSC` section.

## Release and catalogue readiness

Before a project is listed as **Available**:

- Verify setup and execution from a clean checkout of the intended release on the documented environment.
- Check the supplied example workflow and automated tests or documented manual checks.
- Review all mandatory sections for accuracy and replace template placeholders.
- Verify that `README.md` and `README.en.md` are complete, mutually linked at the top and aligned with the same released application.
- Verify that technical identifiers and conventions remain in English and that repository descriptions and topics support international discoverability.
- Verify that the custom `LICENSE`, attribution block, licensing summary and `About CSC` section are present and consistent.
- Verify that the repository description and topics are accurate and useful for discoverability.
- Verify that screenshots presented as application output came from a real execution and that presentation materials accurately describe the release.
- Verify that review questions and extension challenges refer to the released implementation.
- Publish a tagged release with concise release notes and working links.
- Add the project to the appropriate catalogue area with its repository, primary learning level, focus and release.

Planned entries must remain clearly labelled **Planned** and must not imply that runnable applications or releases already exist.
