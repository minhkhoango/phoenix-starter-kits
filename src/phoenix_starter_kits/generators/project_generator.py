from typing import Dict, Any
from .template_engine import TemplateEngine

class ProjectGenerator:
    """Prepares context and generates a project from a template."""

    def __init__(self) -> None:
        self._engine = TemplateEngine()

    def create_project(
        self,
        template_name: str,
        project_name: str,
        destination: str,
    ) -> str:
        """
        Generates a project directory from a specified template.

        Args:
            template_name: The name of the template to use.
            project_name: The desired name for the new project.
            destination: The directory where the project will be created.

        Returns:
            The absolute path to the newly created project directory.
        """
        # Key Decision: Creating a `project_slug` is a common best practice
        # for project generators. It ensures the directory and package names
        # are valid Python identifiers.
        project_slug = project_name.lower().replace(" ", "_").replace("-", "_")

        context: Dict[str, Any] = {
            "project_name": project_name,
            "project_slug": project_slug,
            # Add other variables like phoenix_endpoint here in the future
        }

        # The engine handles the actual file I/O, this class just sets it up.
        generated_path = self._engine.generate(
            template_name=template_name,
            context=context,
            output_dir=destination,
        )
        return generated_path