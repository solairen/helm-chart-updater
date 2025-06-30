"""
Environment variable configuration and validation.
"""

import os
from typing import Dict, Optional


class Config:
    """Configuration class for environment variables."""

    def __init__(self):
        self.repo_path = os.environ.get("GITHUB_REPOSITORY")
        self.token = os.environ.get("INPUT_TOKEN")
        self.chart_file_path = os.environ.get("INPUT_CHART_PATH", "Chart.yaml")
        self.new_version = os.environ.get("INPUT_NEW_VERSION")
        self.commit_message = os.environ.get("INPUT_COMMIT_MESSAGE")
        self.dependencies_input = os.environ.get("INPUT_DEPENDENCIES", "")

    def get_commit_message(self) -> str:
        """Get commit message with default fallback."""
        return self.commit_message or f"Update Chart.yaml version to {self.new_version}"

    def validate(self) -> None:
        """Validate required environment variables."""
        required_vars = {
            'GITHUB_REPOSITORY': self.repo_path,
            'INPUT_TOKEN': self.token,
            'INPUT_NEW_VERSION': self.new_version
        }

        missing_vars = [var_name for var_name, value in required_vars.items() if not value]

        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

    def to_dict(self) -> Dict[str, Optional[str]]:
        """Convert config to dictionary format."""
        return {
            'repo_path': self.repo_path,
            'token': self.token,
            'chart_file_path': self.chart_file_path,
            'new_version': self.new_version,
            'commit_message': self.commit_message,
            'dependencies_input': self.dependencies_input
        }
