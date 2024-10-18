# Use an official Python runtime as the base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY pyproject.toml poetry.lock /app/
RUN pip install -U pip poetry wheel && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# The actual application code will be mounted at runtime

# Run the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
