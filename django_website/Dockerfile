# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc 
   
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
RUN apt-get install -y pkg-config

# Create and set the working directory
WORKDIR /code

# Copy the requirements file to the container
COPY requirements.txt /code/

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files to the container
COPY . /code/

# Expose port 80
EXPOSE 80

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

