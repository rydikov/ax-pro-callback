FROM python:3.12.2-slim

ENV PYTHONDONTWRITEBYTECODE yes

RUN apt-get update
RUN apt-get install -y git
RUN pip install -e git+https://github.com/rydikov/ax-pro.git@8a1b2c7e503d4e69fdcd659c1796e383f3234427#egg=axpro

WORKDIR /app

COPY src src

COPY requires.txt requires.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r requires.txt
