# Use the official Python image as the base for building the FastAPI app
FROM python:3.11.1

# Set the working directory inside the container
WORKDIR /app

# Copy the backend code into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8000 (FastAPI's default port)
EXPOSE 8000

# Start the FastAPI server
# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--ws", "auto"]
