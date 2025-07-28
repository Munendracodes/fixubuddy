FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Recommended port exposure
EXPOSE 8080

ENV PORT=8080
ENV HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Proper CMD with var expansion and good signal handling
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080"]
