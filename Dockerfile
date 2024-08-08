# Use the official Python image with the required version
FROM python:3.10.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and any other necessary files to the working directory
COPY script.py .

# Make sure the script is executable
RUN chmod +x script.py

# Provide an entrypoint so the script can be run with parameters
ENTRYPOINT ["python3", "script.py"]

# Example command: this can be overridden when the container is run
CMD ["example.csv"]
