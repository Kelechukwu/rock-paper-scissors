FROM python:3.10-slim

COPY . /RPS

WORKDIR /RPS
RUN pip install --upgrade poetry \
    && poetry install \
    && poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && pip install -r requirements.txt

