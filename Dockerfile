FROM python:3.13-slim

LABEL authors="Buddhima Zoysa"

WORKDIR /app

# Copy UV binaries from the official UV image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Some uv/container tweaks
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13

# Copy pyproject and lock file first for better caching
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --locked --no-dev

# Copy source code
COPY . .

# Expose the application port. (If you need to use a different port, change it here and in entrypoint.sh)
EXPOSE 8000

# Use entrypoint script to start the application
ENTRYPOINT ["./entrypoint.sh"]
