FROM python:3.9
WORKDIR /app
ADD . /app
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 && \
    python -m pip install -r requirements.txt
COPY . /app
EXPOSE 8000