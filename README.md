This repository contains the proof-of-concept for `phoenix-starter-kits`, a standalone CLI tool to generate template-driven LLM applications with Arize Phoenix observability built-in.

## Objective

The goal is to drastically reduce the "Time-to-First-Trace" for new Phoenix users by providing production-ready starter projects for common AI/ML use cases.

## Quick Start

1.  **Install and generate project:**
    ```bash
    git clone https://github.com/minhkhoango/phoenix-starter-kits.git
    cd phoenix-starter-kits
    python -m venv .venv && source .venv/bin/activate
    pip install -e .
    mkdir my-new-app && cd my-new-app
    phoenix-starter-kits init
    ```

2.  **Set up project:**
    ```bash
    cd your-project-name
    echo "OPENAI_API_KEY=your_api_key_here" > .env
    pip install -r requirements.txt
    ```

3.  **Start Phoenix and run app:**
    ```bash
    # Terminal 1: Start Phoenix
    pkill -f "phoenix serve" || true
    phoenix serve
    
    # Terminal 2: Run your app
    python main.py
    ```
    View traces at `http://127.0.0.1:6006`

## Architecture

-   **CLI:** Built with `click` for robust and extensible command-line interfaces.
-   **Templating:** Uses `cookiecutter` to generate projects from a set of predefined templates.
-   **Standalone:** Designed as a separate package for easy testing, but architected for simple integration into the main `arize-phoenix` CLI in the future.

## Troubleshooting

- **Connection refused:** Ensure Phoenix is running (`phoenix serve`) before running your app
- **Startup failed:** Kill existing processes with `pkill -f "phoenix serve"`
- **API key errors:** Check `.env` file contains valid `OPENAI_API_KEY`
- **Import errors:** Run `pip install -r requirements.txt`
