# Minimal container to run FastAPI + Manim
FROM python:3.11-slim

# System deps for manim (Cairo-based) + ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \ 
    ffmpeg     libcairo2     libpango-1.0-0     libpangocairo-1.0-0     libgdk-pixbuf2.0-0     && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY backend /app

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
