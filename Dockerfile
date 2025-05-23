FROM python:3.12.2-slim

ENV PYTHONDONTWRITEBYTECODE yes

RUN apt-get update
RUN apt-get install -y git
RUN pip install -e git+https://github.com/rydikov/ax-pro.git@b2349f6b994f6be94ecaf7e435aed877abf4b812#egg=axpro

WORKDIR /app

COPY src src

COPY requires.txt requires.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r requires.txt
