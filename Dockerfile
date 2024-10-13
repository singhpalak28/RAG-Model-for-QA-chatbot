# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 7860 for the Gradio interface
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Command to run the Gradio app
CMD ["python", "app.py"]