# Fyle Backend Challenge

## Introduction

This project is a backend service for a classroom, developed as part of the Fyle Backend Challenge.

## Table of Contents

- [Installation](#installation)
  - [Install Requirements](#install-requirements)
  - [Reset Database](#reset-database)
  - [Start Server](#start-server)
  - [Run Tests](#run-tests)
- [Dockerization](#dockerization)
- [Gunicorn](#gunicorn)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Fork this repository to your GitHub account.
2. Clone the forked repository and proceed with the steps mentioned below.

### Install Requirements

```bash
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset Database
```bash
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
###Start Server
```bash
bash run.sh
```


###Run Tests
```bash
pytest -vvv -s tests/

# for test coverage report
coverage run -m pytest
coverage html
```


##Dockerization
To run the application using Docker, follow these steps:
```bash
#Pull the Docker image from GitHub Packages:
docker pull ghcr.io/dronacharya27/fyle-flask:latest

#Run the Docker container:
docker run -p 7755:7755 ghcr.io/dronacharya27/fyle-flask:latest
```


###Gunicorn
This project uses Gunicorn as the production-ready WSGI server. The Gunicorn configuration is set up in gunicorn_config.py.

