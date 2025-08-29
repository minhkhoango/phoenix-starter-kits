# Purpose: Implements the `init` command logic.
# This file is responsible for handling user input via Click options and
# orchestrating the project generation process.
# ------------------------------------------------------------------------------
import os
import click
from typing import List
from phoenix_starter_kits.generators.project_generator import ProjectGenerator # type: ignore[stub]
from phoenix_starter_kits.generators.template_engine import TemplateNotFoundException # type: ignore[stub]

# --- Constants for available templates ---
# Key Decision: Added 'llamaindex-qa' to the list of available templates.
# This list is now the single source of truth for the CLI.
AVAILABLE_TEMPLATES: List[str] = ["langchain-rag", "llamaindex-qa"]

@click.command("init")
@click.option(
    "--template",
    "template_name",
    type=click.Choice(AVAILABLE_TEMPLATES, case_sensitive=False),
    prompt="Select a template",
    help="The project template to use for initialization.",
)
@click.option(
    "--project-name",
    prompt="Project name",
    help="The name of the new LLM application.",
)
@click.argument(
    "destination",
    type=click.Path(file_okay=False, dir_okay=True, writable=True, resolve_path=True),
    default=".",
)
def init_command(template_name: str, project_name: str, destination: str) -> None:
    """
    Initialize a new LLM application with Phoenix observability.
    """
    # Key Decision: The command layer is responsible for UX (prompts, feedback),
    # while the generator layer handles the core file creation logic. This
    # separation of concerns makes the codebase cleaner.
    click.secho(f"Initializing '{project_name}' using the '{template_name}' template...", fg="cyan")

    # UX Check: For the MVP, we enforce generation in an empty directory to
    # prevent accidental file overwrites. This is a critical safety feature.
    if os.path.exists(destination) and os.listdir(destination):
        # We check if the destination is the current directory or a subdirectory
        target_dir_name = os.path.basename(destination)
        if target_dir_name == ".":
            target_dir_name = "the current directory"
        
        click.secho(f"Error: {target_dir_name} is not empty.", fg="red")
        click.echo("Please run this command in a new or empty directory.")
        raise click.Abort()

    generator = ProjectGenerator()

    try:
        project_path = generator.create_project(
            template_name=template_name,
            project_name=project_name,
            destination=destination,
        )
        click.secho("\nSuccess! Your project has been created at:", fg="green")
        click.echo(project_path)
        click.secho("\nNext steps:", fg="yellow")
        click.echo(f"1. cd {os.path.basename(project_path)}")
        click.echo("2. Set your OPENAI_API_KEY in the .env file")
        click.echo("3. pip install -r requirements.txt")
        click.echo("4. python main.py")

    except TemplateNotFoundException as e:
        click.secho(f"Error: {e}", fg="red")
        raise click.Abort()
    except Exception as e:
        click.secho(f"An unexpected error occurred: {e}", fg="red")
        raise click.Abort()
