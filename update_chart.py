#!/usr/bin/env python3
"""
Entry point script for the Chart.yaml update tool.
This script maintains backward compatibility with the original update_chart.py
"""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from update_chart.main import main  # noqa: E402

if __name__ == "__main__":
    main()
