# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /web-application
WORKDIR /web-application

# Copy the current directory contents into the container at /web-application
COPY . /web-application

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables for database connection
ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV DATABASE_URL=postgresql://myuser:mypassword@localhost/webappdb

# Run app.py when the container launches
CMD ["./wait-for-it.sh", "database:5432", "--", "python", "app.py"]
