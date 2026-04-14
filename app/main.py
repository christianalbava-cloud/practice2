
"""
Entry point for the application. Runs the CLI interface.
"""

from use_cases.commands import run_application
from infrastructure.file_persistence import FilePersistence

if __name__ == "__main__":
    persistence = FilePersistence()
    run_application(persistence)
