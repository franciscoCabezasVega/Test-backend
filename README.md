# Test-backend

This repository contains a simple test to verify the API response on the provided URL.

## Requirements
- Python 3.8+
- pytest
- requests
- pydantic

## Installation
```bash
pip install -r requirements.txt
```

## Running the project
To run the tests, simply run the following command:
```bash
pytest test_api.py
```

## Installation with docker
```bash
docker build -t test-backend .
```

## Running the project with docker
To run the tests with docker, simply run the following command:
```bash
docker run test-backend
```