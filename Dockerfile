# Dockerfile

# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Cloud Run default port
EXPOSE 8080

# Run FastAPI app using Uvicorn on required port
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
