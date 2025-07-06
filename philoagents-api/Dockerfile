# FROM python:3.11-slim

# # Install uv.
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# # Set the working directory.
# WORKDIR /app

# # Install the application dependencies.
# COPY uv.lock pyproject.toml README.md ./
# RUN uv sync --frozen --no-cache

# # Copy the application into the container.
# COPY src/philoagents philoagents/
# COPY tools tools/

# CMD ["/app/.venv/bin/fastapi", "run", "philoagents/infrastructure/api.py", "--port", "8000", "--host", "0.0.0.0"]
# FROM python:3.11-slim

# # Install uv (dependency manager)
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# # Set workdir
# WORKDIR /app

# # Install app dependencies
# COPY uv.lock pyproject.toml README.md ./
# RUN uv sync --frozen --no-cache

# # Copy the application code (for prod only — overridden in dev with volumes)
# COPY src/philoagents philoagents/
# COPY tools tools/

# # Default to production command
# CMD ["uvicorn", "philoagents.infrastructure.api:app", "--host", "0.0.0.0", "--port", "8000"]
# FROM python:3.11-slim

# # Install uv (dependency manager)
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# WORKDIR /app

# COPY uv.lock pyproject.toml README.md ./
# RUN uv sync --frozen --no-cache

# COPY src/philoagents philoagents/
# COPY tools tools/

# # 🔍 Debug: list files to verify COPY worked
# RUN echo "🧾 Directory structure:" && ls -R /app

# # ✅ Final CMD
# CMD ["uvicorn", "philoagents.infrastructure.api:app", "--host", "0.0.0.0", "--port", "8000"]


FROM python:3.11-slim

# Install uv (dependency manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install dependencies
COPY uv.lock pyproject.toml README.md ./
RUN uv sync --frozen --no-cache

# Copy code
COPY src/philoagents philoagents/
COPY tools tools/

# ✅ Ensure Python can find 'philoagents' as a module
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "philoagents.infrastructure.api:app", "--host", "0.0.0.0", "--port", "8000"]

# FROM python:3.11-slim

# # Install uv (Python dependency manager)
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# WORKDIR /app

# # Install dependencies
# COPY uv.lock pyproject.toml README.md ./
# RUN uv sync --frozen --no-cache

# # Copy code
# COPY src/philoagents philoagents/
# COPY tools tools/

# # Ensure app can find code as a module
# ENV PYTHONPATH=/app

# # Port for FastAPI app
# EXPOSE 8000

# # Healthcheck (pings app endpoint)
# HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
#   CMD curl --fail http://localhost:8000/health || exit 1

# # Start the API
# CMD [".venv/bin/uvicorn", "philoagents.infrastructure.api:app", "--host", "0.0.0.0", "--port", "8000"]
