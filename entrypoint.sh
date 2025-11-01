#!/bin/sh
set -e
exec uv run --locked uvicorn agent:app --host 0.0.0.0 --port 8000
