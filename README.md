This repository contains the proof-of-concept for `phoenix-starter-kits`, a standalone CLI tool to generate template-driven LLM applications with Arize Phoenix observability built-in.

## Objective

The goal is to drastically reduce the "Time-to-First-Trace" for new Phoenix users by providing production-ready starter projects for common AI/ML use cases.

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone <repo_url>
    cd phoenix-starter-kits
    ```

2.  **Install in editable mode:**
    This makes the `phoenix-starter-kits` command available in your shell.
    ```bash
    pip install -e .
    ```

3.  **Run the generator:**
    Create a new, empty directory for your project and run the command from there.
    ```bash
    mkdir my-new-app
    cd my-new-app
    phoenix-starter-kits init
    ```

    Follow the prompts to select a template and name your project.

## Architecture

-   **CLI:** Built with `click` for robust and extensible command-line interfaces.
-   **Templating:** Uses `cookiecutter` to generate projects from a set of predefined templates.
-   **Standalone:** Designed as a separate package for easy testing, but architected for simple integration into the main `arize-phoenix` CLI in the future.
