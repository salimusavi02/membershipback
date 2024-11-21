# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]