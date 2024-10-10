# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the program to the container
COPY udp_program.py /app

# Install any dependencies (none in this case, but you can add)
# RUN pip install -r requirements.txt

# Run the Python program
CMD ["python", "udp_program.py"]
