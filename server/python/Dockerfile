FROM python:3.10.0-slim

# add non root user logic
# RUN addgroup --system app && adduser --system --group app

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

# RUN chown -R code:app $HOME
# USER app
COPY ./src /code/src