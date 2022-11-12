FROM python:3.10-slim

COPY . /RPS

WORKDIR /RPS
RUN pip install --upgrade poetry \
    && poetry install

RUN chmod +x entrypoint.sh
