"""
GitHub repository operations for Chart.yaml files.
"""

import base64
import sys
from typing import Dict, Any, Tuple
from github import Github
from github.ContentFile import ContentFile

from .yaml_processor import YamlProcessor


class GitHubRepository:
    """Handles GitHub repository operations."""

    def __init__(self, token: str, repo_path: str):
        """Initialize GitHub repository connection."""
        self.github = Github(token)
        self.repo = self.github.get_repo(repo_path)
        self.repo_path = repo_path

    def get_chart_content(self, chart_file_path: str) -> Tuple[ContentFile, Dict[str, Any]]:
        """Fetch and decode Chart.yaml content from repository."""
        try:
            content = self.repo.get_contents(chart_file_path)
            file_content = base64.b64decode(content.content).decode('utf-8')
            chart_data = YamlProcessor.parse_chart_data(file_content)
            return content, chart_data
        except Exception as e:
            print(f"Chart.yaml not found at path '{chart_file_path}' in repository '{self.repo_path}': {e}")
            sys.exit(1)

    def update_chart_file(
        self,
        content: ContentFile,
        commit_message: str,
        updated_content: str
    ) -> None:
        """Update Chart.yaml file in the repository."""
        try:
            self.repo.update_file(
                content.path,
                commit_message,
                updated_content,
                content.sha
            )
        except Exception as e:
            print(f"Error updating Chart.yaml: {e}")
            sys.exit(1)
