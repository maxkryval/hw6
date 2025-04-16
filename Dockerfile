# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make start script executable and expose a default port
RUN chmod +x start.sh
EXPOSE 8000

# Define the default command to run the application
CMD ["./start.sh"]