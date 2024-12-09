# Base Rasa SDK image
FROM rasa/rasa-sdk:latest

# Copy custom actions and requirements
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the action server port
EXPOSE 5055

# Command to start the action server
CMD ["start", "--actions", "actions"]
