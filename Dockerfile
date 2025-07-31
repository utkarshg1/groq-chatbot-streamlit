FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync

# Make sure we use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "app.py"]
