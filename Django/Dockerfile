# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /home

# Copy the requirements file into the container
COPY requirements.txt /home/

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /home/

# Collect static files (optional, but recommended for production use)
# RUN python manage.py collectstatic --noinput

# Expose the port the Django development server will be running on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
