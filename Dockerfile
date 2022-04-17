FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY Pipfile* ./

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install pipenv
RUN pipenv install --deploy --system


# Remove dependencies
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

USER user