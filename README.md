# Helm Chart Updater

A GitHub Action for automatically updating version information in Helm Chart.yaml files.

## Overview

This action simplifies the process of updating version numbers in Helm chart files during your CI/CD workflow. It automatically updates both the `version` and `appVersion` fields in your `Chart.yaml` file with a single command.

## Features

- Updates both `version` and `appVersion` fields
- Preserves the original file structure
- Provides detailed logging of changes
- Customizable commit messages
- Flexible path configuration

## Usage

Add the following step to your GitHub workflow:

```yaml
- name: Update Helm Chart version
  uses: solairen/helm-chart-updater@main
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
    new_version: '1.2.3'
    # Optional parameters
    chart_path: 'path/to/Chart.yaml'
    commit_message: 'Update chart version to 1.2.3'
```

### Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `token` | GitHub token for repository access | Yes | N/A |
| `new_version` | The new version to set in Chart.yaml | Yes | N/A |
| `chart_path` | Path to the Chart.yaml file | No | `Chart.yaml` |
| `commit_message` | Custom commit message | No | `Update Chart.yaml version to [new_version]` |
| `dependencies`   | Add dependencies to Chart.yaml | No | N/A |

## Example Workflow

```yaml
name: Update Helm Chart

on:
  release:
    types: [published]

jobs:
  update-chart:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Update Helm Chart version
        uses: solairen/helm-chart-updater@main
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          new_version: ${{ github.event.release.tag_name }}
```

## How It Works

1. The action uses the provided GitHub token to authenticate with your repository
2. It fetches the existing Chart.yaml file from the specified path
3. The version fields are updated with the new version number
4. The updated file is committed back to the repository

## Development

### Prerequisites

- Python 3.x
- Docker (for testing the action locally)

### Local Development

Use the provided development container for a consistent development environment:

```bash
# Clone the repository
git clone https://github.com/solairen/helm-chart-updater.git
cd helm-chart-updater

# Use VS Code with Dev Containers extension
# or run the development container directly
docker build -t helm-chart-updater-dev -f docker/Dockerfile-dev .
docker run -it -v $(pwd):/development helm-chart-updater-dev
```

### Testing

Test the action locally by setting the required environment variables:

```bash
export INPUT_TOKEN="your-github-token"
export INPUT_NEW_VERSION="1.0.0"
export GITHUB_EVENT_PATH="owner/repo"
python update_chart.py
```

## Contributing

Contributions are welcome! See CONTRIBUTING.md for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Code of Conduct

Please review our Code of Conduct before contributing to this project.

## Acknowledgments

Thank you to all contributors who have helped with this project.

## Support

If you find this project helpful, consider [buying me a coffee](https://www.buymeacoffee.com/solairen).
