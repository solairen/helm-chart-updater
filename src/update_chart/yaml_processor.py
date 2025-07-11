"""
YAML processing utilities for Chart.yaml files.
"""

import yaml
from typing import Dict, Any, List
from collections import OrderedDict
import sys


class IndentedDumper(yaml.SafeDumper):
    """Custom YAML dumper with proper indentation settings."""

    def increase_indent(self, flow=False, indentless=False):
        return super(IndentedDumper, self).increase_indent(flow, False)


def represent_list(dumper, data):
    """Custom YAML representer for proper list indentation."""
    return dumper.represent_list(data)


def represent_ordereddict(dumper, data):
    """Custom YAML representer for OrderedDict."""
    return dumper.represent_dict(data.items())


# Register the custom representers
yaml.add_representer(OrderedDict, represent_ordereddict)
yaml.add_representer(list, represent_list)


class YamlProcessor:
    """Handles YAML processing operations for Chart.yaml files."""

    @staticmethod
    def parse_dependencies(dependencies_input: str) -> List[Dict[str, Any]]:
        """Parse dependencies from YAML string input."""
        dependencies = []
        if dependencies_input.strip():
            try:
                dependencies = yaml.safe_load(dependencies_input)
                if not isinstance(dependencies, list):
                    raise ValueError(f"Dependencies must be a list, got: {type(dependencies)}")
                    
            except yaml.YAMLError as e:
                raise yaml.YAMLError(f"Invalid YAML format for dependencies: {e}")
                
        return dependencies

    @staticmethod
    def parse_chart_data(file_content: str) -> Dict[str, Any]:
        """Parse Chart.yaml content from string."""
        try:
            return yaml.safe_load(file_content)
        except yaml.YAMLError as e:
            print(f"Error: Invalid YAML format in Chart.yaml: {e}")
            sys.exit(1)

    @staticmethod
    def create_ordered_chart_data(
        chart_data: Dict[str, Any],
        new_version: str,
        dependencies: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Create ordered chart data with proper field ordering."""
        ordered_chart_data = {}

        # Add fields in the desired order
        field_order = ['apiVersion', 'name', 'description', 'type']
        for field in field_order:
            if field in chart_data:
                ordered_chart_data[field] = chart_data[field]

        # Set version fields
        ordered_chart_data['version'] = new_version
        ordered_chart_data['appVersion'] = new_version

        # Set dependencies
        ordered_chart_data['dependencies'] = dependencies if dependencies else chart_data.get('dependencies', [])

        return ordered_chart_data

    @staticmethod
    def generate_yaml_content(ordered_chart_data: Dict[str, Any]) -> str:
        """Generate YAML content with proper formatting."""
        return yaml.dump(
            ordered_chart_data,
            Dumper=IndentedDumper,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            indent=2
        )
