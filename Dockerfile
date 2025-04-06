# Use the official Streamlit base image
FROM python:3.12-slim

# Install system dependencies including libGL
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port Streamlit uses
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "finbot_hosting.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
