# Use a slim Python image
FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock uv.toml ./

# Install dependencies using uv
# --frozen: ensures uv.lock is not updated
# --no-cache: reduces image size
RUN uv sync --frozen --no-cache --no-install-project

# Copy the rest of the application
COPY . .

# Expose the port Cloud Run expects
EXPOSE 8080

# Environment variables for Cloud Run
ENV PORT=8080
ENV HOST=0.0.0.0

# Command to run the application
# We use 'uv run' to ensure the environment is correctly set up
CMD ["uv", "run", "python", "main.py"]
