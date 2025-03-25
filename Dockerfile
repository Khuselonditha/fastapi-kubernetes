# Use official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (for caching layers)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the application port
EXPOSE 8000

# Command to run the FastAPI application
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
