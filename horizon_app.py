"""Entrypoint for hosting this server on Prefect Horizon (horizon_app.py:mcp)."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from kroger_mcp.server import create_server

mcp = create_server()
