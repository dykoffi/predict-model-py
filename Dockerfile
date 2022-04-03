FROM python:3.8-slim


# Install and update 
RUN apt-get update -y && \
    apt-get upgrade -y && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    pip install pipenv

WORKDIR /app
COPY Pipfile .

#Install python dependencies
RUN pipenv install

COPY ./app /app
 
EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT