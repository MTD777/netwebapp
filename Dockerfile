# Use the official Python image
FROM python:3.8

# Set the working directory
WORKDIR /netwebapp

# Copy the project files
COPY . .

# Copy the scripts directory
COPY scripts/ /netwebapp/scripts/

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
