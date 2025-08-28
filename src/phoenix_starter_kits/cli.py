import click
from phoenix_starter_kits.commands.init import init_command # type: ignore[stub]

@click.group()
@click.version_option(package_name="phoenix-starter-kits")
def main() -> None:
    """
    Phoenix Starter Kits: Template-driven initialization for LLM applications
    with built-in observability using Arize Phoenix.
    """
    pass

# Key Decision: Registering the `init` command with the main CLI group.
# This modular approach allows for adding more commands (e.g., `list-templates`)
# in the future without cluttering the main entry point.
main.add_command(init_command)

if __name__ == "__main__":
    main()