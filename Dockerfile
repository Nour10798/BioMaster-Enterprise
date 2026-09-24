# Use official Python lightweight image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies safely
RUN pip install --no-cache-dir -r requirements.txt

# Copy all models, data, and the FastAPI app into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the REST API server when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
