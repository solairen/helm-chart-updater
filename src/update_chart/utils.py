"""
Utility functions for Chart.yaml operations.
"""

from typing import Any, Dict


class ChartUtils:
    """Utility functions for Chart operations."""

    @staticmethod
    def print_chart_info(chart_data: Dict[str, Any], new_version: str) -> None:
        """Print current chart information and new version."""
        print("Current Chart.yaml contents:")
        for key, value in chart_data.items():
            print(f"{key}: {value}")
        print(f"\nNew version to apply: {new_version}")

    @staticmethod
    def print_updated_content(updated_content: str) -> None:
        """Print the updated YAML content."""
        print("\nNew Chart.yaml contents:")
        print(updated_content)

    @staticmethod
    def print_success_message(new_version: str) -> None:
        """Print success message after update."""
        print(
            f"\nSuccessfully updated Chart.yaml in repository "
            f"with version {new_version}"
        )
