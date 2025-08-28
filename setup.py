# Decision: Including a basic setup.py for maximum compatibility with older
# tooling and editable installs (`pip install -e .`), even though pyproject.toml
# is the modern standard.
# ------------------------------------------------------------------------------
from setuptools import setup

if __name__ == "__main__":
    setup()