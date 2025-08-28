# Purpose: A thin wrapper around the Cookiecutter library.
# Key Decision: Abstracting the specific templating library (Cookiecutter)
# behind our own `TemplateEngine` class is a smart architectural choice. If we
# ever wanted to switch to a different engine (like Copier), we would only
# need to change this one file, not the entire application.
# ------------------------------------------------------------------------------
import sys
from pathlib import Path
from typing import Dict, Any, cast

# Third-party imports
from cookiecutter.main import cookiecutter  # type: ignore[import]
from cookiecutter.exceptions import RepositoryNotFound  # type: ignore[import]

class TemplateNotFoundException(Exception):
    """Custom exception for when a template directory is not found."""
    pass

class TemplateEngine:
    """A wrapper around Cookiecutter to generate projects from templates."""

    def __init__(self) -> None:
        # Key Decision: Using `importlib.resources` or `pathlib` to locate the
        # templates directory ensures that it works correctly even when the
        # package is installed (e.g., via pip), not just when running from source.
        # For simplicity in this standalone version, we use `pathlib`.
        # When integrating with Phoenix, `importlib.resources` is more robust.
        
        # This assumes the templates are located relative to this file.
        # This path is: src/phoenix_starter_kits/generators/ -> src/phoenix_starter_kits/ -> src/ -> root
        self.templates_dir = Path(__file__).parent.parent / "templates"

    def generate(self, template_name: str, context: Dict[str, Any], output_dir: str) -> str:
        """
        Generates a project from a template using Cookiecutter.

        Args:
            template_name: The name of the template subdirectory.
            context: A dictionary of variables to inject into the template.
            output_dir: The directory to generate the project in.

        Returns:
            The path to the generated project.
        """
        template_path = self.templates_dir / template_name
        if not template_path.exists():
            raise TemplateNotFoundException(f"Template '{template_name}' not found at {template_path}")

        try:
            # Key Decision: `no_input=True` is crucial for a non-interactive CLI.
            # We provide all the necessary variables via `extra_context`.
            # We cast the path to a string as Cookiecutter expects a string path.
            result_path = cookiecutter(
                template=str(template_path),
                extra_context=context,
                output_dir=output_dir,
                no_input=True,
            )
            # The return type of cookiecutter is `str`, which we know is correct.
            return cast(str, result_path)
        except RepositoryNotFound as e:
            # This is a more user-friendly error than a generic traceback.
            print(f"Error finding template repository: {e}", file=sys.stderr)
            raise
        except Exception as e:
            print(f"An error occurred during project generation: {e}", file=sys.stderr)
            raise