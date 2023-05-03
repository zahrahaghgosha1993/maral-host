# Dockerfile for Django Applications
# Section 1- Base Image
FROM python:3.9-slim

# Section 2- Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Section 3- Project libraries
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

# Section 4- Code
WORKDIR /app
COPY . .