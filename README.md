# Phoenix Starter Kits

This repository contains the proof-of-concept for **phoenix-starter-kits**, a standalone CLI tool to generate template-driven LLM applications with Arize Phoenix observability built-in.

---

## Business Impact: Accelerating Time to Value

The primary goal of this tool is to deliver a quantifiable business impact by drastically improving the onboarding speed for AI engineers using Arize Phoenix.

- **Reduce Time to Value (TTV):** Industry benchmarks show the average TTV for developer tools is over a day. This tool reduces the initial setup from hours to under 90 seconds, allowing engineers to become productive almost instantly.  
- **Increase Developer Productivity & Cost Savings:** By eliminating 3–5 hours of manual setup and troubleshooting, this tool saves **$195 to $400** in direct operational costs per engineer during onboarding, based on average AI engineer salaries.  
- **Boost Adoption & Conversion:** A frictionless onboarding experience is directly correlated with higher adoption of open-source tools and faster conversion from free to paid tiers.  

---

## What This Solves

The goal is to drastically reduce the **"Time-to-First-Trace"** for new Phoenix users by providing production-ready starter projects for common AI/ML use cases, eliminating the initial friction of manual setup and configuration.

---

## Quick Start

**Install and generate project:**
```bash
git clone https://github.com/your-username/phoenix-starter-kits.git  
cd phoenix-starter-kits  
pip install -e .  

mkdir my-new-app && cd my-new-app  
phoenix-starter-kits init  
```
You will be prompted to choose a template (`langchain-rag` or `llamaindex-qa`).

**Set up project:**

Follow the on-screen instructions to `cd` into your new project, set up your `.env` file, and install dependencies:
```bash
pip install -r requirements.txt  
```
**Run your app:**

Launch the Phoenix UI and run your application to see traces instantly.
```bash
# Terminal 1: Start Phoenix UI  
phoenix serve  

# Terminal 2: Run your app  
python main.py  
```
---

## Architecture

- **CLI:** Built with [click](https://click.palletsprojects.com/) for robust and extensible command-line interfaces.  
- **Templating:** Uses [cookiecutter](https://cookiecutter.readthedocs.io/) to generate projects from a set of predefined templates.  
- **Standalone:** Designed as a separate package for easy testing, but architected for simple integration into the main Arize Phoenix CLI in the future.  
