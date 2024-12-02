FROM python:3.12.2-slim

ENV PYTHONDONTWRITEBYTECODE yes

RUN apt-get update
RUN apt-get install -y git
RUN pip install -e git+https://github.com/rydikov/ax-pro.git@094bf9db3af6b1641a08215d6b45adba179cffd0#egg=axpro

WORKDIR /app

COPY src src

COPY requires.txt requires.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r requires.txt
