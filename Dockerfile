# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Ensure app is discoverable by adding root to PYTHONPATH
ENV PYTHONPATH=/code

# ✅ Cloud Run-friendly: use PORT env variable
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
