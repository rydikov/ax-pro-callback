FROM python:3.12.2-slim

ENV PYTHONDONTWRITEBYTECODE yes

RUN apt-get update
RUN apt-get install -y git
RUN pip install -e git+https://github.com/rydikov/ax-pro.git@52ed273304a784d8bab5664ce8bd540b4bdddb9c#egg=axpro

WORKDIR /app

COPY src src

COPY requires.txt requires.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r requires.txt
