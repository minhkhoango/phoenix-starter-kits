This repository contains the proof-of-concept for `phoenix-starter-kits`, a standalone CLI tool to generate template-driven LLM applications with Arize Phoenix observability built-in.

## Objective

The goal is to drastically reduce the "Time-to-First-Trace" for new Phoenix users by providing production-ready starter projects for common AI/ML use cases.

## Quick Start

1.  **Clone and install:**
    ```bash
    git clone https://github.com/minhkhoango/phoenix-starter-kits.git
    cd phoenix-starter-kits
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -e .
    ```

2.  **Generate a project:**
    ```bash
    mkdir my-new-app && cd my-new-app
    phoenix-starter-kits init
    ```

3.  **Set up and run your project:**
    ```bash
    cd your-project-name  # Replace with actual project name
    echo "OPENAI_API_KEY=your_api_key_here" > .env  # Get key from OpenAI platform
    pip install -r requirements.txt
    phoenix serve &  # Start Phoenix in background
    python main.py   # Run your application
    ```

4.  **View traces:** Open `http://127.0.0.1:6006` in your browser

## Architecture

-   **CLI:** Built with `click` for robust and extensible command-line interfaces.
-   **Templating:** Uses `cookiecutter` to generate projects from a set of predefined templates.
-   **Standalone:** Designed as a separate package for easy testing, but architected for simple integration into the main `arize-phoenix` CLI in the future.

## Troubleshooting

- **Connection refused errors:** Ensure Phoenix is running (`phoenix serve`)
- **API key errors:** Check your `.env` file contains valid `OPENAI_API_KEY`
- **Import errors:** Run `pip install -r requirements.txt`
