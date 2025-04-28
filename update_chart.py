#!/usr/bin/env python3

import sys
import yaml
import base64
from github import Github
from collections import OrderedDict
import os

# Environment variables
repo_path = os.environ.get("GITHUB_REPOSITORY")
token = os.environ.get("INPUT_TOKEN")
chart_file_path = (
    os.environ.get("INPUT_CHART_PATH")
    or "Chart.yaml")
new_version = os.environ.get("INPUT_NEW_VERSION")
commit_message = (
    os.environ.get("INPUT_COMMIT_MESSAGE")
    or f"Update Chart.yaml version to {new_version}")

try:
    # Initialize GitHub connection with token
    g = Github(token)

    # Get repository
    repo = g.get_repo(repo_path)

    # Get Chart.yaml content
    try:
        content = repo.get_contents(chart_file_path)
    except Exception as e:
        print(f"Chart.yaml not found at path '{chart_file_path}' in repository '{repo_path}': {e}")
        sys.exit(1)

    # Decode and parse YAML
    file_content = base64.b64decode(content.content).decode('utf-8')
    chart_data = yaml.safe_load(file_content)

    # Print the parsed data
    print("Current Chart.yaml contents:")
    for key, value in chart_data.items():
        print(f"{key}: {value}")

    print(f"\nNew version to apply: {new_version}")

    # Create ordered dictionary with desired field order
    ordered_chart_data = OrderedDict()
    ordered_chart_data['apiVersion'] = chart_data.get('apiVersion')
    ordered_chart_data['name'] = chart_data.get('name')
    ordered_chart_data['description'] = chart_data.get('description')
    ordered_chart_data['version'] = new_version
    ordered_chart_data['appVersion'] = new_version
    ordered_chart_data['type'] = chart_data.get('type')

    # Convert back to YAML - keeping string formatting
    updated_content = ""
    for key, value in ordered_chart_data.items():
        updated_content += f"{key}: {value}\n"

    # Print the new content
    print("\nNew Chart.yaml contents:")
    print(updated_content)

    # Update file in repository
    repo.update_file(
        content.path,
        commit_message,
        updated_content,
        content.sha
    )

    print(f"\nSuccessfully updated Chart.yaml in repository with version {new_version}")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)