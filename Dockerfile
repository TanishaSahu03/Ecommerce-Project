# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN python -m venv /myenv

# Install the dependencies in the virtual environment
# RUN /env/bin/pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the directories for media and static files
RUN mkdir -p /app/media /app/static

# Expose port 8000 to be able to access the app from the host machine
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
