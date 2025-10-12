# Use a smaller base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for PostgreSQL, MySQL, etc.)
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app using Gunicorn in production
# (If your app factory is create_app() in app.py)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
