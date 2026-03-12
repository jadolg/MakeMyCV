FROM python:3.14-slim

# Install system dependencies for WeasyPrint
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    shared-mime-info \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group
RUN useradd -m -r -s /bin/bash appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure the non-root user owns the app directory so it can create the static/ folder at runtime
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
