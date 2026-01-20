"""
Main entry point for the Chart.yaml update tool.
"""

import sys
from typing import NoReturn

from .config import Config
from .github_repository import GitHubRepository
from .utils import ChartUtils
from .yaml_processor import YamlProcessor


def main() -> None:
    """Main function to update Chart.yaml version and dependencies."""
    try:
        # Initialize and validate configuration
        config = Config()
        config.validate()

        # Parse dependencies
        dependencies = YamlProcessor.parse_dependencies(config.dependencies_input)

        # Initialize GitHub repository
        github_repo = GitHubRepository(config.token, config.repo_path)

        # Get Chart.yaml content
        content, chart_data = github_repo.get_chart_content(config.chart_file_path)

        # Print current chart information
        ChartUtils.print_chart_info(chart_data, config.new_version)

        # Create ordered chart data
        ordered_chart_data = YamlProcessor.create_ordered_chart_data(
            chart_data, config.new_version, dependencies
        )

        # Generate updated YAML content
        updated_content = YamlProcessor.generate_yaml_content(ordered_chart_data)

        # Print the updated content
        ChartUtils.print_updated_content(updated_content)

        # Update file in repository
        github_repo.update_chart_file(
            content, config.get_commit_message(), updated_content
        )

        # Print success message
        ChartUtils.print_success_message(config.new_version)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def handle_error(error: Exception) -> NoReturn:
    """Handle errors and exit gracefully."""
    print(f"Error: {error}")
    sys.exit(1)


if __name__ == "__main__":
    main()
